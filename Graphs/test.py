def outside():
    print('outside')

    def inside():
        print('inside')
        a = 1
        if a:
            print('a')
            return a, True
        b = 1
        if b:
            return b, True
        return False
    return inside()


print(outside())
