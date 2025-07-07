import hashlib

def simple_hash(text):
    return int(hashlib.sha1(text.encode()).hexdigest(), 16) % (10 ** 8)

def extract_features(logs):
    features = []
    for log in logs:
        features.append([
            simple_hash(log['service']),
            len(log['message']),
        ])
    return features
