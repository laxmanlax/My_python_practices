def isValid(s):
     validate = {
         "}": "{",
         "]": "[",
         ")": "("
     }
     test_stack =[]
     for i in s:
         if i in validate.values():
             test_stack.append(i)
        elif test_stack !=[] and validate[i]==test_stack[-1]:
            test_stack.pop()
        else:
            return False
            
    return test_stack==[] 
