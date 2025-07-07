# LogSentinel-AI

Detect anomalies in Linux log files using open-source AI models.

## 📌 What This Project Does

This tool analyzes Linux system logs (e.g., `/var/log/syslog`) and uses machine learning to identify unusual or suspicious activity. Great for learning about:

- Cybersecurity
- Log monitoring
- AI-based anomaly detection

## 🤖 Tech Stack

| Component       | Tool Used       |
|----------------|-----------------|
| Language        | Python          |
| AI Library      | scikit-learn    |
| Log Parsing     | Regex           |
| Visualization   | (optional) Streamlit or Matplotlib |
| ML Model        | Isolation Forest |

## 🔧 How It Works

1. Parses Linux log files
2. Extracts features like service name, message length
3. Uses AI to detect outliers
4. Prints alerts for potential anomalies

## 🚀 How to Run

1. Clone the repo or download the files  
2. Install dependencies:  
```bash
pip install -r requirements.txt
