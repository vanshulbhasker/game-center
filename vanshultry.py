import random
import time

print"..................................................................................WELCOME TO THE GAME CENTER..........................................................................."
print 
name=raw_input("Hello Gamer Enter Your Name")


print "so",name,"its time to play..."
print
res='r'
while res=='r' or res=='R':
    
    print"press 1 to play HANGMAN"
    print"press 2 to play THE STICKS GAME"
    print"press 3 to play a G.K. quiz"
    print"press 4 to use our own encryptor and decryptor "
    print"press 5 to play the Tic Tac Toe game"
    pf=input(" choose your desired game")
    pf=int(pf)
    if pf>5 or pf<1:
        while pf>5 or pf<1:
            pf=input ("I am hard of hearing can you please choose it again...")
            pf=int(pf)
    if pf==1:
        restart='r'


        #hangman game
        print "rules:"
        time.sleep(1)
        print "#there is a word that you have to guess"
        time.sleep(3)
        print "#you will be given 10 chances to guess any character of the word "
        time.sleep(3)
        print "#every wrong guess reduces your chances to attempt by 1"
        time.sleep(3)
        print "#if your chances to attempt become 0,this guy will be hanged till death"
        time.sleep(1)

        print "        0      "
        print "       /|\     "
        print " ___/ \____"
        time.sleep(3)
        print"#every correct guess will in no way affect your chances to attempt"
        time.sleep(3)
        print"#on a side note,dont use spaces as you have to guess only a particular character of the word and space is counted as a character"
        time.sleep(5)
        print"    thats it..."
        print "    go ahead and play...."
        time.sleep(0.5)
        while restart=='r' or restart=='R':
            print
            print "good luck"
            time.sleep(2)

            print
            print
            print
            w1='creative'
            w2='wonders'
            w3='amazing'
            w4='secret'
            w5='hangman'
            i=random.randint(1,5)
            if i==1:
                word=w1
            if i==2:
                word=w2
            if i==3:
                word=w3
            if i==4:
                word=w4
            if i==5:
                word=w5
            l=len(word)
            jugaad=''
            for op in word:
                if op not in jugaad:
                    jugaad+=op

            print "your word is:-"
            dashes='_ '*l
            print dashes
            turns=10
            guesses=''
            nw=''
            photo=1
            while turns>0:
                g=raw_input("guess any character")
                if g not in word:
                    print "wrong guess"
                    turns-=1
                    if photo==1:
                        print " ________  "
                        print "|              "
                        print "|      0      "
                        print "|     /|\     "
                        print "|     / \     "
                        print"he is in the hanging area"
                    photo+=1
                    if photo==4:
                        print " ________  "
                        print "|      l       "
                        print "|      0      "
                        print "|     /|\     "
                        print "|     / \     "
                        print" | _________"
                        print"dont u want to save this innocent???"
                        print
                        print"he will die.......!!!!"

                for i in word:
                    if i==g:
                        guesses+=g
                for i in word:
                    if i in guesses:
                        print i,
                        if i not in nw:
                            nw+=i
                        
                                    
                    else:
                        print '_',
                if len(nw)==len(jugaad):
                    print
                    print
                    print"you won",name
                    print 
                    print "        0           "
                    print "       /|\         "
                    print " ___/ \____ "
                    print"the guy is free..."
                    break

                        
                print
                print "turns left=",turns
                if turns==0:
                    print " ________ "
                    print "|     |          "
                    print "|     '@        "
                    print "|     /|\        "
                    print "|     / \        "
                    print "|________  "
                    print"the guy is dead,you killed him"

                    print "you lose"
                    print"the word was",word
            restart=raw_input("like the game?? press 'r' to restart and any other key to exit")

    if pf==2:
        restart='r'
        while restart=='r' or restart=='R':
            #the sticks game
            print "rules:-"
            time.sleep(1)
            print "#there are 21 sticks in this game "
            time.sleep(1.5)
            print "#you have to choose sticks in the range(1-4)"
            time.sleep(3)
            print "#the same will be done by the computer"
            time.sleep(3)
            print "#at the end,the one who takes the last stick will lose"
            print
            print
            time.sleep(3)
            print "lets begin"
            time.sleep(1)
            print
            print

            restart='r'
            while restart=='r' or restart=='R':
                sticks=21
                while sticks>0:
                    
                    a=input("enter no. of sticks (1-4)")
                    a=int(a)
                    if sticks==1:
                        if a!=1:
                            print"there is only one stick left , you have to take it , I know I won but still as a formality, go for it"
                            continue
                    if sticks==0:
                        break

                    if a<=4 and a>=1:
                        sticks-=a
                        if sticks==0:
                            break
                        print"sticks left=",sticks
                        b=5-a
                        print "computer took",b
                        sticks-=b
                        print "sticks left=",sticks
                    else:
                        print  "out of range"
                    
                print "you took the last stick,so you lose"
                time.sleep(1)
                restart=raw_input("press r to restart the game")

    if pf==3:
        #general quiz

        print "So, " ,name, ", you picked general quiz, this is a true or false game. You will be given 20 statements. After each statement, enter 1 for true or 2 for false."
        print "caution,if u press anything other than 1 or 2 it will be counted as a wrong answer"

        jlkjl=raw_input("Press any key to continue...")
        

        userScore = 0 
        
        statementOne = int(raw_input("1:Japanese snooker tables have shorter legs than normal ones:")) 
        statementTwo = int(raw_input("2:Doughnuts originated in Holland:")) 
        statementThree = int(raw_input("3:Hollywood film idol Rudolf Valentino choked to death on a golden ratio:")) 
        statementFour = int(raw_input("4:Cleopatra was Egyptian:")) 
        statementFive = int(raw_input("5:The Egyptian goalkeeper in the 1934 World Cup Finals was called Mustapha Kamel:")) 
        statementSix = int(raw_input("6:The Mexican Hat Dance is the official dance of Mexico:")) 
        statementSeven = int(raw_input("7:Plastic surgeons in the USA have developed fake testicles for neutered dogs so the appear normal:")) 
        statementEight = int(raw_input("8:A Zeedonk is the offspring from a Zebra and a Donkey:")) 
        statementNine = int(raw_input("9:King Francis I of Portugal was known as Francis the flatulent:")) 
        statementTen = int(raw_input("10:Before forming a band, Dave Dee, Dozy, Beaky, Mick and Titch were all policemen")) 
        statementEleven = int(raw_input("11:The outlaw Butch Cassidys father was born in Blackburn Lancashire:")) 
        statementTwelve = int(raw_input("12:There is only one river in Saudi Arabia:")) 
        statementThirteen = int(raw_input("13:Between 1937 & 1945 in Germany, Heinz did a version of tinned spaghetti shaped like swastikas:")) 
        statementFourteen = int(raw_input("14:Dogs are colour blind:")) 
        statementFifteen = int(raw_input("15:Women blink twice as much as men:")) 
        statementSixteen = int(raw_input("16:The larger a chili pepper, the hotter it is:")) 
        statementSeventeen = int(raw_input("17.Film star John Wayne was in the 1936 US Olympic basket ball team:")) 
        statementEighteen = int(raw_input("18.You can get warts from touching toads:")) 
        statementNineteen = int(raw_input("19.Hair yanked out by the roots will not grow back:")) 
        statementTwenty = int(raw_input("20.Blue is the colour that is liked the most worldwide:")) 
        
                              
        if statementOne == 1: 
            userScore = userScore + 1 
        if statementTwo ==1: 
            userScore = userScore + 1 
        if statementThree == 2: 
            userScore = userScore + 1 
        if statementFour == 2: 
            userScore = userScore + 1 
        if statementFive == 1: 
            userScore = userScore + 1 
        if statementSix == 1: 
            userScore = userScore + 1 
        if statementSeven == 1: 
            userScore = userScore + 1 
        if statementEight == 1: 
            userScore = userScore + 1 
        if statementNine == 2: 
            userScore = userScore + 1 
        if statementTen == 2: 
            userScore = userScore + 1 
        if statementEleven == 2: 
            userScore = userScore + 1 
        if statementTwelve == 2: 
            userScore = userScore + 1 
        if statementThirteen == 1: 
            userScore = userScore + 1 
        if statementFourteen == 2: 
            userScore = userScore + 1 
        if statementFifteen == 1: 
            userScore = userScore + 1 
        if statementSixteen == 2: 
            userScore = userScore + 1 
        if statementSeventeen == 2: 
            userScore = userScore + 1 
        if statementEighteen == 2: 
            userScore = userScore + 1 
        if statementNineteen == 2: 
            userScore = userScore + 1 
        if statementTwenty == 1: 
            userScore = userScore + 1 

        klklk=raw_input("Press any key to find out your final score...") 
        print"Well", name,  ",you scored",userScore,"out of 20."

        if userScore == 20: 
            print"Well done",name," 100% is always appreciable.."

        if userScore < 20: 
            if userScore > 15: 
                print"So close !!!!" 

            if userScore < 15: 
                if userScore > 10: 
                    print"Not bad." 

                if userScore < 10: 
                    if userScore > 0: 
                        print"Unlucky!"

                    if userScore == 0: 
                        print"Now That's embarrasing",name


    if pf==4:
        #encryptor decryptor
        nos='0123456789'
        print"so ",name,'you have choosen to use our encryptor and decryptor'
        r='r'
        while r=='r' or r=='R':
            op=input("press 1 to encrypt text and 2 to decrypt text")
            while op!=1 and op!=2:
                op=input("I am hard of hearing please input again") 
            if op==1:
                plain_text =raw_input("enter the text to be encrypted")
                encrypted=''
                for c in plain_text:

                    if c==' ':
                        encrypted+=' '
                    else:
                        x = ord(c)
                        x-=5
                        c2 = chr(x)
                        encrypted += c2
                print "your encrypted text is :  ", encrypted
                print

                print"you can use it as your password or anywhere else,no copyright issues.....  :-)"
                print

            if op==2:
                encrypted_text =raw_input("enter encrypted text")
             
                plain_text = ""
                for c in encrypted_text:

                    if c==' ':
                        plain_text+=' '
                    else:
                        x = ord(c)
                        x+=5
                        c2 = chr(x)
                        plain_text = plain_text + c2
                print"your decrypted text is :  ", plain_text
                time.sleep(1)

            r=raw_input("liked it? then give it another try press r to restart the game or any other character to exit")

            
