import random
import matplotlib.pyplot as plot
import math

# dbscan algorithm - O(n^2)

def euclidean_distance(point1, point2):
    distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
    return distance

def dbscan(points,eps,min_points):
	cluster_id = 1
	# -1 means unclassified point
	clusters = [-1 for i in range(len(points))]
	for i,point in enumerate(points):
		if clusters[i] == -1:
			if expand_cluster(points,(i,point),cluster_id,eps,min_points,clusters):
				cluster_id=cluster_id+1

	return clusters


def expand_cluster(points,current_point,cluster_id,eps,min_points,clusters):
	seeds = region_query(points,current_point,eps,clusters)
	
	if len(seeds) < min_points:
		# 0 means noise point
		clusters[point[0]] = 0
		return False
	
	else:
		for i,point in seeds:
			clusters[i]=cluster_id
		seeds.remove(current_point)

		while len(seeds)>0:
			current_point = seeds.pop(0)
			result = region_query(points,current_point,eps,clusters)

			if len(result) >= min_points:
				for i,point in result:
					if clusters[i] == -1:
						seeds.append((i,point))
					clusters[i]=cluster_id

		return True


def region_query(points,current_point,eps,clusters):
	seeds = []
	for i,point in enumerate(points):
		if euclidean_distance(current_point[1],point) < eps:
			seeds.append((i,point))

	return seeds;


# for testing
if __name__ == "__main__":
    points = []
    
    for i in range(50):
        x = random.randint(10,20)
        y = random.randint(10,20)
        points.append((x,y))

    for i in range(50):
        x = random.randint(40,50)
        y = random.randint(40,50)
        points.append((x,y))
        
        
    for i in range(50):
        x = random.randint(50,60)
        y = random.randint(20,30)
        points.append((x,y))
        

    eps=5
    min_points=10

    result = dbscan(points,eps,min_points)
    
    colors = ["yellow","green","red","blue"]
    
    for i,point in enumerate(points):
        plot.scatter(point[0],point[1], color=colors[result[i]])
    
    plot.xlabel('X-axis')
    plot.ylabel('Y-axis')
    plot.title('K Mean')

    plot.show()
    