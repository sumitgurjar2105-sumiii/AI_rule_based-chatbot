import datetime
import time
print("WELCOME ! to AI RULE BASED ChatBot 🤖")
name=input("plz enter your name :")
#greetings depends on time
prehour=datetime.datetime.now().hour
if 5<= prehour <=11:
    print("GOOD MORNING !",name)
elif 11<= prehour <=17:
    print("GOOD AFTERNOON!",name)
elif 17<= prehour<=20:
        print("GOOD EVENING !",name)
else:
     print("GOOD NIGHT!",name)


print("namste! I am your AI rule Based chatbot")
print("you can ask me a Question and type 'bye' for exit")

#dict to stores some responces
responces={
    "hello":"hello,how are you ? do want to know somthing",
    "yes":"ok",
    "how are you?":"i am fine",
    "i am also fine":"nice",
    "motivate me":"keep going on brother nothing is imposible",
    "functions ky hhote he":"function block of code hote jo specific task perform krte he",
    "list kya hoti he":"list ek data type hote he jo data ko store krne ke liye use hote he,ye mutable hote he",
    "tuple kya hote he":"tuple bhi in-bui;t data type hote he jo data store krte he bilkul list ki trh but ye immutable hote he",
    "dictionary":"dicts bhii in buit data type hoti he jo ki key-values me data ko store krke rkhti he",
    "sets":"sets bhi ek data type he jo dict ki trh hote he or yen unique id reserved krte he ",
    "python":"python one of the most easy and funny aprogrammming language he jisse tum ai-ml bhi kr skte ho "
}
#method to getRESopnces
def getResponce(userinput):
     userinput=userinput.lower()
     for eachkey in responces:
            if eachkey in userinput:
               return responces[eachkey]
          
     print("Sorry i do not know about it,i will learn it soon")
          
#get input
while True:
     uinput=input("ask me a question :")
     reply=getResponce(uinput)
     print("🤖:"," ",reply)

     if "bye" in uinput.lower():
       break