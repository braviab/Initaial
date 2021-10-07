import re
#if number contains any of the given expressions its an invalid card
number="[a-zA-z-\s]"
#to check user input is valid otherwise promt the user again for valid input
temp=0
while(temp==0):
    user_input=input()
    if(re.search(number,user_input)):
        temp=0
    else:
        temp=1
#checksum
z=len(user_input)
card=int(user_input)
sum1=0
sum2=0
while(z!=0):
    lastdigit=card%10
    sum1=sum1+lastdigit
    card=card // 10
    lasttolast=(card % 10)*2
    if lasttolast> 9:
        a=lasttolast%10
        sum2=sum2+a
        b=lasttolast//10
        sum2=sum2+b
    else:
        sum2=sum2+lasttolast
    card=card //10
    z=z-1
sum=sum1+sum2
checksum=sum%10
c=user_input
if checksum==0:
    Len=len(c)
    if Len==15 and (int(c[0:2])==34 or int(c[0:2])==37):
        print("AMERICAN EXPRESS")

    elif Len==16 and (int(c[0:2])<=55 and int(c[0:2])>=51):
        print("MASTER CARD")
    elif Len<=16 or Len>=13 and int(c[0:1])==4:
        print("VISA")
else:
    print("INVALID")