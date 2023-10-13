# parking_lot/parking_lot.py
import datetime
from parking_lot import *

class ParkingLotManager:
    """
    This Class is used to create a Parking Lot with One or More level of parking.
    
    Attributes
        is_parking_lot_full, parking_lot_level_details, vehicle_with_allotted_parking_details, level_with_free_parking_start
    Methods
        allocate_parking_lot_to_vehicle(), deallocate_parking_lot_for_vehicle()
    """
    def __init__(self, *levels):
        self.is_full = False
        self.parking_lot_level_details = list(levels)
        self.vehicle_with_allotted_parking_details = {}
        self.level_with_free_parking_start = 0
        self.total_levels = len(self.parking_lot_level_details)
    
    def __str__(self):
        return (f"{BLUE} Parking Lot Manager {RESET}\nIs Parking Lot Full : {self.is_full}\nLevels Detail: {len(self.parking_lot_level_details)} levels\nFilled Parking Lot Count : {len(self.vehicle_with_allotted_parking_details)}")

    def add_level(self,level):
        for existing_level in self.parking_lot_level_details:
            if existing_level.level_name == level.level_name:
                print("Level with this name already exist")
                return False
        else:
            self.parking_lot_level_details.append(level)
            return True

    def search_vehicle_parking_spot(self,vehicel_number):
        if vehicel_number in self.vehicle_with_allotted_parking_details:
            return self.vehicle_with_allotted_parking_details[vehicel_number]
        else:
            print("Vehicel with this number is not in parking spot")
            return False

    def allocate_parking_lot_to_vehicle(self,vehicel_number):
        if self.is_full:
            print("Parking Lot is Full")
            return False
        if len(self.parking_lot_level_details) == 0:
            print("Parking Lot Levels is Empty")
            return False
        if vehicel_number in self.vehicle_with_allotted_parking_details:
            print("Vehicle is already in parking spot")
            return False
        for index in range(self.level_with_free_parking_start,self.total_levels):
            if not self.parking_lot_level_details[index].is_full():
                self.level_with_free_parking_start = index
                allocated_spot = self.parking_lot_level_details[index].get_available_spot()
                allotted_parking_detail = {
                    'spot_detail':allocated_spot,
                    'created_date': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                }
                self.vehicle_with_allotted_parking_details[vehicel_number] = allotted_parking_detail
                if index == self.total_levels-1 and self.parking_lot_level_details[index].is_full():
                    self.is_full = True
                return allotted_parking_detail
        else:
            self.is_full = True
            return False


    def deallocate_parking_lot_for_vehicle(self,vehicel_number):
        if vehicel_number in self.vehicle_with_allotted_parking_details:
            for level in self.parking_lot_level_details:
                if level.level_name == self.vehicle_with_allotted_parking_details[vehicel_number]['spot_detail']['level']:
                    level.put_released_spot(self.vehicle_with_allotted_parking_details[vehicel_number]['spot_detail']['spot'])
                    break
            else:
                print("Unable to find the level in parking lot")
                return False
            
            del self.vehicle_with_allotted_parking_details[vehicel_number]
            self.level_with_free_parking_start = 0
            self.is_full = False
            return True
        else:
            print("Vehicle is not in parking spot")
            return False
        



