from tkinter import *

bg_color = '#eccc68' #f6e58d

l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
L = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')


def encript():
    p = en_plain.get('1.0', END)
    key = int(en_key.get())

    c = []
    for i in p:
        if i!=' ':
            if i in l:
                index = (l.index(i) + 3)%26
                c.append(l[index])
            elif i in L:
                index = (L.index(i) + 3)%26
                c.append(L[index])
            
    en_cipher.delete('1.0', END)
    for i in c:
        en_cipher.insert(END, i)


def decrypt():
    c = en_cipher.get('1.0', END)
    key = int(en_key.get())
    
    p = []
    for i in c:
        if i!=' ':
            if i in l:
                index = (l.index(i) - 3)%26
                p.append(l[index])
            elif i in L:
                index = (L.index(i) - 3)%26
                p.append(L[index])
    
    en_plain.delete('1.0', END)
    for i in p:
        en_plain.insert(END, i)
    

def clear():
    en_plain.delete('1.0', END)
    en_cipher.delete('1.0', END)


root = Tk()
root.title('Shift Cipher')
root.geometry("720x530+450+40")
root['bg'] = bg_color

Label(root, text="Shift Cipher", font=('Consolas', 24), bg=bg_color).pack(pady=(15, 0))

Label(root, text="PlainText", font=('', 14), bg=bg_color,).place(x=50, y=100)
en_plain = Text(root, font=('Calibri (Body)', 14))
en_plain.place(x=50, y=128, height=350, width=220)

Label(root, text="CipherText", font=('', 14), bg=bg_color,).place(x=450, y=100)
en_cipher = Text(root, font=('Calibri (Body)', 14) )
en_cipher.place(x=450, y=128, height=350, width=220)

Label(root, text='Enter key', font=('Bahnschrift', 12), bg=bg_color, ).place(x=306, y=170)
en_key = Entry(root, font=('Bahnschrift', 12), justify='center', )
en_key.place(x=381, y=171, height=25, width=25)
en_key.insert(0,"3")

btn_encrypt = Button(root, text='Encrypt', font=('Arial Rounded MT Bold', 12, 'bold'), height=2, width=12, bg='purple', fg='white', relief=FLAT, command=encript)
btn_encrypt.pack(pady=(180,25))

btn_decrypt = Button(root, text='Decrypt', font=('Arial Rounded MT Bold', 12, 'bold'), height=2, width=12, bg='red', fg='white', relief=FLAT, command=decrypt)
btn_decrypt.pack()

btn_clear = Button(root, text='Clear', font=('Arial Rounded MT Bold', 12, 'bold'), height=2, width=12, bg='green', fg='white', relief=FLAT, command=clear)
btn_clear.pack(pady=(25,0))

root.mainloop()