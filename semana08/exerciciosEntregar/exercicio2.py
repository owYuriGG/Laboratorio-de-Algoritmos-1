def primo(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
            else:
             return True

print((primo(7)))