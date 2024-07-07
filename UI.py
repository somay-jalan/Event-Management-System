from PyInquirer import prompt,Separator
from examples import *

from prompt_toolkit.validation import Validator, ValidationError
import time
import mysql.connector
import os
import re
from datetime import datetime
import json  
host = 'localhost'
username = 'somay'
password = 'somay'
connection = mysql.connector.connect(user=username, password=password,host=host)
cursor = connection.cursor()
cursor.execute('USE DBMS_Project_final')

class EmailIDValidatorForParticpant(Validator):
    def validate(self, document):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(re.fullmatch(regex, document.text)):
            pass
        else:
            raise ValidationError(message="Please enter a valid email.",
                                  cursor_position=len(document.text))
        execution='select * from participant where Email=%(emailID)s ;'
        cursor.execute(execution,{"emailID":document.text})
        result=cursor.fetchall()
        if len(result)!=0:
            raise ValidationError(message="Account already associated with the EmailID.",
                                  cursor_position=len(document.text))

class EmailIDValidatorForOrganizer(Validator):
    def validate(self, document):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(re.fullmatch(regex, document.text)):
            pass
        else:
            raise ValidationError(message="Please enter a valid email.",
                                  cursor_position=len(document.text))
        execution='select * from organizer where Email=%(emailID)s ;'
        cursor.execute(execution,{"emailID":document.text})
        result=cursor.fetchall()
        if len(result)!=0:
            raise ValidationError(message="Account already associated with the EmailID.",
                                  cursor_position=len(document.text))

class EmailIDValidatorForAdmin(Validator):
    def validate(self, document):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(re.fullmatch(regex, document.text)):
            pass
        else:
            raise ValidationError(message="Please enter a valid email.",
                                  cursor_position=len(document.text))
        execution='select * from admin where Email=%(emailID)s ;'
        cursor.execute(execution,{"emailID":document.text})
        result=cursor.fetchall()
        if len(result)!=0:
            raise ValidationError(message="Account already associated with the EmailID.",
                                  cursor_position=len(document.text))

class NameValidator(Validator):
    def validate(self, document):
        if(len(document.text)>2):
            return
        else:
            raise ValidationError(message="Length of name should be more than 2.",
                                  cursor_position=len(document.text))

class PasswordValidator(Validator):
    def validate(self, document):
        if(len(document.text)>7):
            return
        else:
            raise ValidationError(message="Length of password should be more than 7.",
                                  cursor_position=len(document.text))

class PhoneNoValidator(Validator):
    def validate(self, document):
        if(len(document.text)>9):
            return
        else:
            raise ValidationError(message="Length of Phone Number should be more than 9.",
                                  cursor_position=len(document.text))

class DateTimeValidator(Validator):
    def validate(self, document):
        try:
            datetime.strptime(document.text, "%Y-%m-%d %H:%M:%S")

        except:
            raise ValidationError(message="Date and Time not added are not in proper format",
                                  cursor_position=len(document.text))

def AdminValidator(document,CurrAdmin):
    if document!=CurrAdmin[2]:
        execution='select * from admin where Email=%(emailID)s ;'
        cursor.execute(execution,{"emailID":document})
        result=cursor.fetchall()
        if len(result)!=0:
            return True
        else:
            raise ValidationError(message="Given EmailID not present in Database.",
                cursor_position=len(document))
    else:
        raise ValidationError(message="Can't remove current Admin",
                cursor_position=len(document))

def OrganizerValidator(document):
    execution='select * from organizer where Email=%(emailID)s ;'
    cursor.execute(execution,{"emailID":document})
    result=cursor.fetchall()
    if len(result)!=0:
        return True
    else:
        raise ValidationError(message="Given EmailID not present in Database.",
            cursor_position=len(document))

class PrintColor():
    def background(code):
        return "\33[{code}m".format(code=code)
 
    def style_text(code):
        return "\33[{code}m".format(code=code)
 
    def color_text(code):
        return "\33[{code}m".format(code=code)
    def reset():
        return "\33[0m"    

def sentenceAnimate(sentence,newLine=False):
    sentence=str(sentence)
    for i in sentence:
        print(i,end='',flush=True)
        time.sleep(0.01)
    if newLine:
        print()
    
def HomePage():
    os.system('cls' if os.name == 'nt' else 'clear')
    sentenceAnimate((PrintColor.color_text(32)+"Welcome to Event Managment System"+PrintColor.reset()).center(os.get_terminal_size().columns),True)
    HomePage = [
        {
            'type': 'list',
            'name': 'user_option',
            'message': 'Please Choose your desired option.',
            'choices': ["Sign Up Page","Sign In Page","Exit"]
        },
    ]
    answers = prompt(HomePage, style=custom_style_2)
    if answers['user_option']=="Sign In Page":
        SignInPage(False)
    elif answers['user_option']=="Sign Up Page":
        SignUpPage()
    elif answers['user_option']=="Exit":
        exit()

def SignUpPage():
    os.system('cls' if os.name == 'nt' else 'clear')
    sentenceAnimate((PrintColor.color_text(32)+"Sign Up Page"+PrintColor.reset()).center(os.get_terminal_size().columns),True)
    SignUpPagePrompt=[
        {
            'type': 'list',
            'name': 'user_mode',
            'message': 'Please choose your role.',
            'choices': ["Participant","Organizer","Admin","Home Page","Exit"]
        }
    ]
    answers = prompt(SignUpPagePrompt, style=custom_style_2)
    if answers["user_mode"]=="Participant":
        ParticipantSignUp()
    elif answers["user_mode"]=="Organizer":
        OrganizerSignUp()
    elif answers["user_mode"]=="Admin":
        AdminSignUp()
    elif answers["user_mode"]=="Home Page":
        HomePage()
    elif answers["user_mode"]=="Exit":
        exit()

def ParticipantSignUp():
    os.system('cls' if os.name == 'nt' else 'clear')
    sentenceAnimate((PrintColor.color_text(32)+"Sign Up Page for Participant"+PrintColor.reset()).center(os.get_terminal_size().columns),True)
    ParticipantSignUpPrompt=[
        {
            'type':'input',
            'name':'Name',
            'message':'Enter your name:',
            'validate':NameValidator
        },
        {
            'type':'input',
            'name':'EmailID',
            'message':'Enter your EmailID:',
            'validate':EmailIDValidatorForParticpant
        },
        {
            'type':'input',
            'name':'Password',
            'message':'Enter your password:',
            'validate':PasswordValidator
        },
        {
            'type':'input',
            'name':'PhoneNo',
            'message':'Enter your PhoneNo:',
            'validate':PhoneNoValidator
        },
        {
            'type':'input',
            'name':'RollNo',
            'message':'Enter your Roll Number (If you don\'t have a roll number just press enter):',
        }

    ]
    answers = prompt(ParticipantSignUpPrompt, style=custom_style_2)
    Name=answers['Name']
    Email=answers['EmailID']
    Password=answers['Password']
    PhoneNo=answers['PhoneNo']
    RollNo=None if answers['RollNo']=="" else answers['RollNo']
    PID=int(''.join([str(ord(i))for i in Email])[:8])
    check=True
    while check:
        execution='select * from participant where PID=%(PID)s ;'
        cursor.execute(execution,{"PID":PID})
        result=cursor.fetchall()
        if len(result)==0:
            check=False
        else:
            PID+=1
    try:
        execution='INSERT INTO `participant` (`PID`, `Name`, `Email`, `Password`, `PhoneNo`, `RollNo`)VALUES(%(PID)s,%(Name)s,%(Email)s,%(Password)s,%(PhoneNo)s,%(RollNo)s)'
        cursor.execute(execution,{"PID":PID,"Name":Name,"Email":Email,"Password":Password,"PhoneNo":PhoneNo,"RollNo":RollNo})
        connection.commit()
        sentenceAnimate("\x1b[101mYou have been successfully added as participant.\x1b[0m",True)
        SuccessfulSignUpPrompt=[{
            'type': 'list',
            'name': 'user_mode',
            'message': 'What would you like to do next?',
            'choices': ["Sign In Page","Home Page","Exit"]
        }
        ]
        answers = prompt(SuccessfulSignUpPrompt, style=custom_style_2)
        if answers["user_mode"]=="Sign In Page":
            SignInPage(False)
        elif answers["user_mode"]=="Home Page":
            HomePage()
        else:
            exit()
    except Exception as e:
        print(e.args)
        sentenceAnimate("\x1b[101mThere was some issue with adding you as participant, please try later.\x1b[0m",True)
        exit()

