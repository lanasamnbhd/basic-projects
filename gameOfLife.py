from typing import List


class game_of_life:
    def gameOfLife(self, board:List[List[int]]) -> None:

        """
        do not return anything
        """
        neighbours=[(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]
        rows=len(board)
        cols=len(board[0])

        #a copy of the original board
        copy_board=[[board[row][col] for col in range(cols)] for row in range(rows)]


        #iterate through board cell by cell
        for row in range(rows):
            for col in range(cols):

                #for each cell count the number of live neighnours
                live_neighbours=0
                for neighbour in neighbours:
                    r=(row+neighbour[0])
                    c=(col+neighbour[1])

                    #check the validity of the neighboring cell and if it was originally a live  cell
                    #the evaluation is done against the copy, since that is never updated
                    if (r<rows and r>=0) and (c<cols and c>=0) and (copy_board[r][c]==1):
                        live_neighbours+=1

                if copy_board[row][col]==1 and (live_neighbours<2 or live_neighbours>3):
                    board[row][col]=0

                if copy_board[row][col]==0 and live_neighbours==3:
                    board[row][col]=1

