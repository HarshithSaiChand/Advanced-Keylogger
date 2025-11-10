# Advanced-Keylogger

> **🔒 Educational Cybersecurity Research Tool**  
> **⚠️ Authorized Testing & Internship Project Only**

A comprehensive Python-based keylogger for **controlled cybersecurity research** and **authorized penetration testing** in sandboxed environments.

---

## ⚠️ Ethical Use Declaration

**This software is intended EXCLUSIVELY for:**
- ✅ Authorized security research in isolated lab environments
- ✅ Academic cybersecurity education with institutional approval
- ✅ Personal system security auditing on hardware you own
- ✅ Defensive tool development and testing

**Absolutely prohibited for:**
- ❌ Unauthorized surveillance or monitoring
- ❌ Deployment on systems without explicit written consent
- ❌ Malicious intent or illegal activities
- ❌ Commercial use without proper licensing

**By using this tool, you agree to comply with all applicable laws: CFAA, GDPR, wiretapping statutes, and institutional policies.**

---

## 🎯 Features

| Capability | Description | Defensive Value |
|------------|-------------|-----------------|
| **Keystroke Logging** | Records keyboard input with real-time keyword detection | Understand keylogging behavior for detection |
| **System Reconnaissance** | Harvests hostname, IPs, platform details | Study information gathering tactics |
| **Clipboard Monitoring** | Captures copied text data | Analyze data exfiltration vectors |
| **Audio Surveillance** | Records microphone input | Test audio capture detection |
| **Screenshot Capture** | Takes desktop screenshots | Visual monitoring analysis |
| **Automated Exfiltration** | Emails logs via SMTP | Research data theft methods |
| **Keyword Alerts** | Immediate alerts on sensitive words | Simulate DLP bypass techniques |

---

## 🛠️ Requirements

### System Requirements
- **OS:** Windows 10/11 (due to `win32clipboard`)
- **Python:** 3.8+
- **Network:** Isolated lab network recommended

### Dependencies
```bash
pip install -r requirements.txt
```

---

## 📦 Quick Start

### 1. Clone & Setup
```bash
# Clone repository
git clone https://github.com/HarshithSaiChand/Advanced-Keylogger.git
cd Advanced-Keylogger

# Create virtual environment
python -m venv .venv
.\.venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration
Create a `.env` file (never commit this to Git):

```bash
# .env (add to .gitignore!)
EMAIL_USER="your_test_email@gmail.com"
EMAIL_APP_PASSWORD="your_app_specific_password"
RECIPIENT_EMAIL="security-lab@your-institution.com"
FILE_PATH="C:\CyberLab\Keylogger_Test"
MICROPHONE_TIME=10
```

### 3. Define Keywords
Edit `predefwords.txt`:
```
password
login
credit card
ssn
admin
```

### 4. Run in Controlled Environment
```bash
# Activate virtual environment first
.\.venv\Scripts\activate

# Run the tool
python KeyLogger.py

# Press ESC to stop and send report
```

---

## 📁 Project Structure

```
Advanced-Keylogger/
├── .gitignore              # Must exclude .env and generated files
├── .env.example           # Template for configuration
├── LICENSE                # Educational Use Only
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── KeyLogger.py           # Main script
└── predefwords.txt        # Keyword list for alerts
```

---

## 🔧 Configuration Options

Edit variables in `.env` or script header:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `MICROPHONE_TIME` | Audio recording duration (seconds) | 10 |
| `FILE_PATH` | Directory for log files | `D:\Cyber\...` |
| `email_address` | Sender email (SMTP) | From `.env` |
| `predefined_words_file` | Keyword list path | `predefwords.txt` |

---

## 🐛 Known Issues & Internship TODOs

| Issue | Severity | Recommended Fix |
|-------|----------|-----------------|
| Typo in `clipbortd_infomation` | Low | Refactor variable naming |
| Broken keyword detection logic | Medium | Debug `temp` buffer concatenation |
| No encryption of log files | **High** | Implement Fernet encryption |
| Hardcoded default paths | Medium | Use relative paths + os.path.join() |
| Single-threaded blocking | Low | Add threading for audio capture |
| Missing error handling | Medium | Add try/except for SMTP failures |

**Internship Goal:** Refactor v2.0 with encryption, improved stealth, and defensive countermeasure integration.

---

## ⚖️ License

**Educational Use Only License**  
This project is licensed for academic and authorized security research only. Commercial or malicious use is strictly prohibited.

---

## 📞 Support

**For internship-related queries:**
- **Supervisor:** [Your Supervisor's Name]
- **Institution:** [Your Institution Name]

---

<p align="center">
<strong>🔬 "To defeat an attacker, you must think like one – but act with integrity."</strong>
</p>

---

**Last Updated:** 2025-11-10  
**Version:** 1.0-Internship  
**Author:** Harshith Sai Chand
