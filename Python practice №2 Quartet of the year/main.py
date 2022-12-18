while True:
    def quartet__of__year(month):
        if month in range(1, 4):
            return("First quartet")
        elif month in range(4, 7):
            return("Second quartet")
        elif month in range(7, 10):
            return("Third quartet")
        elif month in range(10, 13):
            return("Fourth quartet")
        else:
            return("No such value exists.")

    quartet = int(input())
    print(quartet__of__year(quartet))