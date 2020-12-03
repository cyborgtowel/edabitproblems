# Concert Seats

def can_see_stage(n):
    for row in range(len(n)-1):
        for col in range(len(n[row])):
            front = n[row][col]
            back = n[row+1][col]
            if front >= back:
                return False
    return True 

print(can_see_stage([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]))#True

print(can_see_stage([
  [0, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]))#True

print(can_see_stage([
  [2, 0, 0], 
  [1, 1, 1], 
  [2, 2, 2]
]))#False

print(can_see_stage([
  [1, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]))#False