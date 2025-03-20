def duplicate_k(arr, K):
    n = len(arr)
    possible_dups = 0
    last = n - 1

  
    for i in range(n):
        if i > last - possible_dups:  
            break
        if arr[i] == K:
            
            if i == last - possible_dups:
                arr[last] = K  
                last -= 1
                break
            possible_dups += 1

   
    i = last - possible_dups
    while i >= 0:
        if arr[i] == K:
            if i + possible_dups < n:
                arr[i + possible_dups] = K  
            possible_dups -= 1
            if i + possible_dups < n:
                arr[i + possible_dups] = K 
        else:
            if i + possible_dups < n:
                arr[i + possible_dups] = arr[i]  
        i -= 1


arr = [1, 2, 3, 2, 4, 2, 5]  
K = 2

duplicate_k(arr, K)

print("Modified array:", arr)