def OrganizerSignUp():
    os.system('cls' if os.name == 'nt' else 'clear')
    sentenceAnimate((PrintColor.color_text(32)+"Sign Up Page for Organizer"+PrintColor.reset()).center(os.get_terminal_size().columns),True)
    print("\x1b[101mNote: After you have filled all the deatils one of the admins will approve your application only then you will given access to organizer portal.\x1b[0m")
    OrganizerSignUpPrompt=[
        {
            'type':'input',
            'name':'Name',
            'message':'Enter your name:',
            'validate':NameValidator
        },
        {
            'type':'input',
            'name':'EmailID',
            'message':'Enter your EmailID:',
            'validate':EmailIDValidatorForOrganizer
        },
        {
            'type':'input',
            'name':'Password',
            'message':'Enter your password:',
            'validate':PasswordValidator
        },
        {
            'type':'list',
            'name':'Club/Seminar',
            'message':'You are an organizer of?:',
            'choices': ["Club","Seminar"]
        },

    ]
    answers = prompt(OrganizerSignUpPrompt, style=custom_style_2)
    Name=answers['Name']
    Email=answers['EmailID']
    Password=answers['Password']
    Club_Seminar=answers['Club/Seminar']
    OID=int(''.join([str(ord(i))for i in Email])[:8])
    check=True
    while check:
        execution='select * from organizer where OID=%(OID)s ;'
        cursor.execute(execution,{"OID":OID})
        result=cursor.fetchall()
        if len(result)==0:
            check=False
        else:
            OID+=1
    try:
        execution='INSERT INTO `organizer` (`OID`, `Name`, `Email`, `Password`, `Club/Seminar`)VALUES(%(OID)s,%(Name)s,%(Email)s,%(Password)s,%(Club_Seminar)s)'
        cursor.execute(execution,{"OID":OID,"Name":Name,"Email":Email,"Password":Password,"Club_Seminar":Club_Seminar})
        connection.commit()
        sentenceAnimate("\x1b[101mYour application has been sent to admin for approval.\x1b[0m",True)
        SuccessfulSignUpPrompt=[{
            'type': 'list',
            'name': 'user_mode',
            'message': 'What would you like to do next?',
            'choices': ["Sign In Page","Home Page","Exit"]
        }
        ]
        answers = prompt(SuccessfulSignUpPrompt, style=custom_style_2)
        if answers["user_mode"]=="Sign In Page":
            SignInPage(False)
        elif answers["user_mode"]=="Home Page":
            HomePage()
        else:
            exit()
    except Exception as e:
        print(e.args)
        sentenceAnimate("\x1b[101mThere was some issue with adding you as organizer, please try later.\x1b[0m",True)
        exit()

def AdminSignUp():
    os.system('cls' if os.name == 'nt' else 'clear')
    sentenceAnimate((PrintColor.color_text(32)+"Sign Up Page for Admin"+PrintColor.reset()).center(os.get_terminal_size().columns),True)
    print("\x1b[101mNote: After you have filled all the deatils one of the admins will approve your application only then you will given access to admin portal.\x1b[0m")
    AdminSignUpPrompt=[
        {
            'type':'input',
            'name':'Name',
            'message':'Enter your name:',
            'validate':NameValidator
        },
        {
            'type':'input',
            'name':'EmailID',
            'message':'Enter your EmailID:',
            'validate':EmailIDValidatorForAdmin
        },
        {
            'type':'input',
            'name':'Password',
            'message':'Enter your password:',
            'validate':PasswordValidator
        },
        {
            'type':'input',
            'name':'PhoneNo',
            'message':'Enter your PhoneNo:',
            'validate':PhoneNoValidator
        }

    ]
    answers = prompt(AdminSignUpPrompt, style=custom_style_2)
    Name=answers['Name']
    Email=answers['EmailID']
    Password=answers['Password']
    PhoneNo=answers['PhoneNo']
    AID=int(''.join([str(ord(i))for i in Email])[:8])
    check=True
    while check:
        execution='select * from admin where AID=%(AID)s ;'
        cursor.execute(execution,{"AID":AID})
        result=cursor.fetchall()
        if len(result)==0:
            check=False
        else:
            AID+=1
    try:
        execution='INSERT INTO `admin` (`AID`, `Name`, `Email`, `Password`, `PhoneNo`)VALUES(%(AID)s,%(Name)s,%(Email)s,%(Password)s,%(PhoneNo)s)'
        cursor.execute(execution,{"AID":AID,"Name":Name,"Email":Email,"Password":Password,"PhoneNo":PhoneNo})
        connection.commit()
        sentenceAnimate("\x1b[101mYour application has been sent to admin for approval.\x1b[0m",True)
        SuccessfulSignUpPrompt=[{
            'type': 'list',
            'name': 'user_mode',
            'message': 'What would you like to do next?',
            'choices': ["Sign In Page","Home Page","Exit"]
        }
        ]
        answers = prompt(SuccessfulSignUpPrompt, style=custom_style_2)
        if answers["user_mode"]=="Sign In Page":
            SignInPage(False)
        elif answers["user_mode"]=="Home Page":
            HomePage()
        else:
            exit()
    except Exception as e:
        print(e.args)
        sentenceAnimate("\x1b[101mThere was some issue with adding you as admin, please try later.\x1b[0m",True)
        exit()

def SignInPage(wrongInfo):
    os.system('cls' if os.name == 'nt' else 'clear')
    if wrongInfo:
        print((PrintColor.color_text(32)+"Sign In Page"+PrintColor.reset()).center(os.get_terminal_size().columns))
        print("Please fill the following details.")
        print("\x1b[101mWrong EmailID or Password.\x1b[0m")
    else:
        sentenceAnimate((PrintColor.color_text(32)+"Sign In Page"+PrintColor.reset()).center(os.get_terminal_size().columns),True)
        print("Please fill the following details.")
    SignInPagePrompt=[
        {
            'type': 'input',
            'name':'EmailID',
            'message':'Enter your Email ID:'
        },
        {
            'type': 'password',
            'name':'password',
            'message':'Enter your password:',
        },
        {
            'type': 'list',
            'name': 'user_mode',
            'message': 'Please choose your role.',
            'choices': ["Participant","Organizer","Admin","Home Page","Exit"]
        },
        
        
    ]
    answers = prompt(SignInPagePrompt, style=custom_style_2)
    emailID=answers["EmailID"]
    password=answers["password"]
    user_mode=answers["user_mode"]
    if user_mode=="Participant":
        execution='select * from participant where Email=%(emailID)s and password=%(password)s;'
        cursor.execute(execution,{"emailID":emailID,"password":password})
        result=cursor.fetchall()
        if len(result)==0:
            SignInPage(True)
        else:
            ParticipantPage(result[0])
    elif user_mode=="Organizer":
        execution='select * from organizer where Email=%(emailID)s and password=%(password)s;'
        cursor.execute(execution,{"emailID":emailID,"password":password})
        result=cursor.fetchall()
        if len(result)==0:
            SignInPage(True)
        else:
            if("YES" in result[0][-1]):
                OrganizerPage(result[0])
            else:
                print("\x1b[101mYou are not yet approved by admin to be an organizer.\x1b[0m")
                BackPrompt=[
                    {
                        'type': 'list',
                        'name': 'back_option',
                        'message': 'Please choose an option.',
                        'choices': ["Home Page","Exit"]
                    }
                ]
                answers = prompt(BackPrompt, style=custom_style_2)
                if answers['back_option']=="Home Page":
                    HomePage()
                elif answers['back_option']=="Exit":
                    exit()
                
    elif user_mode=="Admin":
        execution='select * from admin where Email=%(emailID)s and password=%(password)s;'
        cursor.execute(execution,{"emailID":emailID,"password":password})
        result=cursor.fetchall()
        if len(result)==0:
            SignInPage(True)
        else:
            if("YES" in result[0][-1]):
                AdminPage(result[0])
            else:
                print("\x1b[101mYou are not yet approved by another admin to be an admin.\x1b[0m")
                BackPrompt=[
                    {
                        'type': 'list',
                        'name': 'back_option',
                        'message': 'Please choose an option.',
                        'choices': ["Home Page","Exit"]
                    }
                ]
                answers = prompt(BackPrompt, style=custom_style_2)
                if answers['back_option']=="Home Page":
                    HomePage()
                elif answers['back_option']=="Exit":
                    exit()
    elif user_mode=="Home Page":
        HomePage()
    elif user_mode=="Exit":
        exit()
        
def ParticipantPage(ParticipantInfo):
    PID=ParticipantInfo[0]
    ParticipantName=ParticipantInfo[1]
    ParticipantEmail=ParticipantInfo[2]
    ParticipantPassword=ParticipantInfo[3]
    ParticipantPhoneNo=ParticipantInfo[4]
    ParticipantRollNo=ParticipantInfo[5]
    os.system('cls' if os.name == 'nt' else 'clear')
    sentenceAnimate((PrintColor.color_text(32)+"Welcome "+ParticipantName+"!"+PrintColor.reset()).center(os.get_terminal_size().columns),True)
    ParticipantPagePrompt=[
        {
            'type': 'list',
            'name': 'participant_choice',
            'message': 'What would you like to do today?',
            'choices': ["Explore Events","View previously registered events","View Upcoming Registered Event","Logout","Exit"]  
        }
    ]
    answers = prompt(ParticipantPagePrompt, style=custom_style_2)
    if answers['participant_choice']=="Explore Events":
        ExploreEventPage(ParticipantInfo)
    elif answers['participant_choice']=="View previously registered events":
        PastRegisteredEventPage(ParticipantInfo)
    elif answers['participant_choice']=="View Upcoming Registered Event":
        UpcomingRegisteredEventPage(ParticipantInfo)  

