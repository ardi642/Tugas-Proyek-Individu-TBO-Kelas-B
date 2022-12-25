# Python3 program to validate
# domain name
# using regular expression
import re

# Function to validate
# domain name.
def isValidDomain(str):
    # Regex to check valid
    # domain name.
    regex = "^((?!-)[A-Za-z0-9-]" + "{1,63}(?<!-)\\.)" +"+[A-Za-z]{2,6}"
    # Compile the ReGex
    p = re.compile(regex)
    # If the string is empty
    # return false
    if (str == None):
        return False

    # Return if the string
    # matched the ReGex
    if(re.search(p, str)):
        return True
    else:
        return False

while True:
    namaDomain = input("Masukkan Nama Domain : ")
    cek = isValidDomain(namaDomain)

    if (cek):
        print("Nama Domain " + namaDomain + " valid")
    else:
        print("Nama Domain " + namaDomain + " tidak valid")
    
    print()
    ulang = input("Apakah ingin memvalidasi nama domain lagi ? (y/t) : ")

    if (ulang == "y" or ulang == 'Y"):
        # os.system("cls")
        print()
        continue
    else:
        break
        
