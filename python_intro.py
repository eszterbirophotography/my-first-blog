def lenght(inches):
    try:
        inches = float(inches)
        print(inches*2.54)
    except ValueError:
        print("Please type numbers only")
inches = input("Please provide number of inches:>>>")
result {'input': 'inches', 'str.[inches*2.54]': 'cm'}
lenght(inches)
