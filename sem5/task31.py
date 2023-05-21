##31. Найти n-ое число Фибоначчи
def fib(n):
    if n in [0,1]:
        return n
    return fib(n-1) + fib(n-2)
n = int (input("Enter a number: "))
print(f"The lement #(n) of Fibo sequence is: {fib(n)}")