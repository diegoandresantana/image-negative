
import tkFileDialog
from Tkinter import *

from PIL import Image, ImageTk


import numpy as np

import cv2
"""
    Negative Image Samples (Process image, show image negative, trunc, tozero_inv and other with countors)
    05/09/2018
    Autor: Diego Andre Sant'Ana
    Disciplina: Visao Computacional
    
"""

class TELA:
	def __init__(self):
		self.clicked = False
		self.fingerling = {}

		#janela
		self.window = Tk()
		self.window.title("Sem imagem")
		self.window.attributes('-zoomed', True)

		#lado esquerdo
		self.frameMenuLateral = Frame(self.window)
		self.frameMenuLateral.pack(side=LEFT, anchor=N)

		self.frameControls = LabelFrame(self.frameMenuLateral, text="Controles", padx = 5, pady = 5)
		self.frameControls.pack(anchor=N, pady=5, padx=5, fill=X)

		self.frameControlsOrganize = Frame(self.frameControls)
		self.frameControlsOrganize.pack(fill=X, expand=False)

		self.selecionaImagem = Button(self.frameControlsOrganize, text="Selecione a Imagem", padx=5, pady=5, command = self.selecionaImagem)
		self.selecionaImagem.pack(padx=5, pady=5, expand=True, fill=X)

		self.buttonOpen = Button(self.frameControlsOrganize, text="Executar Procedimentos", padx=5, pady=5, command = self.criaContorno)
		self.buttonOpen.pack(padx=5, pady=5, expand=True, fill=X)

		#lado direito

		self.frameImages = LabelFrame(self.window,text="Imagens", padx = 5, pady = 5)
		self.frameImages.pack(side=RIGHT, pady=5, padx=5, expand=True, fill=BOTH)


		self.frameControlsOrganize2 = Frame(self.frameImages )
		self.frameControlsOrganize2.pack(fill=X, expand=False)
		self.frameControlsOrganize2.columnconfigure(0, weight=3)
		self.frameControlsOrganize2.columnconfigure(1, weight=3)
		self.frameControlsOrganize2.columnconfigure(2, weight=3)
		self.frameControlsOrganize2.grid( row=0,padx=20,sticky="nsew")
		self.frameControlsOrganize2.grid( row=1,padx=20,sticky="nsew")
		self.frameControlsOrganize2.grid(row=2,padx=20,sticky="nsew")



		self.frameImg1 = LabelFrame(self.frameControlsOrganize2, text="ORIGINAL", padx=5, pady=5)
		self.frameImg1['width'] = 340
		self.frameImg1['height'] =240
		self.frameImg1.grid(column=0,row=0)

		#Imagem cinza
 		self.frameImg2 = LabelFrame(self.frameControlsOrganize2, text="GRAY", padx=5, pady=5)
		self.frameImg2['width'] = 340
		self.frameImg2['height'] = 230
		self.frameImg2.grid(column=1,row=0 )

		#inversao de cores
		self.frameImg3 = LabelFrame(self.frameControlsOrganize2, text="BINARY", padx=5, pady=5)
		self.frameImg3['width'] = 340
		self.frameImg3['height'] = 230
		self.frameImg3.grid(column=2,row=0 )

		#Contorno
		self.frameImg4 = LabelFrame(self.frameControlsOrganize2, text="CONTORNO", padx=5, pady=5)
		self.frameImg4['width'] = 340
		self.frameImg4['height'] = 230
		self.frameImg4.grid(column=0,row=1 )

		#'BINARY',
		self.frameImg5 = LabelFrame(self.frameControlsOrganize2, text="ADAPTIVE_THRESH_GAUSSIAN_C", padx=5, pady=5)
		self.frameImg5['width'] = 340
		self.frameImg5['height'] = 230
		self.frameImg5.grid(column=1,row=1 )

		#'BINARY_INV',
		self.frameImg6 = LabelFrame(self.frameControlsOrganize2, text="BINARY_INV", padx=5, pady=5)
		self.frameImg6['width'] = 340
		self.frameImg6['height'] = 230
		self.frameImg6.grid(column=2,row=1)

		#'TRUNC',
		self.frameImg7 = LabelFrame(self.frameControlsOrganize2, text="TRUNC", padx=5, pady=5)
		self.frameImg7['width'] = 340
		self.frameImg7['height'] = 230
		self.frameImg7.grid(column=0,row=2)


		#'TOZERO','
		self.frameImg8 = LabelFrame(self.frameControlsOrganize2, text="TOZERO", padx=5, pady=5)
		self.frameImg8['width'] = 340
		self.frameImg8['height'] = 230
		self.frameImg8.grid(column=1,row=2)

		#TOZERO_INV'
		self.frameImg9 = LabelFrame(self.frameControlsOrganize2, text="TOZERO_INV", padx=5, pady=5)
		self.frameImg9['width'] = 340
		self.frameImg9['height'] = 230
		self.frameImg9.grid(column=1,row=2)



		self.window.mainloop()

	def click(self, event):
		self.mouseXClick = event.x
		self.mouseYClick = event.y
		self.clicked = True

	def release(self, event):
		# type: (object) -> object
		self.clicked = False



	def carregaImagem(self,img,frame,op):

		labelImg = Label( frame, width=int(340-5), height=int(230-5))
		labelImg.pack( expand=True,  fill=BOTH, padx=5, pady=5)
		imgResize= Image.fromarray(img).resize((340 -12, 230-12),Image.ADAPTIVE )
		imgtk = ImageTk.PhotoImage(image=imgResize)
		labelImg.imgtk = imgtk
		labelImg.configure(image=imgtk)
		if(op==1):
			self.labelImg1=labelImg
		elif(op==2):
			self.labelImg2=labelImg
		elif(op==3):
			self.labelImg3=labelImg
		elif(op==4):
			self.labelImg4=labelImg
		elif(op==5):
			self.labelImg5=labelImg
		elif(op==6):
			self.labelImg6=labelImg
		elif(op==7):
			self.labelImg7=labelImg
		elif(op==8):
			self.labelImg8=labelImg
		elif(op==9):
			self.labelImg9=labelImg

	def criaContorno(self):
		#converte para cinza
		self.img2= cv2.cvtColor(self.imagemOriginal, cv2.COLOR_BGR2GRAY)

		#binario
		ret, thresh = cv2.threshold(np.copy(self.img2), 127, 255, 0)
		# encontra os contornos
		self.img3, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		#desenha os contornos
		self.img4=cv2.drawContours(self.imagemOriginal, contours, -1, (0,0,255), 1)

		# seguindo o tutorial de THRESH do Open CV -> 'ADAPTIVE_THRESH_GAUSSIAN_C','BINARY_INV','TRUNC','TOZERO','TOZERO_INV'
		ret,self.img5 = cv2.threshold(self.img2,127,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
		ret,self.img6 = cv2.threshold(self.img2,127,255,cv2.THRESH_BINARY_INV)
		ret,self.img7 = cv2.threshold(self.img2,127,255,cv2.THRESH_TRUNC)
		ret,self.img8 = cv2.threshold(self.img2,127,255,cv2.THRESH_TOZERO)
		ret,self.img9 = cv2.threshold(self.img2,127,255,cv2.THRESH_TOZERO_INV)

		for w in (self.frameImg2,self.frameImg3,self.frameImg4, self.frameImg5, self.frameImg6,self.frameImg7, self.frameImg8, self.frameImg9):
			  for f in w.winfo_children():
   					 f.destroy()

		self.carregaImagem(self.img2,self.frameImg2,2)
		self.carregaImagem(self.img3,self.frameImg3,3)
		self.carregaImagem(self.img4,self.frameImg4,4)
		self.carregaImagem(self.img5,self.frameImg5,5)
		self.carregaImagem(self.img6,self.frameImg6,6)
		self.carregaImagem(self.img7,self.frameImg7,7)
		self.carregaImagem(self.img8,self.frameImg8,8)
		self.carregaImagem(self.img9,self.frameImg9,9)




	def selecionaImagem(self):
		options = {

            'title': 'Selecione a imagem dos formatos JPG ou PNG.',
            'filetypes': (("Arquivo JPG", '*.jpg'), ('Arquivo PNG', '*.png'))

        }
		filename = tkFileDialog.askopenfilename(**options)
		if(filename != ''):
			self.file = filename
			self.window.title(self.file)
			self.imagemOriginal = cv2.imread(self.file  )

			for w in (self.frameImg1,self.frameImg2,self.frameImg3,self.frameImg4, self.frameImg5, self.frameImg6,self.frameImg7, self.frameImg8, self.frameImg9):
				 for f in w.winfo_children():
   					 f.destroy()

			self.carregaImagem(self.imagemOriginal,self.frameImg1,1)


tela = TELA()

