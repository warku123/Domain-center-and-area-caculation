import cv2
import collections
import numpy as np
np.set_printoptions(suppress=True)

scale = 326.2

bin = cv2.imread('pic7_bin.png', cv2.IMREAD_GRAYSCALE)
# print(bin)
maxx, maxy = bin.shape

visited = set()
# return count, sumx, sumy
def dfs(x, y):
    if (x,y) in visited or bin[x][y]==0:
        return 0, 0, 0
    # print(x,y)
    q = collections.deque()
    q.append((x,y))
    visited.add((x, y))
    sumx, sumy = 0, 0
    all_cnt = 0
    
    while len(q)>0:
        tx, ty = q.popleft()
        sumx += tx
        sumy += ty
        all_cnt += 1
        for dir in [[0,-1],[-1,0],[0,1],[1,0]]:
            nextx, nexty = tx+dir[0], ty+dir[1]
            if nextx>=maxx or nexty>=maxy or nextx<0 or nexty<0 or (nextx, nexty) in visited or bin[nextx][nexty]==0:
                continue
            visited.add((nextx, nexty))
            q.append((nextx, nexty))
            
    return all_cnt, sumx, sumy


ans = []
for i in range(maxx):
    for j in range(maxy):
        cnt,x,y = dfs(i, j)
        if cnt!=0:
            ans.append([cnt, x/cnt, y/cnt])

real_area = ans[1:]

ori = cv2.imread("pic7.png")
for idx, point in enumerate(real_area):
    cnt, x, y = point
    if cnt >= 300:
        cv2.circle(ori, (int(y), int(x)), 5, (0, 0, 255), -1)
        cv2.putText(ori, "point:{}".format(idx),(int(y)+10, int(x)-15),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        cv2.putText(ori, "{:.2f},{:.2f}".format(y,x),(int(y)+10, int(x)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        cv2.putText(ori, "area:{}".format(int(cnt*scale)),(int(y)+10, int(x)+15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
cv2.imwrite("pic7_final.png", ori)

for idx, data in enumerate(real_area):
    print(str(idx)+str(data))    

