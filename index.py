from tkinter import *
from tkinter import messagebox
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
            bg='#7f9dc0',
            border=0,
            justify='left',
            font=("Arial", 18)

        )
        sel_btn1 = Button(
            text="ĐỘNG VẬT",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#dfa801",
            cursor="hand2",
            command=lambda: start_game(1),
        )

        sel_btn2 = Button(
            text="CƠ THỂ",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#dfa801",
            cursor="hand2",
            command=lambda: start_game(2),
        )

        sel_btn3 = Button(
            text="MÀU SẮC",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#dfa801",
            cursor="hand2",
            command=lambda: start_game(3),
        )

        sel_btn4 = Button(
            text="HOA QUẢ",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#dfa801",
            cursor="hand2",
            command=lambda: start_game(4),
        )

        sel_btn5 = Button(
            text="HÌNH KHỐI",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#dfa801",
            cursor="hand2",
            command=lambda: start_game(5),
        )

        sel_btn6 = Button(
            text="RAU CỦ",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#dfa801",
            cursor="hand2",
            command=lambda: start_game(6),
        )

        sel_btn7 = Button(
            text="XE CỘ",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#dfa801",
            cursor="hand2",
            command=lambda: start_game(7),
        )
        lab_img1.grid(row=0, column=0, padx=20)
        sel_btn1.grid(row=0, column=4, pady=(10, 0), padx=0, )
        sel_btn2.grid(row=1, column=4, pady=(10, 0), padx=0, )
        sel_btn3.grid(row=2, column=4, pady=(10, 0), padx=0, )
        sel_btn4.grid(row=3, column=4, pady=(10, 0), padx=0, )
        sel_btn5.grid(row=4, column=4, pady=(10, 0), padx=0, )
        sel_btn6.grid(row=5, column=4, pady=(10, 0), padx=0, )
        sel_btn7.grid(row=6, column=4, pady=(10, 0), padx=0, )

    def show_option():
        start_btn.destroy()
        lab_img.destroy()
        intro.destroy()
        option()
    
    main_window = Tk()

    main_window.geometry("500x500+500+150")
    main_window.resizable(0, 0)
    main_window.title("VUA TIẾNG VIỆT")
    main_window.configure(background="#2a363b")
    

    img = PhotoImage(file="back.png")

    lab_img = Label(
        main_window,
        text="VUA TIẾNG VIỆT",
        bg='#dfa801',
        font=("Titillium 15 bold", 30)
    )
    lab_img.pack(pady=(50, 0))

    start_btn = Button(
        main_window,
        text="BẮT ĐẦU",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#dfa801",
        font=("", 13),
        cursor="hand2",
        command=show_option,
    )
    start_btn.pack(pady=(150,20))
    def show_intro():
        messagebox.showinfo("HƯỚNG DẪN", "NGƯỜI CHƠI CÓ 15 GIÂY ĐỂ TRẢ LỜI \n \n MỖI CÂU TRẢ LỜI ĐÚNG ĐƯỢC 5 ĐIỂM \n \n MỖI LẦN DÙNG GỢI Ý BỊ TRỪ ĐI 1 ĐIỂM \n")
        
    intro=Button(
        text="HƯỚNG DẪN",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#dfa801",
        font=("", 13),
        command=show_intro,
    )
    intro.pack(pady=(0,0))

    pygame.mixer.init()
    pygame.mixer.music.load("1.mp3")
    pygame.mixer.music.play(loops=100)
    
    main_window.mainloop()


start_main_page()
