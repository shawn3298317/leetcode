def solution(arr):
	
	ret = []
	neg_flag = False

	for l in arr:
		if l[0] == "-":
			neg_flag = True
			l = l[1:]
		try :
			if neg_flag: ret.append( -1*int("".join(l))+1 )
			else: ret.append( int("".join(l))+1 )
		except:
			ret.append(None)
	return ret

print solution([["2","7","1","9"],["-","9","9"],["a","1"]])

def solution(self, costs):
        
        n_house = len(costs)
        n_color = len(costs[0]) if n_house > 0 else 0
        
        #Edge cases: 0
        if n_house == 0 or n_color == 0: return 0
        
        #Edge cases: 1
        if n_color == 1:
            if n_house > 1: return 0
            else: return costs[0][0]
        
        #Cases: n
        DP_cost = [x[:] for x in [[0]*n_color]*n_house]
        
        for n in xrange(n_house):
            for k in xrange(n_color):
                if n != 0:
                    DP_cost[n][k] = min([DP_cost[n-1][c] + costs[n][k]\
					 for c in xrange(n_color) if c != k])
                else:
                    DP_cost[0][k] = costs[0][k]
                    
        
        return min([DP_cost[-1][k] for k in xrange(n_color)])
