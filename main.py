from parking_lot.parking_lot import ParkingLotManager
from parking_lot.parking_lot_level import ParkingLotLevel

# Terminal Text Alteration Code
RESET = '\x1b[0m'
BOLD = '\x1b[1m'
BG_GRAY = '\x1b[7m'
UNDER_LINE = '\x1b[4m'

RED = '\x1b[31m'
GREEN = '\x1b[32m'

# Define the main function
def main():
    level_a = ParkingLotLevel('A',20)
    level_b = ParkingLotLevel('B',20,21)
    parking_lot_manager = ParkingLotManager(level_a,level_b)

    help()
    while True:
        user_input = list(input('>>>').split(' '))
        try:
            if len(user_input) == 1 and len(user_input[0])>6:
                # If the length of input string word is 1 and word length is grater than 6. Then it is a vehicel number
                detail = parking_lot_manager.allocate_parking_lot_to_vehicle(user_input[0])
                if detail:
                    print(f"Parking Spot is: {detail['spot_detail']}")
                else:
                    print("Parking spot finding failed.")
            elif user_input[0].lower() == 's':
                if len(user_input[1]):
                    detail = parking_lot_manager.search_vehicle_parking_spot(user_input[1])
                    print(detail['spot_detail'])
                else:
                    print("Please enter a valid vehicel number")
            elif user_input[0] == 'rm':
                if user_input[1]:
                    if parking_lot_manager.deallocate_parking_lot_for_vehicle(user_input[1]):
                        print("Successfully Cleared the parking spot")
                else:
                    print(f"{RED} Please input correct format {RESET}")
            elif user_input[0] == 'add' and len(user_input) >2:
                level_name = user_input[1]
                total_spot = int(user_input[2])
                start_number = int(user_input[3]) if len(user_input) == 4 else 1
                level = ParkingLotLevel(level_name,total_spot,start_number)
                if parking_lot_manager.add_level(level):
                    print(f"{GREEN} Level added successfully {RESET}")
                else:
                    print(f"{RED} Level creation failed {RESET}")
            elif user_input[0] == 'info':
                print(parking_lot_manager)
                for level in parking_lot_manager.parking_lot_level_details:
                    print(level)
            elif user_input[0] == 'exit':
                choice = input("If exit all the stored data will be deleted. Do you want exit [Y/n] : ")
                if choice == 'Y':
                    break
            elif user_input[0] == 'help':
                help()
            else:
                raise
        except:
            print(f"{RED} Please enter a valid input {RESET}")
        
        
def help():
    print(f"""
          {BOLD} {UNDER_LINE} Parking Lot Instruction {RESET}\n
          To get parking spot for a vehicle just type the '{BG_GRAY} <vehicle number>{RESET}'.\n
          Eg: {BOLD} WX11YZ111 {RESET}\n
          To search parked vehicel detail use '{BG_GRAY}s <vehicle number>{RESET}'\n
          Eg: {BOLD} s WX11YZ1111 {RESET}\n
          To deallocated parking lot of a vehicle '{BG_GRAY}rm <vehicle number>{RESET}'\n
          Eg: {BOLD} rm WX11YZ1111 {RESET}\n
          To add new level in parking lot '{BG_GRAY}add <level name> <total spot> <spot starting number (optional)>{RESET}'\n
          Eg: {BOLD} add X 25 5 {RESET}\n
          To show information about parking lot and levels use '{BG_GRAY}info{RESET}'\n
          Eg: {BOLD} info {RESET}\n
          To show HELP '{BG_GRAY}help{RESET}'\n
          Eg: {BOLD} help {RESET}\n
          To exit from application '{BG_GRAY}exit{RESET}'\n
          Eg: {BOLD} exit {RESET}\n
          """)


# Invoke the main function when the script is run
if __name__ == "__main__":
    main()