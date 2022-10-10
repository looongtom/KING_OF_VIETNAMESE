from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import pygame


def start_main_page():
    
    def start_game(args):
        main_window.destroy()
        if args == 1:
            from Options import Animals
            Animals.main()
        elif args == 2:
            from Options import Body_parts
            Body_parts.main()
        elif args == 3:
            from Options import Colour
            Colour.main()
        elif args == 4:
            from Options import Fruit
            Fruit.main()
        elif args == 5:
            from Options import Shapes
            Shapes.main()
        elif args == 6:
            from Options import Vegetable
            Vegetable.main()
        elif args == 7:
            from Options import Vehicles
            Vehicles.main()
    
    
    def option():    
        lab_img1 = Button(
            text="CHỌN CHỦ ĐỀ",
            bg='#16D3E0',
            border=5,

            justify='right',
            font=("Kristen ITC", 20)

        )
        
       
        sel_btn1 = Button(
            
        text="ĐỘNG VẬT",
        width=13,
        borderwidth=8,
        font=("", 15),
        fg="#000000",
        bg="#dfa801",
        cursor="hand2",
        command=lambda: start_game(1),
        )
        
        sel_btn2 = Button(
            text="CƠ THỂ",
            width=13,
            borderwidth=8,
            font=("", 15),
            fg="#000000",
            bg="#dfa801",
            cursor="hand2",
            command=lambda: start_game(2),
        )

        sel_btn3 = Button(
            text="MÀU SẮC",
            width=13,
            borderwidth=8,
            font=("", 15),
            fg="#000000",
            bg="#dfa801",
            cursor="hand2",
            command=lambda: start_game(3),
        )

        sel_btn4 = Button(
            text="HOA QUẢ",
            width=13,
            borderwidth=8,
            font=("", 15),
            fg="#000000",
            bg="#dfa801",
            cursor="hand2",
            command=lambda: start_game(4),
        )

        sel_btn5 = Button(
            text="HÌNH KHỐI",
            width=13,
            borderwidth=8,
            font=("", 15),
            fg="#000000",
            bg="#dfa801",
            cursor="hand2",
            command=lambda: start_game(5),
        )

        sel_btn6 = Button(
            text="RAU CỦ",
            width=13,
            borderwidth=8,
            font=("", 15),
            fg="#000000",
            bg="#dfa801",
            cursor="hand2",
            command=lambda: start_game(6),
        )

        sel_btn7 = Button(
            text="XE CỘ",
            width=13,
            borderwidth=8,
            font=("", 15),
            fg="#000000",
            bg="#dfa801",
            cursor="hand2",
            command=lambda: start_game(7),
        )
        lab_img1.place(x= 138, y = 20)
        sel_btn1.place(x=50,y=120)
        sel_btn2.place(x=297,y=120)
        sel_btn3.place(x=50,y=190)
        sel_btn4.place(x=297,y=190)
        sel_btn5.place(x=50,y=260)
        sel_btn6.place(x=297, y=260)
        sel_btn7.place(x=50, y=330)
        
    def show_option():
        start_btn.destroy()
        lab_img.destroy()
        intro.destroy()
        option()
        
    
    
    main_window = Tk()
    main_window.geometry("500x500+300+100")
    main_window.resizable(0, 0)
    main_window.title("VUA TIẾNG VIỆT")
  
    photo0 = Image.open("bg.png")
    resize = photo0.resize((500,500), Image.ANTIALIAS)
    photo1=ImageTk.PhotoImage(resize)
    bg_label = Label(main_window, image = photo1)
    bg_label.place(x=0, y = 0, relwidth = 1, relheight = 1)


    img = PhotoImage(file='back.png')
    
    def dong():
        main_window.destroy()
    img_exit = Image.open("thoat.png")
    resize = img_exit.resize((50,50), Image.ANTIALIAS)
    exit=ImageTk.PhotoImage(resize)
    lab_exit = Button(
        main_window,
        image = exit,
        bg='#312D4B',
        borderwidth=0,
        command = dong,
    )    
    lab_exit.pack( anchor='nw', pady=3, padx=7)
    
    logo1 = Image.open("logo1.png")
    resize = logo1.resize((200,102), Image.ANTIALIAS)
    photo3=ImageTk.PhotoImage(resize)
    


    lab_img = Label(
    main_window,
    image = photo3,
    fg ='#000000',
    bg='#312D4B',
    
    )
    lab_img.place(x= 179, y = 7)

    

    start_btn = Button(
        main_window,
        text="BẮT ĐẦU",
        width=15,
        borderwidth=5,
        fg="#000000",
        bg="#FED329",
        font=("", 13),
        cursor="hand2",
        command=show_option,
    )
    start_btn.pack(pady=(340,20))
    def show_intro():
        messagebox.showinfo("HƯỚNG DẪN", "NGƯỜI CHƠI CÓ 15 GIÂY ĐỂ TRẢ LỜI \n \n MỖI CÂU TRẢ LỜI ĐÚNG ĐƯỢC 5 ĐIỂM \n \n MỖI LẦN DÙNG GỢI Ý BỊ TRỪ ĐI 1 ĐIỂM \n")
        
    intro=Button(
        text="HƯỚNG DẪN",
        width=15,
        borderwidth=5,
        fg="#000000",
        bg="#FED329",
        font=("", 13),
        command=show_intro,
    )
    intro.pack(pady=(0,0))
    
    pygame.mixer.init()
    pygame.mixer.music.load("1.mp3")
    pygame.mixer.music.play(loops=100)


    # def play():
    #     pygame.mixer.music.load("1.mp3")
    #     pygame.mixer.music.play(loops=100)
    # def stop():
    #     pygame.mixer.music.stop()
    # global is_on
    # is_on = True
    # def switch():
    #     global is_on
        
    #     if is_on:
    #         on_button.config(image = img_off)
    #         pygame.mixer.music.load("1.mp3")
    #         pygame.mixer.music.play(loops=100)
    #         stop()
    #         is_on = False
    #     else:
    #         on_button.config(image = img_on)
    #         is_on = True    
    #         play()
    
    # on = Image.open("loabat.png")
    # resize1 = on.resize((30,30), Image.ANTIALIAS)
    # img_on=ImageTk.PhotoImage(resize1)
    # off = Image.open("loatat.png")
    # resize2 = off.resize((35,35), Image.ANTIALIAS)
    # img_off=ImageTk.PhotoImage(resize2)
    # on_button = Button(
    #     main_window,
    #     image=img_on,
    #     bg='#312D4B',
    #     border=0,
    #     justify='center',
    #     command=switch,
    # )
    # on_button.place(x=40,y=5)
    # off_button = Button(
    #     main_window,
    #     image=img_off,
    #     bg='#312D4B',
    #     border=0,
    #     justify='center',
    #     command=switch,
    # )
    # on_button.place( anchor='nw', x=7, y =50)
        
    main_window.mainloop()


start_main_page()
