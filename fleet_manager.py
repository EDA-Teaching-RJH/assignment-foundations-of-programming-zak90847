crew_names =["Janeway", "Chakotay", "Tuvok","Seven"]
crew_ranks =["Captain", "Commander","Lieutenant", "Specilist"]
crew_divs =["Command", "Command", "Security", "Science"]

def show_loading_screen():
    """Hanles the boot sequence"""
    print("BOOTING SYSTEM...\n...\nWELCOME TO FLEET COMMAND")
    for i in range(5):

        print(f"Loading module{i}")
    
def display_crew():
    """Prints all crew members in a formatted list."""
    print(f"\n--- Current Crew List ---")
    for i in range(len(crew_names)):
            print(f"{crew_names[i]} - {crew_ranks[i]} ({crew_divs[i]})")

def add_crew_member():
        """Collects input and adds a new member to all lists simultaneously"""
        name = input("Name: ")
        rank = input("Rank: ")
        div = input("Division: ") 

        crew_names.append(name)
        crew_ranks.append(rank)
        crew_divs.append(div)
        print(f"Success: {name} added to the database")

def remove_crew_member():
            """Safely removes a member by name after verifying they exist."""
            name = input("Name to remove: ")
            if name in crew_names:
                idx = crew_names.index(name)
                crew_names.pop(idx)
                crew_divs.pop(idx)
                crew_ranks.pop(idx)
                print(f"Entry for {name} deleted")
            else:
                print("Error: Name not found in system.")
def analyze_ranks():
            """Calculates and displays officer statistics (Counting Captains and Commanders)."""
            high_rank_count = 0
            for rank in crew_ranks:
                if rank == "Captain" or rank == "Commander":
                    high_rank_count += 1
            print(f"Analysis Complete. High ranking officers detected: {high_rank_count}")
                    
def main_menu():
                """The central controller for the application logic"""
                show_loading_screen()
                
                while True:
                    print("/n--- MAIN MENU ---")
                    print("1. View Crew")
                    print("2. Add Crew")
                    print("3. Remove Crew")
                    print("4. Analyze Data")
                    print("5. Exit")
                   
                    choice = input("Selection : ")
                    if choice == "1": display_crew()               
                    elif choice == "2": add_crew_member()             
                    elif choice == "3": remove_crew_member()
                    elif choice == "4": analyze_ranks()
                    elif choice == "5":
                        print("Shutting down. Goodbye , Captain.")
                    break
                else:
                    print("Invalid selection . Please try again.")

if __name__ == "__main__":
            main_menu()