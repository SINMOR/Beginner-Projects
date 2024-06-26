# a dictionary that stores questions and answers 
# have a variable that tracks the score of the player 
# loop through the dictionary using the key values pairs
# display each question to the user and allow them to answer
# tell them if they are right or wrong  
# show the final result  when quiz is completed 

quiz = {
    'question1':{
        'question': 'What is the capital of France',
        'answer':'Paris'
    },
    'question2':{
        'question':'What is the capital of Germany',
        'answer': 'Berlin '
    },
    'question3':{
        'question':'What is the capital of Kenya ',
        'answer': 'Nairobi '
    },
    'question4':{
        'question':'What is the capital of Morocco',
        'answer': 'Rabat '
    },
    'question5':{
        'question':'What is the capital of Switzerland',
        'answer': 'Bern '
    },
    'question6':{
        'question':'What is the capital of Uganda',
        'answer': 'Kampala '
    },
    'question7':{
        'question':'What is the capital of Tanzania',
        'answer': 'Arusha '
    }
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input('Answer? ')
    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1 
        print(f'Your score is: {score} ')
    else:
        print('Incorrect')
        print(f'The correct answer is: {value["answer"]}')
        print(f'Your score is: {score} ')
        
print(f'You got {score} out of 7 questions correctly')
print(f'Your percentage is {score/7*100}')