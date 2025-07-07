from parser import parse_line
from features import extract_features
from anomaly import AnomalyDetector

def run(filepath):
    logs = []
    with open(filepath, 'r') as f:
        for line in f:
            parsed = parse_line(line)
            if parsed:
                logs.append(parsed)

    X = extract_features(logs)
    detector = AnomalyDetector()
    detector.train(X)
    preds = detector.predict(X)

    for i, pred in enumerate(preds):
        if pred == -1:
            print(f"⚠️ Anomaly detected: {logs[i]}")

if __name__ == "__main__":
    run("logs/sample_syslog.log")
