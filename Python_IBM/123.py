import re
text = "Sender: bounceback@c.bloomberg.com mk"
regexp = "Sender:\s\w*@(.*\s)"
var = re.findall(regexp, text)
cctr = 'c.bloomberg.com'
bl = var[0]

if bl == cctr:
    print ("Yes")
else:
    print ("No")


print (bl)
print (cctr)

print(type(bl))
print(type(cctr))

if bl == "c.bloomberg.com":
    print ("yes")
    



