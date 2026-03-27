# telecom-node-monitor
Telecom Node Status Monitor with CI/CD Pipeline
# Telecom Node Monitor 🚀

A cloud-native REST API for monitoring telecom network nodes 
(HLR, HSS, EIR, MNP, UDM) with automated CI/CD pipeline.

## 🎯 Features
- Real-time node status monitoring
- Active alarm detection
- Dockerized deployment
- Automated CI/CD with GitHub Actions
- Helm chart for Kubernetes deployment

## 🛠️ Tech Stack
- Python + Flask
- Docker
- Kubernetes + Helm
- GitHub Actions CI/CD
- Pytest automation

## 📡 API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/health` | GET | Health check |
| `/nodes` | GET | All node statuses |
| `/nodes/<name>` | GET | Specific node status |
| `/alarms` | GET | Active alarms |

## 🚀 How to Run

### Local
```bash
pip install -r requirements.txt
python app.py
```

### Docker
```bash
docker build -t telecom-node-monitor .
docker run -p 5000:5000 telecom-node-monitor
```

### Kubernetes
```bash
helm install telecom-monitor ./helm
```

## 🧪 Run Tests
```bash
pytest test_app.py -v
```

## 👨‍💻 Author
Nagendra Babu — 8+ years Telecom Engineer