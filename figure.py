
from init import chess_board,player_one,player_two,trash
from errors import chess_eror





def vertical(pos_now:list,map:list):
    all_pos,all_open_pos = [],[]
    n=pos_now[1]
    for i in range(len(map)):
        for j in range(len(map[i])):
            if j==n:all_pos.append([i,j])
    ontheright = all_pos[:pos_now[0]]
    ontheleft = all_pos[pos_now[0]+1:]
    for i in range(len(ontheright)-1,-1,-1):
        if map[ontheright[i][0]][ontheright[i][1]]=="":all_open_pos.append(ontheright[i])
        else:
            all_open_pos.append(ontheright[i])
            break
    for i in ontheleft:
        if map[i[0]][i[1]]=="":all_open_pos.append(i)
        else:
            all_open_pos.append(i)
            break
    return (all_open_pos)
def horizen(pos_now:list,map:list): # ВЛЕВО-ВПРАВО
    all_pos,all_open_pos  = [],[]
    n=pos_now[0]
    for i in range(len(map[n])):all_pos.append([n,i])
    ontheright,ontheleft = all_pos[:pos_now[1]],all_pos[pos_now[1]+1:]
    for i in range(len(ontheright)-1,-1,-1):
        if map[ontheright[i][0]][ontheright[i][1]]=="":all_open_pos.append(ontheright[i])
        else:
            all_open_pos.append(ontheright[i])
            break
    for i in ontheleft:
        if map[i[0]][i[1]]=="":all_open_pos.append(i)
        else:
            all_open_pos.append(i)
            break
    return (all_open_pos)
def diagonal(pos_now, map):  # ПО ДИАГОНАЛЯМ
    n = len(map) 
    # 1 - в левый нижний угол
    ll = []
    for i in range(1, min(pos_now[0], pos_now[1]) + 1):
        if map[pos_now[0] - i][pos_now[1] - i] == "":ll.append([pos_now[0] - i, pos_now[1] - i])
        else:
            ll.append([pos_now[0] - i, pos_now[1] - i])
            break
    # 2 - в левый верхний угол
    lh = []
    for i in range(1, min(n - pos_now[0] - 1, pos_now[1]) + 1):
        if map[pos_now[0] + i][pos_now[1] - i] == "":lh.append([pos_now[0] + i, pos_now[1] - i])
        else:
            lh.append([pos_now[0] + i, pos_now[1] - i])
            break
    # 3 - в правый верхний угол
    rh = []
    for i in range(1, min(n - pos_now[0] - 1, n - pos_now[1] - 1) + 1):
        if map[pos_now[0] + i][pos_now[1] + i] == "":rh.append([pos_now[0] + i, pos_now[1] + i])
        else:
            rh.append([pos_now[0] + i, pos_now[1] + i])
            break
    # 4 - в правый нижний угол
    rl = []
    for i in range(1, min(pos_now[0], n - pos_now[1] - 1) + 1):
        if map[pos_now[0] - i][pos_now[1] + i] == "":rl.append([pos_now[0] - i, pos_now[1] + i])
        else:
            rl.append([pos_now[0] - i, pos_now[1] + i])
            break

    return ll+lh+rh+rl






def hod_hourse(pos_now,pos_will):
    if (pos_now[0]-1==pos_will[0] and pos_now[1]-2==pos_will[1]) or (pos_now[0]+1==pos_will[0] and pos_now[1]-2==pos_will[1]) or (pos_now[0]+2==pos_will[0] and pos_now[1]-1==pos_will[1]) or (pos_now[0]+2==pos_will[0] and pos_now[1]+1==pos_will[1])  or (pos_now[0]+1==pos_will[0] and pos_now[1]+2==pos_will[1]) or (pos_now[0]-1==pos_will[0] and pos_now[1]+2==pos_will[1]) or (pos_now[0]-2==pos_will[0] and pos_now[1]-1==pos_will[1]) or (pos_now[0]-2==pos_will[0] and pos_now[1]+1==pos_will[1]):return True
    else: return False
def hod_pawn(pos_now,pos_will,map):
    if map[pos_will[0]][pos_will[1]]=="":
        if (pos_now[0]+1==pos_will[0] and pos_now[1]==pos_will[1]) or (pos_now[0]-1==pos_will[0] and pos_now[1]==pos_will[1]):return True
        else:return False
    else:
        if (pos_now[0]+1==pos_will[0] and pos_now[1]+1==pos_will[1]) or (pos_now[0]+1==pos_will[0] and pos_now[1]-1==pos_will[1]) or (pos_now[0]-1==pos_will[0] and pos_now[1]+1==pos_will[1]) or (pos_now[0]-1==pos_will[0] and pos_now[1]-1==pos_will[1]):return True
        else:return False
def rook(pos_now,pos_will,map_ch):
    all_pos_rook = vertical(pos_now=pos_now,map=map_ch)+horizen(pos_now=pos_now,map=map_ch)
    return True if pos_will in all_pos_rook else False
def hod_elf(pos_now,pos_will,map_ch):
    all_pos_elf = diagonal(pos_now=pos_now,map=map_ch)
    return True if pos_will in all_pos_elf else False
def hod_queen(pos_now,pos_will,map_ch):
    all_pos_queen = vertical(pos_now=pos_now,map=map_ch)+horizen(pos_now=pos_now,map=map_ch)+diagonal(pos_now=pos_now,map=map_ch)
    return True if pos_will in all_pos_queen else False



def king(pos_now,pos_will,map_ch):
    all_pos_king = [[pos_now[0]-1,pos_now[1]-1],[pos_now[0],pos_now[1]-1],[pos_now[0]+1,pos_now[1]-1],[pos_now[0]+1,pos_now[1]],[pos_now[0]+1,pos_now[1]+1],[pos_now[0],pos_now[1]+1],[pos_now[0]-1,pos_now[1]+1],[pos_now[0]-1,pos_now[1]]]
    return True if pos_will in all_pos_king else False





