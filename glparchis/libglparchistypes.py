"""
    In this file we are going to add all opengl objects and his generation information
    We are going to add Types of NAMES, TEXTURES...
    Invoking for exemple opengl_dado will give all to draw a dice without position information
    
    DOn't use pusxmatrix nor popmatrix, 
"""

class TPlayers:
    Yellow=0
    Blue=1
    Red=2
    Green=3
    Gray=4
    Fuchsia=5
    Orange=6
    Turquoise=7

class TNames:
    """
        0-31 is for pieces
        34- Casillas
    """
    Board=32
    Dice=33

class TTextures:
    """
        Las texturas de texNumber se llamarán 0
        Las textures
    """
    #TexNumber
    Number0=0
    Number1=1
    Number2=2
    Number3=3
    Number4=4
    Number5=5
    Number6=6
    Number7=7
    Number8=8
    Number9=9
    #TextDecor begin by 1000
    PieceInitial=1000
    Wood=1001
    Sure=1002
    Dice=1003

## Types of square. One for fisically different objects
class TSquareTypes:
    Initial4=0
    Final4=1
    ObliqueLeft4=2
    ObliqueRight4=4
    ObliqueLeft6=11
    ObliqueRight6=12
    ObliqueLeft8=13
    ObliqueRight8=14
    Normal=3
    Initial3=5
    Final3=6
    Initial6=7
    Final6=8
    Initial8=9
    Final8=10

    ## Return initial type depending of maximum number of players
    ## @param int Maximum number of players
    def Initial(maxplayers):
        if maxplayers==3:
            return TSquareTypes.Initial3
        elif maxplayers==4:
            return TSquareTypes.Initial4
        elif maxplayers==6:
            return TSquareTypes.Initial6
        elif maxplayers==8:
            return TSquareTypes.Initial8
            
            
    ## Return Final type depending of maximum number of players
    ## @param int Maximum number of players
    def Final(maxplayers):
        if maxplayers==3:
            return TSquareTypes.Final3
        elif maxplayers==4:
            return TSquareTypes.Final4
        elif maxplayers==6:
            return TSquareTypes.Final6
        elif maxplayers==8:
            return TSquareTypes.Final8
    
    
