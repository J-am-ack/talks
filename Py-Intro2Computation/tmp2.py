while True:
    arr = input()
    if not arr:
        break
    letters = ['a','b','c','d','e','f','A','B','C','D','E','F']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    Find = True
    for i in arr:
        # for letter in letters:
        #     if i != letters:
        #         for number in numbers:
        #             if i == number:
        #                 Find = True\
        if i not in letters and i not in numbers:
            Find = False
    if not Find:
        print("invalid!")
    else:
        result = 0
        digit = []
        for i in arr:
            digit.append(i)
        for j in range(len(digit)):
            # fix: 你这个目前只能处理小写，处理不了大写
            # 好像也不是，字母都有点问题（？
            for p in range(len(letters)//2):
                if digit[j] == letters[p] or digit[j] == letters[p+6]:
                    digit[j] = (p+1)%6+9
        for q in range(len(digit)):
            single = int(digit[q])*16**(len(digit)-q-1)
            result = result + single
        print(result)       
