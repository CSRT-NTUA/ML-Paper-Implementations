from random import randint
import matplotlib.pyplot as plt
from math import sqrt


def eucl_dist(a,b):
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def region_query(points:list,curr_point:tuple,eps:float)->list: # O(n)
    return [point for point in points if eucl_dist(curr_point,point)<=eps]

def dbscan(points:list,eps:float,minPts=4)->dict: # O(n²)
    cluster_id={tuple:int}
    curr_cluster=1 # 0 is for noise
    for point in points:
        if point in cluster_id: continue
        if expand_cluster(points,point,curr_cluster,eps,minPts,cluster_id):
            curr_cluster+=1
    return cluster_id

def expand_cluster(points:list,point:tuple,curr_cluster:int,eps:float,minPts:int,cluster_id:dict)->bool:
    seeds=region_query(points,point,eps)
    if len(seeds)<minPts:
        cluster_id[point]=0 # Noise
        return False
    for seed in seeds:
        cluster_id[seed]=curr_cluster
    seeds.remove(point)
    while seeds:
        curr_point=seeds.pop(0)
        curr_seeds=region_query(points,curr_point,eps)
        if len(curr_seeds)>=minPts:
            for seed in curr_seeds:
                clid=cluster_id.get(seed,-1)
                if clid in [-1,0]: # if the point is noise or unvisited
                    if clid==-1: seeds.append(seed)
                    cluster_id[seed]=curr_cluster
    return True
    

def plot(data,cluster_id:dict={},title='DBSCAN Plot'):
    colors=['black','red','green','blue','purple','yellow','orange','pink','brown','grey']
    for point in data: plt.scatter(*point,color=colors[cluster_id.get(point,0)])
    plt.title(title)
    plt.show()
    

if __name__ == '__main__':
    data=[]
    for i in range(25):
        data.append((randint(0,10),randint(0,10)))
    for i in range(15):
        data.append((randint(20,40),randint(20,40)))
    for i in range(25):
        data.append((randint(60,75),randint(60,75)))
    for i in range(100,140,3): # simple pattern
        y =  randint(0, 5)
        data.append((i, i+y))
        data.append((i, 200-i-y))
    for i in range(10): # Noise
        data.append((randint(0,150),randint(0,150)))
    
    
    cluster_id=dbscan(data,eps=10)
    plot(data,cluster_id)
    