from init import chess_board,player_one,player_two,trash
from errors import chess_eror
from figure import hod_hourse,hod_pawn,rook,hod_elf,hod_queen,king



def change_position(pos_now,pos_will,name,map):
    now = map[pos_now[0]][pos_now[1]]   
    will = map[pos_will[0]][pos_will[1]]
    if now!='':
        
        if will=="":
            map[pos_now[0]][pos_now[1]]=""
            map[pos_will[0]][pos_will[1]]=name            
        else:
            if will[0]!=now[0]:
                players = {'d':player_two,'w':player_one}
                trash.append(name)
                map[pos_now[0]][pos_now[1]]=""
                map[pos_will[0]][pos_will[1]]=name
                
                return ['',name]

            else:
                chess_eror("motion on me")
    else:
        chess_eror(error="change figure is empty")
    


def hod(pos_now,pos_will,che_map,n):
    if -1<pos_now[0]<8 and -1<pos_now[0]<8 and -1<pos_will[0]<8 and -1<pos_will[0]<8:
        name = che_map[pos_now[0]][pos_now[1]]
        if len(name)!=0 and (n%2==0 and name[0]=='w') or (n%2!=0 and name[0]=='d'):
            if 'hourse' in name:
                if hod_hourse(pos_now=pos_now,pos_will=pos_will):change_position(pos_now=pos_now,pos_will=pos_will,name=name,map=che_map)
                else:print("НЕ КОРРЕКТНЫЙ ХОД")
            elif 'pawn' in name:
                if hod_pawn(pos_now=pos_now,pos_will=pos_will,map=che_map):change_position(pos_now=pos_now,pos_will=pos_will,name=name,map=che_map)
                else:print("НЕ КОРРЕКТНЫЙ ХОД")
            elif "rook" in name:
                if rook(pos_now=pos_now,pos_will=pos_will,map_ch=che_map):change_position(pos_now=pos_now,pos_will=pos_will,name=name,map=che_map)
                else:print("НЕ КОРРЕКТНЫЙ ХОД")
            elif "elf" in name:
                if hod_elf(pos_now=pos_now,pos_will=pos_will,map_ch=che_map): change_position(pos_now=pos_now,pos_will=pos_will,name=name,map=che_map)
                else:print("НЕ КОРРЕКТНЫЙ ХОД")
            elif 'queen' in name:
                if hod_queen(pos_now=pos_now,pos_will=pos_will,map_ch=che_map):change_position(pos_now=pos_now,pos_will=pos_will,name=name,map=che_map)
            elif 'king' in name:
                if king(pos_now=pos_now,pos_will=pos_will,map_ch=che_map):change_position(pos_now=pos_now,pos_will=pos_will,name=name,map=che_map)
        else:
            print('НЕ ВАШ ХОД')
        def ret_chess_map(map:list):
            all_figure_white = {"pawn":"♙","king":"♔","queen":"♕","rook":"♖","elf":"♗","hourse":"♘"}
            all_figure_dark = {"pawn":"♟","king":"♚","queen":"♛","rook":"♜","elf":"♝","hourse":"♞"}
            ret_map = [[' ' for j in range(8)]for i in range(8)]
            for i in range(len(map)):
                for j in range(len(map[i])):
                    if map[i][j]=='':
                        ret_map[i][j]==""
                    if "d" in map[i][j]:
                        for k in all_figure_dark:
                            if k in map[i][j]:
                                ret_map[i][j]=all_figure_dark[k]
                    else:
                        for k in all_figure_white:
                            if k in map[i][j]:
                                ret_map[i][j]=all_figure_white[k]
            return ret_map
        return ret_chess_map(che_map)
