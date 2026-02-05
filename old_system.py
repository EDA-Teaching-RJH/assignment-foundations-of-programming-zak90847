n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"] 

active = True

def run_system_monolith():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    
    
    loading = 0
    while loading < 5:
        print("Loading module " + str(loading))
        loading += 1  #the loading sequence never ends because the computer is never told 
    #to increase the counter variable.
    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = input("Select option: ")
        
        if opt == "1": #The program fails to recognise menu choices because it uses the giving
            print("Current Crew List:") #"giving a value" symbol(=) isntead of the comparing
                                        # values symbol(==).
            for i in range(len(n)): #The system crashes when trying to view the crew because
                print(n[i] + " - " + r[i]) #it searches for 10 people when only 4 exist.
                
        elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            
           
            n.append(new_name)#new crew memebers are added without rank or division which
            r.append(new_rank)# breaks the organisation of the database.
            d.append(new_div)#Because different lists are updated at different times,
            print("Crew member added.")#names eventually stop matching up with the correct ranks.
            
        elif opt == "3":
            rem = input("Name to remove: ")
            if rem in n:#the script shuts shown instantly if you try and remove a name
                idx = n.index(rem) #contains a typo or isnt on the list.
            n.pop(idx)
            r.pop(idx)
            d.pop(idx)
            print("Removed.")
        else:
            print("Error: crew member not found in data base.")
            
            if opt == "4":
                print("Analyzing...")
        count = 0
        for rank in r:
                if rank == "Captain" or rank == "Commander":#The officer count is always wrong
                    count = count + 1#because the code accidently labels every single person
                   #as a high-ranking officer
                    print("High ranking officers: " + str(count)) #The program crashes when showing
                elif opt == "5":#results because it tries to combine a mathematical number and a
                    print("Shutting down.")#text sentence into one line.
                    break
            
        else:
            print("Invalid.")
            
        
        x = 10
        if x > 5:
            print("System Check OK")
        else:
            print("System Failure")
            
       
        if len(n) > 0:
            print("Database has entries.")
        if len(n) == 0:
            print("Database empty.")

        
        fuel = 100
        consumption = 0
        while fuel > 0:
            
            print("Idling...")
            feul-= 100 #The feul checking logic is useless because it is forced to stop immediately
            break #after it starts regardless of the fuel left.
            
        print("End of cycle.")

run_system_monolith()#The program appears to do nothing when started becasue the instrucution to
#actually run the system missing its activation brackets.