def ExploreEventPage(ParticipantInfo):
    PID=ParticipantInfo[0]
    ParticipantName=ParticipantInfo[1]
    os.system('cls' if os.name == 'nt' else 'clear')
    sentenceAnimate((PrintColor.color_text(32)+"Here is a list of upcoming events.(You can select each event to see its description and register)"+PrintColor.reset()).center(os.get_terminal_size().columns),True)
    currentTime=datetime.now()
    execution='select * from events where StartDateTime>%(currentTime)s and Approved="YES"'
    cursor.execute(execution,{"currentTime":currentTime})
    result=cursor.fetchall()
    briefDescription=[]
    for i in range(len(result)):
        result[i]=list(result[i])
        result[i].append(result[i][4]+"|"+str(result[i][1])+"|"+list(result[i][6])[0])
        briefDescription.append(result[i][4]+"|"+str(result[i][1])+"|"+list(result[i][6])[0])
    briefDescription.append("Go Back")
    briefDescription.append("Logout")
    briefDescription.append("Exit")
    ExploreEventsPagePrompt=[
        {
            'type': 'list',
            'name': 'event_choice',
            'message': 'Event name|Start date|Free or Tickted',
            'choices': briefDescription  
        }
    ]
    answers = prompt(ExploreEventsPagePrompt, style=custom_style_2)
    if answers["event_choice"]=="Go Back":
        ParticipantPage(ParticipantInfo)
    elif answers["event_choice"]=="Logout":
        HomePage()
    elif answers["event_choice"]=="Exit":
        exit()
    else:
        for i in result:
            if answers["event_choice"] in i:
                EventDescriptionPage(ParticipantInfo,i,True)
                break
                
def EventDescriptionPage(ParticipantInfo,event,UpcomingEvent,UpcomingRegisterPage=False):
    PID=ParticipantInfo[0]
    ParticipantName=ParticipantInfo[1]
    EID=event[0]
    EventStartTime=event[1]
    EventEndTime=event[2]
    EventDescription=event[3]
    EventName=event[4]
    EventNumberOfParticipants=event[5]
    EventType=event[6]
    if(event[7]!='null'):
        EventRequirementsForParticipants=eval(event[7])
    else:
        EventRequirementsForParticipants={}
    OID=event[8]
    os.system('cls' if os.name == 'nt' else 'clear')
    sentenceAnimate((PrintColor.color_text(32)+"Event Description"+PrintColor.reset()).center(os.get_terminal_size().columns),True)
    print("\x1b[1;31mName:\x1b[0m"+EventName)
    print("\x1b[1;31mDescription:\x1b[0m"+EventDescription)
    print("\x1b[1;31mStart Time:\x1b[0m"+str(EventStartTime))
    print("\x1b[1;31mEnd Time:\x1b[0m"+str(EventEndTime))
    print("\x1b[1;31mNumber of participants:\x1b[0m"+str(EventNumberOfParticipants))
    print("\x1b[1;31mRequirement for event:\x1b[0m")
    for i in EventRequirementsForParticipants:
        print("\t\x1b[38;5;201m"+i+":\x1b[0m"+EventRequirementsForParticipants[i])
    print("\x1b[1;31mFree/Ticketed:\x1b[0m"+list(EventType)[0])
    if UpcomingEvent:
        execution='select * from participant_events where PID=%(PID)s and EID=%(EID)s'
        cursor.execute(execution,{"PID":PID,"EID":EID})
        result=cursor.fetchall()
        if(len(result)!=0):
            Registraion=False
        else:
            Registraion=True
        if Registraion:
            RegisterForEventPrompt=[
                {
                    'type': 'list',
                    'name': 'register_choice',
                    'message': 'Do you want to register?',
                    'choices': ["Register","Go Back","Logout","Exit"]  
                }
            ]
            answers = prompt(RegisterForEventPrompt, style=custom_style_2)
            if answers['register_choice']=="Go Back":
                if UpcomingRegisterPage:
                    UpcomingRegisteredEventPage(ParticipantInfo)
                else:
                    ExploreEventPage(ParticipantInfo)
            elif answers['register_choice']=="Logout":
                HomePage()
            elif answers['register_choice']=="Exit":
                exit()
            elif answers['register_choice']=="Register":
                try:
                    execution='INSERT INTO `participant_events` (`PID`, `EID`)VALUES(%(PID)s, %(EID)s)'
                    cursor.execute(execution,{"PID":PID,"EID":EID})
                    connection.commit()
                    execution='select count(*) from participant_events where EID=%(EID)s;'
                    cursor.execute(execution,{"EID":EID})
                    result=cursor.fetchall()
                    count=result[0][0]
                    execution='UPDATE `events` SET NumberOfParticipants =%(count)s WHERE EID = %(EID)s;'
                    cursor.execute(execution,{"count":count,"EID":EID})
                    connection.commit()
                    print("\x1b[101mRegistered succesfully for the event.\x1b[0m")
                    SuccessfulRegisterForEventPrompt=[
                        {
                            'type': 'list',
                            'name': 'register_choice',
                            'message': 'What would you like to do?',
                            'choices': ["Go Back","Logout","Exit"]  
                        }
                    ]
                    answers = prompt(SuccessfulRegisterForEventPrompt, style=custom_style_2)
                    if answers['register_choice']=="Go Back":
                        if UpcomingRegisterPage:
                            UpcomingRegisteredEventPage(ParticipantInfo)
                        else:
                            ExploreEventPage(ParticipantInfo)
                    elif answers['register_choice']=="Logout":
                        HomePage()
                    elif answers['register_choice']=="Exit":
                        exit()
                except Exception as e:
                    if e.args[0]==1644:
                        print("\x1b[101mMaximum participants limit exceeded for this event!\x1b[0m")
                        UnSuccessfulRegisterForEventPrompt=[
                            {
                                'type': 'list',
                                'name': 'register_choice',
                                'message': 'What would you like to do?',
                                'choices': ["Go Back","Logout","Exit"]  
                            }
                        ]
                        answers = prompt(UnSuccessfulRegisterForEventPrompt, style=custom_style_2)
                        if answers['register_choice']=="Go Back":
                            if UpcomingRegisterPage:
                                UpcomingRegisteredEventPage(ParticipantInfo)
                            else:
                                ExploreEventPage(ParticipantInfo)
                        elif answers['register_choice']=="Logout":
                            HomePage()
                        elif answers['register_choice']=="Exit":
                            exit()
                    else:
                        print(e.args)
                        print("\x1b[101mThere for an issue please try again later.\x1b[0m")
                    # ExploreEventPage(ParticipantInfo)
        else:
            DeRegisterForEventPrompt=[
                {
                    'type': 'list',
                    'name': 'register_choice',
                    'message': 'Looks like you are already registered for this event? ',
                    'choices': ["De-Register","Go Back","Logout","Exit"]  
                }
            ]
            answers = prompt(DeRegisterForEventPrompt, style=custom_style_2)
            if answers['register_choice']=="Go Back":
                if UpcomingRegisterPage:
                    UpcomingRegisteredEventPage(ParticipantInfo)
                else:
                    ExploreEventPage(ParticipantInfo)
            elif answers['register_choice']=="Logout":
                HomePage()
            elif answers['register_choice']=="Exit":
                exit()
            elif answers['register_choice']=="De-Register":
                try:
                    execution='DELETE FROM `participant_events` where PID=%(PID)s and EID=%(EID)s'
                    cursor.execute(execution,{"PID":PID,"EID":EID})
                    connection.commit()
                    execution='select count(*) from participant_events where EID=%(EID)s;'
                    cursor.execute(execution,{"EID":EID})
                    result=cursor.fetchall()
                    count=result[0][0]
                    execution='UPDATE `events` SET NumberOfParticipants =%(count)s WHERE EID = %(EID)s;'
                    cursor.execute(execution,{"count":count,"EID":EID})
                    connection.commit()
                    print("\x1b[101mYou have been De-Registered from the event.\x1b[0m")
                    SuccessfulDeRegisterForEventPrompt=[
                        {
                            'type': 'list',
                            'name': 'De-register_choice',
                            'message': 'What would you like to do?',
                            'choices': ["Go Back","Logout","Exit"]  
                        }
                    ]
                    answers = prompt(SuccessfulDeRegisterForEventPrompt, style=custom_style_2)
                    if answers['De-register_choice']=="Go Back":
                        if UpcomingRegisterPage:
                            UpcomingRegisteredEventPage(ParticipantInfo)
                        else:
                            ExploreEventPage(ParticipantInfo)
                    elif answers['De-register_choice']=="Logout":
                        HomePage()
                    elif answers['De-register_choice']=="Exit":
                        exit()
                except Exception as e:
                    print(e.args)
                    print("\x1b[101mThere for an issue please try again later.\x1b[0m")
                    exit()
    else:
        GoBackEventPrompt=[
            {
                'type': 'list',
                'name': 'register_choice',
                'message': 'Do you want to do next?',
                'choices': ["Go Back","Logout","Exit"]  
            }
        ]
        answers = prompt(GoBackEventPrompt, style=custom_style_2)
        if answers['register_choice']=="Go Back":
            PastRegisteredEventPage(ParticipantInfo)
        elif answers['register_choice']=="Logout":
            HomePage()
        elif answers['register_choice']=="Exit":
            exit()

