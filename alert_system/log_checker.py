import os

def scan_log(log_path, error_keywords):
    if not os.path.exists(log_path):
        return []

    errors_found = []
    with open(log_path, 'r') as f:
        for line in f:
            for keyword in error_keywords:
                if keyword in line:
                    errors_found.append(line.strip())
    return errors_found
