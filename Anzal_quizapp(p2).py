import time     #for importing time
import threading #for calling two function a same time

# function for timer it will hit zero after 60 seconds
def countdown():
    global my_time
    my_time = 60
    for x in range(my_time):
        my_time= my_time-1
        timer =f'                                        Time: 00:{my_time:02}'
        print (timer,end = '\r')
        time.sleep(1) #for delaying execution for one second
        
# questions , options and answers are displayed when we call the function 
def quiz_content():
    # questions will be on a while loop till the timer hits zero
    while my_time > 0: 
        
        # questions and answers are stored in a list
        questions = ["Q(1): How many colors are there in a rainbow ?\n",
                    "Q(2): Which is smallest planet in our solar system?\n",
                    "Q(3): General Election in India hold after how many years?\n",
                    "Q(4): Which is smallest continent in the world?\n",
                    "Q(5): Who is the first prime minister of India?\n"]

        options   = [['(a) 10', '(b) 9', '(c) 7', '(d) 11'],
                    ['(a) Earth   ', '(b) Mars', '(c) Mercury',  '(d) Saturn'],
                    ['(a) 2', '(b) 10', '(c) 6', '(d) 5'],
                    ['(a) Asia', '(b) Australia', '(c) Europe', '(d) Antartica'],
                    ['(a) Indira Gandhi', '(b) Jawaharlal Nehru', '(c) Narendra Modi ','(d) Motilal Nehru']]

        answers = ['c','c','d','b','b']
        choosed_options = []
        score = 0
        question_number = 0
        print(' WELCOME TO THE QUIZ!!!!!!')
        for question in questions:
            print('=============================================')
            print(question)
            for option in options[question_number]:
                print(option)
            
            choosed_option = input('Enter (a) (b) (c) (d): \n').lower()
            #when timer hits the zero function exit he loop
            if my_time == 0:
                print("TIME'S UP !!!!!! \n")
                print(f' you scored  {(score/5)*100}% in this quiz')
                break
            if question_number + 1 == len(questions):
                print('FINISHED !!!!')
                print(f' you scored  {(score/5)*100}% in this quiz')
                break
           
            choosed_options.append(choosed_option)

            if choosed_option == answers[question_number]:
                score = score+1

           
           
            question_number = question_number + 1

        if question_number + 1 == len(questions):
            break
        
    


#method for executing both timer and questions program at the same time
timer_process = threading.Thread(target=countdown, args =())
quiz_process = threading.Thread(target=quiz_content, args = ())

timer_process.start()
quiz_process.start()







