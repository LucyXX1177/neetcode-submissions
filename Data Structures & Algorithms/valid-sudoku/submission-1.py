class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        print(self.check_row_and_check_nine (board) , self.check_column(board) )
        return self.check_row_and_check_nine (board) and self.check_column(board) 
    
    def check_row_and_check_nine(self,board):
        for i in range(len(board)):
            current_row=[]
            for j in range(len(board[i])):
                if board[i][j]!=".":
                    current_row.append(board[i][j])
                print(i,j,"every")
                if (i+1)%3==0 and (j+1)%3==0:
                    current_nine=[board[i-2][j-2],board[i-2][j-1],board[i-2][j],
                                  board[i-1][j-2],board[i-1][j-1],board[i-1][j],
                                  board[i][j-2],board[i][j-1],board[i][j]]
                    print("current_nine",current_nine)
                    count_none=0
                    for z in range(len(current_nine)):
                        if current_nine[z]==".":
                            count_none+=1

                    if count_none!=0:
                        if len(current_nine)!=len(set(current_nine))+count_none-1:
                            
                            return False 
                    else:
                        if len(current_nine)!=len(set(current_nine)):
                            return False


                    

            if len(current_row)!=len(set(current_row)):
                print('row error')
                return False 
            
        return True
    
    def check_column(self,board):
        
        for j in range(len(board)):
            current_col=[]
            for i in range(len(board[j])):
                if board[i][j]!=".":
                    current_col.append(board[i][j])
            
            if len(current_col)!=len(set(current_col)):
                return False 
        return True 



            
                
        