# 🚀 Automatic Website Deployment to AWS EC2 using GitHub Actions & Paramiko

## 📌 Project Overview

This project demonstrates a complete **CI/CD (Continuous Integration & Continuous Deployment)** pipeline for automatically deploying a website hosted on an AWS EC2 instance.

Whenever changes are pushed to the **main** branch, GitHub Actions automatically:

- Detects the code changes
- Installs the required Python packages
- Creates a temporary SSH key from GitHub Secrets
- Connects securely to the EC2 instance using Paramiko
- Uploads the updated HTML file
- Replaces the existing website hosted by Apache

No manual deployment is required.

---

## 🛠️ Technologies Used

- Python
- Flask
- Git
- GitHub
- GitHub Actions
- Paramiko
- AWS EC2
- Apache Web Server
- SSH

---

## 📂 Project Structure

```
AWS_EC2_AUTOMATION/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── templates/
│   └── index.html
│
├── app.py
├── deploy.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Workflow

```
Developer
     │
     ▼
Modify HTML File
     │
     ▼
Git Push
     │
     ▼
GitHub Repository
     │
     ▼
GitHub Actions
     │
     ▼
Install Python Dependencies
     │
     ▼
Create SSH Key from GitHub Secrets
     │
     ▼
Paramiko SSH Connection
     │
     ▼
AWS EC2 (Ubuntu)
     │
     ▼
Apache Web Server
     │
     ▼
Website Updated Automatically
```

---

## 🔐 GitHub Secrets

The following repository secrets are required:

| Secret Name | Description |
|-------------|-------------|
| EC2_HOST | EC2 Public IP Address |
| EC2_USERNAME | SSH Username (ubuntu) |
| EC2_KEY | Complete contents of the EC2 Private Key (.pem) |

---

## 🚀 Deployment Process

1. Edit `templates/index.html`
2. Commit the changes

```bash
git add .
git commit -m "Updated Website"
git push origin main
```

3. GitHub Actions automatically starts.
4. Paramiko connects to the EC2 instance.
5. The updated HTML file is copied to:

```
/var/www/html/index.html
```

6. Refresh the website to see the latest changes.

---

## ▶️ Run Flask Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser:

```
http://localhost:5000
```

---

## 📦 GitHub Actions

The workflow automatically executes on every push to the **main** branch.

Workflow file:

```
.github/workflows/deploy.yml
```

---

## 📸 Project Demo

### Local Development

- Flask Application
- HTML Template

### Automated Deployment

- Git Push
- GitHub Actions Trigger
- Paramiko SSH
- AWS EC2
- Apache Web Server
- Live Website Updated

---

## 🎯 Features

- Automated Deployment
- Secure SSH Authentication
- GitHub Actions CI/CD
- Paramiko-Based Deployment
- Apache Web Server Hosting
- AWS EC2 Integration
- Zero Manual File Upload

---

## 📈 Future Enhancements

- Deploy complete website (HTML, CSS, JS, Images)
- Multi-file synchronization
- Docker support
- Nginx deployment
- AWS CodeDeploy integration
- SSL using Let's Encrypt
- Rollback on deployment failure

---

## 👩‍💻 Author

**Dipali Patil**

AWS | DevOps | Python | Cloud Computing Enthusiast

---
