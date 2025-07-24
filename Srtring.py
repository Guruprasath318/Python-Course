#String method
name = "Guruprasath"
print(name.capitalize())
print(name.casefold())

#indexing
mobile="8526225895"
secret_num=mobile[:2] + "******" + mobile[-2:]
print(secret_num)

#title method
song="shape OF you"
artist="GuruPrasath S"
formatted_term=f"{song.title()} - {artist.title()}"
print(formatted_term)

#replace method
location="chennai central"
transfer=location.replace("chennai central","Thambaram")
print(transfer)

#split & strip method 
msg="your coupon is: UX52365. Please save it"
coupon=msg.split(":")[1].split(".")[0].strip()
print(coupon)

#find method
#method 1
strn="Hi this is your gp"
if "gp" in strn:
    print("Yes its correct")

#method 2
find=strn.find("gp")
print(find)

#firt and last name 
initial="".join([word[0].upper() for word in name.split()])
print(initial)

#strip method
dirty=" jktamilan   "
clean=dirty.strip()
print(clean)

#len method
s1="that my portfolio for viewing the exited to show in publically"
length=len(s1.split())
print(length)