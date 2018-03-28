# Programmer: Chung Chin Leon
# Date: 2017/12/16

# Program
import sys
sys.stdin = open("billboard.in","r")
sys.stdout = open("billboard.out","w")
board1 = input().split(" ")
board2 = input().split(" ")
truck = input().split(" ")
b1x1 = int(board1[0])
b1y1 = int(board1[1])
b1x2 = int(board1[2])
b1y2 = int(board1[3])
b2x1 = int(board2[0])
b2y1 = int(board2[1])
b2x2 = int(board2[2])
b2y2 = int(board2[3])
tx1 = int(truck[0])
ty1 = int(truck[1])
tx2 = int(truck[2])
ty2 = int(truck[3])

b_area1 = (b1x2-b1x1) * (b1y2-b1y1)
b_area2 = (b2x2-b2x1) * (b2y2-b2y1)

def calculation(bx1,bx2,tx1,tx2,by1,by2,ty1,ty2):
    if bx1 == tx1:
        x1 = tx1
    elif bx1 < tx1:
        x1 = tx1
    else:
        x1 = bx1
    if bx2 == tx2:
        x2 = tx2
    elif bx2 > tx2:
        x2 = tx2
    else:
        x2 = bx2
    if by1 == ty1:
        y1 = ty1
    elif by1 < ty1:
        y1 = ty1
    else:
        y1 = by1
    if by2 == ty2:
        y2 = ty2
    elif by2 > ty2:
        y2 = ty2
    else:
        y2 = by2
    area = (x2 - x1) * (y2 - y1)
    return area

t_area1 = calculation(b1x1,b1x2,tx1,tx2,b1y1,b1y2,ty1,ty2)
area1 = (b_area1-t_area1)
t_area2 = calculation(b2x1,b2x2,tx1,tx2,b2y1,b2y2,ty1,ty2)
area2 = (b_area2-t_area2)
print(area1 + area2)