def PastRegisteredEventPage(ParticipantInfo):
    PID=ParticipantInfo[0]
    ParticipantName=ParticipantInfo[1]
    os.system('cls' if os.name == 'nt' else 'clear')
    sentenceAnimate((PrintColor.color_text(32)+"Here is a list of your previously registered events.(You can click on each event to see its description)"+PrintColor.reset()).center(os.get_terminal_size().columns),True)
    currentTime=datetime.now()
    execution='select * from events where startdatetime<%(currentTime)s and Approved="YES" and  EID in (select EID from participant_events where PID=%(PID)s);'
    cursor.execute(execution,{"currentTime":currentTime,"PID":PID})
    result=cursor.fetchall()
    briefDescription=[]
    for i in range(len(result)):
        result[i]=list(result[i])
        result[i].append(result[i][4]+"|"+str(result[i][1])+"|"+list(result[i][6])[0])
        briefDescription.append(result[i][4]+"|"+str(result[i][1])+"|"+list(result[i][6])[0])
    briefDescription.append("Go Back")
    briefDescription.append("Logout")
    briefDescription.append("Exit")
    ExploreEventsPagePrompt=[
        {
            'type': 'list',
            'name': 'event_choice',
            'message': 'Event name|Start date|Free or Tickted',
            'choices': briefDescription  
        }
    ]
    answers = prompt(ExploreEventsPagePrompt, style=custom_style_2)
    if answers["event_choice"]=="Go Back":
        ParticipantPage(ParticipantInfo)
    elif answers["event_choice"]=="Logout":
        HomePage()
    elif answers["event_choice"]=="Exit":
        exit()
    else:
        for i in result:
            if answers["event_choice"] in i:
                EventDescriptionPage(ParticipantInfo,i,False)
                break

def UpcomingRegisteredEventPage(ParticipantInfo):
    PID=ParticipantInfo[0]
    ParticipantName=ParticipantInfo[1]
    os.system('cls' if os.name == 'nt' else 'clear')
    sentenceAnimate((PrintColor.color_text(32)+"Here is a list of your upcoming events for which you have registered.(You can click on each event to see its description)"+PrintColor.reset()).center(os.get_terminal_size().columns),True)
    currentTime=datetime.now()
    execution='select * from events where startdatetime>%(currentTime)s and Approved="YES" and EID in (select EID from participant_events where PID=%(PID)s);'
    cursor.execute(execution,{"currentTime":currentTime,"PID":PID})
    result=cursor.fetchall()
    briefDescription=[]
    for i in range(len(result)):
        result[i]=list(result[i])
        result[i].append(result[i][4]+"|"+str(result[i][1])+"|"+list(result[i][6])[0])
        briefDescription.append(result[i][4]+"|"+str(result[i][1])+"|"+list(result[i][6])[0])
    briefDescription.append("Go Back")
    briefDescription.append("Logout")
    briefDescription.append("Exit")
    ExploreEventsPagePrompt=[
        {
            'type': 'list',
            'name': 'event_choice',
            'message': 'Event name|Start date|Free or Tickted',
            'choices': briefDescription  
        }
    ]
    answers = prompt(ExploreEventsPagePrompt, style=custom_style_2)
    if answers["event_choice"]=="Go Back":
        ParticipantPage(ParticipantInfo)
    elif answers["event_choice"]=="Logout":
        HomePage()
    elif answers["event_choice"]=="Exit":
        exit()
    else:
        for i in result:
            if answers["event_choice"] in i:
                EventDescriptionPage(ParticipantInfo,i,True,UpcomingRegisterPage=True)
                break

def OrganizerPage(OrganizerInfo):
    os.system('cls' if os.name == 'nt' else 'clear')
    OID=OrganizerInfo[0]
    OrganizerName=OrganizerInfo[1]
    OrganizerEmail=OrganizerInfo[2]
    OrganizerPassword=OrganizerInfo[3]
    OrganizerEventType=OrganizerInfo[4]
    sentenceAnimate((PrintColor.color_text(32)+"Welcome "+OrganizerName+"!"+PrintColor.reset()).center(os.get_terminal_size().columns),True)
    OrganizerPagePrompt=[
        {
            'type': 'list',
            'name': 'participant_choice',
            'message': 'What would you like to do today?',
            'choices': ["Create a new event","Manage upcoming events","View Past Events","Logout","Exit"]  
        }
    ]
    answers = prompt(OrganizerPagePrompt, style=custom_style_2)
    if  answers['participant_choice']=="Create a new event":
        CreateNewEventPage(OrganizerInfo)
    elif answers['participant_choice']=="Manage upcoming events":
        ManageUpcomingEventPage(OrganizerInfo)
    elif answers['participant_choice']=="View Past Events":
        OrganizerPastEvent(OrganizerInfo)
    elif answers['participant_choice']=='Logout':
        HomePage()
    elif answers['participant_choice']=='Exit':
        exit()

def CreateNewEventPage(OrganizerInfo):
    os.system('cls' if os.name == 'nt' else 'clear')
    OID=OrganizerInfo[0]
    OrganizerName=OrganizerInfo[1]
    OrganizerEmail=OrganizerInfo[2]
    sentenceAnimate((PrintColor.color_text(32)+"Create a new event page"+PrintColor.reset()).center(os.get_terminal_size().columns),True)
    NewEventPrompt=[
        {
            'type':'input',
            'name':'Name',
            'message':'Enter event name:',
            'validate':NameValidator
        },
        {
            'type':'input',
            'name':'Description',
            'message':'Enter event description:',
        },
        {
            'type':'input',
            'name':'MaxParticipants',
            'message':'Enter Maximum Participants allowed(0 for no limit):',
        },
        {
            'type':'list',
            'name':'TicketType',
            'message':'Is your event Free or Ticketed:',
            'choices':['Free','Ticketed']
        },
        {
            'type':'input',
            'name':'StartDateTime',
            'message':'Enter the start date and time (YYYY-MM-DD HH:MM:SS):',
            'validate':DateTimeValidator
        },
        {
            'type':'input',
            'name':'EndDateTime',
            'message':'Enter the end date and time (YYYY-MM-DD HH:MM:SS):',
            'validate':DateTimeValidator  
        },
        {
            'type':'list',
            'name':'Requirement',
            'message':'Are there any requirements for your event',
            'choices':['Yes','No']
        },
        {
            'type':'input',
            'name':'RequirementName',
            'message':'Enter the title for your Requirement :',
            'when':lambda answers: answers['Requirement']=='Yes'       
        },
        {
            'type':'input',
            'name':'RequirementDescription',
            'message':'Enter the Description for your Requirement :',
            'when':lambda answers: answers['Requirement']=='Yes'       
        }
    ]
    answers = prompt(NewEventPrompt, style=custom_style_2)
    Name=answers['Name']
    Description=answers['Description']
    MaxParticipant=answers['MaxParticipants']
    Type=answers['TicketType']
    StartDateTime=datetime.strptime(answers['StartDateTime'], "%Y-%m-%d %H:%M:%S")
    EndDateTime=datetime.strptime(answers['EndDateTime'], "%Y-%m-%d %H:%M:%S")
    if answers['Requirement']=='Yes':
        Requirement={}
        Requirement[answers['RequirementName']]=answers['RequirementDescription']
    else:
        Requirement=None
    Requirement=json.dumps(Requirement)
    EID=int(''.join([str(ord(i))for i in OrganizerEmail])[:8])+1
    check=True
    while check:
        execution='select * from events where EID=%(EID)s ;'
        cursor.execute(execution,{"EID":EID})
        result=cursor.fetchall()
        if len(result)==0:
            check=False
        else:
            EID+=1
    try:
        execution="INSERT INTO events (EID,StartDateTime, EndDateTime, Description, Name, NumberOfParticipants, Type, RequirementsForParticipants, OID, Approved,max_participants) VALUES (%(EID)s, %(StartDateTime)s, %(EndDateTime)s, %(Description)s, %(Name)s, %(NumberOfParticipants)s, %(Type)s, %(RequirementsForParticipants)s,%(OID)s,%(Approved)s,%(max_participants)s)"
        cursor.execute(execution,{"EID":EID,'StartDateTime':StartDateTime,'EndDateTime':EndDateTime,'Description':Description,"Name":Name,"NumberOfParticipants":0,"Type":Type,"RequirementsForParticipants":Requirement,"OID":OID,"Approved":"NO",'max_participants':MaxParticipant})
        connection.commit()
        sentenceAnimate("\x1b[101mYour event has been succesfully added.\x1b[0m",True)
        SuccessfulEventCreated=[{
            'type': 'list',
            'name': 'user_mode',
            'message': 'What would you like to do next?',
            'choices': ["Go back","Logout","Exit"]
        }
        ]
        answers = prompt(SuccessfulEventCreated, style=custom_style_2)
        if answers["user_mode"]=="Go back":
            OrganizerPage(OrganizerInfo)
        elif answers["user_mode"]=="Logout":
            HomePage()
        else:
            exit()
    except Exception as e:
        if e.args[0]==1644:
            sentenceAnimate("\x1b[101mOrganizer already has 5 or more unapproved events!\x1b[0m",True)
            UnSuccessfulEventCreated=[
                {
                'type': 'list',
                'name': 'user_mode',
                'message': 'What would you like to do next?',
                'choices': ["Go back","Logout","Exit"]
                }
            ]
            answers = prompt(UnSuccessfulEventCreated, style=custom_style_2)
            if answers["user_mode"]=="Go back":
                OrganizerPage(OrganizerInfo)
            elif answers["user_mode"]=="Logout":
                HomePage()
            else:
                exit()
        else:
            print(e.args)
            sentenceAnimate("\x1b[101mThere was some issue with a new event, please try later.\x1b[0m",True)
            exit()

