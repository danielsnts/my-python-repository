# Aqui se encontram as funções uteis para converter EXCEL para SQLite3
import openpyxl
workbook = openpyxl.load_workbook('planilha.xlsx')

sheet = workbook.active
celula = sheet['A1']

print(celula)