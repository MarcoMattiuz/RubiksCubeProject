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

    #D works
    def D_move(self): 
        #green face start
        face = self.cube[1][-3:]
        whiteFaceRow = self.cube[0][:3]
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
    
        #first row 
        self.cube[0][:3] = [self.cube[0][6],self.cube[0][3],whiteFaceRow[0]]
        #second row
        whiteFace2Row = self.cube[0][3:6] 
        self.cube[0][3:6] = [self.cube[0][7],self.cube[0][4],whiteFaceRow[1]]
        #third row 
        self.cube[0][-3:] =  [self.cube[0][8],whiteFace2Row[2],whiteFaceRow[2]]
     

    #DI works  
    def DI_move(self): 
        #green face start
        face = self.cube[1][-3:]
        whiteFaceRow = self.cube[0][:3]
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
        #change green face orientation

           #first row 
        self.cube[0][:3] = [whiteFaceRow[2],self.cube[0][5],self.cube[0][8]]
        #second row
        whiteFace2Row = self.cube[0][3:6] 
        self.cube[0][3:6] =[whiteFaceRow[1],self.cube[0][4],self.cube[0][7]]
        #third row 
        self.cube[0][-3:] = [whiteFaceRow[0],whiteFace2Row[0],self.cube[0][6]]
    #F works    
    def F_move(self): 
        # yellow face start
        face = self.cube[2][-3:]
        greenFaceRow = self.cube[1][:3]
        #yellow face
        self.cube[2][6] = self.cube[4][8]
        self.cube[2][7] = self.cube[4][5]
        self.cube[2][8] = self.cube[4][2]
        
        #red face
        self.cube[4][2] = self.cube[0][0]
        self.cube[4][5] = self.cube[0][1]
        self.cube[4][8] = self.cube[0][2]

        #white face
        self.cube[0][0] = self.cube[3][6]
        self.cube[0][1] = self.cube[3][3]
        self.cube[0][2] = self.cube[3][0]

        #orange face
        self.cube[3][0] = face[0]
        self.cube[3][3] = face[1]
        self.cube[3][6] = face[2]
        
        #change green face orientation
       
        #first row 
        self.cube[1][:3] = [self.cube[1][6],self.cube[1][3],greenFaceRow[0]]
        #second row
        greenFace2Row = self.cube[1][3:6] 
        self.cube[1][3:6] = [self.cube[1][7],self.cube[1][4],greenFaceRow[1]]
        #third row 
        self.cube[1][-3:] = [self.cube[1][8],greenFace2Row[2],greenFaceRow[2]]
        
    #FI works
    def FI_move(self): 
        # yellow face start
        face = self.cube[2][-3:]
        greenFaceRow = self.cube[1][:3]
        #yellow face
        self.cube[2][6] = self.cube[3][0]
        self.cube[2][7] = self.cube[3][3]
        self.cube[2][8] = self.cube[3][6]
        
        #orange face
        self.cube[3][0] = self.cube[0][2]
        self.cube[3][3] = self.cube[0][1]
        self.cube[3][6] = self.cube[0][0]

        #white face
        self.cube[0][0] = self.cube[4][2]
        self.cube[0][1] = self.cube[4][5]
        self.cube[0][2] = self.cube[4][8]

        #red face
        self.cube[4][2] = face[2]
        self.cube[4][5] = face[1]
        self.cube[4][8] = face[0]  
        #change green face orientation
       
        #first row 
        self.cube[1][:3] = [greenFaceRow[2],self.cube[1][5],self.cube[1][8]]
        #second row
        greenFace2Row = self.cube[1][3:6] 
        self.cube[1][3:6] =[greenFaceRow[1],self.cube[1][4],self.cube[1][7]]
        #third row 
        self.cube[1][-3:] = [greenFaceRow[0],greenFace2Row[0],self.cube[1][6]]
        
    #B works perfect
    def B_move(self): 
        # yellow face start
        face = self.cube[2][:3]
        blueFaceRow = self.cube[5][:3]
        #yellow face
        self.cube[2][0] = self.cube[3][2]
        self.cube[2][1] = self.cube[3][5]
        self.cube[2][2] = self.cube[3][8]
        
        #orange face
        self.cube[3][2] = self.cube[0][8]
        self.cube[3][5] = self.cube[0][7]
        self.cube[3][8] = self.cube[0][6]

        #white face
        self.cube[0][6] = self.cube[4][0]
        self.cube[0][7] = self.cube[4][3]
        self.cube[0][8] = self.cube[4][6]

        #red face
        self.cube[4][0] = face[2]
        self.cube[4][3] = face[1]
        self.cube[4][6] = face[0]  
           #change blue face orientation
       
           #first row 
        self.cube[5][:3] = [self.cube[5][6],self.cube[5][3],blueFaceRow[0]]
        #second row
        blueFace2Row = self.cube[5][3:6] 
        self.cube[5][3:6] = [self.cube[5][7],self.cube[5][4],blueFaceRow[1]]
        #third row 
        self.cube[5][-3:] =  [self.cube[5][8],blueFace2Row[2],blueFaceRow[2]]
        
    #BI works perfect
    def BI_move(self): 

        # yellow face start
        face = self.cube[2][:3]
        blueFaceRow = self.cube[5][:3]
        #yellow face
        self.cube[2][0] = self.cube[4][6]
        self.cube[2][1] = self.cube[4][3]
        self.cube[2][2] = self.cube[4][0]
        
        #red face
        self.cube[4][0] = self.cube[0][6]
        self.cube[4][3] = self.cube[0][7]
        self.cube[4][6] = self.cube[0][8]

        #white face
        self.cube[0][6] = self.cube[3][8]
        self.cube[0][7] = self.cube[3][5]
        self.cube[0][8] = self.cube[3][2]

        #orange face
        self.cube[3][2] = face[0]
        self.cube[3][5] = face[1]
        self.cube[3][8] = face[2]  
        
        #first row 
        self.cube[5][:3] = [blueFaceRow[2],self.cube[5][5],self.cube[5][8]]
        #second row
        blueFace2Row = self.cube[5][3:6] 
        self.cube[5][3:6] = [blueFaceRow[1],self.cube[5][4],self.cube[5][7]]
        #third row 
        self.cube[5][-3:] =  [blueFaceRow[0],blueFace2Row[0],self.cube[5][6]]
    #L works
    def L_move(self): 
        # green face start
        face = [self.cube[1][0],self.cube[1][3],self.cube[1][6]]
        redFaceRow = self.cube[4][:3]
        #green face
        self.cube[1][0] = self.cube[2][0]
        self.cube[1][3] = self.cube[2][3]
        self.cube[1][6] = self.cube[2][6]
        
        #yellow face
        self.cube[2][0] = self.cube[5][8]
        self.cube[2][3] = self.cube[5][5]
        self.cube[2][6] = self.cube[5][2]

        #blue face
        self.cube[5][2] = self.cube[0][6]
        self.cube[5][5] = self.cube[0][3]
        self.cube[5][8] = self.cube[0][0]

        #white face
        self.cube[0][0] = face[0]
        self.cube[0][3] = face[1]
        self.cube[0][6] = face[2]  
        #change green face orientation
        #first row 
        self.cube[4][:3] = [self.cube[4][6],self.cube[4][3],redFaceRow[0]]
        #second row
        redFace2Row = self.cube[4][3:6] 
        self.cube[4][3:6] = [self.cube[4][7],self.cube[4][4],redFaceRow[1]]
        #third row 
        self.cube[4][-3:] = [self.cube[4][8],redFace2Row[2],redFaceRow[2]]
    #LI works
    def LI_move(self): 
        # green face start
        face = [self.cube[1][0],self.cube[1][3],self.cube[1][6]]
        redFaceRow = self.cube[4][:3]
        #green face
        self.cube[1][0] = self.cube[0][0]
        self.cube[1][3] = self.cube[0][3]
        self.cube[1][6] = self.cube[0][6]
        
        #white face
        self.cube[0][0] = self.cube[5][8]
        self.cube[0][3] = self.cube[5][5]
        self.cube[0][6] = self.cube[5][2]

        #blue face
        self.cube[5][2] = self.cube[2][6]
        self.cube[5][5] = self.cube[2][3]
        self.cube[5][8] = self.cube[2][0]

        #yellow face
        self.cube[2][0] = face[0]
        self.cube[2][3] = face[1]
        self.cube[2][6] = face[2]  
        #change green face orientation
        #first row 
        self.cube[4][:3] = [redFaceRow[2],self.cube[4][5],self.cube[4][8]]
        #second row
        redFace2Row = self.cube[4][3:6] 
        self.cube[4][3:6] = [redFaceRow[1],self.cube[4][4],self.cube[4][7]]
        #third row 
        self.cube[4][-3:] = [redFaceRow[0],redFace2Row[0],self.cube[4][6]]
 
    #R works
    def R_move(self): 
        # green face start
        face = [self.cube[1][2],self.cube[1][5],self.cube[1][8]]
        orangeFaceRow = self.cube[3][:3]
        #green face
        self.cube[1][2] = self.cube[0][2]
        self.cube[1][5] = self.cube[0][5]
        self.cube[1][8] = self.cube[0][8]
        
        #white face
        self.cube[0][2] = self.cube[5][6]
        self.cube[0][5] = self.cube[5][3]
        self.cube[0][8] = self.cube[5][0]

        #blue face
        self.cube[5][6] = self.cube[2][2]
        self.cube[5][3] = self.cube[2][5]
        self.cube[5][0] = self.cube[2][8]

        #yellow face
        self.cube[2][2] = face[0]
        self.cube[2][5] = face[1]
        self.cube[2][8] = face[2]  

        #change green face orientation
        #first row 
        self.cube[3][:3] = [self.cube[3][6],self.cube[3][3],orangeFaceRow[0]]
        #second row
        orangeFace2Row = self.cube[3][3:6] 
        self.cube[3][3:6] = [self.cube[3][7],self.cube[3][4],orangeFaceRow[1]]
        #third row 
        self.cube[3][-3:] = [self.cube[3][8],orangeFace2Row[2],orangeFaceRow[2]]

    #R works
    def RI_move(self): 
        # green face start
        face = [self.cube[1][2],self.cube[1][5],self.cube[1][8]]
        orangeFaceRow = self.cube[3][:3]
        #green face
        self.cube[1][2] = self.cube[2][2]
        self.cube[1][5] = self.cube[2][5]
        self.cube[1][8] = self.cube[2][8]
        
        #yellow face
        self.cube[2][2] = self.cube[5][6]
        self.cube[2][5] = self.cube[5][3]
        self.cube[2][8] = self.cube[5][0]

        #blue face
        self.cube[5][6] = self.cube[0][2]
        self.cube[5][3] = self.cube[0][5]
        self.cube[5][0] = self.cube[0][8]

        #yellow face
        self.cube[0][2] = face[0]
        self.cube[0][5] = face[1]
        self.cube[0][8] = face[2] 

        #change green face orientation
        #first row 
        self.cube[3][:3] = [orangeFaceRow[2],self.cube[3][5],self.cube[3][8]]
        #second row
        orangeFace2Row = self.cube[3][3:6] 
        self.cube[3][3:6] = [orangeFaceRow[1],self.cube[3][4],self.cube[3][7]]
        #third row 
        self.cube[3][-3:] = [orangeFaceRow[0],orangeFace2Row[0],self.cube[3][6]]




     



     
