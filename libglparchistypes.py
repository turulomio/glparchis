"""
    In this file we are going to add all opengl objects and his generation information
    We are going to add Types of NAMES, TEXTURES...
    Invoking for exemple opengl_dado will give all to draw a dice without position information
    
    DOn't use pusxmatrix nor popmatrix, 
"""


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