def ManageUpcomingEventPage(OrganizerInfo):
    os.system('cls' if os.name == 'nt' else 'clear')
    OID=OrganizerInfo[0]
    OrganizerName=OrganizerInfo[1]
    OrganizerEmail=OrganizerInfo[2]
    sentenceAnimate((PrintColor.color_text(32)+"Manage Upcoming Events(Select the one you would like to change/check in detail)"+PrintColor.reset()).center(os.get_terminal_size().columns),True)
    currentTime=datetime.now()
    execution='select * from events where StartDateTime>%(currentTime)s and OID=%(OID)s'
    cursor.execute(execution,{"currentTime":currentTime,"OID":OID})
    result=cursor.fetchall()
    briefDescription=[]
    for i in range(len(result)):
        result[i]=list(result[i])
        result[i].append(result[i][4]+"|"+str(result[i][1])+"|"+list(result[i][9])[0])
        briefDescription.append(result[i][4]+"|"+str(result[i][1])+"|"+list(result[i][9])[0])
    briefDescription.append("Go Back")
    briefDescription.append("Logout")
    briefDescription.append("Exit")
    ExploreEventsPagePrompt=[
        {
            'type': 'list',
            'name': 'event_choice',
            'message': 'Event name|Start date|Approved?',
            'choices': briefDescription  
        }
    ]
    answers = prompt(ExploreEventsPagePrompt, style=custom_style_2)
    if answers["event_choice"]=="Go Back":
        OrganizerPage(OrganizerInfo)
    elif answers["event_choice"]=="Logout":
        HomePage()
    elif answers["event_choice"]=="Exit":
        exit()
    else:
        for i in result:
            if answers["event_choice"] in i:
                EventChangePage(OrganizerInfo,i)
                break
    
def EventChangePage(OrganizerInfo,EventInfo,Notpastevent=True):
    EID=EventInfo[0]
    EventStartTime=EventInfo[1]
    EventEndTime=EventInfo[2]
    EventDescription=EventInfo[3]
    EventName=EventInfo[4]
    EventNumberOfParticipants=EventInfo[5]
    EventType=list(EventInfo[6])[0]
    if EventInfo[7]!='null':
        EventRequirementsForParticipants=eval(EventInfo[7])
    else:
        EventRequirementsForParticipants={}
    EventApproval=list(EventInfo[9])[0]
    os.system('cls' if os.name == 'nt' else 'clear')
    sentenceAnimate((PrintColor.color_text(32)+"Event Description and change Page"+PrintColor.reset()).center(os.get_terminal_size().columns),True)
    print("\x1b[1;31mName:\x1b[0m"+EventName)
    print("\x1b[1;31mDescription:\x1b[0m"+EventDescription)
    print("\x1b[1;31mStart Time:\x1b[0m"+str(EventStartTime))
    print("\x1b[1;31mEnd Time:\x1b[0m"+str(EventEndTime))
    print("\x1b[1;31mNumber of participants:\x1b[0m"+str(EventNumberOfParticipants))
    print("\x1b[1;31mRequirement for event:\x1b[0m")
    for i in EventRequirementsForParticipants:
        print("\t\x1b[38;5;201m"+i+":\x1b[0m"+EventRequirementsForParticipants[i])
    print("\x1b[1;31mFree/Ticketed:\x1b[0m"+EventType)
    print("\x1b[1;31mApproval Status(No means that an admin is yet to review your event application):\x1b[0m"+EventApproval)
    if Notpastevent:
        EventChangePagePrompt=[
            {
                'type': 'list',
                'name': 'eventChange_choice',
                'message': 'What would you like to do?',
                'choices': ["View Participants Information","Change Event Information","Go Back","Logout","Exit"]  
            }
        ]
        answers = prompt(EventChangePagePrompt, style=custom_style_2)
        if answers['eventChange_choice']=="View Participants Information":
            execution='SELECT p.Name, p.Email, p.PhoneNo, p.RollNo FROM participant p INNER JOIN participant_events pe ON p.PID = pe.PID WHERE pe.EID = %(EID)s'
            cursor.execute(execution,{"EID":EID})
            result=cursor.fetchall()
            print("\x1b[38;5;217mName | Email | Phone No | Roll no:\x1b[0m")
            for i in result:
                if(i[3]==None):
                    print(i[0]+" | "+i[1]+" | "+i[2]+" | "+"None")
                else:
                    print(i[0]+" | "+i[1]+" | "+i[2]+" | "+i[3])
                ParticipantInfoPrompt=[
                    {
                        'type': 'list',
                        'name': 'participantInfo_choice',
                        'message': 'What would you like to do?',
                        'choices': ["Go Back","Logout","Exit"]  
                    }
                ]
                answers = prompt(ParticipantInfoPrompt, style=custom_style_2)
                if answers['participantInfo_choice']=="Go Back":
                    ManageUpcomingEventPage(OrganizerInfo)
                if answers['participantInfo_choice']=="Logout":
                    HomePage()
                if answers['participantInfo_choice']=="Exit":
                    exit()
        elif answers['eventChange_choice']=="Change Event Information":
            EventInfoChangePrompt=[
                {
                    'type': 'checkbox',
                    'name': 'EventInfo_choice',
                    'message': 'What would you change about the event?',
                    'choices': [
                        {'name':"Name"},{'name':"Description"},{'name':"Start Date and Time"},{'name':"End Date and Time"},{'name':"Requirements"},{'name':"Ticket Type"}]
                }
            ]
            
            answers = prompt(EventInfoChangePrompt, style=custom_style_2)
            changeWanted=answers['EventInfo_choice']
            if 'Name' in changeWanted:
                ChangePrompt=[
                    {
                        'type': 'input',
                        'name': 'newName',
                        'message': 'What do you want the new name to be?',
                        'validate':NameValidator
                    }
                ]
                answers = prompt(ChangePrompt, style=custom_style_2)
                name=answers['newName']
                execution="update events set name=%(name)s where EID=%(EID)s;"
                cursor.execute(execution,{"EID":EID,"name":name,})
                connection.commit()
            if 'Description' in changeWanted:
                ChangePrompt=[
                    {
                        'type': 'input',
                        'name': 'newDescription',
                        'message': 'What do you want the new Description to be?',
                    }
                ]
                answers = prompt(ChangePrompt, style=custom_style_2)
                Description=answers['newDescription']
                execution="update events set description=%(Description)s where EID=%(EID)s;"
                cursor.execute(execution,{"EID":EID,"Description":Description,})
                connection.commit()
            if 'Start Date and Time' in changeWanted:
                ChangePrompt=[
                    {
                        'type':'input',
                        'name':'newStartDateTime',
                        'message':'Enter the new start date and time (YYYY-MM-DD HH:MM:SS):',
                        'validate':DateTimeValidator
                    }
                ]
                answers = prompt(ChangePrompt, style=custom_style_2)
                StartDateTime=answers['newStartDateTime']
                execution="update events set StartDateTime=%(StartDateTime)s where EID=%(EID)s;"
                cursor.execute(execution,{"EID":EID,"StartDateTime":StartDateTime,})
                connection.commit()
            if 'End Date and Time' in changeWanted:
                ChangePrompt=[
                    {
                        'type':'input',
                        'name':'newEndDateTime',
                        'message':'Enter the new end date and time (YYYY-MM-DD HH:MM:SS):',
                        'validate':DateTimeValidator
                    }
                ]
                answers = prompt(ChangePrompt, style=custom_style_2)
                EndDateTime=answers['newEndDateTime']
                execution="update events set EndDateTime=%(EndDateTime)s where EID=%(EID)s;"
                cursor.execute(execution,{"EID":EID,"EndDateTime":EndDateTime,})
                connection.commit()
            if 'Requirements' in changeWanted:
                ChangePrompt=[
                    {
                        'type':'list',
                        'name':'Requirement',
                        'message':'Are there any requirements for your event',
                        'choices':['Yes','No']
                    },
                    {
                        'type':'input',
                        'name':'RequirementName',
                        'message':'Enter the title for your Requirement :',
                        'when':lambda answers: answers['Requirement']=='Yes'       
                    },
                    {
                        'type':'input',
                        'name':'RequirementDescription',
                        'message':'Enter the Description for your Requirement :',
                        'when':lambda answers: answers['Requirement']=='Yes'       
                    }
                ]
                answers = prompt(ChangePrompt, style=custom_style_2)
                if answers['Requirement']=='Yes':
                    Requirement={}
                    Requirement[answers['RequirementName']]=answers['RequirementDescription']
                else:
                    Requirement=None
                Requirement=json.dumps(Requirement)
                execution="update events set RequirementsForParticipants=%(Requirement)s where EID=%(EID)s;"
                cursor.execute(execution,{"EID":EID,"Requirement":Requirement,})
                connection.commit()
            if 'Ticket Type' in changeWanted:
                ChangePrompt=[
                    {
                        'type':'list',
                        'name':'TicketType',
                        'message':'Is your event Free or Ticketed:',
                        'choices':['Free','Ticketed']
                    }
                ]
                answers = prompt(ChangePrompt, style=custom_style_2)
                TicketType=answers['TicketType']
                execution="update events set type=%(TicketType)s where EID=%(EID)s;"
                cursor.execute(execution,{"EID":EID,"TicketType":TicketType,})
                connection.commit()
            EventInfoChangePrompt=[
                {
                    'type': 'list',
                    'name': 'participantInfo_choice',
                    'message': 'What would you like to do?',
                    'choices': ["Go Back","Logout","Exit"]  
                }
            ]
            answers = prompt(EventInfoChangePrompt, style=custom_style_2)
            if answers['participantInfo_choice']=="Go Back":
                ManageUpcomingEventPage(OrganizerInfo)
            if answers['participantInfo_choice']=="Logout":
                HomePage()
            if answers['participantInfo_choice']=="Exit":
                exit()
        elif answers['eventChange_choice']=="Go Back":
            ManageUpcomingEventPage(OrganizerInfo)
        elif answers['eventChange_choice']=="Logout":
            HomePage()
        elif answers['eventChange_choice']=="Exit":
            exit()
    else:
        EventChangePagePrompt=[
            {
                'type': 'list',
                'name': 'eventChange_choice',
                'message': 'What would you like to do?',
                'choices': ["Go Back","Logout","Exit"]  
            }
        ]
        answers = prompt(EventChangePagePrompt, style=custom_style_2)
        if answers['eventChange_choice']=="Go Back":
            OrganizerPastEvent(OrganizerInfo)
        elif answers['eventChange_choice']=="Logout":
            HomePage()
        elif answers['eventChange_choice']=="Exit":
            exit()

