# import pyttsx3
# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()


file = open('lesson1.txt', 'r')


read = file.readlines()
modified = []

for line in read:
    if line[-1] == '\n':
        modified.append(line[:-1])
    else:
        modified.append(line)
print(modified)