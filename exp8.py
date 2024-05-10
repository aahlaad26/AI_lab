from sklearn.tree import DecisionTreeClassifier

class RealTimeClassifier:
    def __init__(self, max_samples=1000, max_features=10):
        self.max_samples = max_samples
        self.max_features = max_features
        self.model = DecisionTreeClassifier()
        self.X = []
        self.y = []

    def update(self, features, label):
        if len(self.X) < self.max_samples:
            self.X.append(features)
            self.y.append(label)
        else:
            self.X.pop(0)
            self.y.pop(0)
            self.X.append(features)
            self.y.append(label)

        if len(self.X) >= 10:  # Retrain the model when we have enough data
            self.model.fit(self.X, self.y)

    def predict(self, features):
        if len(self.X) < 10:
            return None  # Insufficient data for prediction
        else:
            return self.model.predict([features])[0]

# Example usage:
classifier = RealTimeClassifier()

# Simulating real-time data stream
data_stream = [
    ([0.1, 0.2, 0.3], "Normal"),
    ([0.5, 0.6, 0.7], "Anomalous"),
    ([0.3, 0.4, 0.5], "Normal"),
    ([0.8, 0.9, 1.0], "Anomalous"),
    # More incoming data...
]

for features, label in data_stream:
    classifier.update(features, label)
    prediction = classifier.predict(features)
    if prediction is not None:
        print("Predicted:", prediction)
