#Maths Quiz - ALUKO SAYO ENOCH
import time
#Welcoming address
print("Dare to create your Dream World, with...PYTHON PROGRAMMING!!!")
time.sleep(2)
print('Mortal Combat saga: choose your destiny: mBlock/Scratch or Python Programming!!!')
print('')
print('Remember to press "Enter" key after every question')
time.sleep(1)
name=input('Type your name here: ')
time.sleep(1)
print('Good morning', name + '!' +  ' happy to have you on our quiz Show!!!!')
print('')
print('Sage Mode Naruto vs Itachi, Round 1:Let Play some trick before the quiz show!!!')
Gender = input('Enter your Gender here: ')
if  Gender == 'female' or Gender == 'male' :
    print ('Are you a Programming Freak?' , name)
    time.sleep(1)
else:
    print('I guess you are a Scratch or mBlock code titan!')
    time.sleep(1)  
    print('')
response= input("Type Yes, if Yes or No , if not!!!")
if response == 'Yes' or  response == 'yes' :
    print ('You should be proud of yourself and dare to be a problem solver!!!', name)
    time.sleep(1)
elif response == 'No' or  response == 'no' :
    print('I guess you are a Scratch or mBlock code titan!', name)
    time.sleep(1)
else:
    print ('Error, calling.... 999!!!, I suspect, you are an intruder, RIGHT!, leave this place now, else I will call for your arrest')
    time.sleep(1)
#============== Score Board Syntax============================
def main():
    import random
    questions={}
    score = 0


    for i in range(5):
        int_a = random.randint(0,5)
        int_b = random.randint(0,20)
        operators = ['+','-','*']
        operator_value = random.choice(operators)
        question = str(int_a)+''+str(operator_value)+''+str(int_b)
        answer = eval(question)
        question+=': '

        questions.update({question:str(answer)})


    for q in questions.keys():
        user_answer=input(q)
        if questions.get(q)== str(user_answer):
            score+=1
            print('Correct!')
        else:
            print('Incorrect')
    print('You got' , str(score), 'correctly, out of 5 questions,',  name,', flawless victory!')
    main()
main()
