def TowerOfHanoi(n , source, target, midway):
    if n == 1:
        print("Move disk 1 source" ,source ,"to target" ,target)
        return
    TowerOfHanoi( n -1, source, midway, target)
    print("Move disk" ,n ,"from source" ,source ,"to target" ,target)
    TowerOfHanoi( n -1, midway, target, source)

n = 4
TowerOfHanoi(n, 'A', 'C', 'B')