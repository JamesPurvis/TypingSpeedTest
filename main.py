import math
import random
import time

def start_test():
    user_input = input("Hello, what is your name? ")

    if check_name(user_input) == False:
        print("Welcome to the typing test, " + user_input)
        user_prompt = generate_prompt()
        print(user_prompt)
        start_time = time.time()
        user_try = input('Try your luck and copy the prompt:')
        print('It looks like you scored ' + str(calc_result(user_try, user_prompt)) + "% and it took you " + calc_time_elapsed(start_time))
    else:
        print("Please enter a valid name!")
        start_test()


def calc_time_elapsed(start_time):
  stop_time = time.time()
  elapsed_time = stop_time - start_time

  if elapsed_time > 60:
      elapsed_time_mins = math.floor(elapsed_time / 60)
      return str(elapsed_time_mins) + " " + "minutes!"
  else:
      return str(math.floor(elapsed_time)) + " " + "seconds!"

import math

def calc_result(user_try, user_prompt):
    possible_correct = len(user_prompt)
    character_diff = possible_correct - len(user_try)
    wrong_char_score = 0

    for i in range(len(user_try)):
        if user_try[i] != user_prompt[i]:
            wrong_char_score += 1

    true_wrong = character_diff + wrong_char_score

    if true_wrong != 0:
        percentage = possible_correct / true_wrong
    else:
        percentage = 100

    return math.floor(percentage)







def check_name(user_name):
    if len(user_name) == 0 or user_name.isspace():
        return True
    else:
       return False

def generate_sentence():
    subjects = ['I', 'You', 'He', 'She', 'They']
    verbs = ['eat', 'sleep', 'drink', 'play', 'read']
    objects = ['pizza', 'tacos', 'pepperonis', 'hamburgers']

    subject = random.choice(subjects)
    verb = random.choice(verbs);
    object = random.choice(objects)

    sentence = subject + " " + verb + " " + object

    return sentence

def generate_prompt():
    prompt = ""
    for a in range(40):
       prompt = prompt + generate_sentence() + " "

    return prompt







if __name__ == "__main__":
    start_test()





