from logger import logger

def secure_calculator(a: float, b: float, operation: str) -> str:
    """
    Безопасный калькулятор. Никаких eval(), только строгая проверка операций.
    """
    logger.info(f"Tool call: secure_calculator(a={a}, b={b}, operation='{operation}')")
   
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        logger.warning("Попытка передать нечисловые значения в калькулятор.")
        return "Ошибка: Аргументы должны быть числами."

    if operation == "add":
        return str(a + b)
    elif operation == "subtract":
        return str(a - b)
    elif operation == "multiply":
        return str(a * b)
    elif operation == "divide":
        if b == 0:
            return "Ошибка: Деление на ноль невозможно."
        return str(a / b)
    else:
        logger.warning(f"Попытка использовать неизвестную операцию: {operation}")
        return "Ошибка: Неизвестная операция. Разрешены только add, subtract, multiply, divide."

CALCULATOR_TOOL_SCHEMA = {
    "name": "secure_calculator",
    "description": "Perform basic arithmetic operations on two numbers. Do NOT try to calculate mathematically without using this tool.",
    "input_schema": {
        "type": "object",
        "properties": {
            "a": {"type": "number", "description": "First number"},
            "b": {"type": "number", "description": "Second number"},
            "operation": {
                "type": "string",
                "enum": ["add", "subtract", "multiply", "divide"],
                "description": "The mathematical operation to perform"
            }
        },
        "required": ["a", "b", "operation"]
    }
}