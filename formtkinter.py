import tkinter as tk
from tkinter import ttk, messagebox

#Membuat tampilan aplikasi Tkinter
root = tk.Tk()

#Membuat nama aplikasi 
root.title("Students Application AW3")

#Membuat tulisan
tk.Label(root, text="Hello Students AW3!").grid(row=0, column=0)
tk.Label(root, text="Please Input Your Identity!").grid(row=1, column=0)

#Membuat tulisan input text
tk.Label(root, text="First Name ").grid(row=2, column=0)
tk.Label(root, text="Last Name ").grid(row=3, column=0)
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry1.grid(row=2, column=1)
entry2.grid(row=3, column=1)

#Membuat Input Email
tk.Label(root, text="Email").grid(row=4, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=4, column=1 )

#Membuat Input Password
tk.Label(root, text="Password").grid(row=5, column=0)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=5, column=1)

#Membuat Tempat Tanggal lahir
tk.Label(root, text="Place and Date of Birth").grid(row=6, column=0)
entry_place = tk.Entry(root)
entry_place.grid(row=6, column=1)
frame_ttl = tk.Frame(root)
frame_ttl.grid(row=7, column=1)

day = ttk.Combobox(frame_ttl, values=list(range(1,32)), width=5, state="readonly")
day.grid(row=0, column=0)
day.set("1")

month = ttk.Combobox(frame_ttl, values=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],width=5, state="readonly")
month.grid(row=0, column=1)
month.set("Jan")

year = ttk.Combobox(frame_ttl, values=list(range(1990, 2025)), width=7, state="readonly")
year.grid(row=0, column=2)
year.set("2000")

#Input Nomor telepon
tk.Label(root, text="Phone Number").grid(row=8, column=0)
entry_phone = tk.Entry(root)
entry_phone.grid(row=8, column=1)

#Input Alamat Rumah
tk.Label(root, text="Address").grid(row=9, column=0)
entry_address = tk.Entry(root)
entry_address.grid(row=9, column=1)

#Membuat radio button (memilih hanya 1 option) jenis kelamin
tk.Label(root, text="Choose Your Gender!").grid(row=10, column=0)
gender = tk.IntVar() #untuk membuat option
tk.Radiobutton(root, text="Male", variable=gender, value=0).grid(row=10, column=1, sticky="w")
tk.Radiobutton(root, text="Female", variable=gender, value=1).grid(row=11, column=1, sticky="w")

#Membuat Combo box kelas
tk.Label(root, text="Choose Your Class").grid(row=12, column=0)
combo_box = ttk.Combobox(root, values=["7 AE 1", "8 AE 1", "9 AE 1"], state="readonly")
combo_box.grid(row=12, column=1, sticky="w")
combo_box.set("7 AE 1")

#Membuat Check Box Button Makanan kesukaan
tk.Label(root, text="Choose Your Favorite Food").grid(row=13, column=0)
food1 = tk.IntVar()
tk.Checkbutton(root, text="Nasi Goreng", variable=food1).grid(row=14, column=1,sticky="w")
food2 = tk.IntVar()
tk.Checkbutton(root, text="Bakso", variable=food2).grid(row=15, column=1,sticky="w")
food3 = tk.IntVar()
tk.Checkbutton(root, text="Mie Ayam", variable=food3).grid(row=16, column=1,sticky="w")

#Membuat Listbox ukuran sepatu
tk.Label(root, text="Choose Your Size Shoes").grid(row=17, column=0)
frame_list = tk.Frame(root)
frame_list.grid(row=17, column=1, columnspan=2, pady=10)
scrollbar =tk.Scrollbar(frame_list)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
mylist = tk.Listbox(frame_list, yscrollcommand=scrollbar.set, height=5)
mylist.pack(side=tk.LEFT, fill=tk.BOTH)
for line in range (36,45):
    mylist.insert(tk.END, str(line))
scrollbar.config(command=mylist.yview)

#Function Message Box Register
def register():
    #First Name and Last Name
    first_name = entry1.get()
    last_name = entry2.get()
    email = entry_email.get()
    password = entry_password.get()
    phone = entry_phone.get()
    address = entry_address.get()
    
    #Validasi email dan password
    if email == "" or password == "":
        messagebox.showwarning("Warning", "Email and Password Must be filled")
    elif "@" not in email:
        messagebox.showerror("Error", "Email Invalid")
    else:
        messagebox.showinfo("Success", "Registration Success!")
        
    #Gender
    if gender.get() == 0:
        gender_text = "Male"
    elif gender.get() == 1:
        gender_text = "Female"
    else:
        gender_text = "Not Selected"
    
    #Class
    classes = combo_box.get()
    
    # Food
    foods = []
    if food1.get() == 1:
        foods.append("Nasi Goreng")
    if food2.get() == 1:
        foods.append("Bakso")
    if food3.get() == 1:
        foods.append("Mie Ayam")
    if not foods:
        foods_text = "None"
    else:
        foods_text = ", ".join(foods)

    #Shoes
    try:
        size = mylist.get(mylist.curselection())
    except:
        size = "Not Selected"
        
    #Summary
    summary = f"""
    ==== STUDENT DATA ====
    Name    : {first_name} {last_name}
    Gender  : {gender_text}
    Class   : {classes}
    Food    : {foods_text}
    Shoe Size : {size}
    """
    messagebox.showinfo("Summary", summary)
    

#Membuat Tombol Register
btn_register = tk.Button(root, text="Register", command=register)
btn_register.grid(row=20, column=0)

#Membuat tombol exit
btn_exit = tk.Button(root, text="Exit", command=root.destroy)
btn_exit.grid(row=20, column=1)

#Menampilkan aplikasi Tkinter
root.mainloop()