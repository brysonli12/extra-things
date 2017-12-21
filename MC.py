# MC Practice
# 12/21/2017
# A simple way of keeping track of your MC answers (or answers to anhy set of questions).
# stores your answers in a file you specify

print "Hello, welcome to MC pratice."

print "Please enter the name of your task today."

task = raw_input("=> ")

print "File to be created: ", task, ".txt"


f = open(task.replace('\n', '') + ".txt", "w")

print "-----------------------------"
print "   ENTER \"quit\" to quit"
print "-----------------------------"

questionNum = 1
try:
  while task != "quit":
    task = raw_input(str(questionNum) + ". ")
    if task != "quit":
        f.write(str(questionNum) + ". " + task + "\n")
        questionNum+= 1

print "#End of session"/
