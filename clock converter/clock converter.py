def convert24():
    str1=input("enter your time 00:00:00 AM/PM=")  
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]  
    elif str1[-2:] == "AM":
        return str1[:-2]  
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]    
    else:
        return str(int(str1[:2]) + 12) + str1[2:8] 
# here we are converting 12 hours watch into 24 hours watch

def convert12():
    str2=input("enter your time 00:00:00=")
    if str2[0]+str2[1]=="00":
        return "00"+" PM"
    if str2[0]+str2[1]=="12":
        return "12"+" AM"
    if int(str2[0]+str2[1])>=1 and int(str2[0]+str2[1])<=11:
        return str2+" AM"
    if int(str2[0]+str2[1])>=13 and int(str2[0]+str2[1])<=23:
        return str(int(str2[0]+str2[1])-12)+" PM"
    else:
        return "input out of range"
# here we are converting 24 hours watch into 12 hours watch

def main():
    convert=input("enter which watch you want to convert 12/24=")
    if convert=="12":
        print(convert24())
    else:
        print(convert12())
main()
# here we create function for which watch we want to convert 
