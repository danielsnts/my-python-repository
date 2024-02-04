# importando dependencias do Tkinter
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# importando pillow
from PIL import ImageTk, Image

# tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date

# importando main
from main import *

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
app_logo = Label(frame_logo, image=app_lg, text=" Sistema de Registro de Alunos", width=850, compound=LEFT, anchor=NW,
                 font=('Verdana 15'), bg=color6, fg=color1)
app_logo.place(x=5, y=0)

# abrindo a imagem

imagem = Image.open('logo.png')
imagem = imagem.resize((130, 130))
imagem = ImageTk.PhotoImage(imagem)
l_imagem = Label(frame_details, image=imagem, bg=color1, fg=color4)
l_imagem.place(x=390, y=10)


# Criando dunções para CRUD
# Função adcionar
def add():
    global imagem, imagem_string, l_imagem
    # Obtendo os valores
    name = e_name.get()
    email = e_email.get()
    tel = e_tel.get()
    gender = c_gender.get()
    date = birthday.get()
    address = e_address.get()
    course = c_course.get()
    img = imagem_string
    list = [name, email, tel, gender, date, address, course, img]

    # Verificando se a lista contem valores vazios
    for i in list:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

    # Registra os valores
    sistema_de_registro.register_student(list)

    # Limpando os campos de entrada
    e_name.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    c_gender.delete(0, END)
    birthday.delete(0, END)
    e_address.delete(0, END)
    c_course.delete(0, END)

    # Mostrando os valores na tabela
    show_students()


# Função procurar
def seach():
    global imagem, imagem_string, l_imagem

    # Obtendo o ID
    id_student = int(e_search.get())

    # Procurando aluno
    data = sistema_de_registro.search_student(id_student)

    # Limpando campos de entrada
    e_name.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    c_gender.delete(0, END)
    birthday.delete(0, END)
    e_address.delete(0, END)
    c_course.delete(0, END)

    # Inserir valors nos campos de entrada
    e_name.insert(END, data[1])
    e_email.insert(END, data[2])
    e_tel.insert(END, data[3])
    c_gender.insert(END, data[4])
    birthday.insert(END, data[5])
    e_address.insert(END, data[6])
    c_course.insert(END, data[7])

    imagem = data[8]
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_details, image=imagem, bg=color1, fg=color4)
    l_imagem.place(x=390, y=10)


# Função Atualizar
def update():
    global imagem, imagem_string, l_imagem

    # Obtendo o id
    id_student = int(e_search.get())

    # Obtendo os valores
    name = e_name.get()
    email = e_email.get()
    tel = e_tel.get()
    gender = c_gender.get()
    date = birthday.get()
    address = e_address.get()
    course = c_course.get()
    img = imagem_string
    list = [name, email, tel, gender, date, address, course, img, id_student]

    # Verificando se a lista contem valores vazios
    for i in list:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

    # Registra os valores
    sistema_de_registro.update_students(list)

    # Limpando os campos de entrada
    e_name.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    c_gender.delete(0, END)
    birthday.delete(0, END)
    e_address.delete(0, END)
    c_course.delete(0, END)

    # Abrindo Imagem
    imagem = Image.open('logo.png')
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_details, image=imagem, bg=color1, fg=color4)
    l_imagem.place(x=390, y=10)
    # Mostrando os valores na tabela
    show_students()


# Função Deletar
def delete():
    global imagem, imagem_string, l_imagem

    # Obtendo o id
    id_student = int(e_search.get())

    # Deletando o aluno
    sistema_de_registro.delete_students(id_student)

    # Limpando os campos de entrada
    e_name.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    c_gender.delete(0, END)
    birthday.delete(0, END)
    e_address.delete(0, END)
    c_course.delete(0, END)

    e_address.delete(0, END)

    # Abrindo Imagem
    imagem = Image.open('logo.png')
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_details, image=imagem, bg=color1, fg=color4)
    l_imagem.place(x=390, y=10)
    # Mostrando os valores na tabela
    show_students()


# Criando os campos de entrada ----------------------------------

l_name = Label(frame_details, text="Name *", anchor=NW, font=('Ivy 10'), bg=color1, fg=color4)
l_name.place(x=4, y=10)
e_name = Entry(frame_details, width=30, justify='left', relief='solid')
e_name.place(x=7, y=40)

l_email = Label(frame_details, text="Email *", anchor=NW, font=('Ivy 10'), bg=color1, fg=color4)
l_email.place(x=4, y=70)
e_email = Entry(frame_details, width=30, justify='left', relief='solid')
e_email.place(x=7, y=100)

l_tel = Label(frame_details, text="Telephone *", anchor=NW, font=('Ivy 10'), bg=color1, fg=color4)
l_tel.place(x=4, y=130)
e_tel = Entry(frame_details, width=15, justify='left', relief='solid')
e_tel.place(x=7, y=160)

l_gender = Label(frame_details, text="Gender *", anchor=NW, font=('Ivy 10'), bg=color1, fg=color4)
l_gender.place(x=127, y=130)
c_gender = ttk.Combobox(frame_details, width=7, font=('Ivy 8 bold'), justify='center')
c_gender['values'] = ('M', 'F', 'T')
c_gender.place(x=130, y=160)

