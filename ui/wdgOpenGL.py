## -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtOpenGL import *
from PyQt4.QtGui import *
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from objloader import  *

class wdgOpenGL(QGLWidget):
    def __init__(self, parent=None):
        QGLWidget.__init__(self, parent)

        self.object = 0
        self.xRot = 0
        self.yRot = 0
        self.zRot = 0

        self.lastPos = QPoint()

        self.trolltechGreen = QColor.fromCmykF(0.40, 0.0, 1.0, 0.0)
        self.trolltechPurple = QColor.fromCmykF(0.39, 0.39, 0.0, 0.0)
        
        


    def initializeGL(self):
        self.qglClearColor(self.trolltechPurple.dark())

#        self.obj = OBJ("parchis4.obj", swapyz=True)
        self.ficha = OBJ("dado.obj", swapyz=True)        
        glShadeModel(GL_FLAT)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0))
        glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)             
        
        
#        glEnable(GL_DEPTH_TEST);
#        glFrontFace(GL_CCW);
##      
##        GLfloat light_ambient[] =  {1, 1, 1, 1};
##        GLfloat light_diffuse[] =  {0, 0, 1, 0};
##        GLfloat light_specular[] =  {0, 0, 0, 0};
##        GLfloat light_position[] =  {5.0, 5.0, 5.0, 0.0};
##      
##      
#        glEnable(GL_LIGHTING);
##        glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient);
##        glLightfv(GL_LIGHT0, GL_POSITION, light_position);
#        glEnable(GL_LIGHT0);
#      
#        glEnable(GL_COLOR_MATERIAL);
#        glColorMaterial(GL_FRONT,GL_AMBIENT_AND_DIFFUSE);
#        glShadeModel (GL_SMOOTH);
##        self.object = self.makeObject()
##        glShadeModel(GL_FLAT)
##        glEnable(GL_DEPTH_TEST)
#        glEnable(GL_CULL_FACE)
        

    def paintGL(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#        gluLookAt(0,0,5,0, 0, 0,0,0,-1);
        glTranslated(0.0, 0.0, -5.0)
#        glRotated(45, 0.0, 0.0, 1.0)
#        glRotated(self.yRot / 16.0, 0.0, 1.0, 0.0)
#        glRotated(self.zRot / 16.0, 0.0, 0.0, 1.0)
        print "OJÑLKJJ"
#        glCallList(self.obj.gl_list)

#        glPushMatrix()
##        glTranslated(0.0, 0.0, 4.0)
#        glCallList(self.ficha.gl_list)
#        glPopMatrix()
        glPushMatrix()
        glColor3d(0,1,1)
        glBegin(GL_QUADS)
        glVertex3d(0, 0, 0)
        glVertex3d(1, 1, -12);
        glVertex3d(1, 1, 10)
        glVertex3d(2, 2, 2)
        glEnd()
        glPopMatrix()

#        self.swapBuffers()

    def resizeGL(self, width, height):
        print "Resized"
        side = min(width, height)
        glViewport((width - side) / 2, (height - side) / 2, side, side)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        
#        gluPerspective(45.0, width/float(height), 1, 100.0)
        glOrtho(-0.5, +0.5, +0.5, -0.5, 4.0, 15.0)
        glMatrixMode(GL_MODELVIEW)
#        glLoadIdentity()

#
#// Our 3DS model class
#class CModel3DS
#{
#	public:
#		CModel3DS(std::string filename);
#		virtual void Draw() const;
#		virtual void CreateVBO();
#		virtual ~CModel3DS();
#	protected:
#		void GetFaces();
#		unsigned int m_TotalFaces;
#		Lib3dsFile * m_model;
#		GLuint m_VertexVBO, m_NormalVBO;
#};
#
#// Load 3DS model
#CModel3DS::CModel3DS(std::string filename)
#{
#	m_TotalFaces = 0;
#	
#	m_model = lib3ds_file_load(filename.c_str());
#	// If loading the model failed, we throw an exception
#	if(!m_model)
#	{
#		throw strcat("Unable to load ", filename.c_str());
#	}
#}
#
#// Destructor
#CModel3DS::~CModel3DS()
#{
#	glDeleteBuffers(1, &m_VertexVBO);
#	glDeleteBuffers(1, &m_NormalVBO);
#	
#	if(m_model != NULL)
#	{
#		lib3ds_file_free(m_model);
#	}
#}
#
#// Copy vertices and normals to the memory of the GPU
#void CModel3DS::CreateVBO()
#{
#	assert(m_model != NULL);
#	
#	// Calculate the number of faces we have in total
#	GetFaces();
#	
#	// Allocate memory for our vertices and normals
#	Lib3dsVector * vertices = new Lib3dsVector[m_TotalFaces * 3];
#	Lib3dsVector * normals = new Lib3dsVector[m_TotalFaces * 3];
#	
#	Lib3dsMesh * mesh;
#	unsigned int FinishedFaces = 0;
#	// Loop through all the meshes
#	for(mesh = m_model->meshes;mesh != NULL;mesh = mesh->next)
#	{
#		lib3ds_mesh_calculate_normals(mesh, &normals[FinishedFaces*3]);
#		// Loop through every face
#		for(unsigned int cur_face = 0; cur_face < mesh->faces;cur_face++)
#		{
#			Lib3dsFace * face = &mesh->faceL[cur_face];
#			for(unsigned int i = 0;i < 3;i++)
#			{
#				memcpy(&vertices[FinishedFaces*3 + i], mesh->pointL[face->points[i]].pos, sizeof(Lib3dsVector));
#			}
#			FinishedFaces++;
#		}
#	}
#	
#	// Generate a Vertex Buffer Object and store it with our vertices
#	glGenBuffers(1, &m_VertexVBO);
#	glBindBuffer(GL_ARRAY_BUFFER, m_VertexVBO);
#	glBufferData(GL_ARRAY_BUFFER, sizeof(Lib3dsVector) * 3 * m_TotalFaces, vertices, GL_STATIC_DRAW);
#	
#	// Generate another Vertex Buffer Object and store the normals in it
#	glGenBuffers(1, &m_NormalVBO);
#	glBindBuffer(GL_ARRAY_BUFFER, m_NormalVBO);
#	glBufferData(GL_ARRAY_BUFFER, sizeof(Lib3dsVector) * 3 * m_TotalFaces, normals, GL_STATIC_DRAW);
#	
#	// Clean up our allocated memory
#	delete vertices;
#	delete normals;
#	
#	// We no longer need lib3ds
#	lib3ds_file_free(m_model);
#	m_model = NULL;
#}
#
#// Count the total number of faces this model has
#void CModel3DS::GetFaces()
#{
#	assert(m_model != NULL);
#	
#	m_TotalFaces = 0;
#	Lib3dsMesh * mesh;
#	// Loop through every mesh
#	for(mesh = m_model->meshes;mesh != NULL;mesh = mesh->next)
#	{
#		// Add the number of faces this mesh has to the total faces
#		m_TotalFaces += mesh->faces;
#	}
#}
#
#// Render the model using Vertex Buffer Objects
#void CModel3DS::Draw() const
#{
#	assert(m_TotalFaces != 0);
#	
#	// Enable vertex and normal arrays
#	glEnableClientState(GL_VERTEX_ARRAY);
#	glEnableClientState(GL_NORMAL_ARRAY);
#	
#	// Bind the vbo with the normals
#	glBindBuffer(GL_ARRAY_BUFFER, m_NormalVBO);
#	// The pointer for the normals is NULL which means that OpenGL will use the currently bound vbo
#	glNormalPointer(GL_FLOAT, 0, NULL);
#	
#	glBindBuffer(GL_ARRAY_BUFFER, m_VertexVBO);
#	glVertexPointer(3, GL_FLOAT, 0, NULL);
#	
#	// Render the triangles
#	glDrawArrays(GL_TRIANGLES, 0, m_TotalFaces * 3);
#	
#	glDisableClientState(GL_VERTEX_ARRAY);
#	glDisableClientState(GL_NORMAL_ARRAY);
#}
#
#// A render widget for QT
#class CRender : public QGLWidget
#{
#	public:
#		CRender(QWidget *parent = 0);
#	protected:
#		virtual void initializeGL();
#		virtual void resizeGL(int width, int height);
#		virtual void paintGL();
#	private:
#		CModel3DS * monkey;
#};
#
#// Constructor, initialize our model-object
#CRender::CRender(QWidget *parent) : QGLWidget(parent)
#{
#	try
#	{
#		monkey = new CModel3DS("monkey.3ds");
#	}
#	catch(std::string error_str)
#	{
#		std::cerr << "Error: " << error_str << std::endl;
#		exit(1);
#	}
#}
#
#// Initialize some OpenGL settings
#void CRender::initializeGL()
#{
#	glClearColor(0.0, 0.0, 0.0, 0.0);
#	glShadeModel(GL_SMOOTH);
#	
#	// Enable lighting and set the position of the light
#	glEnable(GL_LIGHT0);
#	glEnable(GL_LIGHTING);
#	GLfloat pos[] = { 0.0, 4.0, 4.0 };
#	glLightfv(GL_LIGHT0, GL_POSITION, pos);
#	
#	// Generate Vertex Buffer Objects
#	monkey->CreateVBO();
#}
#
#// Reset viewport and projection matrix after the window was resized
#void CRender::resizeGL(int width, int height)
#{
#	// Reset the viewport
#	glViewport(0, 0, width, height);
#	// Reset the projection and modelview matrix
#	glMatrixMode(GL_PROJECTION);
#	glLoadIdentity();
#	// 10 x 10 x 10 viewing volume
#	glOrtho(-5.0, 5.0, -5.0, 5.0, -5.0, 5.0);
#	glMatrixMode(GL_MODELVIEW);
#	glLoadIdentity();
#}
#
#// Do all the OpenGL rendering
#void CRender::paintGL()
#{
#	glClear(GL_COLOR_BUFFER_BIT);
#	
#	// Draw our model
#	monkey->Draw();
#	
#	// We don't need to swap the buffers, because QT does that automaticly for us
#}
#
#int main(int argc, char **argv)
#{
#	QApplication app(argc, argv);
#	CRender * window = new CRender();
#	window->show();
#	return app.exec();
#}
#
