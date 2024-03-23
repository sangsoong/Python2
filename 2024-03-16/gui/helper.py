import PySimpleGUI as sg
from helper2 import AddressBook

"""
def ui():
    # All the stuff inside your window.
    layout = [
        [sg.Text("What's your name?")],
        [sg.InputText()],
        [sg.Button("Ok"), sg.Button("Cancel")],
    ]

    # Create the Window
    window = sg.Window("Hello Example", layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        # if user closes window or clicks cancel
        if event == sg.WIN_CLOSED or event == "Cancel":
            break

        print("Hello", values[0], "!")

    window.close()
"""

addressbook = AddressBook()


def make_window(theme):
    sg.theme(theme)

    ad_layout = [
        [sg.Text("Name", size=(13, 1)), sg.Input(k="-ADName-", size=(35, 1))],
        [sg.Text("Phone Number", size=(13, 1)), sg.Input(k="-ADNum-", size=(35, 1))],
        [sg.Text("Address", size=(13, 1)), sg.Input(k="-ADAddr-", size=(35, 1))],
        [sg.Button("Submit", k="-ADSubmit-")],
    ]

    rm_layout = [
        [
            sg.Text("Find by"),
            sg.Radio("Name", "RM", default=True, k="-RMName-"),
            sg.Radio("Phone Number", "RM", k="-RMNum-"),
            sg.Radio("Address", "RM", k="-RMAddr-"),
        ],
        [sg.Input(k="-RMStr-", size=(60, 1))],
        [sg.Button("Submit", k="-RMSubmit-")],
    ]

    mf_layout = [
        [sg.Text("Name", size=(13, 1)), sg.Input(k="-ADName-", size=(15, 1))],
        [sg.Text("Phone Number", size=(13, 1)), sg.Input(k="-ADNum-", size=(15, 1))],
        [sg.Text("Address", size=(13, 1)), sg.Input(k="-ADAddr-", size=(15, 1))],
        [sg.Button("Submit", k="-ADSubmit-")],
    ]

    main_layout = [
        [
            sg.Text(
                "This program will support your works associated with address.",
                font=" 5",
            )
        ],
        [
            sg.Text(
                "Choose what you want to do.",
                font=" 5",
            )
        ],
        [
            sg.TabGroup(
                [
                    [
                        sg.Tab("Add Address", ad_layout),
                        sg.Tab("Remove Address", rm_layout),
                        sg.Tab("Modify Address", mf_layout),
                    ]
                ],
                border_width=5,
            ),
            sg.Button("Exit", k="-EP-"),
        ],
        [
            sg.Multiline(
                "Information of Address will be displayed here.",
                expand_x=True,
                expand_y=True,
                disabled=True,
                k="-ML-",
            )
        ],
    ]

    window = sg.Window(
        "Address Book Program",
        main_layout,
        grab_anywhere=True,
        resizable=True,
        margins=(0, 0),
        finalize=True,
    )
    window.maximize()

    return window


def main():
    window = make_window(sg.theme())

    while True:
        event, values = window.read(timeout=100)
        if (event in (None, "Exit")) or (event in (None, "-EP-")):
            break
        if event in (None, "-ADSubmit-"):
            name = values["-ADName-"]
            num = values["-ADNum-"]
            addr = values["-ADAddr-"]
            addressbook.addr_add(name, num, addr)
        if event in (None, "-RMSubmit-"):
            modes = ["-RMName-", "-RMNum-", "-RMAddr-"]
            mode = [fb for fb in modes if values[fb] == True]
            str = values["-RMStr-"]
            addressbook.addr_remove(mode[0], str)
        if event in (None, "-MFSubmit-"):
            addressbook.addr_modify()
        addressbook.file_reader()
        MLStr = addressbook.addr_findall()
        window["-ML-"].update(MLStr)

    window.close()
    exit(0)
