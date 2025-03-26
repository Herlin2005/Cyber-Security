# 🛡️ Ransomware Detection System

A real-time monitoring system that detects ransomware activity through filesystem analysis and network monitoring, with immediate alerting capabilities.

## ✨ Key Features

### 🔍 Detection Capabilities
- **Filesystem Monitoring**
  - Real-time modification tracking using `watchdog`
  - Entropy analysis for encrypted file detection
  - Ransom note pattern recognition (e.g., `HOW_TO_DECRYPT.txt`)
  - Mass file extension changes detection

### 🌐 Network Protection
- Malicious IP/domain blocklist
- Suspicious port activity monitoring
- Outbound connection analysis

### ⚡ Alert System
- Email notifications with OAuth2 authentication
- Local syslog integration
- Customizable alert thresholds

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Gmail account (for email alerts)
- Administrative privileges (for network monitoring)

### Installation
```bash
# Clone repository
git clone https://github.com/Herlin2005/StyleAT/ransomware-detector.git
cd ransomware-detector

# Create virtual environment
python -m venv venv

# Activate environment
# Linux/Mac:
source venv/bin/activate
# Windows:
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt