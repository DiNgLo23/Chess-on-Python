from init import chess_board
from init import chess_board,player_one,player_two,trash
from errors import chess_eror
from chanching_pos import hod


def game(pos_now:list,pos_will:list,figure_name:str):
    pass




hods = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7} 


print("Привет, это консольные шахматы")
print("Вводи ходы по позициям")
print("Полые фигуры - черные, остальные - белые")
print("Пример хода: A2-A3 (пешка сделает ход вперед)")
print("Для того чтобы закончить игру напишите  - конец")
a="""
    A    B    C    D    E    F    G    H
8 ['♖', '♘', '♗', '♔', '♕', '♗', '♘', '♖'] 8
7 ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'] 7
6 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] 6
5 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] 5
4 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] 4
3 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] 3
2 ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'] 2
1 ['♜', '♞', '♝', '♚', '♛', '♝', '♞', '♜'] 1
    A    B    C    D    E    F    G    H
"""
print(a)





for i in range(1,5898):
    c = input().split('-')
    if c!=['конец']:
        if len(c)==2 and len(c[0])==2 and len(c[1])==2 and c[0][0] in hods and c[1][0] in hods:
            one = [int(int(c[0][1])-1),hods[c[0][0]]]
            two = [int(int(c[1][1])-1),hods[c[1][0]]]
        
            a = list(reversed(hod(pos_now=one,pos_will=two,che_map=chess_board,n=i)))
            print("   ","A    B    C    D    E    F    G    H")
            for i in range(len(a)):
                print(7-i+1,a[i],7-i+1)
            print("   ","A    B    C    D    E    F    G    H")
            if 'wking' not in a:
                print("ИГРА ОКОНЧЕНА В ПОЛЬЗУ ЧЕРНЫХ")
                break
            elif 'dking' not in a:
                print("ИГРА ОКОНЧИЛАСЬ В ПОЛЬЗУ БЕЛЫХ")
                break
        else:
            print("ВВЕДИТЕ КОРРЕКТНЫЙ ХОД")
    else:break