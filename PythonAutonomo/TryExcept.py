try:
    intriger = int(input("Insert intriger"))
except ValueError:
    print("Something went wrong")
finally:
    print("TryExcept finished")
