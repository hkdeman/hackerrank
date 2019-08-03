def minimumBribes(q):
    pos_map = {}
    num_of_bribes = 0
    for index, elem in enumerate(q):
        pos_map[elem] = index # 8:5
    
    for i in range(len(q), 0, -1):
        pos = pos_map[i] # pos 5 for value 8
        diff = abs(pos - (i - 1))
        if diff > 2:
            num_of_bribes = 'Too chaotic'
            break
        for j in range(diff):
            num_of_bribes+=1
            q[pos+j], q[pos+j+1] = q[pos+j+1], q[pos+j] #swap
            pos_map[q[pos+j+1]] += 1
            pos_map[q[pos+j]] -= 1
    
    print(num_of_bribes)