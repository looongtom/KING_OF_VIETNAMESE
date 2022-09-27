from tkinter import *
from random import *
from tkinter import messagebox
import random
import time
import pygame

ANIMALS_ANSWER = ["CHỮ NHẬT", "TAM GIÁC", "HÌNH THANG","HÌNH TRÒN","HÌNH QUẠT","HÌNH TRỤ","HỘP CHỮ NHẬT","KIM TỰ THÁP","HÌNH NÓN"]


ran_num = randrange(0, (len(ANIMALS_ANSWER)))
tmp=ANIMALS_ANSWER[ran_num]
s=tmp
while(s==tmp ):
    l=[]
    s=""
    for i in range(len(tmp)): l.append(tmp[i])
    random.shuffle(l)
    for i in l: 
        if(i!=' '):s+=i
    if(s!=tmp):break
jumbled_rand_word = s
points = 0
coun=0
answ=""

def main():

    pygame.mixer.init()
    pygame.mixer.music.load("2.mp3")
    pygame.mixer.music.play(loops=100)

    def back():
        my_window.destroy()
        import index
        index.start_main_page()
    def Shuff(tmp):
        s=tmp
        while(s==tmp ):
            l=[]
            s=""
            for i in range(len(tmp)): l.append(tmp[i])
            random.shuffle(l)
            for i in l: 
                if(i!=' '):s+=i
            if(s!=tmp):break
        return s
    def change():
        global ran_num
        global coun
        global asnw
        ran_num = randrange(0, (len(ANIMALS_ANSWER)))
        s=Shuff(ANIMALS_ANSWER[ran_num])
        word.configure(text=s)
        get_input.delete(0, END)
        ans_lab.configure(text="")
        coun=0
        answ=""

    def cheak():
        global points, ran_num
        global coun
        global asnw
        global ANIMALS_ANSWER
        user_word = get_input.get().upper()
        if user_word == ANIMALS_ANSWER[ran_num]:
            points += 5
            score.configure(text="ĐIỂM: " + str(points))
            messagebox.showinfo('CHÍNH XÁC', "BẠN TUYỆT LẮM ! HÃY TIẾP TỤC")
            ANIMALS_ANSWER.pop(ran_num)

            if(len(ANIMALS_ANSWER)==0):
                messagebox.showinfo('CHÚC MỪNG', "BẠN ĐÃ CHIẾN THẮNG TRẢ LỜI HẾT CÁC CÂU HỎI")
                my_window.destroy()
                import index
                index.start_main_page()

            ran_num = randrange(0, (len(ANIMALS_ANSWER)))
            s=Shuff(ANIMALS_ANSWER[ran_num])
            word.configure(text=s)
            get_input.delete(0, END)
            ans_lab.configure(text="")
            coun=0
            asnw =""
            run(15)
            
        else:
            messagebox.showerror("SAI RỒI", "CỐ LÊN HÃY THỬ LẠI")
            get_input.delete(0, END)

    def show_answer():
        global points
        global coun
        global answ
        if points > 0:
            n=len(ANIMALS_ANSWER[ran_num])
            if(coun>=n):
                messagebox.showinfo('',"VUI LÒNG ĐIỀN ĐÁP ÁN")
            else:
                if(coun==0):answ=""
                points -= 1
                score.configure(text="Điểm: " + str(points))
                s=ANIMALS_ANSWER[ran_num]
                i=0
                answ+=s[coun]
                coun+=1
                ans_lab.configure(text=answ)
                time.sleep(0.5)
            #ans_lab.configure(text=str(n))
        else:
            ans_lab.configure(text='Không đủ điểm')

    my_window = Tk()
    my_window.geometry("600x600+500+150")
    my_window.resizable(0, 0)
    my_window.title("Vua Tiếng Việt")
    my_window.configure(background="#2a363b")
    img1 = PhotoImage(file="back.png")

    lab_img1 = Button(
        my_window,
        image=img1,
        bg='#2a363b',
        border=0,
        justify='center',
        command=back,
    )
    lab_img1.pack(anchor='nw', pady=10, padx=10)
    second=StringVar()
    second.set("10")
    time_title=StringVar()
    time_title.set("Thời gian")
    count_set=Label(
       # width=8, font=("Titillium",15),textvariable=time_title
        text="Thời gian",
        bg="#dfa801",
        fg="#2a363b",
        font="Titillium  15 bold"
    )
    count_set.place(x=478,y=30.455)
    count_down=Label(
            width=2, font=("Titillium",30),textvariable=second
    )
    #count_down.config(bg="2a363b")
    count_down.place(x=500,y=61)

    def run(temp):
        while temp >-1:
            mins,secs = divmod(temp,60)
            second.set("{0:2d}".format(secs))
            my_window.update()
            time.sleep(1)
            if (temp == 0):
                messagebox.showinfo("ĐÃ HẾT GIỜ", "ĐÃ HẾT GIỜ \n HÃY THỬ LẠI VÀO LẦN SAU")
                back()
            temp -= 1
    

    score = Label(text="Điểm: 0", pady=16, bg="#2a363b", fg="#dfa801", font="Titillium  14 bold"
    )
    score.pack(anchor="n")

    word = Label(   text=jumbled_rand_word, pady=10, width=18, bg="#dfa801",  fg="#000000", font="Titillium  50 bold"  
    )


    word.pack()
    #word.grid(pady=(10))
    get_input = Entry(  font="none 26 bold", borderwidth=10,  justify='center',  
    )
    get_input.pack()

    submit = Button( text="Kiểm tra",  width=18,   borderwidth=8,  font=("", 18),  fg="#000000",  bg="#dfa801", command=cheak, 
    )
    submit.pack(pady=(10, 20))

    change = Button( text="Đổi từ",width=18,borderwidth=8,fg="#000000", bg="#dfa801",font=("", 18),command=change, 
    )
    change.pack()
    ans = Button(text="Gợi ý", width=18, borderwidth=8, fg="#000000",  bg="#dfa801", font=("", 18), command=show_answer, 
    )
    ans.pack(pady=(20, 10))
    ans_lab = Label(  text="",  bg="#2a363b", fg="#dfa801",  font="Courier 17 bold", )
    ans_lab.pack()
    run(15)
    my_window.mainloop()
