"""
    In this file we are going to add all opengl objects and his generation information
    We are going to add Types of NAMES, TEXTURES...
    Invoking for exemple opengl_dado will give all to draw a dice without position information
    
    DOn't use pusxmatrix nor popmatrix, 
"""

from OpenGL.GL import glBegin, glBindTexture, glColor3d, glDisable, glEnable, glEnd, glInitNames, glPopMatrix, glPopName, glPushName, glPushMatrix, glRotated, glScaled, glTexCoord2f, glTranslated, glTranslatef, glVertex3d, glVertex3fv, GL_TEXTURE_2D, GL_QUADS, GL_POLYGON, GL_LINE_LOOP
from OpenGL.GLU import gluCylinder, gluDisk, gluNewQuadric, gluQuadricDrawStyle, gluQuadricNormals, gluQuadricTexture, GLU_FILL, GLU_SMOOTH

class TNames:
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
    
    

def opengl_dice(qglwidget):
    glInitNames()
    glPushMatrix()
    print("DADO")
    glPushName(TNames.Dice)
    print("DADO")
    glScaled(3,3,3);
    glColor3d(255, 255, 255);

    glEnable(GL_TEXTURE_2D);
    glBindTexture(GL_TEXTURE_2D, qglwidget.texture(TTextures.Dice))
    unter=1.0/3.0;
    doster=2.0/3.0;
    glBegin(GL_QUADS);
    v0=  (0.0, 0.0, 0.0) 
    v1=( 1.0, 0.0, 0.0) 
    v2=( 1.0, 0.0, 1.0) 
    v3=  (0.0, 0.0, 1.0) 

    v4=(0.0, 0.0, 1.0)
    v5=( 1.0, 0.0, 1.0)
    v6=( 1.0, 1.0, 1.0)
    v7=(0.0, 1.0, 1.0)

    v8=(0.0, 0.0, 0.0)
    v9=(0.0, 1.0, 0.0)
    v10=( 1.0, 1.0, 0.0)
    v11=( 1.0, 0.0, 0.0) 

    v12=(0.0, 1.0, 0.0) 
    v13=(0.0, 1.0, 1.0) 
    v14=( 1.0, 1.0, 1.0) 
    v15=( 1.0, 1.0, 0.0) 

    v16=( 1.0, 0.0, 0.0) 
    v17=( 1.0, 1.0, 0.0) 
    v18=( 1.0, 1.0, 1.0) 
    v19=( 1.0, 0.0, 1.0) 

    v20=(0.0, 0.0, 1.0) 
    v21=(0.0, 1.0, 1.0) 
    v22=(0.0, 1.0, 0.0)
    v23=(0.0, 0.0, 0.0)
    glTexCoord2f(0.0, unter);glVertex3fv(v0)
    glTexCoord2f(0.25, unter);glVertex3fv(v1)
    glTexCoord2f(0.25, doster);glVertex3fv(v2)
    glTexCoord2f(0.0, doster);glVertex3fv(v3)  
    glTexCoord2f(0.25, doster);glVertex3fv(v4)
    glTexCoord2f(0.5, doster);glVertex3fv(v5)
    glTexCoord2f(0.5, 1.0);glVertex3fv(v6)
    glTexCoord2f(0.25, 1.0);glVertex3fv(v7)  
    glTexCoord2f(0.25, doster);glVertex3fv(v8)
    glTexCoord2f(0.5, doster);glVertex3fv(v9)
    glTexCoord2f(0.5, unter);glVertex3fv(v10)
    glTexCoord2f(0.25, unter);glVertex3fv(v11)  
    glTexCoord2f(0.25, 0.0);glVertex3fv(v12)
    glTexCoord2f(0.5, 0.0);glVertex3fv(v13)
    glTexCoord2f(0.5, unter);glVertex3fv(v14)
    glTexCoord2f(0.25, unter);glVertex3fv(v15)  
    glTexCoord2f(0.5, unter);glVertex3fv(v16)
    glTexCoord2f(0.75, unter);glVertex3fv(v17)
    glTexCoord2f(0.75, doster);glVertex3fv(v18)
    glTexCoord2f(0.5, doster);glVertex3fv(v19) 
    glTexCoord2f(0.75, unter);glVertex3fv(v20)
    glTexCoord2f(1.0, unter);glVertex3fv(v21)
    glTexCoord2f(1.0, doster);glVertex3fv(v22)
    glTexCoord2f(0.75, doster);glVertex3fv(v23)
    glEnd();

    glPopName();
    glDisable(GL_TEXTURE_2D)
    glPopMatrix();
    
    
def opengl_piece(qglwidget):
    pass
