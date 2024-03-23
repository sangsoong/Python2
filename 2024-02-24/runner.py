import PySimpleGUI as sg
import os

sg.theme('Dark Blue 3')  # please make your windows colorful


# =====
tab1=sg.Tab('title1', [[sg.Multiline(s=(150,100), key='first_tab')]])
Tg = sg.TabGroup([[tab1]])


# =====
layout = [[sg.Text('Filename')],
            [sg.Input(size=(145, 1), key='path_name'), sg.Button('Read', enable_events=True, key='read_event')],
            [sg.Input(size=(145, 1), readonly=True, key='browsed_path', enable_events=True), sg.FileBrowse('Browse', target='browsed_path')],
            [Tg],
            [sg.OK(), sg.Cancel()]]

window = sg.Window('Get filename example', layout).Finalize()
window.Maximize()

def read_file(file):
    if os.path.isfile(file):
        with open(file, 'r', encoding='UTF8') as file_data:
            return file_data.read()


# =====
# 'C:' + os.path.join(' ', 'baejunwoo', '2024-02-24', 'memo.txt').strip()
condition = True
while condition:
    event, values = window.read()
    print(event)
    if event == 'read_event':
        window['first_tab'].update(read_file(values['path_name']))
        #window['first_tab'].
    elif event == 'browsed_path':
        window['first_tab'].update(read_file(values['browsed_path']))

    if event in [sg.WIN_CLOSED]:
        condition = False

    if condition == False:
        print('break')
        break


# =====
window.close()