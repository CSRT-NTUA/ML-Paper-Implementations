import random
import matplotlib.pyplot as plt
from collections import deque

UNCLASSIFIED = -1
NOISE = 0

def region_query(dataset, point_index, eps):
    neighbors = []
    for i, point in enumerate(dataset):
        if i != point_index and euclidean_distance(point, dataset[point_index]) <= eps:
            neighbors.append(i)
    return neighbors

def euclidean_distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def expand_cluster(dataset, point_index, cluster_id, eps, min_pts, clusters):
    seeds = deque(region_query(dataset, point_index, eps))
    if len(seeds) < min_pts:
        clusters[point_index] = NOISE
        return False
    else:
        clusters[point_index] = cluster_id
        while seeds:
            current_point_index = seeds.popleft()
            if clusters[current_point_index] == UNCLASSIFIED:
                neighbor_points = region_query(dataset, current_point_index, eps)
                if len(neighbor_points) >= min_pts:
                    seeds.extend(neighbor_points)
            if clusters[current_point_index] == UNCLASSIFIED or clusters[current_point_index] == NOISE:
                clusters[current_point_index] = cluster_id
    return True

def dbscan(dataset, eps, min_pts):
    cluster_id = 1
    clusters = [UNCLASSIFIED] * len(dataset)
    for i, point in enumerate(dataset):
        if clusters[i] == UNCLASSIFIED:
            if expand_cluster(dataset, i, cluster_id, eps, min_pts, clusters):
                cluster_id += 1
    return clusters

def plot_clusters(dataset, clusters):
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

    for i, point in enumerate(dataset):
        if clusters[i] == NOISE:
            plt.scatter(point[0], point[1], color='black')
        else:
            plt.scatter(point[0], point[1], color=colors[clusters[i] % len(colors)])

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('DBSCAN Clustering')
    plt.show()

if __name__ == "__main__":
    dataset = []
    
    # First cluster
    for _ in range(100):
        rand_x = random.uniform(0, 3)
        rand_y = random.uniform(0, 3)
        dataset.append([rand_x, rand_y])

    # Second cluster
    for _ in range(100):
        rand_x = random.uniform(7, 10)
        rand_y = random.uniform(0, 3)
        dataset.append([rand_x, rand_y])

    # Third cluster
    for _ in range(100):
        rand_x = random.uniform(3.5, 6.5)
        rand_y = random.uniform(6, 10)
        dataset.append([rand_x, rand_y])


    eps = 1.0
    min_pts = 5

    clusters = dbscan(dataset, eps, min_pts)
    plot_clusters(dataset, clusters)
