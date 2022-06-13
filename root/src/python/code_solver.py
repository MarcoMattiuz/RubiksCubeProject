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
#methods D,F,R,L,B - inverse DI,FI,RI,LI,BI
class cubeSolver:
    cube = []*6

    def __init__(self,array):
        self.cube = array.copy()


    def D_move(self): 
        #green face start
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

    def DI_move(self): 
        #green face start
        face = self.cube[1][-3:]
       
        #green face
        self.cube[1][6] = self.cube[3][6]
        self.cube[1][7] = self.cube[3][7]
        self.cube[1][8] = self.cube[3][8]
        
        #orange face
        self.cube[3][6] = self.cube[5][6]
        self.cube[3][7] = self.cube[5][7]
        self.cube[3][8] = self.cube[5][8]

        #blue face
        self.cube[5][6] = self.cube[4][6]
        self.cube[5][7] = self.cube[4][7]
        self.cube[5][8] = self.cube[4][8]

        #red face
        self.cube[4][6] = face[0]
        self.cube[4][7] = face[1]
        self.cube[4][8] = face[2]    
        
    def F_move(self): 
        # yellow face start
        face = self.cube[2][:3]
       
        #yellow face
        self.cube[2][0] = self.cube[3][2]
        self.cube[2][1] = self.cube[3][5]
        self.cube[2][2] = self.cube[3][8]
        
        #orange face
        self.cube[3][2] = self.cube[0][8]
        self.cube[3][5] = self.cube[0][5]
        self.cube[3][8] = self.cube[0][2]

        #white face
        self.cube[0][6] = self.cube[4][0]
        self.cube[0][7] = self.cube[4][3]
        self.cube[0][8] = self.cube[4][6]

        #red face
        self.cube[4][0] = face[2]
        self.cube[4][3] = face[1]
        self.cube[4][6] = face[0]    





     
