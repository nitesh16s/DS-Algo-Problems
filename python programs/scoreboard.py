def climbingLeaderboard(scores, alice):
    scores = sorted(list(set(scores)), reverse=True)
    ans = []
    for i in range(len(alice)):
        for j in range(len(scores)-1,-1,-1):
            if alice[i] <= scores[j]:
                ans.append(j)
                break
    if alice[0] < scores[0]:
    	ans.insert(0,len(scores)+1,)
    if alice[0] == scores[0]:
    	ans.insert(0,len(scores))
    return ans

print(climbingLeaderboard([100,50,40,20,10], [5,25,50,120]))