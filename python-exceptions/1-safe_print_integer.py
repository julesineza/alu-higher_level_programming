def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except:
        return False        


value1=1
value2="jules"
safe_print_integer(value2)

