class ChessBoard():

    def __init__(self) -> None:
        self.board = self.initialize_board()    
    
    
    def initialize_board(player_one,player_two):
        #########
        #Create Chess map
        #########
        chess_map = [['' for j in range(8)]for i in range(8)] #DON'T TOUCH
        #########
        #Sets positions all figure 
        #########
        for i in player_one.pos_all_figur: chess_map[player_one.pos_all_figur[i][1]][player_one.pos_all_figur[i][0]] = i
        for i in player_two.pos_all_figur: chess_map[player_two.pos_all_figur[i][1]][player_two.pos_all_figur[i][0]] = i
       # chess_map = list(reversed(chess_map))
        
        return chess_map


class Player():

    def __init__(self,color:str) -> None:
        self.color = color

    # name:str | int = "None" # Имя пользователя

    
    def set_color_for_player(self):
        if self.color =="dark":
            self.pos_all_figur = {"dpawn1":[0,1],"dpawn2":[1,1],"dpawn3":[2,1],"dpawn4":[3,1],"dpawn5":[4,1],"dpawn6":[5,1],"dpawn7":[6,1],"dpawn8":[7,1],
                        'dlrook':[0,0],"drrook":[7,0],
                        "dlhourse":[1,0],"drhourse":[6,0],
                        "dlelf":[2,0],"drelf":[5,0],
                        'dqueen':[4,0],
                        'dking':[3,0]}# Pawn - пешка, Rook - ладья,  Hourse - лошадь,   Elf - слон,   Queen - ферзь,   King - король
        
        elif self.color =="white":
            self.pos_all_figur = {"wpawn1":[0,6],"wpawn2":[1,6],"wpawn3":[2,6],"wpawn4":[3,6],"wpawn5":[4,6],"wpawn6":[5,6],"wpawn7":[6,6],"wpawn8":[7,6],
                        'wlrook':[0,7],"wrrook":[7,7],
                        "wlhourse":[1,7],"wrhourse":[6,7],
                        "wlelf":[2,7],"wrelf":[5,7],
                        'wqueen':[4,7],
                        'wking':[3,7]}# Pawn - пешка, Rook - ладья,  Hourse - лошадь,   Elf - слон,   Queen - ферзь,   King - король
  
        else:
            return("Ops, Error for color")
        

#########
# Init players
# Инициализация игроков
#########
player_one = Player(color="white")
player_two = Player(color="dark")


#########
# Set user color
# Установка цвета
#########
player_one.set_color_for_player()
player_two.set_color_for_player()



############
# Create CHESS_BOARD
# Создание шахматной доски
############
chess_board = ChessBoard.initialize_board(player_one=player_one,player_two=player_two)


trash = []# ALL KILLS FIGURE


