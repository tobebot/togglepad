import subprocess
import shutil


def toggle_touchpad():
     # Intentar utilizar synclient
    if check_tool_availability('synclient'):
        print("Using 'synclient'")
        '''
        subprocess.run(['synclient', 'TouchpadOff=$(synclient -l | grep "TouchpadOff" | awk \'{print !$3}\')'])
        print("Se utilizó synclient para toogle del touchpad.")
        '''
        toggle_touchpad_synclient()
        # Intentar utilizar xinput
    elif check_tool_availability('xinput'):
        print("Using 'xinput'")
        '''        
        touchpad_id = get_touchpad_id_with_xinput()
        if touchpad_id is not None:
            subprocess.run(['xinput', 'set-prop', str(touchpad_id), 'Device Enabled', '0'])
            print("Se utilizó xinput para toogle del touchpad.")
        '''
        toggle_touchpad_xinput()

    # Intentar utilizar libinput
    elif check_tool_availability('libinput'):
        print("Using 'libinput'")
        subprocess.run(['libinput', 'debug-gui', 'toggle-touchpad'])
        print("Se utilizó libinput para toogle del touchpad.")
    else:
        print("No se encontraron herramientas compatibles para toogle del touchpad.")

def check_tool_availability(tool):
    return shutil.which(tool) is not None

def toggle_touchpad_synclient():
    # Es captura la sortida del comandament 'synclient -l'
    # Aquesta sortida es en forma de bytes
    output = subprocess.check_output(['synclient', '-l'])
    # Es passa 'output' a string en format 'utf-8' i es separa per salts de linia '\n'
    # Es a dir, en comptes d'un resultat unic en bytes tot junt, ara tenim una serie de strings
    # separats per un salt de linia que en el resultat en bytes era representat per els caracters '\n'
    output = output.decode('utf-8').split('\n')

    for line in output:
        # Es busca la cadena 'TouchpadOff'
        if 'TouchpadOff' in line:
            # Dos opcions de TouchpadOff:
            # TouchpadOff             = 1
            # TouchpadOff             = o

            # Es busca l'estat actual, que es el valor darrera del caracter '='
            # Es converteix a 'int' el valor
            # i '.strip()' elimina els espais innecessaris
            current_state = int(line.split('=')[1].strip())
            # Es canvia l'estat actual per un de nou
            new_state = 1 - current_state
            # Es torna a cridar al comandament 'synclient'
            # i es canvia el valor antic pel nou 'new-state'
            subprocess.call(['synclient', 'TouchpadOff={}'.format(new_state)])
            print('TouchpadOff = {}'.format(new_state))
            break

def toggle_touchpad_xinput():
    # Obtener el ID del touchpad
    touchpad_id = get_touchpad_id()
    if touchpad_id is not None:
        # Obtener el estado actual del touchpad
        current_state = get_touchpad_state(touchpad_id)
        # Cambiar el valor del estado del touchpad
        new_state = 1 if current_state == 0 else 0
        # Es passa el nou estat al dispositiu a traves d'una funcio
        set_touchpad_state(touchpad_id, new_state)
        print("Toogle del touchpad realizado correctamente.")
    else:
        print("No se encontró el ID del touchpad.")
        

def get_touchpad_id():
    # Es comproba la sortida del comando 'xinput --list'
    output = subprocess.check_output(['xinput', '--list'])
    # Es passa 'output' a string en format 'utf-8' i es separa per salts de linia '\n'
    # Es a dir, en comptes d'un resultat unic en bytes tot junt, ara tenim una serie de strings
    # separats per un salt de linia que en el resultat en bytes era representat per els caracters '\n'
    lines = output.decode('utf-8').split('\n')
    # Busca el texte 'Touchpad', i quan el troba
    for line in lines:
        if 'TouchPad' in line:
            # Es busca la posicio dtre del st
            id_start_index = line.index('id=')
            id_end_index = line.index('\t', id_start_index)
            touchpad_id = line[id_start_index+3:id_end_index]
            return touchpad_id
    return None

def get_touchpad_id_with_xinput():
    # Es reb el resultat del comando 'xinput --list'
    # Aquesta sortida es en forma de bytes
    output = subprocess.check_output(['xinput', '--list'])
    # Es passa 'output' a string en format 'utf-8' i es separa per salts de linia '\n'
    # Es a dir, en comptes d'un resultat unic en bytes tot junt, ara tenim una serie de strings
    # separats per un salt de linia que en el resultat en bytes era representat per els caracters '\n'
    lines = output.decode('utf-8').split('\n')
    for line in lines:
        if 'TouchPad' in line:
            id_start_index = line.index('id=')
            id_end_index = line.index('\t', id_start_index)
            touchpad_id = line[id_start_index+3:id_end_index]
            print('Touchpad ID = {}'.format(touchpad_id))
            return touchpad_id
    return None

def get_touchpad_state(touchpad_id):
    output = subprocess.check_output(['xinput', 'list-props', touchpad_id])
    lines = output.decode('utf-8').split('\n')
    for line in lines:
        if 'Device Enabled' in line:
            state = int(line.split(':')[1].strip())
            return state
    return None

def set_touchpad_state(touchpad_id, state):
    subprocess.run(['xinput', 'set-prop', touchpad_id, 'Device Enabled', str(state)])

toggle_touchpad()