l_birthday = Label(frame_details, text="Data de nascimento *", anchor=NW, font=('Ivy 10'), bg=color1, fg=color4)
l_birthday.place(x=220, y=10)
birthday = DateEntry(frame_details, width=18, justify='center', background='darkblue', foreground='white',
                     borderwidth=2, year=2023)
birthday.place(x=224, y=40)

l_address = Label(frame_details, text="Address *", anchor=NW, font=('Ivy 10'), bg=color1, fg=color4)
l_address.place(x=220, y=70)
e_address = Entry(frame_details, width=20, justify='left', relief='solid')
e_address.place(x=224, y=100)

courses = ['Engenharia',
           'Medicina',
           'Socias',
           "Acupuntura",
           "Agrimensura",
           "Agrocomputação",
           "Agroecologia",
           "Agroindústria",
           "Agronegócio",
           "Agropecuária",
           "Alimentos",
           "Análise de Dados",
           "Análise e Desenvolvimento de Sistemas",
           "Apicultura e Meliponicultura",
           "Aquicultura",
           "Arqueologia",
           "Arquitetura de Dados",
           "Artes do Espetáculo",
           "Artes e Mídias Digitais",
           "Assessoria Executiva Digital",
           "Atividades de Inteligência e Gestão de Sigilos"
           ]

l_course = Label(frame_details, text="Courses *", anchor=NW, font=('Ivy 10'), bg=color1, fg=color4)
l_course.place(x=220, y=130)
c_course = ttk.Combobox(frame_details, width=20, font=('Ivy 8 bold'), justify='center')
c_course['values'] = (courses)
c_course.place(x=224, y=160)


# funcao para escolher imagem

def choose_image():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_details, image=imagem, bg=color1, fg=color4)
    l_imagem.place(x=390, y=10)

    loading_botton['text'] = 'Trocar de foto'


loading_botton = Button(frame_details, command=choose_image, text='LOAD IMAGE'.upper(), width=20, compound=CENTER,
                        anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=color1, fg=color0)
loading_botton.place(x=390, y=160)


# Tabela Alunos
def show_students():
    # creating a treeview with dual scrollbars
    list_header = ['id', 'name', 'email', 'Telephone', 'sexo', 'Data', 'Endereço', 'course']

    # view all students
    df_list = sistema_de_registro.view_all_students()

    tree_student = ttk.Treeview(frame_table, selectmode="extended", columns=list_header, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree_student.yview)
    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree_student.xview)

    tree_student.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_student.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_table.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "center", "center", "center", "center", "center", "center"]
    h = [40, 150, 150, 70, 70, 70, 120, 100, 100]
    n = 0

    for col in list_header:
        tree_student.heading(col, text=col.title(), anchor=NW)
        # adjust the column's width to the header string
        tree_student.column(col, width=h[n], anchor=hd[n])

        n += 1

    for item in df_list:
        tree_student.insert('', 'end', values=item)


# Procurar aluno -----------

frame_search = Frame(frame_bottons, width=40, height=50, bg=color1, relief=RAISED)
frame_search.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)

l_name = Label(frame_search, text="search aluno [ Entra ID ]", height=1, anchor=NW, font=('Ivy 10'), bg=color1,
               fg=color4)
l_name.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)
e_search = Entry(frame_search, width=5, justify='center', relief="solid", font=('Ivy 10'))
e_search.grid(row=1, column=0, pady=10, padx=0, sticky=NSEW)

botton_search = Button(frame_search, command=seach, anchor=CENTER, text="search", width=9, overrelief=RIDGE,
                       font=('ivy 7 bold'), bg=color1, fg=color0)
botton_search.grid(row=1, column=1, pady=10, padx=0, sticky=NSEW)

# Botoes ---------------fse-----

app_img_add = Image.open('add.png')
app_img_add = app_img_add.resize((25, 25))
app_img_add = ImageTk.PhotoImage(app_img_add)
app_add = Button(frame_bottons, command=add, image=app_img_add, text=" Add", width=100, compound=LEFT, relief=GROOVE,
                 overrelief=RIDGE, font=('Ivy 11'), bg=color1, fg=color0)
app_add.grid(row=1, column=0, pady=5, padx=10, sticky=NSEW)

app_img_update = Image.open('update.png')
app_img_update = app_img_update.resize((25, 25))
app_img_update = ImageTk.PhotoImage(app_img_update)
app_update = Button(frame_bottons, command=update, image=app_img_update, text=" Update", width=100, compound=LEFT,
                    relief=GROOVE, overrelief=RIDGE, font=('Ivy 11'), bg=color1, fg=color0)
app_update.grid(row=2, column=0, pady=5, padx=10, sticky=NSEW)

app_img_delete = Image.open('delete.png')
app_img_delete = app_img_delete.resize((25, 25))
app_img_delete = ImageTk.PhotoImage(app_img_delete)
app_delete = Button(frame_bottons, command=delete, image=app_img_delete, text=" Delete", width=100, compound=LEFT,
                    relief=GROOVE, overrelief=RIDGE, font=('Ivy 11'), bg=color1, fg=color0)
app_delete.grid(row=3, column=0, pady=5, padx=10, sticky=NSEW)

# Linha separatoria ---------------------------------------------------

l_line = Label(frame_bottons, relief=GROOVE, text='h', width=1, height=123, anchor=NW, font=('Ivy 1'), bg=color1,
               fg=color0)
l_line.place(x=240, y=15)

# chamar a tabela
show_students()

window.mainloop()
