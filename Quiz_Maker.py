from random import shuffle, randint
import re

# From file quiz.txt first separate questions from answers and put them in separate files.
quiz_file = open('C:\\Users\\Kaja\\Desktop\\MY-PROJECTS\\quiz.txt','r+')
lines = quiz_file.readlines()
questions = []
answers = []
# unique id for every question-answer pair:
line_id = 0

for line in lines:
    line_id += 1
    line = str(line_id) + '_' + line
    questions.append(line.split('?')[0] + '?' + '\n')
    shuffle(questions)
    answers.append(str(line_id) + '_' + line.split('?')[1])
    shuffle(answers)

def open_file(file_string, file_array):
    file = open(file_string, 'w+');
    for el in file_array:
        file.write(el)
    file.close()
    return file

questions_file = open_file('C:\\Users\\Kaja\\Desktop\\MY-PROJECTS\\questions.txt', questions)
#for question in questions:
    #questions_file.write(question)
#questions_file.close()

answers_file = open_file('C:\\Users\\Kaja\\Desktop\\MY-PROJECTS\\answers.txt', answers)
#for answer in answers:
    #answers_file.write(answer)
#answers_file.close()

quiz_file.close()


# creating quiz of 10 questions:
quiz_on = True
while quiz_on:
    questions_file = open('C:\\Users\\Kaja\\Desktop\\MY-PROJECTS\\questions.txt','r+')
    question_id = 0
    quiz_questions = []

    # list of 10 random lines in questions file
    pick_question = []
    for i in range(1,11):
        pick_question.append(randint(1,100))

    for question in questions_file:
        question_id += 1
        if question_id in pick_question:
            quiz_questions.append(question)

    questions_file.close()

    # finding answers to the 10 questions:
    answers_file = open('C:\\Users\\Kaja\\Desktop\\MY-PROJECTS\\answers.txt','r+')
    quiz_answers = []
    for question in quiz_questions:
        for answer in answers:
            # if answer and question have the same unique id:
            if answer[0:2] == question[0:2]:
                quiz_answers.append(answer)
    answers_file.close()

    # defining quiz as dictionary, where key is question and value is answer
    quiz = {}
    for question in quiz_questions:
        for answer in quiz_answers:
            if question[0:2] == answer[0:2]:
                quiz[question] = answer

    # collecting user answers to all 10 questions and matching them with correct answers
    user_answers = []
    correct_answers = []
    wrong_answers = []
    for question in quiz_questions:
            # displaying question without unique id at the beginning:
            user_answer = input(question.split('_')[1])
            if user_answer != '' and re.search(user_answer.lower(), quiz[question].lower()):
                correct_answers.append(user_answer)
            else:
                wrong_answers.append(user_answer)

    if len(correct_answers) > len(wrong_answers):
        print('Congrats! You had {} correct answers and {} wrong answers.'.format(len(correct_answers), len(wrong_answers)))
        print('Wrong answers are:')
        print(wrong_answers)
    else:
        print('Oops! You had {} wrong answers and {} correct answers.'.format(len(wrong_answers), len(correct_answers)))
        print('Wrong answers are:')
        print(wrong_answers)

    if input('Would you like to take another quiz? (y/n)').lower()[0] == 'y':
        quiz_on = True
    else:
        quiz_on = False
