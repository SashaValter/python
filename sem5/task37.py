# введите число и выведите строку из чисел (n:0)
def revers_str(n: int) -> None:# в данном случае функция не возвращает ничего, требуется для завершения вызова рекурсии
    print(n, end=" ")
    if n == 0:
        return
    else:
        revers_str(n-1)
n = int(input("введите число: "))
revers_str(n)