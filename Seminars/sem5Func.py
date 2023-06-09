def NFib(n) :
    if n in [0,1]:
        return n
    return NFib( n - 1) + NFib(n - 2) 

def IsSimple(number):
    if number > 2 and number % 2 !=0:
        for i in range(3, number // 2):
            if number % i == 0:
                return False
        return True
    else:
        return False
    
def ReverseRange(num):
    print(num, end=' ')
    if num > 0:
        return ReverseRange(num - 1)
    