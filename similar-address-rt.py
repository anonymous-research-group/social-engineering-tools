# This program is basically the same as another one. This one will randomly generate some address and test whether there exists a similar address.
import random
from ethereum.utils import check_checksum
from web3 import Web3
import secrets

w3=Web3('wss://mainnet.infura.io/v3/<ADD YOUR INFURA KEY HERE>')

letterList=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','A','B','C','D','E','F']
upper=['A','B','C','D','E','F']
lower=['a','b','c','d','e']
startIndex=17
endIndex=27

LETTERS=22
TESTS=10000
MAX=(endIndex-startIndex)*LETTERS


replacingSequence=list(range(0,MAX))
random.shuffle(replacingSequence)

total_found=0
total_tested=0
for _ in range(0,TESTS):
    originalAccount=w3.eth.account.create(secrets.token_hex(32))
    originalAddress=originalAccount.address
    if not check_checksum(originalAddress):
        print("Invalid EIP55 address")
    else:
        total_tested+=1
        found=False
        k=0
        replacedAddress=""
        while not found and k<MAX:

            position=startIndex+replacingSequence[k]//LETTERS
            replacedLetter=letterList[replacingSequence[k]%LETTERS]
            originalLetter=originalAddress[position]
            if replacedLetter.lower()!=originalLetter.lower():
                temp=list(originalAddress)
                temp[position]=replacedLetter
                replacedAddress="".join(temp)
                if check_checksum(replacedAddress):
                    found=True
            k=k+1

        if found:
            print("ORIG:", originalAddress, "ORIG. PRIV. KEY:", w3.toHex(originalAccount.privateKey)[2:], "EIP-55-MATCHING SUB:", replacedAddress)
            total_found+=1


print(total_found," out of ",total_tested )


