class Wordy:
    math_str =[]

    math_Exp={
            "plus":"+",
            "minus":"-",
            "multiplied":"*",
            "divided":"/",
            "times":"*",
            "raised":"**"
             }

    def __init__(self, inputstr):
        self.inputstr = inputstr
        try:
            self.calculate = self.calculate(inputstr)
        except Exception as e:
            print(e)

    def plus(self, a, b):
        return a+b

    def minus(self, a, b):
        return a-b

    def multiplied(self, a, b):
        return a*b

    def divided(self, a, b):
        return a/b

    def times(self, a, b):
        return a*b

    def raised(self, a, b):
        return a**b

    def initilise(self,value, a, b):
        initilise_exp_result = 0
        if value == "plus":
            initilise_exp_result = self.plus(a, b)
        if value == "minus":
            initilise_exp_result =  self.minus(a, b)
        if value == "multiplied":
            initilise_exp_result = self.multiplied(a, b)
        if value == "divided":
            initilise_exp_result = self.divided(a, b)
        if value =="times":
            initilise_exp_result = self.times(a, b)
        if value =="raised":
            initilise_exp_result = self.raised(a, b)
        return initilise_exp_result

    def is_expression(self, chunk):
        result = map(lambda x:x==chunk,self.math_Exp)
        result.sort()
        result.reverse()
        return result[0]

    def process_string(self, inputstr):
        splited = inputstr.split()
        for chunk in splited[2:len(splited)]:
            try:
                newstr = chunk.replace("?", "").replace("th", "")
                self.math_str.append(int(newstr))
            except:
                if self.is_expression(chunk):
                    self.math_str.append(chunk)

    def calculate(self, inputstr):
        self.process_string(inputstr)
        exprn_vlu =self.math_str
        expression_result1 = self.initilise(exprn_vlu[1],exprn_vlu[0],exprn_vlu[2])
        if len(exprn_vlu) > 3:
            expression_result2 = self.initilise(exprn_vlu[3],expression_result1,exprn_vlu[4])
            return expression_result2
        else :
            return expression_result1


test1 = Wordy("What is 22  minus 3?")
print test1.calculate
