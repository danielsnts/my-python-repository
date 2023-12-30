# importando dependencias do Tkinter
from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# importando pillow
from PIL import ImageTk, Image

# tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date


# cores
color0 = "#2e2d2b"  # Preta
color1 = "#feffff"  # Branca
color2 = "#e5e5e5"
color3 = "#00a095"
color4 = "#403d3d"
color6 = "#003452"

# criando window
window = Tk()
window.title("")
window.geometry('810x535')
window.configure(background=color1)
window.resizable(width=FALSE, height=FALSE)

style = Style(window)
style.theme_use("clam")

# Criando Frames
frame_logo = Frame(window, width=850, height=52, bg=color6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

frame_bottons = Frame(window, width=100, height=200, bg=color1, relief=RAISED)
frame_bottons.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_details = Frame(window, width=800, height=100, bg=color1, relief=SOLID)
frame_details.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW)

frame_table = Frame(window, width=800, height=100, bg=color1, relief=SOLID)
frame_table.grid(row=3, column=0, pady=0, padx=10, sticky=NSEW, columnspan=5)


# Trabalhando no frame logo ------------------------------------
global imagem, imagem_string, l_imagem

app_lg = Image.open('logo.png')
app_lg = app_lg.resize((50, 50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text=" Sistema de Registro de Alunos", width=850, compound=LEFT, anchor=NW, font=('Verdana 15'), bg=color6, fg=color1)
app_logo.place(x=5, y=0)


# abrindo a imagem

imagem = Image.open('logo.png')
imagem = imagem.resize((130, 130))
imagem = ImageTk.PhotoImage(imagem)
l_imagem = Label(frame_details, image=imagem, bg=color1, fg=color4)
l_imagem.place(x=390, y=10)

# Criando os campos de entrada ----------------------------------

l_nome = Label(frame_details, text="Nome *", anchor=NW, font=('Ivy 10'), bg=color1, fg=color4)
l_nome.place(x=4, y=10)
e_nome = Entry(frame_details, width=30, justify='left', relief='solid')
e_nome.place(x=7, y=40)

l_email = Label(frame_details, text="Email *", anchor=NW, font=('Ivy 10'), bg=color1, fg=color4)
l_email.place(x=4, y=70)
e_email = Entry(frame_details, width=30, justify='left', relief='solid')
e_email.place(x=7, y=100)

l_tel = Label(frame_details, text="Telefone *", anchor=NW, font=('Ivy 10'), bg=color1, fg=color4)
l_tel.place(x=4, y=130)
e_tel = Entry(frame_details, width=15, justify='left', relief='solid')
e_tel.place(x=7, y=160)

l_gender = Label(frame_details, text="Sexo *", anchor=NW, font=('Ivy 10'), bg=color1, fg=color4)
l_gender.place(x=127, y=130)
c_gender = ttk.Combobox(frame_details, width=7, font=('Ivy 8 bold'), justify='center')
c_gender['values'] = ('M','F', 'T')
c_gender.place(x=130, y=160)

l_birthday = Label(frame_details, text="Data de nascimento *", anchor=NW, font=('Ivy 10'), bg=color1, fg=color4)
l_birthday.place(x=220, y=10)
birthday = DateEntry(frame_details, width=18, justify='center', background='darkblue', foreground='white', borderwidth=2, year=2023)
birthday.place(x=224, y=40)

l_address = Label(frame_details, text="Endereço *", anchor=NW, font=('Ivy 10'), bg=color1, fg=color4)
l_address.place(x=220, y=70)
e_address = Entry(frame_details, width=20, justify='left', relief='solid')
e_address.place(x=224, y=100)

courses = ['Engenharia', 'Medicina', 'Socias']

l_course = Label(frame_details, text="courses *", anchor=NW, font=('Ivy 10'), bg=color1, fg=color4)
l_course.place(x=220, y=130)
c_course = ttk.Combobox(frame_details, width=20, font=('Ivy 8 bold'), justify='center')
c_course['values'] = (courses)
c_course.place(x=224, y=160)


# funcao para escolher imagem

def escolher_imagem():
	global imagem, imagem_string, l_imagem

	imagem = fd.askopenfilename()
	imagem_string=imagem

	imagem = Image.open(imagem)
	imagem = imagem.resize((130,130))
	imagem = ImageTk.PhotoImage(imagem)
	l_imagem = Label(frame_details, image=imagem, bg=color1, fg=color4)
	l_imagem.place(x=390, y=10)

	botao_carregar['text'] = 'Trocar de foto'


botao_carregar = Button(frame_details, command=escolher_imagem, text='Carregar Foto'.upper(), width=20, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=color1, fg=color0)
botao_carregar.place(x=390, y=160)


# Tabela Alunos
def mostrar_alunos():

	# creating a treeview with dual scrollbars
	list_header = ['id','Nome','email',  'Telefone','sexo','Data', 'Endereço','course']

	# view all students
	df_list = []

	tree_aluno = ttk.Treeview(frame_table, selectmode="extended",columns=list_header, show="headings")

	# vertical scrollbar
	vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree_aluno.yview)
	# horizontal scrollbar
	hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree_aluno.xview)

	tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
	tree_aluno.grid(column=0, row=1, sticky='nsew')
	vsb.grid(column=1, row=1, sticky='ns')
	hsb.grid(column=0, row=2, sticky='ew')
	frame_table.grid_rowconfigure(0, weight=12)

	hd=["nw","nw","nw","center","center","center","center","center","center"]
	h=[40,150,150,70,70,70,120,100,100]
	n=0

	for col in list_header:
		tree_aluno.heading(col, text=col.title(), anchor=NW)
		# adjust the column's width to the header string
		tree_aluno.column(col, width=h[n],anchor=hd[n])

		n+=1

	for item in df_list:
		tree_aluno.insert('', 'end', values=item)



