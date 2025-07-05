# python-alert-system
Python-based alert system to monitor logs and send failure notifications via email.

# Python Alert System

A simple Python-based alert system to monitor job logs or runtime conditions and send email/SMS alerts upon failure or anomalies.

##  Features
- Monitors log files for error patterns
- Sends alerts via email (SMTP)
- Extendable to SMS or Teams/Webhooks
- Configurable schedule and thresholds

## Tech Stack
- Python 3.x
- `smtplib` / `email`
- `logging`, `argparse`, `schedule`
- Optional: Azure Logic App or SendGrid API

## Usage

```bash
python alert_system/monitor.py --config alert_config.yaml
