import PySimpleGUI as sg

def crypt(string: str) -> str:
    input_string = string.strip()
    alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result: str = ""
    for i in range(0, len(input_string)):
        c: str = input_string[i]
        if c.upper() not in alphabet:
            result += c
            continue
        is_uppercase: bool = c.isupper()
        c_index = alphabet.find(c.upper())
        c_new_index = c_index + 13
        if c_new_index >= 26:
            c_new_index = c_new_index - 26
        if is_uppercase:
            c_new = alphabet[c_new_index].upper()
        else:
            c_new = alphabet[c_new_index].lower()
        result += c_new
    return result

sg.theme('DarkGreen4')

layout = [[sg.Text('Enter text to be encrypted...')],
          [sg.Multiline(key='-IN-', enable_events=True)],
          [sg.Multiline(key='-OUT-', disabled=True)]],

window = sg.Window('ROT13 Encryption', layout)

while True:  # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    else:
        window['-OUT-'].update(crypt(values['-IN-']))

window.close()

