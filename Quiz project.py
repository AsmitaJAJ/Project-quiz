import tkinter.ttk
import string

name=input("Enter your name, please: ")
quizq = [    {"question": "What is the capital of France? \na. Paris \nb. Delhi \nc. Mexico city \nd. Lucknow", "answer": "a"},
                      {"question": "What is the largest planet in our solar system? \na. Earth, \nb. Jupiter \nc.Mars \nd.Venus", "answer": "b"},
                      {"question": "Who is the author of the Percy Jackson series? \na.Random author \nb. Rick roirdan \nc. JK rowling \n d. Ceazy", "answer": "b"},
                      {"question": "What is a qubit? \na. quantum bit \nb. Bit \nc. quantum state \nd. something else", "answer": "a"},
                      {"question": "What is the largest planet in our solar system? \na. Earth, \nb. Jupiter \nc.Mars \nd.Venus", "answer": "b"},
                      {"question": "Who is the author of the Harry Potter series? \na.Random author \nb. Rick roirdan \nc. ui \n d. Ceazy", "answer": "c"}]

marks= 0
for question in quizq:
   user_answer = input(question["question"] + ": ")
   if user_answer.lower() == question["answer"].lower():
       print("Correct!")
       marks+= 1
   else:
       print("Incorrect.Correct answer is option: " ,question["answer"])
a=len(quizq)
print("You scored", marks, "out of", a, name)
if marks<(marks/a)*100<40:
    print("You have failed. Minimum pass percentage is 40%")
else:
    print("You have passed. Congrats")
