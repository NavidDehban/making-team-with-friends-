def dfs_cycle(u, p, color: list,
            mark: list, par: list):
    global cyclenumber

 
    if color[u] == 2:
        return

    if color[u] == 1:
        cyclenumber += 1
        cur = p
        mark[cur] = cyclenumber
        while cur != u:
            cur = par[cur]
            mark[cur] = cyclenumber

        return

    par[u] = p

    
    color[u] = 1

    
    for v in graph[u]:
        if v == par[u]:
            continue
        dfs_cycle(v, u, color, mark, par)
    color[u] = 2
	
def addEdge(u, v):
    graph[u].append(v)
    graph[v].append(u)
	
def printCycles(edges, mark: list):

    for i in range(1, edges + 1):
        if mark[i] != 0:
            cycles[mark[i]].append(i)

    # for i in range(1, cyclenumber + 1):

        
    #     print("Cycle Number %d:" % i, end = " ")
    #     for x in cycles[i]:
    #         print(x, end = " ")
    #     print()
		
def creat_graph(enemies):
    for i in enemies:
        addEdge(i[0], i[1])
		
def input_():
    in1 = input().split()
    n = int(in1[0])
    m = int(in1[1])
    edges = m
    enemies = []
    for i in range(m):
        in2 = input().split()
        enemies.append([int(in2[0]),int(in2[1])])
    creat_graph(enemies)
    dfs_cycle(1, 0, color, mark, par)	
    for i in range(1, edges + 1):
        if mark[i]==0:
            dfs_cycle(i, 0, color, mark, par)
    printCycles(n, mark)

    counter = 0
    for i in cycles:
        if len(i)%2 == 1:
            counter += 1
    if (n - counter)%2 == 1:
        counter += 1 
    print(counter)
	
N = 100000
graph = [[] for i in range(N)]
cycles = [[] for i in range(N)]
color = [0] * N
par = [0] * N
mark = [0] * N
cyclenumber = 0

input_()

