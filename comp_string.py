# Mission string pe comparison operator chalana.
print("CONSISTENCY> INTENSITY")
print("====Name sorting checker===")
name1=input("put your first name here:")
name2=input("put second name here:")
print(name1==name2)
print(name1 !=name2)
print(name1 > name2)  #  Dictionary mein baad mein aata?
print(name1 < name2 )  #  fivtionary mein pehele aata?
print("====LOGIC===")
if name1.lower()==name2.lower():
    print("name is same ")
elif name1.lower() < name2.lower():
    print (f"first name dictionary mein pehle aayega ")
else:
    print(f"second name dictionary mein pehle aayega")        
    print("consistency >intensity")