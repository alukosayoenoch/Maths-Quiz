# Maths-Quiz
import time
import math

print("Hi guys, I am a Mathemagician developed by Aluko")
print("Aluko is of the opinion that, I defies all Scratch/mBblock GUI Maths' Wizard, If you care to try out my ingenious endowment, can I know your name?")
Name=input("Type your name here: ")
print("How are you doing today?",Name)

def main() :
   
   menu_option = input("""I can help you with the following Mathematical problems? Input the corresponding number: 
1 = Addittion
2 = Subtraction
3 = Multiplication
4 = Division
5 = Sin Cosine Tan
6 = Square Root
7 = Quadratic Equation
""")
   var1 = float(input('Enter the first value: '))
   var2 = float(input('Enter the second value: '))
   if menu_option == '1':
      print (var1,'+', var2)
      time.sleep(1)
      print (var1+var2)
      time.sleep(2)
      main()
   if menu_option == '2':
      print (var1,'-', var2)
      time.sleep(1)
      print (var1-var2)
      time.sleep(2)
      main()
   if menu_option == '3':
      print (var1,'*', var2)
      time.sleep(1)
      print (var1*var2)
      time.sleep(2)
      main()
   if menu_option == '4':
      print (var1,'/', var2)
      time.sleep(1)
      print (var1/var2)
      time.sleep(2)
      main()
   if menu_option == '5':
      print ('Sine, Cosine and Tan are: ')
      time.sleep(2)
      a=math.sin(math.radians(var1))
      b=math.cos(math.radians(var1))
      c=math.tan(math.radians(var1))
      d=math.sin(math.radians(var2))
      e=math.cos(math.radians(var2))
      f=math.tan(math.radians(var2))
      print ("The sine of", var1, "is:",a)
      print ("The cosine of", var1, "is:",b)
      print ("The tan of", var1, "is:",c)
      print ("The sine of", var2, "is:",d)
      print ("The cosine of", var2, "is:",e)
      print ("The tan of", var2, "is:",f)
      time.sleep(2)
      main()
   if menu_option == '6':
      print ("Square Root of variables")
      time.sleep(1)
      g=math.sqrt(var1)
      h=math.sqrt(var2)
      print ("Square Root of", var1, "is:",g)
      print ("Square Root of", var2, "is:",h)
      time.sleep(2)
      main()
   if menu_option == '7':
      print ("To find the roots of Equations enter the coefficient of X^2, X and the constant value, C")
      time.sleep(1)
      a=float(input("Type the coefficient of X^2: "))
      b=float(input("Type the coefficient of X: "))
      c=float(input("Type the constant value: "))
      step1= float(b*b)
      step2= float(step1 - 4*a*c)
      step3= math.sqrt(step2)
      step4= float(-b + step3)
      step6= float(2*a)
      step5= float(-b - step3)
      step7= float(step4 / step6)
      step8= float(step5 / step6)
      print ("The roots of the equations are :", step7, "and", step8)
      time.sleep(2)
      main()
   
   else:
      print ('Error, Your input is invalid, please try again')
      time.sleep(1)
      main()

main()
