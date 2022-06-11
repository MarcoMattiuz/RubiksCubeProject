from numpy import *

"""         
                    -----
                  | Y Y Y |
                  | Y Y Y | 
                  | Y Y Y |
                    -----
                  | G G G |
                  | G G G |
                  | G G G |
            -----   -----   -----   
          | O O O | W W W | R R R | 
          | O O O | W W W | R R R | 
          | O O O | W W W | R R R | 
            -----   -----   -----   
                  | B B B |
                  | B B B |
                  | B B B |
                    -----
"""  
"""         
                    -----
                  | N N N |
                  | N N N | 
                  | 2N N N |
                    -----
                  | B B B |
                  | B B B |
                  | 1B B B |
            -----   -----   -----   
          | L L3 L | 0D D D | 4R R R | 
          | L L L | D D D | R R R | 
          | L L L | D D D | R R R | 
            -----   -----   -----   
                  | F F 5F |
                  | F F F |
                  | F F F |
                    -----
"""  

class cubeSolver:
    cube = []*6

    def __init__(self,array):
        self.cube = array.copy()


    def D_move(self): 
        
        face = self.cube[1][-3:]
       
        #green face
        self.cube[1][6] = self.cube[4][6]
        self.cube[1][7] = self.cube[4][7]
        self.cube[1][8] = self.cube[4][8]
        
        #red face
        self.cube[4][6] = self.cube[5][6]
        self.cube[4][7] = self.cube[5][7]
        self.cube[4][8] = self.cube[5][8]

        #blue face
        self.cube[5][6] = self.cube[3][6]
        self.cube[5][7] = self.cube[3][7]
        self.cube[5][8] = self.cube[3][8]

        #orange face
        self.cube[3][6] = face[0]
        self.cube[3][7] = face[1]
        self.cube[3][8] = face[2]
        





     
