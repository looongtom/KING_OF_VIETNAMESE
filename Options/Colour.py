from tkinter import *
from random import *
from tkinter import messagebox
import random
import time
import pygame
from PIL import ImageTk,Image
ANIMALS_ANSWER = ["DA TRỜI", "TÍM THAN", "XANH LÁ","ĐỎ ĐÔ","HỒNG PHẤN","GHI SÁNG"]


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
    my_window.geometry("600x600+100+20")
    my_window.resizable(0, 0)
    my_window.title("Vua Tiếng Việt")
    # my_window.configure(background="#2a363b")
    photo2 = Image.open("anhnen1.png")
    resize = photo2.resize((600,600), Image.ANTIALIAS)
    photo3=ImageTk.PhotoImage(resize)
    bg_label2 = Label(my_window, image = photo3)
    bg_label2.place(x=0, y = 0, relwidth = 1, relheight = 1)
   

    img1 = PhotoImage(file="back.png")

    lab_img1 = Button(
        my_window,
        image=img1,
        bg='#154854',
        border=0,
        justify='center',
        command=back,
    )
    lab_img1.pack(anchor='nw', pady=45, padx=30)

    img2 = Image.open("logo2.png")
    resize = img2.resize((400,100), Image.ANTIALIAS)
    img3=ImageTk.PhotoImage(resize)
    lab_img2 = Button(
        my_window,
        image = img3,
        bg='#154854',
        borderwidth=0,
    )    
    lab_img2.pack()
    second=StringVar()
    second.set("10")
    time_title=StringVar()
    time_title.set("Thời gian")
    count_set=Label(
       # width=8, font=("Titillium",15),textvariable=time_title
        text="Thời gian",
        bg="#154854",
        fg="#dfa801",
        font="Titillium  14 bold"
    )
    count_set.place(x=490,y=40.455)
    count_down=Label(
            width=2, font=("Titillium",15),textvariable=second
    )
    #count_down.config(bg="2a363b")
    count_down.place(x=520,y=70)

    def run(temp):
        global points
        
        while temp >-1:
            mins,secs = divmod(temp,60)
            second.set("{0:2d}".format(secs))
            my_window.update()
            time.sleep(1)
            if (temp == 0):
                # messagebox.showinfo("ĐÃ HẾT GIỜ", "ĐÃ HẾT GIỜ \n BẠN GIÀNH ĐƯỢC ",strPoint," ĐIỂM" "\nHÃY THỬ LẠI VÀO LẦN SAU")
                messagebox.showinfo("ĐÃ HẾT GIỜ","BẠN GIÀNH ĐƯỢC "+str(points)+" ĐIỂM\nHÃY THỬ LẠI VÀO LẦN SAU")
                back()
            temp -= 1
    

    score = Label(text="Điểm: 0", pady=5, bg="#154854", fg="#dfa801", font="Titillium  14 bold"
    )
    score.pack(anchor="n")

    word = Label(   text=jumbled_rand_word, pady=10, width=15,relief='raise', borderwidth=5, bg="#dfa801",  fg="#000000", font="Titillium  30 bold"  
    )


    word.place(x= 117, y=270)
    #word.grid(pady=(10))
    get_input = Entry(  font="none 18 bold", relief = 'raise',borderwidth=5,  justify='center',  
    )
    get_input.place(x=165, y= 354)

    submit = Button( text="Kiểm tra",  width=12,   borderwidth=5,  font=("", 14),  fg="#000000",  bg="#dfa801", command=cheak, 
    )
    submit.place(x=228, y= 400)

    change = Button( text="Đổi từ",width=12,borderwidth=5,fg="#000000", bg="#dfa801",font=("", 14),command=change, 
    )
    change.place(x=228, y= 460)
    
    ans = Button(text="Gợi ý", width=12, borderwidth=5, fg="#000000",  bg="#dfa801", font=("", 14), command=show_answer, 
    )
    ans.place(x=228, y=520 )
    ans_lab = Label(  text="",  bg="#154854", fg="#dfa801",  font="Courier 18 bold", )
    ans_lab.place(x=224, y = 570)
    run(15)
    my_window.mainloop()
