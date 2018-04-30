
# coding: utf-8


from tkinter import *
from tkinter import ttk  
from tkinter import filedialog
import time


window = Tk()

multiplyer = 1.3
w=800 *multiplyer
h=450 *multiplyer
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws/2) - (w/2)    
y = (hs/2) - (h/2)
window.geometry('%dx%d+%d+%d' % (w, h, x, y))



window.title("I am beta jump")


progressbar = ttk.Progressbar(window, orient = HORIZONTAL, length = 258 *multiplyer)
progressbar.place(x = 0 *multiplyer,y = 10 *multiplyer)




progressbar.config(mode = 'determinate', maximum = 10, value = 0)


# # label time



label_time = Label(window, text = "",font = ("Times New Roman ",13))
label_time.place(x = 5 *multiplyer, y =50 *multiplyer)


# # activate botton 3-9



def clickMe(): # 5
    progressbar.config(mode = 'indeterminate')
    progressbar.start()
    import beta_jump
    filename1 = filedialog.askopenfile()
    t0 = time.time() 
    global demo
    demo = beta_jump.beta_jump(filename = filename1.name) ##filename1 is not string, https://stackoverflow.com/questions/29990224/how-to-get-a-string-from-the-tkinter-filedialog-in-python-3
    botton_activate.configure(text=" Beta Jump \n has been activate! ",justify='center')
    botton_activate.configure(bg='green',fg = 'white')
    bottom_image.configure(image = photo2)
    progressbar.stop()
    progressbar.config(mode = 'determinate', maximum = 10, value = 10)
    t1 = time.time() 
    label_time.config(text = f"total time {round(t1-t0,1)} seconds! beta jump activated!")
# Adding a Button # 6
botton_activate = Button(window,text="Activate Beta Jump", command=clickMe, width=int(18 *multiplyer) , height= int(9 *multiplyer) , bg='red' , fg='blue', bd=30
     ,cursor= 'heart' , activebackground='green' , activeforeground='white',font = ("Times New Roman bold",13))
botton_activate.place(x = int(20 *multiplyer), y =int(100 *multiplyer))

# # file selector 4-33 go to activate click button

# # Label ask questions

label_ask = Label(window, text = "Talk to Beta Jump",font = ("Times New Roman bold",15))
label_ask.place(x =int(60*multiplyer), y =int(360*multiplyer))

# # ask input


text_ask = Entry(window,width=  int(60*multiplyer))




text_ask.place(x = 10 *multiplyer, y =400 *multiplyer)


# # botton image high x20,width x10


def clickMe_photo():
    try:
        label_answer.config(text = demo.ask(text_ask.get()))
    except:
        label_answer.config(text="ZZZZZZZZzzzzzzzzz")



photo1 = PhotoImage(file = 'black.gif')
photo2 = PhotoImage(file = 'beta_jump.gif')

bottom_image = Button(width=520 *multiplyer, height=360 *multiplyer,fg='red' , bg='black' , bd=5
                 , activebackground='green' , activeforeground='white', cursor= 'heart'
                 , underline= 1, state=NORMAL,image = photo1,command=clickMe_photo )



bottom_image.place(x = 260 *multiplyer, y =0 *multiplyer)


# # answer label


label_answer = Label(window, text = "",width=int(27 *multiplyer), justify='center',font = ("Times New Roman bold",25),fg='#9c51ff')
label_answer.place(x = int(260 *multiplyer), y =int(400 *multiplyer))


window.mainloop()

