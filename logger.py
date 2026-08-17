import os
import re
from datetime import datetime

def log_event(message: str):
    """Безопасно логирует событие, маскируя ключи и токены."""
    os.makedirs("logs", exist_ok=True)
    
    masked_message = re.sub(r'sk-ant-[a-zA-Z0-9\-_]+', '[REDACTED_API_KEY]', message)
    
    log_entry = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {masked_message}\n"
    
    with open("logs/agent_audit.log", "a", encoding="utf-8") as f:
        f.write(log_entry)