#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <utility>
using namespace std;
// Structure to represent a data point
struct DataPoint {
    vector<double> features;
    int label;
};
// Function to calculate Euclidean distance between two data points
double euclideanDistance(const vector<double>& p1, const vector<double>& p2) {
    double distance = 0.0;
    for (size_t i = 0; i < p1.size(); ++i) {
        distance += pow(p1[i] - p2[i], 2);
    }
    return sqrt(distance);
}
// KNN classifier function
int knnClassifier(const vector<DataPoint>& trainingData, const vector<double>& inputFeatures, int k) {
    // Vector to store distances from input to training data points along with their indices
    vector<pair<double, int>> distances;

    // Calculate distances from input to each training data point
    for (size_t i = 0; i < trainingData.size(); ++i) {
        double distance = euclideanDistance(trainingData[i].features, inputFeatures);
        distances.push_back(make_pair(distance, i));
    }

    // Sort distances in ascending order
    sort(distances.begin(), distances.end());

    // Count votes for each class among the k nearest neighbors
    vector<int> classVotes(10, 0); // Assuming labels are from 0 to 9
    for (int i = 0; i < k; ++i) {
        int index = distances[i].second;
        int label = trainingData[index].label;
        classVotes[label]++;
    }

    // Return the class with the highest vote
    return distance(classVotes.begin(), max_element(classVotes.begin(), classVotes.end()));
}
