import numpy as np 

# Sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x*(1-x)

# Training input
training_input = np.array([[0,0,1],
                           [1,1,1],
                           [1,0,1],
                           [0,1,1]])

# Training output
training_output = np.array([[0,1,1,0]]).T

# Initializing weights

np.random.seed(1)

weights = 2 * np.random.random((3,1)) - 1

print("\nWeights before training")
print(weights)

for i in range(20000):
    #Forward propagation
    input_layer = training_input
    outputs = sigmoid(np.dot(input_layer, weights))

    # Cost function
    error = training_output - outputs

    # Back Propagation
    adjustments = error * sigmoid_derivative(outputs)
    weights += np.dot(input_layer.T, adjustments)

print("\nWeights after training")
print(weights)

print("\nOutput")
print(outputs)

# Testing the model

testing_input = np.array([[1,0,0]])

testing_output = sigmoid(np.dot(testing_input,weights))

print("\nTesting output")
print(testing_output)