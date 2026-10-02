# AWS Cloud Environment Manager & Cost Optimizer

A production-ready serverless cloud governance solution that automates cost optimization, environment scheduling, and disaster recovery on AWS using Python Lambda functions and EventBridge.

---

## 📐 Architecture Overview

- **Web Tier:** Flask application running on Gunicorn, deployed using **AWS Elastic Beanstalk (PaaS)**.
- **Automation Engine:** **AWS Lambda (Python 3.9+)** triggered via **Amazon EventBridge Scheduler** rules using CRON expressions.
- **Security:** Granular **IAM Role and Custom Policy** following the Principle of Least Privilege.
- **Governance Strategy:** Tag-based management targeting resources with `Environment: Development`.

---

## 🛠️ Components & Features

1. **EC2 Scheduler (`ec2_scheduler.py`):**
   - Scans EC2 instances filtered by tag `Environment=Development`.
   - Automatically stops instances during off-peak hours (e.g., nightly at 8 PM) to prevent unnecessary billing.

2. **EBS Automated Backup (`ebs_backup.py`):**
   - Identifies active EBS volumes connected to development instances.
   - Triggers automated EBS snapshot creation with tracking tags for compliance.

3. **Least Privilege Security Policy (`iam/lambda_policy.json`):**
   - Custom IAM policy scoped specifically to necessary EC2 execution actions (`StartInstances`, `StopInstances`, `CreateSnapshot`) and CloudWatch logging.

---

## 📁 Repository Structure

```text
cloud-environment-manager/
├── app/
│   ├── app.py
│   └── requirements.txt
├── lambda/
│   ├── ec2_scheduler.py
│   └── ebs_backup.py
├── iam/
│   └── lambda_policy.json
└── README.md

🚀 Deployment Steps
1. Web Dashboard (Elastic Beanstalk)

cd app
zip -r app.zip app.py requirements.txt

2. Security Configuration
Create an IAM Policy using iam/lambda_policy.json and attach it to an IAM Role dedicated to AWS Lambda.

3. Serverless Functions
Deploy lambda/ec2_scheduler.py and lambda/ebs_backup.py as AWS Lambda functions assigned to the created IAM Role.

4. Scheduling
Create EventBridge Scheduler rules:

Nightly Shutdown: cron(0 20 * * ? *) targeting ec2_scheduler with payload {"action": "stop"}.

Daily Backup: cron(0 23 * * ? *) targeting ebs_backup.