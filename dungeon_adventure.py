import random

def main():
    def setup_player():
        #create a variable called name using user input
        #retun a dictionary of player stats: name, health (set a starting health of 10), and inventory (set to an empty list)
        name = input("What is your name: ")
        return {
            "name": name,
            "health": 10,
            "inventory": []
        }


    def create_treasures():
        return {
            "Self-Sealing Stem Bolt": 25,
            "Latinum Bar": 100,
            "Coil Spanner": 40,
            "Comm Badge": 10
        }


    def display_options(room_number):
        print(f"\nYou are currently in Room {room_number}")
        print("1. Search for treasure")
        print("2. Move to next room")
        print("3. Check health and inventory")
        print("4. Quit the game")

    def search_room(player, treasures):
        outcome = random.choice(["treasure", "trap"])

        if outcome == "treasure":
            random_treasure = random.choice(list(treasures))
            print(f"You found: {random_treasure}")
            player["inventory"].append(random_treasure)
            
        else:
            print("\nYou were hit by a trap taking 2 damage points!")
            player["health"] -= 2
        

    def check_status(player):
        print(f"\n{player["name"]} has {player["health"]} health points.")
        
        if len(player["inventory"]) != 0:
            stringified_inventory = ", ".join(player["inventory"])
            print(f"Your inventory contains: {stringified_inventory}")
        else:
            print("Your inventory is empty!")


    def end_game(player, treasures):
        print("\nThe game is over")
        total_inv_value = 0
        for item in player["inventory"]:
            if item in treasures.keys():
                total_inv_value += treasures[item]
        check_status(player)
        print(f"Final Gold: {total_inv_value}")
        

    def run_game_loop(player, treasures):
        for room in range(1, 6):
            while player["health"] > 0:           
                display_options(room)
                choice = input("\nWhat is your choice (1-4): ").strip()

                if choice == "1":
                    search_room(player, treasures)

                elif choice == "2":
                    break
                
                elif choice == "3":
                    check_status(player)

                elif choice == "4":
                    end_game(player, treasures)
                    return

                else:
                    print("Invalid Choice")
                    continue

        end_game(player, treasures)

    #game starts here - LEAVE EVERYTHING BELOW HERE THE SAME
    player = setup_player()
    treasures = create_treasures()
    run_game_loop(player, treasures)

if __name__ == "__main__":
    main()