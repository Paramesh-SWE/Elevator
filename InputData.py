from typing import List
from dataclasses import dataclass

#Comments
@dataclass
class ElevatorInputData():   
    direction : str
    floor : int
    weight : int = 70
        
class ElevatorLoad:
    def __init__(self, input_load: List[ElevatorInputData]):
        self.input_load = input_load
        
    def total_load(self) -> int:
        total_load = 0
        for call in self.input_load:
            total_load += call.weight
        return total_load
          
    def get_load_by_direction(self,direction) -> List[ElevatorInputData] | bool:
        load_by_direction = []
        for call in self.input_load:
            if call.direction == direction:
                load_by_direction.append(call)
        return load_by_direction if len(load_by_direction) > 0 else False
    
    
if __name__ == "__main__":
    e = ElevatorInputData("UP",4)
    v = ElevatorInputData("DOWN",3)
    c = ElevatorInputData("UP",4)
    elev = ElevatorLoad([e,v,c])
    print(elev.get_load_by_floor(3))
    print(elev.get_load_by_direction("UP"))
    print(elev.get_load_by_direction("DOWN"))
