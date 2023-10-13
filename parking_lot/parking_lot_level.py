# parking_lot/parking_lot_level.py
from parking_lot import *

class ParkingLotLevel:

    def __init__(self,level_name,total_spot,spot_start_number=1):
        self.level_name = level_name
        self.total_spot = total_spot
        self.spot_start_number = spot_start_number
        self.available_spots = None
        self.__reset_available_spots()
    
    def get_available_spot(self):
        if len(self.available_spots):
            return {"level":self.level_name,"spot":self.available_spots.pop()}
        return False
    
    def put_released_spot(self,spot_number):
        self.available_spots.append(spot_number)
        if len(self.available_spots) == self.total_spot:
            self.__reset_available_spots()
        return True
    
    def is_full(self):
        return False if len(self.available_spots) else True


    def __reset_available_spots(self):
        self.available_spots = [number for number in range(self.spot_start_number + self.total_spot-1,self.spot_start_number-1,-1)]
    
    def __str__(self):
        return (f"\n{L_BLUE} Parking Lot Level {BOLD} {self.level_name} {RESET}\nTotal Spot : {self.total_spot}\nAvailable Spot : {self.available_spots}\nLevel is Full : {self.is_full()}")
    