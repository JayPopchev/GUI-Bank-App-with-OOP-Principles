from tkinter import Tk, Label, Button, PhotoImage, Frame, RAISED, Toplevel, Entry, StringVar, Radiobutton, SOLID, FLAT, \
    IntVar
import time

import _tkinter

from bank_app.bank_manager import BankManager

bank = BankManager()


# updates the tipe var with a second delay
def update_clock(clock_label):
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, lambda: update_clock(clock_label))


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


def sign_in():
    sign_in_window = Toplevel()
    sign_in_window.title("Sign In your account")
    center_window(sign_in_window, 400, 300)

    sign_in_window.bg_photo = PhotoImage(file="img.png")
    bg_label = Label(sign_in_window, image=sign_in_window.bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Main container frame
    main_frame = Frame(sign_in_window,
                       bg="white",
                       bd=2,
                       relief=SOLID,
                       padx=30,
                       pady=30)
    main_frame.pack(pady=30, padx=30, fill="both", expand=True)

    # Title
    title_label = Label(main_frame,
                        text="Welcome Back",
                        font=('Arial', 22, "bold"),
                        bg="white",
                        fg="#2c3e50")  # Dark blue-gray
    title_label.pack(pady=(0, 25))

    # Name entry
    name_frame = Frame(main_frame, bg="white")
    name_frame.pack(fill="x", pady=(0, 15))

    name_label = Label(name_frame,
                       text="Your Name",
                       font=('Arial', 12),
                       bg="white",
                       fg="#7f8c8d")  # Gray text
    name_label.pack(anchor="w")

    name_entry = Entry(name_frame,
                       font=('Arial', 14),
                       bd=2,
                       relief=SOLID,
                       highlightthickness=1,
                       highlightcolor="#3498db",
                       highlightbackground="#bdc3c7")
    name_entry.pack(pady=(5, 0), fill="x", ipady=5)

    # Account type selection
    type_frame = Frame(main_frame, bg="white")
    type_frame.pack(fill="x", pady=(15, 10))

    type_label = Label(type_frame,
                       text="Account Type",
                       font=('Arial', 12),
                       bg="white",
                       fg="#7f8c8d")
    type_label.pack(anchor="w")

    # Radio button styling
    choice_var = StringVar(value="BasicAccount")
    radio_style = {
        'font': ('Arial', 12),
        'bg': "white",
        'activebackground': "white",
        'selectcolor': "white",
        'fg': "#2c3e50",
        'padx': 5,
        'pady': 8
    }

    radio_frame = Frame(type_frame, bg="white")
    radio_frame.pack(pady=(10, 0), fill="x")

    radio1 = Radiobutton(radio_frame,
                         text="Basic Account",
                         variable=choice_var,
                         value="BasicAccount",
                         **radio_style)
    radio1.pack(anchor="w")

    radio2 = Radiobutton(radio_frame,
                         text="Premium Account",
                         variable=choice_var,
                         value="PremiumAccount",
                         **radio_style)
    radio2.pack(anchor="w")

    radio3 = Radiobutton(radio_frame,
                         text="Gold Account",
                         variable=choice_var,
                         value="GoldAccount",
                         **radio_style)
    radio3.pack(anchor="w")

    # Status label
    status_label = Label(main_frame,
                         text="",
                         font=('Arial', 12),
                         bg="white",
                         height=2)
    status_label.pack(pady=(15, 5), fill="x")

    def find_account():
        name = name_entry.get().strip()
        type_account = choice_var.get()
        try:
            accounts_in_selected_type = bank.get_accounts_by_type(name, type_account)
            money = accounts_in_selected_type.balance
            owner_id = accounts_in_selected_type.account_id
            status_label.config(text=f"Successfully found: {name} || {type_account}", fg="green")
            submit_button.config(state="disabled")
            account_details_window(name, type_account, money, owner_id)
        except ValueError:
            status_label.config(text="Account not found, please try again!", fg="red")

    submit_button = Button(main_frame,
                           text="Sign In",
                           font=('Arial', 14, "bold"),
                           fg='white',
                           bg="#3498db",  # Blue color
                           relief=FLAT,
                           bd=0,
                           padx=20,
                           pady=12,
                           activebackground="#2980b9",
                           activeforeground="white",
                           command=find_account)
    submit_button.pack(pady=(20, 10), fill="x", ipady=5)




def register():
    register_window = Toplevel()
    register_window.title("Register Account")
    center_window(register_window, 500, 500)

    register_window.bg_photo = PhotoImage(file="img.png")
    bg_label = Label(register_window, image=register_window.bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    main_frame = Frame(register_window, bg="white", bd=2, relief=SOLID, padx=20, pady=20)
    main_frame.pack(pady=30, padx=30, fill="both", expand=True)

    # Title label
    title_label = Label(main_frame,
                        text="Create New Account",
                        font=('Arial', 20, "bold"),
                        bg="white",
                        fg="#2c3e50")
    title_label.pack(pady=(0, 20))

    # Name field
    name_frame = Frame(main_frame, bg="white")
    name_frame.pack(pady=(0, 15), fill="x")

    name_label = Label(name_frame,
                       text="Full Name",
                       font=('Arial', 12),
                       bg="white",
                       fg="#7f8c8d")
    name_label.pack(anchor="w")

    name_entry = Entry(name_frame,
                       font=('Arial', 14),
                       bd=2,
                       relief=SOLID)
    name_entry.pack(pady=(5, 0), fill="x")

    # Account type selection
    type_frame = Frame(main_frame, bg="white")
    type_frame.pack(pady=(15, 10), fill="x")

    type_label = Label(type_frame,
                       text="Account Type",
                       font=('Arial', 12),
                       bg="white",
                       fg="#7f8c8d")
    type_label.pack(anchor="w")

    # Radio button styling
    choice_var = StringVar(value="BasicAccount")
    radio_style = {'font': ('Arial', 12),
                   'bg': "white",
                   'activebackground': "white",
                   'selectcolor': "white",
                   'fg': "#2c3e50",
                   'padx': 5,
                   'pady': 5}

    radio_frame = Frame(type_frame, bg="white")
    radio_frame.pack(pady=(10, 0), fill="x")

    radio1 = Radiobutton(radio_frame,
                         text="Basic Account",
                         variable=choice_var,
                         value="BasicAccount",
                         **radio_style)
    radio1.pack(anchor="w")

    radio2 = Radiobutton(radio_frame,
                         text="Premium Account (medium return on deposit and withdraw)",
                         variable=choice_var,
                         value="PremiumAccount",
                         **radio_style)
    radio2.pack(anchor="w")

    radio3 = Radiobutton(radio_frame,
                         text="Gold Account (high return on deposit and withdraw)",
                         variable=choice_var,
                         value="GoldAccount",
                         **radio_style)
    radio3.pack(anchor="w")

    # Status label
    status_label = Label(main_frame,
                         text="",
                         font=('Arial', 12),
                         bg="white",
                         fg="#2ecc71",
                         height=2)
    status_label.pack(pady=(10, 5), fill="x")

    def create_account():
        name = name_entry.get().strip()
        type_account = choice_var.get()
        try:
            bank.create_bank_account(name, type_account)
            status_label.config(text=f"Successfully registered ✓: {name} --- {type_account}", fg="green")
            submit_button.config(state="disabled")
        except ValueError:
            status_label.config(text="Invalid input. Please try again.", fg="red")

    submit_button = Button(main_frame,
                           text="Create Account",
                           font=('Arial', 14, "bold"),
                           fg='white',
                           bg="#3498db",
                           relief=FLAT,
                           bd=0,
                           padx=20,
                           pady=10,
                           activebackground="#2980b9",
                           activeforeground="white",
                           command=create_account)
    submit_button.pack(pady=(20, 10), fill="x")

def account_details_window(account_name, account_type, money, owner_id):
    details_window = Toplevel()
    details_window.title("Account Details")
    center_window(details_window, 400, 300)

    details_window.bg_photo = PhotoImage(file="img.png")
    bg_label = Label(details_window, image=details_window.bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Main container frame
    main_frame = Frame(details_window,
                       bg="white",
                       bd=2,
                       relief=SOLID,
                       padx=30,
                       pady=30)
    main_frame.pack(pady=30, padx=30, fill="both", expand=True)

    # Header section
    header_frame = Frame(main_frame, bg="white")
    header_frame.pack(fill="x", pady=(0, 20))

    title_label = Label(header_frame,
                        text="Account Overview",
                        font=('Arial', 22, "bold"),
                        bg="white",
                        fg="#2c3e50")
    title_label.pack(anchor="w")

    # Account details section
    details_frame = Frame(main_frame, bg="white")
    details_frame.pack(fill="x", pady=(0, 30))

    # Detail rows with consistent styling
    def create_detail_row(parent, label, value):
        row = Frame(parent, bg="white")
        row.pack(fill="x", pady=5)

        lbl = Label(row,
                    text=label,
                    font=('Arial', 12),
                    bg="white",
                    fg="#7f8c8d",
                    width=12,
                    anchor="w")
        lbl.pack(side="left")

        val = Label(row,
                    text=value,
                    font=('Arial', 12, "bold"),
                    bg="white",
                    fg="#2c3e50",
                    anchor="w")
        val.pack(side="left", padx=10)
        return row

    create_detail_row(details_frame, "Account Holder:", account_name)
    create_detail_row(details_frame, "Account Type:", account_type)
    create_detail_row(details_frame, "Account ID:", str(owner_id))

    # Balance display with emphasis
    balance_frame = Frame(details_frame, bg="white", pady=15)
    balance_frame.pack(fill="x", pady=(10, 0))

    balance_label = Label(balance_frame,
                          text="Current Balance:",
                          font=('Arial', 14),
                          bg="white",
                          fg="#7f8c8d")
    balance_label.pack(anchor="w")

    balance_value = Label(balance_frame,
                          text=f"${money:.2f}",
                          font=('Arial', 28, "bold"),
                          bg="white",
                          fg="#27ae60")
    balance_value.pack(anchor="w", pady=(5, 0))

    # Action buttons section
    buttons_frame = Frame(main_frame, bg="white")
    buttons_frame.pack(fill="x", pady=(20, 0))

    def deposit():
        deposit_btn.config(state="disabled")
        withdraw_btn_.config(state="disabled")
        deposit_window = Toplevel()
        deposit_window.title("Deposit Funds")
        center_window(deposit_window, 400, 300)

        deposit_window.bg_photo = PhotoImage(file="img.png")
        bg_label = Label(deposit_window, image=deposit_window.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        main_deposit_frame = Frame(deposit_window,
                       bg="white",
                       bd=2,
                       relief=SOLID,
                       padx=30,
                       pady=30)

        main_deposit_frame.pack(pady=30, padx=30, fill="both", expand=True)

        header_deposit_frame = Frame(main_deposit_frame, bg="white")
        header_deposit_frame.pack(fill="x", pady=(0, 20))

        title_deposit_label = Label(header_deposit_frame,
                            text="Deposit",
                            font=('Arial', 22, "bold"),
                            bg="white",
                            fg="#2c3e50")
        title_deposit_label.pack(anchor="w")

        # Amount entry
        amount_deposit_frame = Frame(main_deposit_frame, bg="white")
        amount_deposit_frame.pack(fill="x", pady=(0, 15))

        amount_deposit_label = Label(amount_deposit_frame,
                             text="Amount to Deposit",
                             font=('Arial', 12),
                             bg="white",
                             fg="#7f8c8d")
        amount_deposit_label.pack(anchor="w")

        # Currency symbol label
        input_frame = Frame(amount_deposit_frame, bg="white")
        input_frame.pack(fill="x", pady=(5, 0))

        currency_label = Label(input_frame,
                               text="$",
                               font=('Arial', 14),
                               bg="white",
                               fg="#2c3e50")
        currency_label.pack(side="left", padx=(0, 5))
        amount_var = IntVar(value=0)
        amount_entry = Entry(input_frame,
                             font=('Arial', 14),
                             bd=2,
                             relief=SOLID,
                             highlightthickness=1,
                             highlightcolor="#3498db",
                             highlightbackground="#bdc3c7",textvariable=amount_var)
        amount_entry.pack(fill="x", expand=True, ipady=5)
        amount_entry.focus_set()

        # Status label
        status_frame = Frame(main_deposit_frame, bg="white")
        status_frame.pack(fill="x", pady=(10, 0))

        status_deposit_label = Label(status_frame,
                                     text="",
                                     font=('Arial', 12),
                                     bg="white",
                                     wraplength=300,
                                     justify="left")
        status_deposit_label.pack(anchor="w")
        def deposit_action():
            try:
                amount = amount_var.get()
                user = bank.get_accounts_by_type(account_name, account_type)
                user.balance += user.return_on_deposit(amount)
                status_deposit_label.config(text=f"Deposited - {amount:.2f}\nTotal Balance - {user.balance:.2f}", fg="green")
                submit_btn.config(state="disabled")
                balance_value.config(text=f"{user.balance:.2f}")
                deposit_btn.config(state="active")
                withdraw_btn_.config(state="active")

            except (ValueError, _tkinter.TclError):
                status_deposit_label.config(text="Invalid input. Please try again.", fg="red")

        # Submit button
        submit_btn = Button(main_deposit_frame,
                            text="Confirm Deposit",
                            font=('Arial', 14, "bold"),
                            fg='white',
                            bg="#27ae60",  # Green for deposit
                            relief=FLAT,
                            bd=0,
                            padx=20,
                            pady=12,
                            activebackground="#219653",
                            activeforeground="white",
                            command=deposit_action)

        submit_btn.pack(fill="x", pady=(10, 0), ipady=5)

    deposit_btn = Button(buttons_frame,text="Deposit Funds",
                         font=('Arial', 14, "bold"),
                         fg='white',
                         bg="#3498db",
                         relief=FLAT,
                         bd=0,
                         padx=20,
                         pady=12,
                         activebackground=f"dark blue",
                         activeforeground="white",
                         command=deposit)
    deposit_btn.pack(fill="x", pady=8, ipady=5)

    def withdraw():
        deposit_btn.config(state="disabled")
        withdraw_btn_.config(state="disabled")
        withdraw_window = Toplevel()
        withdraw_window.title("Deposit Funds")
        center_window(withdraw_window, 400, 300)

        withdraw_window.bg_photo = PhotoImage(file="img.png")
        bg_label = Label(withdraw_window, image=withdraw_window.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        main_withdraw_frame = Frame(withdraw_window,
                                   bg="white",
                                   bd=2,
                                   relief=SOLID,
                                   padx=30,
                                   pady=30)

        main_withdraw_frame.pack(pady=30, padx=30, fill="both", expand=True)

        header_withdraw_frame = Frame(main_withdraw_frame, bg="white")
        header_withdraw_frame.pack(fill="x", pady=(0, 20))

        title_withdraw_label = Label(header_withdraw_frame,
                                    text="Withdraw",
                                    font=('Arial', 22, "bold"),
                                    bg="white",
                                    fg="#2c3e50")
        title_withdraw_label.pack(anchor="w")

        # Amount entry
        amount_withdraw_frame = Frame(main_withdraw_frame, bg="white")
        amount_withdraw_frame.pack(fill="x", pady=(0, 15))

        amount_withdraw_label = Label(amount_withdraw_frame,
                                     text="Amount to Withdraw",
                                     font=('Arial', 12),
                                     bg="white",
                                     fg="#7f8c8d")
        amount_withdraw_label.pack(anchor="w")

        # Currency symbol label
        input_frame = Frame(amount_withdraw_frame, bg="white")
        input_frame.pack(fill="x", pady=(5, 0))

        currency_label = Label(input_frame,
                               text="$",
                               font=('Arial', 14),
                               bg="white",
                               fg="#2c3e50")
        currency_label.pack(side="left", padx=(0, 5))
        amount_var = IntVar(value=0)
        amount_entry = Entry(input_frame,
                             font=('Arial', 14),
                             bd=2,
                             relief=SOLID,
                             highlightthickness=1,
                             highlightcolor="#3498db",
                             highlightbackground="#bdc3c7", textvariable=amount_var)
        amount_entry.pack(fill="x", expand=True, ipady=5)
        amount_entry.focus_set()

        # Status label
        status_frame = Frame(main_withdraw_frame, bg="white")
        status_frame.pack(fill="x", pady=(10, 0))

        status_withdraw_label = Label(status_frame,
                                     text="",
                                     font=('Arial', 12),
                                     bg="white",
                                     wraplength=300,
                                     justify="left")
        status_withdraw_label.pack(anchor="w")

        def withdraw_action():
            name = account_name
            account_type_variable = account_type
            try:
                amount = amount_var.get()
                user = bank.get_accounts_by_type(name, account_type_variable)
                user.balance += user.return_on_withdraw(amount)
                user.balance -= amount
                status_withdraw_label.config(text=f"Withdrawn - {amount:.2f}\nTotal Balance - {user.balance:.2f}", fg="green")
                withdraw_btn.config(state="disabled")
                balance_value.config(text=f"{user.balance:.2f}")
                deposit_btn.config(state="active")
                withdraw_btn_.config(state="active")
            except (ValueError, _tkinter.TclError):
                status_withdraw_label.config(text="Invalid input. Please try again.", fg="red")

        withdraw_btn = Button(main_withdraw_frame, text="Withdraw Funds",
                             font=('Arial', 14, "bold"),
                             fg='white',
                             bg="#3498db",
                             relief=FLAT,
                             bd=0,
                             padx=20,
                             pady=12,
                             activebackground=f"dark blue",
                             activeforeground="white",
                             command=withdraw_action)
        withdraw_btn.pack(fill="x", pady=8, ipady=5)

    withdraw_btn_ = Button(buttons_frame,text="Withdraw Funds",
                         font=('Arial', 14, "bold"),
                         fg='white',
                         bg="#3498db",
                         relief=FLAT,
                         bd=0,
                         padx=20,
                         pady=12,
                         activebackground=f"dark blue",
                         activeforeground="white",
                         command=withdraw)
    withdraw_btn_.pack(fill="x", pady=8, ipady=5)
    

# main(start window)
def main_window():
    start_window = Tk()
    start_window.title("Sign in")
    center_window(start_window, 500, 400)

    # background image set up
    start_window.bg_photo = PhotoImage(file="img.png")
    bg_label = Label(start_window, image=start_window.bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # information board
    info_label = Label(
        start_window,
        text="Contact: jayalexanderpopchev@gmail.com\ngithub.com/JayPopchev",
        font=('Arial', 10),
        fg='white',
        bg='black',
        padx=10,
        pady=5,
        relief=RAISED,
        bd=3
    )
    info_label.place(relx=0.02, rely=0.02, anchor="nw")  # Top-left

    # real time clock
    clock_label = Label(
        start_window,
        font=('Arial', 14, 'bold'),
        fg='white',
        bg='black',
        padx=10,
        pady=5
    )
    clock_label.place(relx=0.5, rely=0.02, anchor="n")  # Top-center
    update_clock(clock_label)  # Start the clock

    # version label(waiting to learn SQL for bigger usage)
    version_label = Label(
        start_window,
        text="App v1.0.0",
        font=('Arial', 10),
        fg='white',
        bg='black',
        padx=10,
        pady=5,
        relief=RAISED,
        bd=3
    )
    version_label.place(relx=0.98, rely=0.02, anchor="ne")  # Top-right

    # welcome label
    welcome_label = Label(
        start_window,
        text="Welcome",
        font=('Arial', 40, "bold"),
        fg='white',
        bg="black",
        relief=RAISED,
        bd=10,
        padx=20,
        pady=10
    )
    welcome_label.pack(pady=50)

    # creating button from for sign in and register options
    button_frame = Frame(start_window, bg="black")
    button_frame.pack()

    # sign in button that redirects to sign in window
    sign_in_button = Button(
        button_frame,
        text="Sign in",
        fg='white',
        bg='black',
        relief=RAISED,
        activeforeground='white',
        activebackground='black',
        padx=40,
        pady=10,
        cursor='hand2',
        command=sign_in
    )
    sign_in_button.pack(side="left", padx=10, pady=10)  # side=LEFT for horizontal placement

    # register button that redirects to register window
    register_button = Button(
        button_frame,
        text="Register",
        fg='white',
        bg='black',
        relief=RAISED,
        activeforeground='white',
        activebackground='black',
        padx=40,
        pady=10,
        cursor='hand2',
        command=register
    )
    register_button.pack(side="left", padx=10, pady=10)

    start_window.mainloop()

main_window()