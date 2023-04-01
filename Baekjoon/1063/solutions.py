import sys
input = sys.stdin.readline

k_pos, r_pos, n = input().split()

char2int = lambda x : ord(x) - 64 # 1-8
int2char = lambda x : chr(x + 64) # 1-8

k_pos = [ char2int(k_pos[0]), int(k_pos[1]) ]
r_pos = [ char2int(r_pos[0]), int(r_pos[1]) ]
n = int(n)

data = [input().rstrip() for _ in range(n)]

move = {'R' : (1,0), 'L' : (-1,0), 
        'B' : (0,-1), 'T' : (0,1),
        'RT' : (1,1), 'LT' : (-1,1),
        'RB' : (1,-1), 'LB' : (-1,-1),}

for direction in data:
    tmp_k = [ k_pos[0] + move[direction][0], k_pos[1] + move[direction][1] ]
    tmp_r = [ r_pos[0] + move[direction][0], r_pos[1] + move[direction][1] ]
    if 1 <= tmp_k[0] <= 8 and 1 <= tmp_k[1] <= 8:
        if tmp_k == r_pos:
            if 1 <= tmp_r[0] <= 8 and 1 <= tmp_r[1] <= 8:
                r_pos = tmp_r
            else:
                continue
        k_pos = tmp_k

print(int2char(k_pos[0]) + str(k_pos[1]))
print(int2char(r_pos[0]) + str(r_pos[1]))
