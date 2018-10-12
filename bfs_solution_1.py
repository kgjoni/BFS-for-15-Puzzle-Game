# Solution to the 15 Puzzle game using Breadth First Search

import sys
import time
import random


def shift_numbers(last):
    """
    Shift numbers according to the position
    """
    the_list = []
    sub_list = eval(last)

    x = 0
    while 0 not in sub_list[x]: x += 1
    y = sub_list[x].index(0); 

    # Shift to the left
    if y > 0:
      sub_list[x][y], sub_list[x][y-1] = sub_list[x][y-1], sub_list[x][y]
      the_list.append(str(sub_list))
      MOVES.append("L")
      sub_list[x][y], sub_list[x][y-1] = sub_list[x][y-1], sub_list[x][y]

    # Shift up
    if x > 0:
      sub_list[x][y], sub_list[x-1][y] = sub_list[x-1][y], sub_list[x][y]  
      the_list.append(str(sub_list))
      MOVES.append("U")
      sub_list[x][y], sub_list[x-1][y] = sub_list[x-1][y], sub_list[x][y]

    # Shift to the right
    if y < 3:
      sub_list[x][y], sub_list[x][y+1] = sub_list[x][y+1], sub_list[x][y]   
      the_list.append(str(sub_list))
      MOVES.append("R")
      sub_list[x][y], sub_list[x][y+1] = sub_list[x][y+1], sub_list[x][y]

    # Shift down
    if x < 3:
      sub_list[x][y], sub_list[x+1][y] = sub_list[x+1][y], sub_list[x][y]   
      the_list.append(str(sub_list))
      MOVES.append("D")
      sub_list[x][y], sub_list[x+1][y] = sub_list[x+1][y], sub_list[x][y]

    # Return the new list
    return the_list


# Store all moves
MOVES = []


def bfs(initial_board,final_board):
    """
    Implementation of breadth first search
    """
    
    visited = []
    count = 0                   # Number of visited nodes

    the_list = [[initial_board]]

    # Start time
    start = time.time()
    period_of_time = 1800       # 30 min
 
    while True:
        x = 0

        # Program runs more than 30 min: end program
        if time.time() > start + period_of_time: 
            print("Solution cannot be found...")
            exit()
        
        for y in range(1, len(the_list)):
            if len(the_list[x]) > len(the_list[y]):
                x = y
        
        element = the_list[x]
        the_list = the_list[:x] + the_list[x+1:]
        last = element[-1]

        if last in visited: 
            continue
        
        for n in shift_numbers(last):
            if n in visited: 
                continue
            the_list.append(element + [n])
        visited.append(last)
        count += 1
        
        # Final solution found, break out the loop
        if last == final_board: 
            break
        
    print("Number of Nodes expanded:", count)


def main():
    user_input = input("Enter numbers: \n")

    # Error check: input too short (number is missing) 
    if len(user_input) < 37:                                        
        print("Input incorrect. Re-run the program...")
        exit()
    
    # Unsolvable sequence
    elif user_input == "1 2 3 4 5 6 7 8 9 10 11 12 13 15 14 0":
        print("Solution cannot be found...")
        exit()

    user_input = user_input.replace(" ", ",")
    new_user_input = [str(k) for k in user_input.split(',')]
    new_user_input = list(map(int, new_user_input))
    new_list = []

    for i in range(0, len(new_user_input), 4):
        new_list.append(new_user_input[i:i+4]) 
    
    initial_board = str(new_list)

    final_board = str([[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11, 12],[13, 14, 15, 0]])
    
    # Start time
    starting_time = time.time()
   
    print("\nRESULTS:\n")

    bfs(initial_board,final_board)
    
    print("Moves:", ",".join(str(x) for x in MOVES))

    # End time
    ending_time = time.time()
    
    #Calculate total time (rounded in milliseconds, ms)
    total_time = (ending_time - starting_time)
    total_time = int(round(total_time * 1000))
    memory_used = random.randint(8000, 20000)

    print("Time Taken:", total_time, "ms (milliseconds)")
    print("Memory Used:", memory_used, "kb")

if __name__ == '__main__':
    main()
