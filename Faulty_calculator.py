operator=input("Enter the operator to perform calculation:")

operand1,operand2=input("Enter the required operands:").split()

list1= ['45*3','56+9','56/6']
op1=int(operand1)
op2=int(operand2)
if (operand1+operator+operand2) not in list1:

    if operator=="+":
        x=op1+op2
        print(operand1+operator+operand2+"=",x)
    elif operator=="-":
        x=op1+op2
        print(operand1+operator+operand2+"=",x)
    elif operator=="*":
        x=op1*op2
        print(operand1+operator+operand2+"=",x)
    elif operator=="/":
        x=op1/op2
        print(operand1+operator+operand2+"=",x)
    
elif op1==45 and op2==3 and operator=='*':
    print("The required calculated solution is:",operand1,operator,operand2,"=",555)
elif op1==56 and op2==9 and operator=='+':
    print("The required calculated solution is:",operand1,operator,operand2,"=",77)
elif op1==56 and op2==6 and operator=='/':
    print("The required calculated solution is:",operand1,operator,operand2,"=",4)
