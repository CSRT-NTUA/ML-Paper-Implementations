from random import randint,sample
import matplotlib.pyplot as plt

def eucl_dist(a,b):
    return (a[0]-b[0])**2+(a[1]-b[1])**2

def k_means(data:list,k:int)->dict:
    centers=sample(data,k) # Select k random points as centers
    belongs_to={tuple:int}
    has={int:list}
    distances={}
    while True:
        for point in data:
            if point in distances and eucl_dist(point,centers[belongs_to[point]])<=distances[point]: continue # If the point is closer to its center, continue
            if point in belongs_to:has[belongs_to[point]].remove(point)
            min_distance=float('inf')
            for cluster,center in enumerate(centers):
                distance=eucl_dist(point,center)
                if distance<min_distance:
                    min_distance,min_cluster=distance,cluster
            belongs_to[point]=min_cluster
            has.setdefault(min_cluster,[]).append(point)
            distances[point]=min_distance
        # Calculate new centers
        new_centers=[]
        for cluster,center in enumerate(centers): 
            x=y=0
            for point in has[cluster]:
                x+=point[0]
                y+=point[1]
            len_points=len(has[cluster])
            new_centers.append((x/len_points,y/len_points))
        if new_centers==centers:
            return belongs_to
        centers=new_centers
            

def plot(data,belongs_to:dict={},centers=[],title='Plot'):
    colors=['red','green','blue','purple']
    for point in data:      plt.scatter(*point,color=colors[belongs_to.get(point,0)])
    for center in centers:  plt.scatter(*center,color='black',marer='x')
    plt.title(title)
    plt.show()

if __name__ == '__main__':
    data=[]
    for i in range(30):
        data.append((randint(0,10),randint(0,10)))
    for i in range(15):
        data.append((randint(20,40),randint(20,40)))
    for i in range(25):
        data.append((randint(60,75),randint(60,75)))
        
    belongs_to=k_means(data,k=3)
    plot(data,belongs_to,title='Final clusters')