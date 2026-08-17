import sqlite3
import os
from datetime import datetime

def secure_calculator(a: float, b: float, operation: str) -> str:
    """Безопасный калькулятор для базовых математических операций."""
    try:
        if operation == "add":
            return str(a + b)
        elif operation == "subtract":
            return str(a - b)
        elif operation == "multiply":
            return str(a * b)
        elif operation == "divide":
            if b == 0:
                return "Ошибка: Деление на ноль запрещено."
            return str(a / b)
        else:
            return f"Неизвестная операция: {operation}"
    except Exception as e:
        return f"Ошибка вычислений: {str(e)}"

def query_local_db(query_text: str) -> str:
    """Выполняет безопасный read-only SQL-запрос к локальной тестовой базе данных."""
    # Защита: разрешаем только SELECT запросы, блокируем опасные ключевые слова
    forbidden = ["drop", "delete", "insert", "update", "alter", "truncate", "create"]
    lower_query = query_text.lower()
    if any(word in lower_query for word in forbidden):
        return "Ошибка безопасности: Разрешены только операции чтения (SELECT)."
    
    db_path = "local_data.db"
    # Создадим тестовую базу, если её нет
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS info (id INTEGER PRIMARY KEY, topic TEXT, content TEXT)")
        cursor.execute("INSERT OR IGNORE INTO info (id, topic, content) VALUES (1, 'security', 'All inputs must be strictly validated.')")
        cursor.execute("INSERT OR IGNORE INTO info (id, topic, content) VALUES (2, 'internship', 'Task 2 requires multi-tool orchestration.')")
        conn.commit()
        conn.close()

    try:
        # Открываем соединение строго в режиме read-only через URI
        conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
        cursor = conn.cursor()
        cursor.execute(query_text)
        rows = cursor.fetchall()
        conn.close()
        return str(rows)
    except Exception as e:
        return f"Ошибка при запросе к БД: {str(e)}"

def get_system_time() -> str:
    """Возвращает текущее системное время и дату."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")