import sqlite3
from tkinter import messagebox


class RegisterSystem:
    def __init__(self):  # Iniciar
        self.conection = sqlite3.connect('student.db')
        self.cursor = self.conection.cursor()
        self.create_table()

    def create_table(self):  # Criação da tabela

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            telephone TEXT NOT NULL,
            gender TEXT NOT NULL,
            birthday TEXT NOT NULL,
            address TEXT NOT NULL,
            course TEXT NOT NULL,
            picture TEXT NOT NULL)''')

    def register_student(self, student):
        self.cursor.execute(
            'INSERT INTO students(name, email, telephone, gender, birthday, address, course, picture) VALUES (?,?,?,?,?,?,?,?)', (student))
        self.conection.commit()

        # Mostrando menssaem de sucesso
        messagebox.showinfo('Sucesso', 'Registro com sucesso!')

    def view_all_students(self):
        self.cursor.execute("SELECT * FROM students")
        data = self.cursor.fetchall()

        return data
        """for i in data:
            print(f'''ID:{i[0]} |
                email:{i[1]} |
                Tel:{i[2]} |
                Gênero:{i[3]} |
                Data de nascimento:{i[4]} |
                Endereço:{i[5]} |
                Curso:{i[6]} |
                Foto:{i[7]}
                ''')"""

    def search_student(self, id):
        self.cursor.execute("SELECT * FROM students WHERE id=?", (id))
        data = self.cursor.fetchone()

        return data
        """print(f'''ID:{data[0]} |
                email:{data[1]} |
                Tel:{data[2]} |
                Gênero:{data[3]} |
                Data de nascimento:{data[4]} |
                Endereço:{data[5]} |
                Curso:{data[6]} |
                Foto:{data[7]}
                ''')"""

    def update_students(self, new_values):
        query = "UPDATE students SET name=?, email=?, telephone=?, gender=?, birthday=?, address=?, picture=? WHERE id = ? "
        self.conection.execute(query, new_values)
        self.conection.commit()

    def delete_students(self, id):
        self.conection.execute("DELETE FROM students WHERE id=?", (id,))
        self.conection.commit()

        # Mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso', f'Estudante com ID:{id} foi deletado!')



# Criando uma instancia do sistema de registro
sistema_de_registro = RegisterSystem()

# Registrando Estudante
# students(name, email, telephone, gender, birthday, address, course, picture)
#estudante = ('Caio', 'tswkdmekfd@gmail.com', '219832132455', 'M', '18/03/2001', 'Rua dos Pikas', 'Hitoria', '1003.png')
#sistema_de_registro.register_student(estudante)

print(sistema_de_registro.search_student(3))
