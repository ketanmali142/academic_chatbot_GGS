from flask import Flask, request # type: ignore
import requests # type: ignore
#from twilio.twiml.messaging_response import MessagingResponse
#app = Flask(__name__)

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import json
import requests # type: ignore
import os
import random
import textsim2 # type: ignore
from datetime import datetime
chatlist=[] 
prevQuestion="default"
class ultraChatBot():
   
    def __init__(self, json):
        self.json = json
        self.dict_messages = json['data']
        self.ultraAPIUrl = 'https://api.ultramsg.com/instance89174/'
        self.token = 'v3rh1mu4nn0jzcmv'
        
   
    def send_requests(self, type, data):
        url = f"{self.ultraAPIUrl}{type}?token={self.token}"
        headers = {'Content-type': 'application/json'}
        answer = requests.post(url, data=json.dumps(data), headers=headers)
        return answer.json()

    def send_message(self, chatID, text):
        data = {"to" : chatID,
                "body" : text}  
        answer = self.send_requests('messages/chat', data)
       
        return answer
    def send_message2(self, chatID, text):
         data = text_similarity(text)
         print(data)
         if str(data).__contains__("https://firebasestorage.googleapis.com") and (str(data).__contains__(".jpg")):
             print("__________________image______")
             return self.send_image(chatID,str(data))
         if str(data).__contains__("https://firebasestorage.googleapis.com") and (str(data).__contains__(".mp4")):
             print("__________________video______")
             return self.send_video(chatID,str(data))
         if str(data).__contains__("https://firebasestorage.googleapis.com") and (str(data).__contains__(".mp3")):
             print("__________________audio______")
             return self.send_audio(chatID,str(data))      
         if str(data).__contains__("https://firebasestorage.googleapis.com") and (str(data).__contains__(".pdf")):
             print("__________________doc______")
             return self.send_doc(chatID,str(data))     
               
         else:
             return self.send_message(chatID, str(data))
    
    def welcome(self,chatID, noWelcome = False):
        welcome_string = ''
        if (noWelcome == False):
            welcome_string = "Hi , welcome to GCOERC.How can i help you? \n\nLet's get started.You can ask me for : \n\nInstitute Academics \nAdmission Details \nDepartments (Courses) \nExamination Details \nKnow Your Campus \nLearning library \nPlacement Status \nStudent Corner \nMore About GCOERC \nGCOERC Photo Gallery"
        else:
            welcome_string = "wrong command"
        print(welcome_string)    
        return self.send_message(chatID,welcome_string)
    
    def send_default(self,chatID):
        welcome_string = "I'm sorry, I couldn't understand your question."
        print(welcome_string)    
        return self.send_message(chatID,welcome_string)    
    def send_image(self, chatID,picurl):
        data = {"to" : chatID,
                "image" : picurl}  
        answer = self.send_requests('messages/image', data)
        return answer
    
    def send_video(self, chatID,picurl):
        data = {"to" : chatID,
                "video" : picurl}  
        answer = self.send_requests('messages/video', data)
        return answer

    def send_audio(self, chatID,picurl):
        data = {"to" : chatID,
                "audio" : picurl}  
        answer = self.send_requests('messages/audio', data)
        return answer
    
    def send_doc(self, chatID,picurl):
        #timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        #filename = f"document_{timestamp}.pdf"
        data = {"to" : chatID,
                "document" : picurl,
                "filename":"hello.pdf",
                "caption":"doc caption"}  
        answer = self.send_requests('messages/document', data)
        return answer
        
    def Processingـincomingـmessages(self):
        if self.dict_messages != []:
            message =self.dict_messages
            text = message['body'].split()
            incoming_message=str(message['body'])
            chatID  = message['from'] 
            print(str(message['body']))
            if incoming_message=="#123":
                chatlist.append(chatID)             
                return self.welcome(chatID)          
            else: 
             print(chatlist)
             if chatID in chatlist:
              print("chat id match")
              if not message['fromMe']:                
                print(text[0].lower())
                if text[0].lower() == 'hi' or text[0].lower() == 'hii' or text[0].lower() == 'hey':
                    return self.welcome(chatID)
                else:
                    return self.send_message2(chatID,incoming_message.lower())
                
             else: return 'NoCommand'
    def Processingـmybot(incoming_message):
         data = text_similarity(incoming_message)
         print(data)
         return data
            
try:
 os.remove("database.sqlite3")
except:
 print("")

# Load your custom data from a JSON file
with open('clg.json', 'r',encoding="utf8") as file:
    college_data = json.load(file)
# Create a new trainer for the chat bot

# Now, let's interact with the bot
print("Bot: Hi, how can I assist you today?")

def text_similarity(sentence1):
    global prevQuestion
    global college_data
    output=""
    dist=0
    myList=[]
    q=""
   
    print("pq:"+prevQuestion)
    if "yes:" in sentence1.lower():
       sentence1=sentence1.replace("yes:","").replace("Yes:","")
       new_data = [prevQuestion, sentence1]
        # Append new data to the existing list
       college_data.append(new_data)
       print(college_data)
       # Write updated data back to clg.json
       with open('clg.json', 'w', encoding="utf8") as file:
            json.dump(college_data, file, ensure_ascii=False, indent=4)
       return "Data added in Db"
            
    for input_text, response_text in college_data:
        matching_words_count = textsim2.count_matching_words(input_text, sentence1)
        if dist<=matching_words_count:
            dist=matching_words_count
            output=response_text
            if dist==1:
                myList.append(input_text)
            q=input_text
    if dist==1:
        output="Do you want to ask one of the following if yes, then type it " 
        i=1 
        for item in myList:
            output=output+"\n"+str(i)+"."+ item
            i=i+1

    else: 
     if dist<2:
        output="I'm sorry, I couldn't understand your question. do you want to train if Yes then type yes:answer"
        prevQuestion=sentence1

    return output




  