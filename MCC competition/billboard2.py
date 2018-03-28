import sys
sys.stdin = open("billboard.in","r")
sys.stdout = open("billboard.out","w")
board1 = input().split(" ")
board2 = input().split(" ")
b1x1 = int(board1[0])
b1y1 = int(board1[1])
b1x2 = int(board1[2])
b1y2 = int(board1[3])
b2x1 = int(board2[0])
b2y1 = int(board2[1])
b2x2 = int(board2[2])
b2y2 = int(board2[3])
x_overlap = max(0, min(b1x2, b2x2) - max(b1x1, b2x1))
y_overlap = max(0, min(b1y2, b2y2) - max(b1y1, b2y1))
intersect = x_overlap * y_overlap
area = (b1x2-b1x1) * (b1y2-b1y1)
if intersect < int(area/2):
    intersect = 0
total = int(area - intersect)
print (total)
