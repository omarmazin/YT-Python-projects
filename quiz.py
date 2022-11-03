print("Welcome to quiz")

play = input("[+] Do you want to play ? ")
if play != "yes":
    print("Goodbye")
    quit()
print("Let's Start !")
# The correct answer is : 18


def quiz():
    answer = int(input("How old are you : ")) #string == str #integer == int
    
    if answer == 18:
        print("[+] Congrats!")
        quit()
    else : 
        print("[-] nonono")
        return quiz()
quiz()