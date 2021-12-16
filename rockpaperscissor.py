from random import shuffle
list1 = ['Rock','Paper','Scissor']
ui = input("What's your choice from Rock,Paper,Scissor?")
user = ui.capitalize()
shuffle(list1)
alexa = print('Alexa choice is:')
choice = print(list1[0])
Alexa = list1[0]
if user==Alexa:
    print('Yay! Both gets a point')
elif (user == 'Rock' and Alexa == 'Paper'):
    print('Alexa score a point')
elif (user =='Paper' and Alexa =='Scissor'):
    print('Alexa score a point')
elif (user =='Scissor' and Alexa =='Rock'):
    print('Alexa score a point')
else:
    print('You score a point')