def OrganizerPastEvent(OrganizerInfo):
    OID=OrganizerInfo[0]
    OragnizerName=OrganizerInfo[1]
    os.system('cls' if os.name == 'nt' else 'clear')
    sentenceAnimate((PrintColor.color_text(32)+"Here is a list of your previously made events.(You can click on each event to see its description)"+PrintColor.reset()).center(os.get_terminal_size().columns),True)
    currentTime=datetime.now()
    execution='select * from events where startdatetime<%(currentTime)s and OID=%(OID)s;'
    cursor.execute(execution,{"currentTime":currentTime,"OID":OID})
    result=cursor.fetchall()
    briefDescription=[]
    for i in range(len(result)):
        result[i]=list(result[i])
        result[i].append(result[i][4]+"|"+str(result[i][1])+"|"+list(result[i][9])[0])
        briefDescription.append(result[i][4]+"|"+str(result[i][1])+"|"+list(result[i][9])[0])
    briefDescription.append("Go Back")
    briefDescription.append("Logout")
    briefDescription.append("Exit")
    ExploreEventsPagePrompt=[
        {
            'type': 'list',
            'name': 'event_choice',
            'message': 'Event name|Start date|Approved?(No means yet to reviewed)',
            'choices': briefDescription  
        }
    ]
    answers = prompt(ExploreEventsPagePrompt, style=custom_style_2)
    if answers["event_choice"]=="Go Back":
        OrganizerPage(OrganizerInfo)
    elif answers["event_choice"]=="Logout":
        HomePage()
    elif answers["event_choice"]=="Exit":
        exit()
    else:
        for i in result:
            if answers["event_choice"] in i:
                EventChangePage(OrganizerInfo,i,False)
                break

def AdminPage(AdminInfo):
    os.system('cls' if os.name == 'nt' else 'clear')
    AID=AdminInfo[0]
    AdminName=AdminInfo[1]
    sentenceAnimate((PrintColor.color_text(32)+"Welcome "+AdminName+"!"+PrintColor.reset()).center(os.get_terminal_size().columns),True)
    AdminPagePrompt=[
        {
            'type': 'list',
            'name': 'admin_choice',
            'message': 'What would you like to do today?',
            'choices': [
                Separator("MANAGE ADMINS"),
                "   -Approved Admins",
                "   -Rejected Admins Applications",
                "   -Pending Admin Applications",
                Separator("MANAGE ORGANIZERS"),
                "   -Approved Organizers",
                "   -Rejected Organizer Applications",
                "   -Pending Organizers Applications",
                Separator("MANAGE EVENTS"),
                "   -Approved Events",
                "   -Rejected Events",
                "   -Events Applications",
                Separator("OTHER ACTIONS"),
                "   -Logout",
                "   -Exit"
                ]  
        }
    ]
    answers = prompt(AdminPagePrompt, style=custom_style_2)
    if answers['admin_choice']=='   -Exit':
        exit()
    elif answers['admin_choice']=='   -Logout':
        HomePage()
    elif answers['admin_choice']=="   -Approved Admins":
        ApprovedAdminListPage(AdminInfo)
    elif answers['admin_choice']=="   -Rejected Admins Applications":
        RejectedAdminListPage(AdminInfo)
    elif answers['admin_choice']=="   -Pending Admin Applications":
        PendingAdminListPage(AdminInfo)
    elif answers['admin_choice']=="   -Approved Organizers":
        ApprovedOrganizerListPage(AdminInfo)
    elif answers['admin_choice']=="   -Rejected Organizer Applications":
        RejectedOrganizerListPage(AdminInfo)
    elif answers['admin_choice']=="   -Pending Organizers Applications":
        PendingOrganizerListPage(AdminInfo)
    elif answers['admin_choice']=="   -Approved Events":
        ApprovedEventListPage(AdminInfo)
    elif answers['admin_choice']=="   -Rejected Events":
        RejectedEventListPage(AdminInfo)
    elif answers['admin_choice']=="   -Events Applications":
        PendingEventListPage(AdminInfo)

def ApprovedAdminListPage(AdminInfo):
    os.system('cls' if os.name == 'nt' else 'clear')
    sentenceAnimate((PrintColor.color_text(32)+"List of all Approved admins"+PrintColor.reset()).center(os.get_terminal_size().columns),True)
    execution='select * from admin where Approved="YES";'
    cursor.execute(execution)
    result=cursor.fetchall()
    print("\x1b[38;5;201mName | Email | Phone No \x1b[0m")
    for i in result:
        print(i[1]+" | "+i[2]+" | "+i[4])
    AdminRemovalPrompt=[
        {
            'type': 'confirm',
            'message': 'Do you want to remove access of an admin?',
            'name': 'check',
        },
        {
            'type': 'input',
            'name': 'AdminRemove',
            'message': 'Please enter the email address of admin whos access you want to remove',
            'validate': lambda answers: AdminValidator(answers,AdminInfo),
            'when': lambda answers: answers["check"]==True
        }
    ]
    answers = prompt(AdminRemovalPrompt, style=custom_style_2)
    if answers["check"]==True:
        emailID=answers["AdminRemove"]
        execution="update admin set Approved='Rejected' where Email=%(EmailID)s;"
        cursor.execute(execution,{"EmailID":emailID})
        connection.commit()
        sentenceAnimate("\x1b[101mAdmin Access revoked.\x1b[0m",True)
    GoBackEventPrompt=[
        {
            'type': 'list',
            'name': 'register_choice',
            'message': 'Do you want to do next?',
            'choices': ["Go Back","Logout","Exit"]  
        }
    ]
    answers = prompt(GoBackEventPrompt, style=custom_style_2)
    if answers['register_choice']=="Go Back":
        AdminPage(AdminInfo)
    elif answers['register_choice']=="Logout":
        HomePage()
    elif answers['register_choice']=="Exit":
        exit()

