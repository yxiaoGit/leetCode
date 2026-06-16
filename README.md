1. for nqueens problem:

  The logic here is:
     create a 2D np array, init value set as 0. 
     start from first row, for each column, select it set as 1. 
     now select from next row, all valid columns as a list , append to the above (r, c) selected , 
    for example: (0, x) (1, y)  ;  (0,x, 1, z). etc. 
    from this list, for each, select from the next row all valid columns, form a new list, such as (0,x), (1, y) (2, a);    (0,x, (1, y) , (2, c) ... etc.
    keep doing this until reached last row.    this is the list for a selected first row, column (0,x) .
   iterate thru other columns of the first row, get the full valid results.
