try:
    num = float(input("\nBвeдитe число: "))
except ValueError as е:
    print("Этo не число! Интерпретатор как бы говорит нам:")
    print(e)
