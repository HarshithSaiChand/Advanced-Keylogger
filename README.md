# Advanced-Keylogger

&gt; **🔒 Educational Cybersecurity Research Tool**  
&gt; **⚠️ Authorized Testing & Internship Project Only**

A Python-based keystroke monitoring tool with **AES encryption**, **application-specific targeting**, and **automated email exfiltration** for authorized security research in controlled environments.

---

## ⚠️ Ethical Use Declaration

**This software is intended EXCLUSIVELY for:**
- ✅ Authorized penetration testing in isolated lab environments
- ✅ Academic cybersecurity education with institutional approval
- ✅ Personal system security auditing on hardware you own
- ✅ Defensive tool development and testing

**Absolutely prohibited for:**
- ❌ Unauthorized surveillance or monitoring
- ❌ Deployment on systems without explicit written consent
- ❌ Malicious intent or illegal activities

**This code contains hardcoded configurations for demonstration purposes only.**

---

## 🎯 Features

| Capability | Description | Implementation |
|------------|-------------|----------------|
| **Keystroke Logging** | Records all keyboard input with real-time analysis | `pynput` library |
| **AES Encryption** | Encrypts logs using Fernet (symmetric encryption) | `cryptography.fernet` |
| **App-Specific Monitoring** | Only logs when Chrome/Edge are active | `pygetwindow` |
| **Keyword Detection** | 50+ predefined sensitive keywords trigger alerts | Hardcoded list |
| **Special Character Alerts** | Immediate email on symbols like `$`, `%`, `|` | Hardcoded list |
| **Clipboard Capture** | Monitors cut/copy/paste operations | `pyclip` library |
| **Automated Exfiltration** | Emails logs via Gmail SMTP | `smtplib` + TLS |
| **Encrypted Storage** | Logs stored encrypted, decrypted on-demand | `.encrypted` files |

---

## 📁 Repository Structure
