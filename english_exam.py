#-----------------------------------------------------------------------
# Import Modules
#-----------------------------------------------------------------------
import sys
import pandas as pd
import random

# Import the required module for text 
# to speech conversion 
from gtts import gTTS 

# This module is imported so that we can play the converted audio 
import os 

# This module is imported so that we can audio files
import playsound
#import winsound
#import pygame
#from pygame import mixer # Load the required library

#-----------------------------------------------------------------------
# Function greet()
#-----------------------------------------------------------------------
def greet(name):
    """This function greets to
    the person passed in as
    parameter"""
    print("-----------------------------------------------")
    print("-- Hello, " + name)
    print("-- Welcome to Englist Test Program     ")
    print("-----------------------------------------------")


#-----------------------------------------------------------------------
# Function play_text_to_sound
#-----------------------------------------------------------------------
def play_text_to_sound(text_string,time,speed):
    file = 'temp.mp3'
    if(speed=='slow'):
        output = gTTS(text=text_string , lang="en" , slow=True)
    else:
        output = gTTS(text=text_string , lang="en" , slow=False)

    output.save(file)
         
    #os.system("start temp.mp3")
    for i in range(time):
        playsound.playsound(file, True)
    os.remove(file)
    #winsound.PlaySound(file, winsound.SND_ASYNC | winsound.SND_ALIAS )
'''    
    mixer.init()
    clock = pygame.time.Clock()
    mixer.music.load('temp.mp3')
    mixer.music.play()
    while mixer.music.get_busy():
        clock.tick(1000)
    mixer.music.stop()
'''
    

#-----------------------------------------------------------------------
# Function insert_space
#-----------------------------------------------------------------------
def insert_spaces(text):
    s=text
    return " ".join(s[i:i+1] for i in range(0, len(s), 1))



#-----------------------------------------------------------------------
# Main Function
#-----------------------------------------------------------------------
username = input("What's your name:")
#Show wellcom message
greet(username)


#---------------------------------------------
# Read test data from excel file
#---------------------------------------------
#if(sys.argv[0] ==''):
#else:

testfile = 'english_exam.xlsx'

test_db = pd.read_excel(testfile,"List")
number_of_word = len(test_db["Definition"])

#---------------------------------------------
# User decide test range 
#---------------------------------------------
print("Please decide test range(1-"+str(number_of_word)+')')
start = int(input("start:"))
end = int(input("end:"))

print("-----------------------------------------------")
print("0: Read the defintion of word")
print("1: Listen to the word")
print("2: List word randomly")
print("3: Auto Play Mode")
test_mode = int(input("Select Test Mode:"))




#print(test_db)
test_desc = test_db["Definition"][start-1:end]
test_hint = test_db["Hint"][start-1:end]
test_answ = test_db["Answer"][start-1:end]

number_of_test = len(test_desc)
#print("start=",start,";end=",end)
#print(test_db["Answer"][0:10])
#print(test_db["Answer"][80:120])

#print(test_db["Answer"][start-1:end+1])
#print(test_answ);

#input("...")


word_idx = list(range(start-1, end))
#print(word_idx)
#input("...")

#for i in range(start,end):
#    print(i,test_desc[i],test_hint[i],test_answ[i])

q_desc=test_desc
q_hint=test_hint
q_answ=test_answ
q_idx = word_idx

score = 0
ng_idx = 0
wrong_list = [[ "Right" , "Your Wrong Answer"],[ "" , ""]]

random.shuffle(q_idx) #shuffle


#---------------------------------------------
# Test Loop
#---------------------------------------------
if test_mode==3 :
    for i in range(number_of_test):
        idx=q_idx[i]
        os.system('cls')
        text_string = "Number " + str(i+1) + ": "
        print(text_string)
        text_string = "Number " + str(i+1) + ": "  + q_answ[idx]
        play_text_to_sound(text_string,1,"fast")
        play_text_to_sound(q_answ[idx],3,"fast")
        print(q_answ[idx])
        play_text_to_sound(insert_spaces(q_answ[idx]),3,"fast")
    pass

else:    
   

    for i in range(number_of_test):
        idx=q_idx[i]
        #---------------------------------------------
        # Prepare Question
        #---------------------------------------------
        if test_mode==2 :
            text_string = "Question " + str(i+1) + ": "  + q_answ[idx]
            print(text_string)
    
        elif test_mode==1 :
            os.system('cls')
            text_string = "Question " + str(i+1) + ": "
            print(text_string)
            text_string = "Question " + str(i+1) + ": "  + q_answ[idx]
            play_text_to_sound(text_string,1,"fast")
            play_text_to_sound(q_answ[idx],3,"fast")
            print("-----------------------------------------------------")

        else:
            os.system('cls')
            print("Question" , str(i+1) , ":")
            print("Definition:",q_desc[idx])
            print("Hint:",q_hint[idx])
            text_string = "Question " + str(i+1) + ": "  + q_desc[idx]
            play_text_to_sound(text_string,2,"fast")
        
        #---------------------------------------------
        # Check Answer
        #---------------------------------------------
        if test_mode!=2 :
            user_ans = input("Enter your answer: ") 
            if user_ans==q_answ[idx] :
                text_string = "[Pass] You are right !"
                print(text_string)
                play_text_to_sound(text_string,1,"fast")
                score += 1
            else:
                text_string = "[Wrong] answer is " + q_answ[idx] 
                print(text_string)
                play_text_to_sound(text_string,1,"fast")
                #text_string = "answer is " + s
                text_string = insert_spaces(q_answ[idx])
                play_text_to_sound(text_string,2,"fast")
           
                ng_idx += 1
                wrong_list.append( [q_answ[idx] , user_ans ] )
                os.system('pause')
    pass
 
if test_mode==2 :
    input("press enter key to finish ...")
else :
    print("Your test is done" )
    print("Your score is : " , str(score)+ '/' + str(number_of_test))
    print("-----------------------------------------------------")
    for i in (wrong_list):
        print(i)
         

