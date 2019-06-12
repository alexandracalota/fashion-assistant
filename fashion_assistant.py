import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("1000x500")
        self.master.resizable(0, 0)
        self.create_widgets()
        self.current_username = None

    def create_widgets(self):
        self.toolbar = tk.Frame(self.master, bg='orange', relief='raised')

        self.loginBtn = tk.Button(self.toolbar, text='Log In', bg='blue', fg='white',\
            command=self.login, padx=2, pady=2)
        self.registerBtn = tk.Button(self.toolbar, text='Register', bg='purple', \
            fg='white', command=self.register, padx=2, pady=2)

        self.registerBtn.pack(side=tk.RIGHT)
        self.loginBtn.pack(side=tk.RIGHT)

        self.toolbar.pack(side=tk.TOP, fill=tk.X)

    def login(self):
        print('Login')
        self.loginBtn.pack_forget()
        self.registerBtn.pack_forget()

        self.loginFrame = tk.Frame(self.master, bg='grey2', relief='raised')

        username = tk.StringVar()
        password = tk.StringVar()

        label_username = tk.Label(self.loginFrame, text='Username')
        label_password = tk.Label(self.loginFrame, text='Password')

        entry_username = tk.Entry(self.loginFrame, textvariable=username)
        entry_password = tk.Entry(self.loginFrame, textvariable=password)

        label_username.pack(side=tk.TOP, pady=(10, 10))
        entry_username.pack(side=tk.TOP)
        label_password.pack(side=tk.TOP, pady=(10, 10))
        entry_password.pack(side=tk.TOP)

        submit = tk.Button(self.loginFrame, text='Log In', bg='blue', fg='white', command=self.loggedin)
        submit.pack(side=tk.BOTTOM, pady=(10, 10))

        self.loginFrame.pack(pady=(100, 100))

    def loggedin(self):
        print('Checking username')

    def register(self):
        print('Register')
        # self.loginBtn.pack_forget()
        # self.registerBtn.pack_forget()

        # username = tk.StringVar()
        # password = tk.StringVar()
        # age = tk.IntVar()
        # height = tk.IntVar()

        # label_username = tk.Label(self.master, text='Username')
        # label_password = tk.Label(self.master, text='Password')
        # label_age = tk.Label(self.master, text='Age')
        # label_height = tk.Label(self.master, text='Height')

        # entry_username = tk.Entry(self.master, textvariable=username)
        # entry_password = tk.Entry(self.master, textvariable=password)
        # entry_age = tk.Entry(self.master, textvariable=age)
        # entry_height = tk.Entry(self.master, textvariable=height)

        # label_username.pack(side=tk.TOP); entry_username.pack(side=tk.TOP)
        # label_password.pack(side=tk.TOP); entry_password.pack(side=tk.TOP)
        # label_age.pack(side=tk.TOP); entry_age.pack(side=tk.TOP)
        # label_height.pack(side=tk.TOP); entry_height.pack(side=tk.TOP)

        # submit = tk.Button(self.master, text='Register', bg='blue', fg='white', command=self.loggedin)
        # submit.pack()

if __name__ == '__main__':

    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
