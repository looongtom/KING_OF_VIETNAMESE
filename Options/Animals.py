from tkinter import *
from random import *
from tkinter import messagebox
import time

ANIMALS_WORD = ['MIHC', 'ÓHC', 'ỪCU', 'ƯƠHU', 'NƯỢV', 'ÈMO', 'GỰAN', 'ỔH', 'ỈHK', 'GNO', 'ỊVT',
                'HCẾ', 'OVI', 'ÁC', 'ỢNL', 'ÀG', 'ỘUHCt', 'ÔCNG', 'HỎT', 'UÂTR', ]

ANIMALS_ANSWER = ['CHIM', 'CHÓ', 'CỪU', 'HUƠU', 'VƯỢN', 'MÈO', 'NGỰA', 'HỔ', 'KHỈ', 'ONG', 'VỊT',
                  'ẾCH', 'VOI', 'CÁ', 'LỢN', 'GÀ', 'CHUỘT', 'CÔNG', 'THỎ', 'TRÂU', ]

ran_num = randrange(0, (len(ANIMALS_WORD)))
jumbled_rand_word = ANIMALS_WORD[ran_num]

points = 0
coun=0
answ=""

def main():
    def back():
        my_window.destroy()
        import index
        index.start_main_page()

    def change():
        global ran_num
        global coun
        global asnw
        ran_num = randrange(0, (len(ANIMALS_WORD)))
        word.configure(text=ANIMALS_WORD[ran_num])
        get_input.delete(0, END)
        ans_lab.configure(text="")
        coun=0
        answ=""

    def cheak():
        global points, ran_num
        global coun
        global asnw
        user_word = get_input.get().upper()
        if user_word == ANIMALS_ANSWER[ran_num]:
            points += 5
            score.configure(text="ĐIỂM: " + str(points))
            messagebox.showinfo('CHÍNH XÁC', "BẠN TUYỆT LẮM ! HÃY TIẾP TỤC")
            ran_num = randrange(0, (len(ANIMALS_WORD)))
            word.configure(text=ANIMALS_WORD[ran_num])
            get_input.delete(0, END)
            ans_lab.configure(text="")
            coun=0
            asnw =""
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

    score = Label(
        text="Điểm: 0",
        pady=16,
        bg="#2a363b",
        fg="#dfa801",
        font="Titillium  14 bold"
    )
    score.pack(anchor="n")

    word = Label(
        text=jumbled_rand_word,
        pady=10,
        width=18,
        bg="#ffffff",
        fg="#000000",
        font="Titillium  50 bold"
    )

    word.pack()

    get_input = Entry(
        font="none 26 bold",
        borderwidth=10,
        justify='center',
    )
    get_input.pack()

    submit = Button(
        text="Kiểm tra",
        width=18,
        borderwidth=8,
        font=("", 18),
        fg="#000000",
        bg="#dfa801",
        command=cheak,
    )
    submit.pack(pady=(10, 20))

    change = Button(
        text="Đổi từ",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#dfa801",
        font=("", 18),
        command=change,
    )
    change.pack()
    coun=0
    ans = Button(
        text="Đáp án",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#dfa801",
        font=("", 18),
        command=show_answer,
    )
    ans.pack(pady=(20, 10))

    ans_lab = Label(
        text="",
        bg="#2a363b",
        fg="#dfa801",
        font="Courier 17 bold",
    )
    ans_lab.pack()

    my_window.mainloop()