#the tic tac toe game

    
    if pf==5:
        rest="r"
        while rest=="r" or rest =="R":
            print "- represents blank spaces"
            print
            for i in range (3):
                for j in range (3):
                    print "- ",
                print
            print "The following is numbered as:"
            l=["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
            li=["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
            n=0
            for i in range (3):
                for j in range (3):
                    print l[n]," ",
                    n+=1
                print
            L=["-","-","-","-","-","-","-","-","-"]
            print "You are o. The computer is x."
            z=1#Counting the no. of loops
            while True:
                p=(raw_input("Enter the position : ")).upper()
                if p not in l:
                    print "Enter from the available choices"
                    continue
                for i in range(9):
                    if l[i]==p:
                        l[i]="Player"
                        L[i]="o"
                if l[0]==l[1]==l[2]:
                    print l[0],"is the winner."
                    break
                if l[3]==l[4]==l[5]:
                    print l[3],"is the winner."
                    break
                if l[6]==l[7]==l[8]:
                    print l[6],"is the winner."
                    break
                if l[0]==l[4]==l[8]:
                    print l[0],"is the winner."
                    break
                if l[2]==l[4]==l[6]:
                    print l[2],"is the winner."
                    break
                if l[0]==l[3]==l[6]:
                    print l[0],"is the winner."
                    break
                if l[1]==l[4]==l[7]:
                    print l[1],"is the winner."
                    break
                if l[2]==l[5]==l[8]:
                    print l[2],"is the winner."
                    break
                if "-" not in L:
                    print "The game is a draw"
                    break
                k=0#To check whether the set 2 has to undergo.
                while True:
                    if z==1 and l[4]!="Player":
                        c=4#Standard central place
                        break
                    elif True:
                        for i in range(0,9,3):
                            if L[i]==L[i+1]=="x" and L[i+2]!="o":
                                c=i+2
                                break
                            if L[i]==L[i+2]=="x" and L[i+1]!="o":
                                c=i+1
                                break
                            if L[i+1]==L[i+2]=="x" and L[i]!="o":
                                c=i
                                break
                            
                        else:
                            k+=1
                            for i in range(0,3):
                                if L[i]==L[i+3]=="x" and L[i+6]!="o":
                                    c=i+6
                                    break
                                if L[i]==L[i+6]=="x" and L[i+3]!="o":
                                    c=i+3
                                    break
                                if L[i+3]==L[i+6]=="x" and L[i]!="o":
                                    c=i
                                    break
                            else:
                                k+=1
                                while True:
                                    if L[0]==L[4]=="x" and L[8]!="o":
                                        c=8
                                        break
                                    if L[0]==L[8]=="x" and L[4]!="o":
                                        c=4
                                        break
                                    if L[4]==L[8]=="x" and L[0]!="o":
                                        c=0
                                        break
                                    if L[2]==L[4]=="x" and L[6]!="o":
                                        c=6
                                        break
                                    if L[2]==L[6]=="x" and L[4]!="o":
                                        c=4
                                        break
                                    if L[4]==L[6]=="x" and L[2]!="o":
                                        c=2
                                        break
                                    k+=1
                                    break 
                        if k==3:
                            for i in range(0,9,3):
                                if L[i]==L[i+1]=="o" and L[i+2]!="x":
                                    c=i+2
                                    break
                                if L[i]==L[i+2]=="o" and L[i+1]!="x":
                                    c=i+1
                                    break
                                if L[i+1]==L[i+2]=="o" and L[i]!="x":
                                    c=i
                                    break
                            else:
                                for i in range(0,3):
                                    if L[i]==L[i+3]=="o" and L[i+6]!="x":
                                        c=i+6
                                        break
                                    if L[i]==L[i+6]=="o" and L[i+3]!="x":
                                        c=i+3
                                        break
                                    if L[i+3]==L[i+6]=="o" and L[i]!="x":
                                        c=i
                                        break
                                else:
                                    loop=0
                                    #To check whether next loop has to start.
                                    while True:
                                        if L[0]==L[4]=="o" and L[8]!="x":
                                            c=8
                                            break
                                        if L[0]==L[8]=="o" and L[4]!="x":
                                            c=4
                                            break
                                        if L[4]==L[8]=="o" and L[0]!="x":
                                            c=0
                                            break
                                        if L[2]==L[4]=="o" and L[6]!="x":
                                            c=6
                                            break
                                        if L[2]==L[6]=="o" and L[4]!="x":
                                            c=4
                                            break
                                        if L[4]==L[6]=="o" and L[2]!="x":
                                            c=2
                                            break
                                        loop=1
                                        break
                                    if loop==1:
                                        corner=[0,2,6,8]
                                        midcorner=[3,5]
                                        rest=[1,4,7]
                                        while True:
                                            if (L[0]==L[8]=="o" or L[2]==L[6]=="o"):
                                                if L[3]=="-":
                                                    c=3
                                                    break
                                                if L[5]=="-":
                                                    c=5
                                                    break
                                            if (L[0]=="-") or (L[2]=="-") or (L[6]=="-") or (L[8]=="-"):
                                                c=random.choice(corner)
                                                if L[c]!="-":
                                                    continue
                                            elif (L[3] or L[5])=="-":
                                                c=random.choice(midcorner)
                                                if L[c]!="-":
                                                    continue  
                                            else:
                                                c=random.choice(rest)
                                                if L[c]!="-":
                                                    continue
                                            break
                    break
                l[c]="Computer"
                L[c]="x"
                n=0
                a=0
                for i in range (3):
                    for j in range (3):
                        print L[n]," ",
                        n+=1
                    print "                ",
                    for k in range(3):
                        print li[a]," ",
                        a+=1
                    print
                z+=1
                if l[0]==l[1]==l[2]:
                    print l[0],"is the winner."
                    break
                if l[3]==l[4]==l[5]:
                    print l[3],"is the winner."
                    break
                if l[6]==l[7]==l[8]:
                    print l[6],"is the winner."
                    break
                if l[0]==l[4]==l[8]:
                    print l[0],"is the winner."
                    break
                if l[2]==l[4]==l[6]:
                    print l[2],"is the winner."
                    break
                if l[0]==l[3]==l[6]:
                    print l[0],"is the winner."
                    break
                if l[1]==l[4]==l[7]:
                    print l[1],"is the winner."
                    break
                if l[2]==l[5]==l[8]:
                    print l[2],"is the winner."
                    break
        
            rest=raw_input("liked it??? then give it another try press r to restart the game or any other key to exit the game")
    print"game ended........"
    print
    
    print"Do You Want To Play Any Other Game?????"
    print
    
    res=raw_input("press r to restart the console in case you want to play any other game or you can press any other key to quit.......")
    print
    print


    

    

    

