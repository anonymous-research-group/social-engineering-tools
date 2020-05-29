import random
import sys
from ethereum.utils import check_checksum

letterList=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','A','B','C','D','E','F']
upper=['A','B','C','D','E','F']
lower=['a','b','c','d','e']
startIndex=17
endIndex=27     #start with 0x, so indices [17,27) is the middle 10 letters

LETTERS=22
MAX=(endIndex-startIndex)*LETTERS                     # there are 10 positions to replace, and every position has 22(0-9,a-f,A-F) possible symbols. We only replace one symbol, so there are 22*10=220 possible choices. Of course, some of them are invalid (such as replacing "a" by "a", that can be filtered later).
replacingSequence=list(range(0,MAX))                  # generate a sequence from 0 to 219 to represent 220 choices.
random.shuffle(replacingSequence)                     # Shuffle the sequence to make the search be random. It doesn't matter if don't shuffle.


originalAddress=sys.argv[1]                            # get the input from command line
if not check_checksum(originalAddress):
    print("Invalid EIP55 address")                      #check whether the input is valid
else:
    found=False
    k=0
    replacedAddress=""
    while not found and k<MAX:

        position=startIndex+replacingSequence[k]//LETTERS           #we use number 0 to 219 to represent replacing choices. Here we map the number to the choice, i.e. the position and the letter
        replacedLetter=letterList[replacingSequence[k]%LETTERS]


        originalLetter=originalAddress[position]
        #print(k,position,originalLetter,replacedLetter)

        if replacedLetter.lower()!=originalLetter.lower():          #if the original letter and replaced letter are the same, the replacing is invalid
            temp=list(originalAddress)
            temp[position]=replacedLetter
            replacedAddress="".join(temp)
            if check_checksum(replacedAddress):                     #generate the replaced address. Check whether it is a valid EIP-55 address.
                found=True
        k=k+1

    if found:
        print(replacedAddress)
    else:
        print("not found")
