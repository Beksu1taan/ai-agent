import os
from dotenv import load_dotenv
from agent import MultiToolAgent

# Загружаем ключи из .env
load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    print("Ошибка: ANTHROPIC_API_KEY не найден в переменных окружения!")
    exit(1)

def main():
    print("Инициализация Multi-Tool Secure AI Agent...")
    agent = MultiToolAgent(api_key=api_key)
    print("Агент готов! (введите 'exit' для выхода)")
    
    while True:
        try:
            user_input = input("\nВы: ")
            if user_input.lower() in ["exit", "выход"]:
                print("Завершение работы.")
                break
            
            if not user_input.strip():
                continue
                
            response = agent.run(user_input)
            print(f"Агент: {response}")
            
        except KeyboardInterrupt:
            print("\nЗавершение работы.")
            break

if __name__ == "__main__":
    main()