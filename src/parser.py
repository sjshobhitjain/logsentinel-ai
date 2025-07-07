import re

def parse_line(line):
    pattern = r'^(\w{3} \d+ \d+:\d+:\d+) (\S+) (\S+): (.+)'
    match = re.match(pattern, line)
    if match:
        timestamp, hostname, service, message = match.groups()
        return {
            "timestamp": timestamp,
            "hostname": hostname,
            "service": service,
            "message": message
        }
    return None