def RejectedAdminListPage(AdminInfo):
    os.system('cls' if os.name == 'nt' else 'clear')
    sentenceAnimate((PrintColor.color_text(32)+"List of all Rejected admins Applications"+PrintColor.reset()).center(os.get_terminal_size().columns),True)
    execution='select * from admin where Approved="REJECTED";'
    cursor.execute(execution)
    result=cursor.fetchall()
    print("\x1b[38;5;201mName | Email | Phone No \x1b[0m")
    for i in result:
        print(i[1]+" | "+i[2]+" | "+i[4])
    AdminRemovalPrompt=[
        {
            'type': 'confirm',
            'message': 'Do you want to provide access to a rejected admin application?',
            'name': 'check',
        },
        {
            'type': 'input',
            'name': 'AdminAdd',
            'message': 'Please enter the email address of rejected admin application whos access you want to provide',
            'validate': lambda answers: AdminValidator(answers,AdminInfo),
            'when': lambda answers: answers["check"]==True
        }
    ]
    answers = prompt(AdminRemovalPrompt, style=custom_style_2)
    if answers["check"]==True:
        emailID=answers["AdminAdd"]
        execution="update admin set Approved='YES' where Email=%(EmailID)s;"
        cursor.execute(execution,{"EmailID":emailID})
        connection.commit()
        sentenceAnimate("\x1b[101mAdmin Access provided.\x1b[0m",True)
    GoBackEventPrompt=[
        {
            'type': 'list',
            'name': 'register_choice',
            'message': 'Do you want to do next?',
            'choices': ["Go Back","Logout","Exit"]  
        }
    ]
    answers = prompt(GoBackEventPrompt, style=custom_style_2)
    if answers['register_choice']=="Go Back":
        AdminPage(AdminInfo)
    elif answers['register_choice']=="Logout":
        HomePage()
    elif answers['register_choice']=="Exit":
        exit()

def PendingAdminListPage(AdminInfo):
    os.system('cls' if os.name == 'nt' else 'clear')
    sentenceAnimate((PrintColor.color_text(32)+"List of all pending admins Applications"+PrintColor.reset()).center(os.get_terminal_size().columns),True)
    execution='select * from admin where Approved="NO";'
    cursor.execute(execution)
    result=cursor.fetchall()
    print("\x1b[38;5;201mName | Email | Phone No \x1b[0m")
    for i in result:
        print(i[1]+" | "+i[2]+" | "+i[4])
    AdminCheckPrompt=[
        {
            'type': 'list',
            'message': 'Do you want to approve/reject a pending admin application?',
            'name': 'check',
            'choices':['Approve','Reject','NO']
        },
        {
            'type': 'input',
            'name': 'Reject',
            'message': 'Please enter the email address of pending admin application whom you want to reject',
            'validate': lambda answers: AdminValidator(answers,AdminInfo),
            'when': lambda answers: answers["check"]=="Reject"
        },
        {
            'type': 'input',
            'name': 'Approve',
            'message': 'Please enter the email address of pending admin application whos access you want to provide',
            'validate': lambda answers: AdminValidator(answers,AdminInfo),
            'when': lambda answers: answers["check"]=="Approve"
        }
    ]
    answers = prompt(AdminCheckPrompt, style=custom_style_2)
    if answers["check"]=="Approve":
        emailID=answers["Approve"]
        execution="update admin set Approved='YES' where Email=%(EmailID)s;"
        cursor.execute(execution,{"EmailID":emailID})
        connection.commit()
        sentenceAnimate("\x1b[101mAdmin Access provided.\x1b[0m",True)
    elif answers["check"]=="Reject":
        emailID=answers["Reject"]
        execution="update admin set Approved='REJECTED' where Email=%(EmailID)s;"
        cursor.execute(execution,{"EmailID":emailID})
        connection.commit()
        sentenceAnimate("\x1b[101mAdmin Access Rejected.\x1b[0m",True)
    GoBackEventPrompt=[
        {
            'type': 'list',
            'name': 'register_choice',
            'message': 'Do you want to do next?',
            'choices': ["Review more pending admin applications","Go Back","Logout","Exit"]  
        }
    ]
    answers = prompt(GoBackEventPrompt, style=custom_style_2)
    if answers['register_choice']=="Go Back":
        AdminPage(AdminInfo)
    elif answers['register_choice']=="Logout":
        HomePage()
    elif answers['register_choice']=="Exit":
        exit()
    elif answers['register_choice']=="Review more pending admin applications":
        PendingAdminListPage(AdminInfo)

def ApprovedOrganizerListPage(AdminInfo):
    os.system('cls' if os.name == 'nt' else 'clear')
    sentenceAnimate((PrintColor.color_text(32)+"List of all Approved organizers"+PrintColor.reset()).center(os.get_terminal_size().columns),True)
    execution='select * from organizer where Approved="YES";'
    cursor.execute(execution)
    result=cursor.fetchall()
    print("\x1b[38;5;201mName | Email | Club\Seimar \x1b[0m")
    for i in result:
        print(i[1]+" | "+i[2]+" | "+i[4])
    OrganizerRemovalPrompt=[
        {
            'type': 'confirm',
            'message': 'Do you want to remove access of an organizer?',
            'name': 'check',
        },
        {
            'type': 'input',
            'name': 'OrganizerRemove',
            'message': 'Please enter the email address of organizer whos access you want to remove',
            'validate': lambda answers: OrganizerValidator(answers),
            'when': lambda answers: answers["check"]==True
        }
    ]
    answers = prompt(OrganizerRemovalPrompt, style=custom_style_2)
    if answers["check"]==True:
        emailID=answers["OrganizerRemove"]
        execution="update organizer set Approved='Rejected' where Email=%(EmailID)s;"
        cursor.execute(execution,{"EmailID":emailID})
        connection.commit()
        sentenceAnimate("\x1b[101mOrganizer Access revoked.\x1b[0m",True)
    GoBackEventPrompt=[
        {
            'type': 'list',
            'name': 'register_choice',
            'message': 'Do you want to do next?',
            'choices': ["Go Back","Logout","Exit"]  
        }
    ]
    answers = prompt(GoBackEventPrompt, style=custom_style_2)
    if answers['register_choice']=="Go Back":
        AdminPage(AdminInfo)
    elif answers['register_choice']=="Logout":
        HomePage()
    elif answers['register_choice']=="Exit":
        exit()

def RejectedOrganizerListPage(AdminInfo):
    os.system('cls' if os.name == 'nt' else 'clear')
    sentenceAnimate((PrintColor.color_text(32)+"List of all Rejected organizers Application"+PrintColor.reset()).center(os.get_terminal_size().columns),True)
    execution='select * from organizer where Approved="REJECTED";'
    cursor.execute(execution)
    result=cursor.fetchall()
    print("\x1b[38;5;201mName | Email | Club\Seimar \x1b[0m")
    for i in result:
        print(i[1]+" | "+i[2]+" | "+i[4])
    OrganizerRemovalPrompt=[
        {
            'type': 'confirm',
            'message': 'Do you want to provie access of a rejected organizer application?',
            'name': 'check',
        },
        {
            'type': 'input',
            'name': 'OrganizerRemove',
            'message': 'Please enter the email address of organizer whom you want to provide access',
            'validate': lambda answers: OrganizerValidator(answers),
            'when': lambda answers: answers["check"]==True
        }
    ]
    answers = prompt(OrganizerRemovalPrompt, style=custom_style_2)
    if answers["check"]==True:
        emailID=answers["OrganizerRemove"]
        execution="update organizer set Approved='YES' where Email=%(EmailID)s;"
        cursor.execute(execution,{"EmailID":emailID})
        connection.commit()
        sentenceAnimate("\x1b[101mOrganizer Access Provided.\x1b[0m",True)
    GoBackEventPrompt=[
        {
            'type': 'list',
            'name': 'register_choice',
            'message': 'Do you want to do next?',
            'choices': ["Go Back","Logout","Exit"]  
        }
    ]
    answers = prompt(GoBackEventPrompt, style=custom_style_2)
    if answers['register_choice']=="Go Back":
        AdminPage(AdminInfo)
    elif answers['register_choice']=="Logout":
        HomePage()
    elif answers['register_choice']=="Exit":
        exit()

