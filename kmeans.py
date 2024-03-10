import numpy as np
import matplotlib.pyplot as plt
import random

#Random Initialization of the k clusters
def initialize_clusters(data, k):
    indices = np.random.choice(len(data), k, replace=False)
    return data[indices]

def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2, axis=1))
#Find the Euclidean Distance of each data and each cluster and then find the closest centre
def assign_clusters(data, centers):
    distances = np.array([euclidean_distance(data, center) for center in centers])
    assignments = np.argmin(distances, axis=0)
    min_distances = np.min(distances, axis=0)
    return assignments, min_distances
#For each cluster, recalculate the cluster centre
def update_centers(data, assignments, k):
    new_centers = np.array([data[assignments == i].mean(axis=0) for i in range(k)])
    return new_centers

def k_means(data, k, max_iters=100, tolerance=1e-4):
    centers = initialize_clusters(data, k)
    distances = np.full(len(data), np.inf)
    
    for _ in range(max_iters):
        assignments, new_distances = assign_clusters(data, centers)
        
        #If the distance to the nearest cluster center improves, update assignments; otherwise, keep the current assignment.
        # This step implicitly checks if the assignment should be updated by comparing new distances to previous distances and then updating the cluster centers accordingly.
        if np.all(new_distances >= distances):
            break
        distances = new_distances
        
        centers = update_centers(data, assignments, k)
    
    return assignments, distances, centers
#Plotting
def visualize_clusters(data, assignments, centers):
    plt.figure(figsize=(10, 8))
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    k = len(centers)
    for i in range(k):
        cluster_data = data[assignments == i]
        plt.scatter(cluster_data[:, 0], cluster_data[:, 1], s=50, c=colors[i % len(colors)], label=f'Cluster {i}')
        plt.scatter(centers[i][0], centers[i][1], s=200, c='black', marker='X')
    plt.title('Cluster assignments and centers')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

#Testing
dataset = [[0,0], [-0.9, 0], [0.2, -0.2], [5,5.3], [5,5.6], [5,5.7]]
for i in range(100):
    rand_1 = random.randint(0, 5)
    rand_2 = random.randint(0, 5)
    dataset.append([rand_1, rand_2])

for i in range(50):
    rand_1 = random.randint(40, 50)
    rand_2 = random.randint(40, 50)
    dataset.append([rand_1, rand_2])

data = np.array(dataset)
k = 2  # Assigning the number of clusters
assignments, distances, centers = k_means(data, k)

visualize_clusters(data, assignments, centers)
