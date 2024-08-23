def ceaser_cipher(key,message):
        emsg=""
        up="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        low="abcdefghijklmnopqrstuvwxyz"
        for i in message:
                if i.isdigit():
                        n=int(i)
                        n=(n+key)%10
                        emsg+=str(n)
                elif i.isalpha():
                        if i.isupper():
                                index=up.find(i)
                                index=(index+key)%26
                                emsg+=up[index]
                        else:
                                index=low.find(i)
                                index=(index+key)%26
                                emsg+=low[index]
                else:
                        emsg+=i
        return emsg
s=input("Enter Message:")
key=int(input("Enter key:"))
if(key>0):
        print("Encrypted message is: ",ceaser_cipher(key,s))
else:
        print("Invalid Key")