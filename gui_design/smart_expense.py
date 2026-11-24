from PIL import Image

import customtkinter as ctk
#code start
m=ctk.CTk()
m.title("Trizz Expense Tracker")
m.geometry("1200x750")
m.configure(fg_color="#F8F5EF")

#sid-bar design
side_bar=ctk.CTkFrame(m,width=220,corner_radius=0,fg_color="#193D2B")
side_bar.pack(side="left",fill="y")
side_bar.pack_propagate(False)


#side bar buttons 
#leaf image

icon1 = ctk.CTkImage(
    light_image=Image.open("leaf.png"),
    size=(100, 100)
)
label3 = ctk.CTkLabel(side_bar,text="",image=icon1)
label3.pack()

#buttons
btn1=ctk.CTkButton(side_bar,text="🏠 Home",font=("Vintage",18,"bold"),text_color="#fff",fg_color="#193D2B")
btn2=ctk.CTkButton(side_bar,text="📑 Plans",font=("Vintage",18,"bold"),text_color="#fff",fg_color="#193D2B")
btn3=ctk.CTkButton(side_bar,text="📈 Track",font=("Vintage",18,"bold"),text_color="#fff",fg_color="#193D2B")
btn4=ctk.CTkButton(side_bar,text="🎯 Goal",font=("Vintage",18,"bold"),text_color="#fff",fg_color="#193D2B")
btn5=ctk.CTkButton(side_bar,text="💰 Budget",font=("Vintage",18,"bold"),text_color="#fff",fg_color="#193D2B")
btn6=ctk.CTkButton(side_bar,text="🍴 Meals",font=("Vintage",18,"bold"),text_color="#fff",fg_color="#193D2B")
btn7=ctk.CTkButton(side_bar,text="🏢 Habits",font=("Vintage",18,"bold"),text_color="#fff",fg_color="#193D2B")
btn8=ctk.CTkButton(side_bar,text="📖 Journal",font=("Vintage",18,"bold"),text_color="#fff",fg_color="#193D2B")
btn9=ctk.CTkButton(side_bar,text="🗒️ Notes",font=("Vintage",18,"bold"),text_color="#fff",fg_color="#193D2B")

btn1.pack(pady=5)
btn2.pack(pady=5)
btn3.pack(pady=5)
btn4.pack(pady=5)
btn5.pack(pady=5)
btn6.pack(pady=5)
btn7.pack(pady=5)
btn8.pack(pady=5)
btn9.pack(pady=5)

#profile picture in side-bar
icon2 = ctk.CTkImage(
    light_image=Image.open("logo.png"),
    size=(70, 70)
)
label4 = ctk.CTkLabel(side_bar,text="",image=icon2)
label4.pack(pady=10)
label5 = ctk.CTkLabel(side_bar,text="Keep Going, you've got this!",font=("vintage",15), text_color="gray")
label5.pack(pady=5)

# fist text
label=ctk.CTkLabel(m,text='No Spend Challenge',font=('vintage',20,'bold'),text_color="#193D2B")
label.pack(pady=10,padx=10)

# second text
label1=ctk.CTkLabel(m,text='Spend Mindfully. Save Intentionally. See the Difference',font=('vintage',16),text_color="gray")
label1.pack(pady=10,padx=10)

#notification icon
icon = ctk.CTkImage(
    light_image=Image.open("notification.png"),
    size=(25, 25)
)
label2 = ctk.CTkLabel(m,text="",image=icon)
label2.pack()



m.mainloop()