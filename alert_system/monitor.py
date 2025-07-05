from alert_system.config import load_config
from alert_system.log_checker import scan_log
from alert_system.mailer import send_email

def main():
    config = load_config("config.yaml")
    log_path = config['log_path']
    error_keywords = config['error_keywords']

    errors = scan_log(log_path, error_keywords)

    if errors:
        send_email(config, errors)
        print(f"Alert sent for {len(errors)} errors.")
    else:
        print("No errors found.")

if __name__ == "__main__":
    main()
