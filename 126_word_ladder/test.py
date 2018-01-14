class Solution(object):
    def word_dist(self, word):
        return sum([1 if c1!=c2 else 0 for c1, c2 in zip(word[0], word[1])])
    
    def findLadders(self, beginWord, endWord, wordList):
        
        # Contruct word graph O(n^2)
        word_graph = {}
        for word in wordList+[beginWord, endWord]:
            word_graph[word] = [w for w in wordList if w!=word and self.word_dist((w,word))==1]
        
        # print word_graph
        
        # find all shortest path in word_graph O(n+n^2)
        shortest_paths = []
        min_len = len(wordList)+2
        #bfs_queue = [([beginWord],{beginWord:1})]
	bfs_queue = set()
        
        while len(bfs_queue)!=0:
            node = bfs_queue.pop(-1)
            if node[0][-1] == endWord:
                if len(node[0]) < min_len:
                    shortest_paths = [node[0]]
                    min_len = len(node[0])
                elif len(node[0]) == min_len:
                    shortest_paths.append(node[0])
                    
            for neigh in word_graph[node[0][-1]]:
                if neigh not in node[1] and len(node[0])+1 <= min_len: # O(1)
                    new_dict = dict(node[1])
                    new_dict[neigh] = 1
                    bfs_queue.append((node[0]+[neigh], new_dict))
        
        return shortest_paths
