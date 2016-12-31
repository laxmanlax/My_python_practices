class Say:
    NUMS = {
        1000000000: 'billion',
        1000000: 'million',
        1000: 'thousand',
        100:'one hundred',
        90: 'ninety',
        80: 'eighty',
        70: 'seventy',
        60: 'sixty',
        50: 'fifty',
        40: 'forty',
        30: 'thirty',
        20: 'twenty',
        19: 'nineteen',
        17: 'seventeen',
        16: 'sixteen',
        15: 'fifteen',
        14: 'fourteen',
        13: 'thirteen',
        12: 'twelve',
        11: 'eleven',
        10: 'ten',
        9: 'nine',
        8: 'eight',
        7: 'seven',
        6: 'six',
        5: 'five',
        4: 'four',
        3: 'three',
        2: 'two',
        1: 'one',
        0: ''
    }

    def __init__(self, num):
        self.num = num
        if num == 0:
            self.word = 'zero'
        elif num == 100:
            self.word = self.get_val(num)
        else:
            self.word = self.numtoword(num)

    def numtoword(self, num):
        self.num_validation(num)
        print self.breaknumber(num)
        findnum = self.breaknumber(num)
        translate = ''
        if findnum[0]:
            translate += self.name_values(int(findnum[0])) +" "+"billion"
        if findnum[1]:
            if self.name_values(int(findnum[1])) == "":
                pass
            else:
                translate += " "+self.name_values(int(findnum[1])) +" "+"million"
        if findnum[2]:
            if self.name_values(int(findnum[2])) == "":
                pass
            else:
                translate += " "+self.name_values(int(findnum[2])) +" "+"thousand"
        if findnum[3]:
            translate += " "+self.name_values(int(findnum[3]))

        return translate

    def breaknumber(self, num):
        mapdicnry = {0: '', 1: '', 2: '', 3: ''}
        value = str(num)[::-1]
        revvalue = [value[i:i + 3] for i in range(0, len(value), 3)][::-1]
        mapvalue = map(lambda x:x[::-1],revvalue)
        print mapvalue

        if len(mapvalue)==1:
            mapdicnry[3]=mapvalue[0]
        if len(mapvalue)==2:
            print "here"
            mapdicnry[2]=mapvalue[0]
            mapdicnry[3]=mapvalue[1]
        if len(mapvalue)==3:
            mapdicnry[1]=mapvalue[0]
            mapdicnry[2]=mapvalue[1]
            mapdicnry[3]=mapvalue[2]
        if len(mapvalue)==4:
            mapdicnry[0]=mapvalue[0]
            mapdicnry[1]=mapvalue[1]
            mapdicnry[2]=mapvalue[2]
            mapdicnry[3]=mapvalue[3]
        return mapdicnry

    def name_values(self, num):
        value_str = ''
        hundreds_digit, left_over = divmod(num, 100)
        tens_digit, ones_digit = divmod(left_over, 10)
        if hundreds_digit == 0:
            if left_over >= 10 and left_over <= 20:
                 value_str += self.get_val(left_over)
            else:
                value_str +=  self.get_val(tens_digit*10) +"-"+ self.get_val(ones_digit)
        else:
            if left_over >= 10 and left_over <= 20 and hundreds_digit > 0:
                value_str += self.get_val(hundreds_digit) +" "+"hundred"+" "+"and" +" "+self.get_val(left_over)
            else:
                value_str += self.get_val(hundreds_digit) +" "+ "hundred" +" "+"and"+" "+ self.get_val(tens_digit*10) + "-" +self.get_val(ones_digit)

        if hundreds_digit ==0 and tens_digit ==0:
            value_str = ''
            value_str += self.get_val(ones_digit)

        return value_str

    def num_validation(self, num):
        if num < 0 or num > 999999999999:
            raise AttributeError

    def get_val(self, d):
        return self.NUMS[d]


def say(num):
    check = Say(int(num))
    return check.word.lstrip()
