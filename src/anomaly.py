from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.01)

    def train(self, features):
        self.model.fit(features)

    def predict(self, features):
        return self.model.predict(features)
