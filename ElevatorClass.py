from typing import List
from InputData import ElevatorLoad, ElevatorInputData

class Elevator:
    def __init__(self, load: ElevatorLoad, id: int, floors: List[int] = [1,2,3,4,5], max_load: int = 1300):
        self.load = load
        self.id = id
        self.floors = floors
        self.max_load = max_load
        self.current_floor = self.floors[0]
        self.direction = self.load.input_load[0].direction
        self.total_load_count = len(self.load.input_load)
         
    def check_floor(self, floor: int) -> bool:
        if floor in self.floors:
            return True
        else:
            return False
        
    def check_load(self) -> bool:
        if self.load.total_load() >= self.max_load: 
            return False
        else:
            print("Lift is moving!")
            return True
    
    def get_stack_by_direction(self) -> List[ElevatorInputData]:  
        return self.load.get_load_by_direction(direction = self.direction)
               
    def update_direction(self) -> None:
        if self.direction == "UP":
            self.direction = "DOWN"
        else:
            self.direction = "UP"
        
    def update_current_floor(self, floor: int) -> None:
        self.current_floor = floor
          
    def move(self, load_input: ElevatorInputData) -> str:             
        if load_input.direction.upper() == "UP":
            return (f"Elevator {self.id} is moving up from {self.current_floor} to {load_input.floor}.")
        else:
            return (f"Elevator {self.id} is moving down from {self.current_floor} to {load_input.floor}.")  
        
    def run_by_direction(self) -> None:
        for call in self.get_stack_by_direction():
            self.total_load_count -= 1
            if self.check_floor(floor = call.floor):      
                print(self.move(load_input = call))
                self.update_current_floor(floor = call.floor)         
            else:
                print(f"Enter any floors only within: {self.floors}") 
           
    def process_load(self) -> None:  
        if self.check_load():
            while self.total_load_count > 0:
                self.run_by_direction()                 
                self.update_direction()   
        else:
            print("More than max loading capacity of the lift is reached.")
       

            

if __name__ == "__main__":
    e = ElevatorInputData("UP",3)
    v = ElevatorInputData("DOWN",1,100)
    c = ElevatorInputData("UP",2)
    l = ElevatorInputData("DOWN",4)
    elev = ElevatorLoad([e,v,c,l])
    
    e1 = Elevator(load = elev, id = 1)  
    #print(e1.current_floor)
    e1.process_load()
    # print(e1.current_floor)
