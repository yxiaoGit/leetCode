from typing import List
class Position:
    def __init__(self, r1:int, c1:int):
      self.r1 = r1
      self.c1 = c1

    def __str__(self):
        print(f"({self.r1}, {self.c1})")

class Solution:

    def isValid(self, n:int, r1:int, c1:int, allready: List[Position]) -> bool:
        import numpy as np

        # Define a 2D array with 3 rows and 4 columns, initialized to 0
        board = np.zeros((n, n), dtype=int)
        for p in allready:
            board[p.r1][p.c1] = 1

        return self.isValidPosition(n, r1, c1, board)

    def isValidPosition(self, n:int, r1: int, c1:int, board: List[List[int]]) -> bool:

                sameRow=board[r1]
                for c in range(0, n):
                    if board[r1][c] == 1 and c != c1:
                        return False

                for r in range(0,n):
                    if board[r][c1] == 1 and r != r1:
                        return False


                # check diagonal
                r = r1
                c = c1
                while r <= n-1 and c <= n-1 and r >= 0 and c >=0:
                      r = r+1
                      c = c +1
                      if r <= n-1 and c <= n-1 and r >= 0 and c >=0 and board[r][c] == 1 and r != r1 and c != c1:
                         return False

                r = r1
                c = c1
                while r <= n-1 and c <= n-1 and r >= 0 and c >=0:
                      r = r-1
                      c = c -1
                      if r <= n-1 and c <= n-1 and r >= 0 and c >=0 and board[r][c] == 1 and r != r1 and c != c1:
                         return False

                r = r1
                c = c1
                while r <= n-1 and c <= n-1 and r >= 0 and c >=0:
                      r = r+1
                      c = c -1
                      if r <= n-1 and c <= n-1 and r >= 0 and c >=0 and board[r][c] == 1 and r != r1 and c != c1:
                         return False
                r = r1
                c = c1
                while r <= n-1 and c <= n-1 and r >= 0 and c >=0:
                      r = r-1
                      c = c +1
                      if r <= n-1 and c <= n-1 and r >= 0 and c >=0 and board[r][c] == 1 and r != r1 and c != c1:
                         return False


                return True
    # at each additional row for that column, add candidates to the list.
    # when the setting is n, it is a valid solution

    def selectFromNextRow(self, n: int, row:int, already: List[Position]) -> List[List[Position]]:
        a=[]
        for c in range(0, n ):
            if self.isValid(n, row, c, already):
                nextAlready = already.copy()
                nextAlready.append(Position(row, c))
                a.append(nextAlready)
        return a




    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]

        #if n == 2:
        #    return []


        #the list of positions , number of them indicates next row
        resultList = []

        positionList=[[Position(0,0)]]

        for c in range(0, n):
           positionList=[[Position(0,c)]]
           while len(positionList) > 0:
                alreadyList = positionList.pop()
                nextRow=len(alreadyList)
                print(f"next row is {nextRow}")
                for p2 in alreadyList:
                   if p2 is None:
                     print("p in alreadylist is None")
                   else:
                     print(f"alreadyList {p2.r1} {p2.c1}")
                newList = self.selectFromNextRow(n, nextRow, alreadyList)
                if nextRow == n-1 and newList:
                    resultList.append(newList)
                    for plist in newList:
                      for p in plist:
                         print(f" added at row {nextRow} {p.r1} {p.c1}")
                elif len(newList) > 0:
                    print(f"got new positions to list {len(newList)}")
                    for i in newList:
                       positionList.append(i)


        result=[]
        for aboard in resultList:
            boardstr = [["." for _ in range(n)] for _ in range(n)]
            for positionList in aboard :
              for p in positionList:
                 print(f"{p.r1} {p.c1}")
                 boardstr[p.r1][p.c1]="Q"
            boardStrRows = []
            for r in boardstr:
                boardStrRows.append(''.join(r))
            result.append(boardStrRows)

        return result            
