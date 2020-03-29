#!/usr/bin/env python3


import re
import itertools



class Graph(object):
    name = "Larika Sehagal"
    email = "larika18243@iiitd.ac.in"
    roll_num = "2018243"
    def __init__ (self, vertices, edges):
        """
        Initializes object for the class Graph
        Args:
            vertices: List of integers specifying vertices in graph
            edges: List of 2-tuples specifying edges in graph
        """
        self.vertices = vertices        
        ordered_edges = list(map(lambda x: (min(x), max(x)), edges))        
        self.edges    = ordered_edges        
        self.validate()
    def validate(self):
        """
        Validates if Graph if valid or not
        Raises:
            Exception if:
                - Name is empty or not a string
                - Email is empty or not a string
                - Roll Number is not in correct format
                - vertices contains duplicates
                - edges contain duplicates
                - any endpoint of an edge is not in vertices
        """
        if (not isinstance(self.name, str)) or self.name == "":
            raise Exception("Name can't be empty")
        if (not isinstance(self.email, str)) or self.email == "":
            raise Exception("Email can't be empty")
        if (not isinstance(self.roll_num, str)) or (not re.match(ROLLNUM_REGEX, self.roll_num)):
            raise Exception("Invalid roll number, roll number must be a string of form 201XXXX. Provided roll number: {}".format(self.roll_num))
        if not all([isinstance(node, int) for node in self.vertices]):
            raise Exception("All vertices should be integers")
        elif len(self.vertices) != len(set(self.vertices)):
            duplicate_vertices = set([node for node in self.vertices if self.vertices.count(node) > 1])
            raise Exception("Vertices contain duplicates.\nVertices: {}\nDuplicate vertices: {}".format(vertices, duplicate_vertices))
        edge_vertices = list(set(itertools.chain(*self.edges)))
        if not all([node in self.vertices for node in edge_vertices]):
            raise Exception("All endpoints of edges must belong in vertices")
        if len(self.edges) != len(set(self.edges)):
            duplicate_edges = set([edge for edge in self.edges if self.edges.count(edge) > 1])
            raise Exception("Edges contain duplicates.\nEdges: {}\nDuplicate vertices: {}".format(edges, duplicate_edges))
    def graph(self):
        #This function returns a dictionary where the keys are vertices and the value corresponding 
        #to them is a list consisting of direct neighbours of the vertex 
        vertices=self.vertices
        edges=self.edges
        s={}    #dictionary containing the keys=vertices and corresponding values= list of its direct neighbours
        for i in vertices:      
            l=[]            #list containing the immediate neighbours of i
            for j in edges:
                if j[0]==i:
                    l.append(j[1])
                if j[1]==i:
                    l.append(j[0])
            s[i]=l
        return(s)
    def bfs(self,start_node):
        """
        The function uses the algorithm of breadth first search to calculate a nested list of the form 
        [v,[l1],[l2]...]. Here v is the start_node (from where we calculate our distances), list l1 
        consists of immediate neighbours of v , l2 contains the vertices which are one level away from v and so on  
        """
        vertices=self.vertices
        l = [] ;  x = []
        s = self.graph()        
        l.append(start_node) ; x.append(start_node)
        l.append(s[start_node]) ; x.extend(s[start_node])
        x.sort()    
        while x!=vertices: #till all the vertices have been covered so as to know their distances from start_node
            m=[]        
            for i in l[-1]:
                a=s[i]       
                for j in a:
                    if j not in x:
                        m.append(j)
                        x.append(j)
            l.append(m)
            x.sort()
        return(l)
    def min_dist(self, start_node, end_node):
        '''
        Finds minimum distance between start_node and end_node
        Returns:
            An integer denoting minimum distance between start_node
            and end_node
        '''
        l = self.bfs(start_node)    
        for i in range(1,len(l)):   
            x=l[i]
            if end_node in x:
                z=i             #finding the position of end_node wrt start_node from the 
        return(z)               #nested list obtaine from bfs        
        raise NotImplementedError
    def all_possible_paths(self, start_node, end_node, visited=[]):
        """
        The function returns all possible paths from the start_node to the end_node while keeping 
        a track of the vertices crossed so that the path is never like a-b-a (Backtracking)
        """
        s=self.graph()
        visited = visited + [start_node] #the start_node at every step(including the recursion steps) are
        if start_node == end_node:   #added to the visited hence keeping a track of the vertices crossed 
            return [visited]
        if start_node not in s:
            return []
        possible_paths = []
        for i in range(len(s[start_node])):
            j = s[start_node][i]
            if j not in visited:
                a = self.all_possible_paths(j, end_node, visited)   #recursive step; using function to 
                possible_paths.extend(a)                #find the path starting from j to end_node  
                #the process continues till j == end_node
        return possible_paths
        raise NotImplementedError
    def all_shortest_paths(self,start_node, end_node):
        """
        Finds all shortest paths between start_node and end_node
        The function used the values obtained from the function min_dist and all_possible_paths
        to return the paths from all_possible_paths which have length == min_dist+1
        Args:
            start_node: Starting node for paths
            end_node: Destination node for paths

        Returns:
            A list of path, where each path is a list of integers.
        """
        a=self.min_dist(start_node,end_node)
        b=self.all_possible_paths(start_node,end_node,visited=[])
        shortest_paths=[]
        for i in b:
            if len(i) == a+1:   #paths in all_possible_paths having length min_dist+1
                shortest_paths.append(i)    
        return(shortest_paths)
        raise NotImplementedError
    def all_paths(self,node, destination, dist):
        """
        Finds all paths from node to destination with length = dist
        Based on the values obtained from all_possible_paths ; the function return the paths 
        from all_possible_paths which have length equal to dist+1.
        Arg:
            node:start_node or starting point
            destination:end_node
            dist: required distance between the node and the destination  
        Returns:
            List of path, where each path is list ending on destination
            Returns None if there no paths
        """
        a=self.all_possible_paths(node,destination,visited=[])
        all_paths=[]
        for i in a:
            if len(i) == dist+1:
                all_paths.append(i)
        if len(all_paths) == 1:
            all_paths=all_paths[0]
        return all_paths        
        raise NotImplementedError
    def betweenness_centrality(self, node):
        """
        Finds the  betweenness centrality of the given node
        Args:
            node: Node to find betweenness centrality of.
        Returns:
            Single floating point number, denoting betweenness centrality
            of the given node
        """
        l=[]
        for i in self.vertices:
            if i != node:
                l.append(i)
        other_possible_s_and_e=[]
        for x in itertools.combinations(l,2):
            other_possible_s_and_e.append(x)
        list1=[]         
        for i in other_possible_s_and_e:
            x = self.all_shortest_paths(i[0],i[1])
            y=i,x
            list1.append(y)  #containing all shortest paths to all possible combinations
        list2=[]
        for i in list1:
            x=len(i[1])      #Calulating X = total no. of shortest paths from start_node to end_node
            i=list(i)
            i.append(x)
            list2.append(i) #list containing elements of the form [(pair),[shortest paths],X] 
        #calculating Y ; Y = total no. of shortest paths from start_node to end_node which incluse node
        list3=[]
        for i in list2:
            count=0
            for j in i[1]:
                if node in j:
                    count+=1
            i.append(count)
            list3.append(i) #list containing elements of the form [(pair),[shortest paths],X,Y]
        list4=[]    
        for i in list3:
            a=i[2] #X
            b=i[3] #Y
            c=b/a 
            i.append(c)
            list4.append(i) #list containing elements of the form [(pair),[shortest paths],X,Y,Y/X]
        betweeness_centrality=0
        #calculating the sum of all the Y/X obtained so as to get the betweeness centrality of the node
        for i in list4:
            x=i[4]
            betweeness_centrality+=x
        N=len(self.vertices)
        a=(N-1)*(N-2) ; b= a/2  #standardised betweenness centrality = betweeness centrality/[(N-1)*(N-2)/2]
        standardised_betweeness_centrality=betweeness_centrality/b
        return(standardised_betweeness_centrality)
        raise NotImplementedError
    def top_k_betweenness_centrality(self):
        """
        Finds top k nodes based on highest equal betweenness centrality.
        the functions obtains the list1 of tuples t where t[0] corresponds to the vertex and t[1]
        corresponds to t[0]'s betweenness centrality 
        then the list if betweeness centralities is obtained and sorted
        The function returns vertices in list1 having t[1]==the max betweenness centrality
        Returns:
            List a integer, denoting top k nodes based on betweenness
            centrality.
        """
        l=[] ;  q=[]
        for i in self.vertices:
            a=self.betweenness_centrality(i)
            s=i,a       
            l.append(s) #the list of tuples t(vertex,betweenness centrality)
            if a not in q:
                q.append(a)      #list containing all distinct betweenness centralities obtained           
        q.sort()    
        c=q[-1]     #max betweenness centrality
        list_topk_nodes=[]
        for i in l:
            if i[1] == c:   #nodes having max. betweenness centrality
                list_topk_nodes.append(i[0])
        return(list_topk_nodes)
        raise NotImplementedError

vertices = [0,1, 2, 3, 4, 5, 6,7]
edges    = [(0,1),(0,2),(1,2),(1,5),(2,3),(2,4),(3,4),(3,5),(4,5),(4,6),(4,7),(5,6),(5,7),(6,7)]
graph = Graph(vertices,edges)
a=graph.top_k_betweenness_centrality()
#print(a)

