#when you need a list of repetitive strings that has a number that increases, you can create an f string with a limit of how many times to repeat this

inc_num = 1
while inc_num <= 365:
    print(f"if num == {inc_num}:")
    inc_num += 1