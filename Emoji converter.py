#Emoji converter

msg = input(">")
em = msg.split(" ")
dict = {
    ":)":"😊",
    ":(":"😒"
}


out = " "
for ch in em:
    out += dict.get(ch,ch)+" "
print(out)
