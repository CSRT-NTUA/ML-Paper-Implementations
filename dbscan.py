import numpy as np
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cluster_id = None

class DBSCAN:
    def __init__(self, epsilon, min_points):
        self.epsilon = epsilon
        self.min_points = min_points

    def region_query(self, point, points):
        neighbors = []
        for p in points:
            if self.distance(point, p) <= self.epsilon:
                neighbors.append(p)
        return neighbors

    def expand_cluster(self, point, neighbors, cluster_id, points):
        point.cluster_id = cluster_id
        for p in neighbors:
            if p.cluster_id is None:
                p.cluster_id = cluster_id
                new_neighbors = self.region_query(p, points)
                if len(new_neighbors) >= self.min_points:
                    neighbors.extend(new_neighbors)

    def distance(self, p1, p2):
        return np.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

    def dbscan(self, points):
        cluster_id = 0
        for point in points:
            if point.cluster_id is None:
                neighbors = self.region_query(point, points)
                if len(neighbors) < self.min_points:
                    point.cluster_id = -1  # mark as noise
                else:
                    cluster_id += 1
                    self.expand_cluster(point, neighbors, cluster_id, points)

    def plot_clusters(self, points):
        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

        for point in points:
            color = colors[point.cluster_id % len(colors)]
            plt.scatter(point.x, point.y, color=color)

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('DBSCAN Clustering')
        plt.show()



if __name__ == "__main__":
    np.random.seed(0)
    num_points = 200
    noise_level = 0.1
    points = [Point(x, y) for x, y in zip(np.random.rand(num_points) * 10, np.random.rand(num_points) * 10)]

    # Introducing noise
    for point in points[:int(noise_level * num_points)]:
        point.x = np.random.rand() * 10
        point.y = np.random.rand() * 10

    # Initializing DBSCAN
    epsilon = 0.5
    min_points = 5
    dbscan = DBSCAN(epsilon, min_points)

    # Running DBSCAN clustering
    dbscan.dbscan(points)

    # Plotting clusters
    dbscan.plot_clusters(points)