# Procurar aluno -----------

frame_procurar = Frame(frame_bottons, width=40, height=50, bg=color1, relief=RAISED)
frame_procurar.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)

l_nome = Label(frame_procurar, text="Procurar aluno [ Entra ID ]", height=1,anchor=NW, font=('Ivy 10'), bg=color1, fg=color4)
l_nome.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)
e_procurar = Entry(frame_procurar, width=5, justify='center',relief="solid",font=('Ivy 10'))
e_procurar.grid(row=1, column=0, pady=10, padx=0, sticky=NSEW)

botao_procurar = Button(frame_procurar, anchor=CENTER, text="Procurar", width=9, overrelief=RIDGE,  font=('ivy 7 bold'),bg=color1, fg=color0 )
botao_procurar.grid(row=1, column=1, pady=10, padx=0, sticky=NSEW)

# Botoes --------------------

app_img_adicionar = Image.open('add.png')
app_img_adicionar = app_img_adicionar.resize((25,25))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button(frame_bottons,  image=app_img_adicionar, text=" Adicionar", width=100, compound=LEFT, relief=GROOVE, overrelief=RIDGE, font=('Ivy 11'), bg=color1, fg=color0)
app_adicionar.grid(row=1, column=0, pady=5, padx=10, sticky=NSEW)

app_img_atualizar = Image.open('update.png')
app_img_atualizar = app_img_atualizar.resize((25,25))
app_img_atualizar = ImageTk.PhotoImage(app_img_atualizar)
app_atualizar = Button(frame_bottons, image=app_img_atualizar, text=" Atualizar", width=100, compound=LEFT, relief=GROOVE, overrelief=RIDGE, font=('Ivy 11'), bg=color1, fg=color0)
app_atualizar.grid(row=2, column=0, pady=5, padx=10, sticky=NSEW)

app_img_deletar = Image.open('delete.png')
app_img_deletar = app_img_deletar.resize((25,25))
app_img_deletar = ImageTk.PhotoImage(app_img_deletar)
app_deletar = Button(frame_bottons, image=app_img_deletar, text=" Deletar", width=100, compound=LEFT, relief=GROOVE, overrelief=RIDGE, font=('Ivy 11'), bg=color1, fg=color0)
app_deletar.grid(row=3, column=0, pady=5, padx=10, sticky=NSEW)


# linha separatoria ---------------------------------------------------

l_linha = Label(frame_bottons, relief=GROOVE, text='h', width=1, height=123, anchor=NW, font=('Ivy 1'), bg=color1,
				fg=color0)
l_linha.place(x=240, y=15)


# chamar a tabela
mostrar_alunos()

window.mainloop()
