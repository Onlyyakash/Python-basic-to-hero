st = input("enter message: ")
words = st.split(" ")
coding =  input("1 for coding or 0 for decoding")
coding = True if (coding=="1") else False
print(coding)
if(coding):
    nwords = []
    for word in words:
     if(len(word) >= 3):
         r1 = "zhp"
         r2 = "qmf"
         stnew = r1 + word[1:] + word[0] + r2
         nwords.append(stnew) 
     else:
        nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords = []
    for word in words:
     if(len(word) >= 3):
         stnew = word[3:-3] 
         stnew = stnew[-1] + stnew[:-1]
         nwords.append(stnew) 
     else:
        nwords.append(word[::-1])
    print(" ".join(nwords))


#alternative way of coding and decoding
'''
def encode_word(word):
    if len(word) >= 3:
        r1 = "zhp"
        r2 = "qmf"
        return r1 + word[1:] + word[0] + r2
    else:
        return word[::-1]

def decode_word(word):
    if word.startswith("zhp") and word.endswith("qmf"):
        return word[3:-3][-1] + word[3:-3][:-1]
    else:
        return word[::-1]

def process_message(message, coding=True):
    words = message.split(" ")
    if coding:
        return " ".join(encode_word(word) for word in words)
    else:
        return " ".join(decode_word(word) for word in words)
message = input("Enter message: ")
coding_choice = input("1 for coding or 0 for decoding: ")
coding = True if (coding_choice == "1") else False
print(process_message(message, coding))
'''