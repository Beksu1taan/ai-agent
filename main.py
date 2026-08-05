from agent import SecureAgent

def main():
    print("Инициализация Secure AI Agent...")
    try:
        agent = SecureAgent()
    except Exception as e:
        print(f"Ошибка запуска: {e}")
        return

    print("Агент готов! (введите 'exit' для выхода)")
    print("-" * 40)
    
    while True:
        try:
            user_input = input("\nВы: ")
            if user_input.lower().strip() in ['exit', 'quit', 'выход']:
                print("Завершение работы.")
                break
                
            if not user_input.strip():
                continue
                
            response = agent.run(user_input)
            print(f"Агент: {response}")
            
        except KeyboardInterrupt:
            print("\nПринудительное завершение.")
            break
        except Exception as e:
            print(f"\nСбой в интерфейсе: {e}")

if __name__ == "__main__":
    main()