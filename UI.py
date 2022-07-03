import PySimpleGUI as sg

sg.theme('SystemDefault')
# Устанавливаем цвет внутри окна
layout = [  [sg.Text("MFCC",size=(15, 1), font=("Times new roman",11),justification='right'),sg.Multiline(size=(50,5))],
        [sg.Text("Вывод текста",size=(15, 1), font=("Times new roman",11), justification='right'),sg.Input()],
        [sg.Button("Добавить WAV-файл", font=("Times New Roman",12)),sg.Button("Запись/Стоп", font=("Times New Roman",12))]]

# Создаем окно
window = sg.Window('Название окна', layout)
# Цикл для обработки "событий" и получения "значений" входных данных
while True:
    event, values = window.read()

window.close()
