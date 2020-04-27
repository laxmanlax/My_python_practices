def largeGroupPositions(S):
    """
    :type S: str
    :rtype: List[List[int]]
    """
    trackPos = {}
    
    for i in range(len(S)-1):
        cnt = [i,i]
        temp = str(S[i])
        print trackPos,"=======",S[i],i ,cnt

        trackPos[temp] = cnt
        print trackPos 
    
        if S[i]==S[i+1]:
            cnt[1] +=1
        else:
            cnt[1] = cnt[1]
         

        
    print trackPos


S="abbxxxxzzy"
largeGroupPositions(S)