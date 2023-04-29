class my_error(Exception):
    pass
while True:    
    try:
        a = input("Введите число: ")
        b = input("Введите второе число: ")
        c = int(a)/int(b)
        if c == 5:
            raise my_error("Я против 5")
    except ZeroDivisionError as e:
        print("На ноль делить нельзя", e)
    except ValueError:
        print("Поддерживаются только числа")
    else:
        print(c)
        break
    finally:
        print("Конец программы")