def PendingOrganizerListPage(AdminInfo):
    os.system('cls' if os.name == 'nt' else 'clear')
    sentenceAnimate((PrintColor.color_text(32)+"List of all pending organizer Applications"+PrintColor.reset()).center(os.get_terminal_size().columns),True)
    execution='select * from organizer where Approved="NO";'
    cursor.execute(execution)
    result=cursor.fetchall()
    print("\x1b[38;5;201mName | Email | Club/Seminar \x1b[0m")
    for i in result:
        print(i[1]+" | "+i[2]+" | "+i[4])
    AdminCheckPrompt=[
        {
            'type': 'list',
            'message': 'Do you want to approve/reject a pending organizer application?',
            'name': 'check',
            'choices':['Approve','Reject','NO']
        },
        {
            'type': 'input',
            'name': 'Reject',
            'message': 'Please enter the email address of pending organizer application whom you want to reject',
            'validate': lambda answers: OrganizerValidator(answers),
            'when': lambda answers: answers["check"]=="Reject"
        },
        {
            'type': 'input',
            'name': 'Approve',
            'message': 'Please enter the email address of pending organizer application whos access you want to provide',
            'validate': lambda answers: OrganizerValidator(answers),
            'when': lambda answers: answers["check"]=="Approve"
        }
    ]
    answers = prompt(AdminCheckPrompt, style=custom_style_2)
    if answers["check"]=="Approve":
        emailID=answers["Approve"]
        execution="update organizer set Approved='YES' where Email=%(EmailID)s;"
        cursor.execute(execution,{"EmailID":emailID})
        connection.commit()
        sentenceAnimate("\x1b[101mOrganizer Access provided.\x1b[0m",True)
    elif answers["check"]=="Reject":
        emailID=answers["Reject"]
        execution="update Organizer set Approved='REJECTED' where Email=%(EmailID)s;"
        cursor.execute(execution,{"EmailID":emailID})
        connection.commit()
        sentenceAnimate("\x1b[101mOrganizer Access Rejected.\x1b[0m",True)
    GoBackEventPrompt=[
        {
            'type': 'list',
            'name': 'register_choice',
            'message': 'Do you want to do next?',
            'choices': ["Review more pending Organizer applications","Go Back","Logout","Exit"]  
        }
    ]
    answers = prompt(GoBackEventPrompt, style=custom_style_2)
    if answers['register_choice']=="Go Back":
        AdminPage(AdminInfo)
    elif answers['register_choice']=="Logout":
        HomePage()
    elif answers['register_choice']=="Exit":
        exit()
    elif answers['register_choice']=="Review more pending Organizer applications":
        PendingOrganizerListPage(AdminInfo)

def ApprovedEventListPage(AdminInfo):
    os.system('cls' if os.name == 'nt' else 'clear')
    sentenceAnimate((PrintColor.color_text(32)+"List of all Approved events"+PrintColor.reset()).center(os.get_terminal_size().columns),True)
    execution='select * from events where Approved="YES";'
    cursor.execute(execution)
    result=cursor.fetchall()
    print("\x1b[38;5;201mEID | Name | Description | Start Date Time | End Date Time | Type | Requirements For Participants \x1b[0m")
    for i in result:
        print(str(i[0])+" | "+str(i[4])+" | "+str(i[3])+" | "+str(i[1])+" | "+str(i[2])+" | "+str(i[6])+" | "+str(i[7]))
    EventRemovalPrompt=[
        {
            'type': 'confirm',
            'message': 'Do you want to remove approval of an event?',
            'name': 'check',
        },
        {
            'type': 'input',
            'name': 'EventRemove',
            'message': 'Please enter the EID of the event whos approval you want to remove',
            'when': lambda answers: answers["check"]==True
        }
    ]
    answers = prompt(EventRemovalPrompt, style=custom_style_2)
    if answers["check"]==True:
        EID=answers["EventRemove"]
        execution="update events set Approved='REJECTED' where EID=%(EID)s;"
        cursor.execute(execution,{"EID":EID})
        connection.commit()
        sentenceAnimate("\x1b[101mEvent rejected.\x1b[0m",True)
    GoBackEventPrompt=[
        {
            'type': 'list',
            'name': 'register_choice',
            'message': 'Do you want to do next?',
            'choices': ["Go Back","Logout","Exit"]  
        }
    ]
    answers = prompt(GoBackEventPrompt, style=custom_style_2)
    if answers['register_choice']=="Go Back":
        AdminPage(AdminInfo)
    elif answers['register_choice']=="Logout":
        HomePage()
    elif answers['register_choice']=="Exit":
        exit()

def RejectedEventListPage(AdminInfo):
    os.system('cls' if os.name == 'nt' else 'clear')
    sentenceAnimate((PrintColor.color_text(32)+"List of all Rejeted events"+PrintColor.reset()).center(os.get_terminal_size().columns),True)
    execution='select * from events where Approved="REJECTED";'
    cursor.execute(execution)
    result=cursor.fetchall()
    print("\x1b[38;5;201mEID | Name | Description | Start Date Time | End Date Time | Type | Requirements For Participants \x1b[0m")
    for i in result:
        print(str(i[0])+" | "+str(i[4])+" | "+str(i[3])+" | "+str(i[1])+" | "+str(i[2])+" | "+str(i[6])+" | "+str(i[7]))
    EventAddPrompt=[
        {
            'type': 'confirm',
            'message': 'Do you want to provide approval to a rejected event?',
            'name': 'check',
        },
        {
            'type': 'input',
            'name': 'EventAdd',
            'message': 'Please enter the EID of the event you want to approve',
            'when': lambda answers: answers["check"]==True
        }
    ]
    answers = prompt(EventAddPrompt, style=custom_style_2)
    if answers["check"]==True:
        EID=answers["EventAdd"]
        execution="update events set Approved='YES' where EID=%(EID)s;"
        cursor.execute(execution,{"EID":EID})
        connection.commit()
        sentenceAnimate("\x1b[101mEvent approved.\x1b[0m",True)
    GoBackEventPrompt=[
        {
            'type': 'list',
            'name': 'register_choice',
            'message': 'Do you want to do next?',
            'choices': ["Go Back","Logout","Exit"]  
        }
    ]
    answers = prompt(GoBackEventPrompt, style=custom_style_2)
    if answers['register_choice']=="Go Back":
        AdminPage(AdminInfo)
    elif answers['register_choice']=="Logout":
        HomePage()
    elif answers['register_choice']=="Exit":
        exit()

def PendingEventListPage(AdminInfo):
    os.system('cls' if os.name == 'nt' else 'clear')
    sentenceAnimate((PrintColor.color_text(32)+"List of all pending event Applications"+PrintColor.reset()).center(os.get_terminal_size().columns),True)
    execution='select * from events where Approved="NO";'
    cursor.execute(execution)
    result=cursor.fetchall()
    print("\x1b[38;5;201mEID | Name | Description | Start Date Time | End Date Time | Type | Requirements For Participants \x1b[0m")
    for i in result:
        print(str(i[0])+" | "+str(i[4])+" | "+str(i[3])+" | "+str(i[1])+" | "+str(i[2])+" | "+str(i[6])+" | "+str(i[7]))
    EventCheckPrompt=[
        {
            'type': 'list',
            'message': 'Do you want to approve/reject a pending event application?',
            'name': 'check',
            'choices':['Approve','Reject','NO']
        },
        {
            'type': 'input',
            'name': 'Reject',
            'message': 'Please enter the EID of pending event application you want to reject',
            'when': lambda answers: answers["check"]=="Reject"
        },
        {
            'type': 'input',
            'name': 'Approve',
            'message': 'Please enter the EID of pending organizer application you want to approve',
            'when': lambda answers: answers["check"]=="Approve"
        }
    ]
    answers = prompt(EventCheckPrompt, style=custom_style_2)
    if answers["check"]=="Approve":
        EID=answers["Approve"]
        execution="update events set Approved='YES' where EID=%(EID)s;"
        cursor.execute(execution,{"EID":EID})
        connection.commit()
        sentenceAnimate("\x1b[101mEvent Approved.\x1b[0m",True)
    elif answers["check"]=="Reject":
        EID=answers["Reject"]
        execution="update events set Approved='REJECTED' where EID=%(EID)s;"
        cursor.execute(execution,{"EID":EID})
        connection.commit()
        sentenceAnimate("\x1b[101mEvent Rejected.\x1b[0m",True)
    GoBackEventPrompt=[
        {
            'type': 'list',
            'name': 'register_choice',
            'message': 'Do you want to do next?',
            'choices': ["Review more pending Organizer applications","Go Back","Logout","Exit"]  
        }
    ]
    answers = prompt(GoBackEventPrompt, style=custom_style_2)
    if answers['register_choice']=="Go Back":
        AdminPage(AdminInfo)
    elif answers['register_choice']=="Logout":
        HomePage()
    elif answers['register_choice']=="Exit":
        exit()
    elif answers['register_choice']=="Review more pending Organizer applications":
        PendingEventListPage(AdminInfo)

if __name__ == "__main__":
    HomePage()