def perceptron_train(X, y, learning_rate=0.1, epochs=100):
    num_features = len(X[0])
    weights = [0] * num_features
    bias = 0
    
    for _ in range(epochs):
        for i in range(len(X)):
            prediction = 0
            for j in range(num_features):
                prediction += X[i][j] * weights[j] + bias
            if prediction >= 0:
                y_pred = 1
            else:
                y_pred = 0
                
            error = y[i] - y_pred
            for j in range(num_features):
                weights[j] += learning_rate * error * X[i][j]
            bias += learning_rate * error
            
    return weights, bias

def perceptron_predict(X, weights, bias):
    predictions = []
    for i in range(len(X)):
        prediction = 0
        for j in range(len(weights)):
            prediction += X[i][j] * weights[j] + bias
        if prediction >= 0:
            y_pred = 1
        else:
            y_pred = 0
        predictions.append(y_pred)
    return predictions


X_train = [[0, 0], [0, 1], [1, 0], [1, 1]]
y_train = [0, 0, 0, 1]

X_test = [[0, 1], [1, 1]]

# Train
weights, bias = perceptron_train(X_train, y_train)

# Test
predictions = perceptron_predict(X_test, weights, bias)

# Print predictions
print("Predictions:", predictions)
