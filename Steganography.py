from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import filedialog
import cv2
import math


class DashBoard:
    def __init__(self):
        self.wn = Tk()
        self.wn.attributes("-fullscreen", True)
        self.wn['bg'] = '#FFF8DC'
        self.message = StringVar()

        self.image_display_size = 1000, 1000

        # =============== FRAME AND LABEL AND ENTRY ========================
        self.Frame = Frame(self.wn, bg='black', width=2530, height=1400, bd=10)
        self.Frame.place(x=15, y=10)

        self.EncryptionFrame = Frame(self.Frame, bg='white', width=1265, height=1380)
        self.EncryptionFrame.place(x=0, y=0)

        self.DecryptionFrame = Frame(self.Frame, bg='white', width=1238, height=1380)
        self.DecryptionFrame.place(x=1270, y=0)

        self.lbl_encode = Label(self.EncryptionFrame, text='Encode', font=('arial2', 20, 'bold'), bg='white')
        self.lbl_encode.place(x=550, y=10)

        self.lbl_decode = Label(self.DecryptionFrame, text='Decode', font=('arial2', 20, 'bold'), bg='white')
        self.lbl_decode.place(x=550, y=10)

        self.lbl_encode_key = Label(self.EncryptionFrame, text='Key', font=('arial2', 13, 'bold'), bg='white')
        self.lbl_encode_key.place(x=40, y=805)

        self.ent_encode_key = Entry(self.EncryptionFrame, font=('arial2', 13, 'bold'), bg='white', bd=2)
        self.ent_encode_key.place(x=80, y=805)

        self.lbl_decode_key = Label(self.DecryptionFrame, text='Key', font=('arial2', 13, 'bold'), bg='white')
        self.lbl_decode_key.place(x=40, y=600)

        self.ent_decode_key = Entry(self.DecryptionFrame, font=('arial2', 13, 'bold'), bg='white', bd=2)
        self.ent_decode_key.place(x=80, y=600)

        # self.Photo_Frame = Frame(self.EncryptionFrame, bg='orange', width=1180, bd=0)
        # self.Photo_Frame.place(x=40, y=80, height=400)
        # =================== ENCODE =======================
        self.Encode_Photo_Frame = LabelFrame(self.EncryptionFrame, bg='white', width=800, bd=10)
        self.Encode_Photo_Frame.place(x=190, y=80, height=500)

        self.Encode_Stego_Frame = LabelFrame(self.EncryptionFrame, bg='white', width=800, bd=10)
        self.Encode_Stego_Frame.place(x=190, y=855, height=500)

        self.ent_encode_msg = Text(self.EncryptionFrame, width=140, bd=20)
        self.ent_encode_msg.place(x=50, y=600, height=200)

        self.on_click_button = Button(self.EncryptionFrame, text="Click Here to add Image", bg='white', fg='black',
                                      font=('bell mt', 10, 'bold'), bd=0, command=self.encode_image)
        self.on_click_button.place(x=40, y=52)

        self.encode_button = Button(self.EncryptionFrame, text="Encode", bg='white', fg='black', bd=3,
                                      font=('bell mt', 8, 'bold'), command=self.encrypt_data_into_image)
        self.encode_button.place(x=270, y=805)

        self.decode_button = Button(self.DecryptionFrame, text="Decode", bg='white', fg='black', bd=3,
                                    font=('bell mt', 8, 'bold'), command=self.decrypt)
        self.decode_button.place(x=270, y=600)

        self.encode_clear_button = Button(self.EncryptionFrame, text="Clear", bg='white', fg='black', bd=1,
                                    font=('bell mt', 10, 'bold'), command=self.clear_btn)
        self.encode_clear_button.place(x=320, y=805)

        # =================== DECODE =======================
        self.Decode_Stego_Frame = LabelFrame(self.DecryptionFrame, bg='white', width=800, bd=10)
        self.Decode_Stego_Frame.place(x=190, y=80, height=500)

        self.Decode_Photo_Frame = LabelFrame(self.DecryptionFrame, bg='white', width=800, bd=10)
        self.Decode_Photo_Frame.place(x=190, y=855, height=500)

        self.ent_encode_msg = Text(self.EncryptionFrame, width=140, bd=20)
        self.ent_encode_msg.place(x=50, y=600, height=200)

        self.decode_frame_msg = LabelFrame(self.DecryptionFrame, text='Secret Message', bg='white',
                                           font=('arial', 10, 'bold'), bd=10, width=1150)
        self.decode_frame_msg.place(x=40, y=650, height=200)

        self.decode_on_click_button = Button(self.DecryptionFrame, text="Click Here to add Stego Image", bg='white',
                                             fg='black', font=('bell mt', 10, 'bold'), bd=0, command=self.decode_image)
        self.decode_on_click_button.place(x=40, y=52)

        self.show_menu()
        self.wn.mainloop()

    # =============== Methods =====================

    def show_menu(self):
        my_menu = Menu(self.wn)
        self.wn.config(menu=my_menu)
        management_menu = Menu(my_menu, tearoff=False)
        my_menu.add_cascade(label="Management", menu=management_menu)

        management_menu.add_cascade(label="User")
        management_menu.add_cascade(label="Store")

        account_menu = Menu(my_menu, tearoff=False)
        my_menu.add_cascade(label="Account", menu=account_menu)

        account_menu.add_cascade(label="Switch Account")
        account_menu.add_cascade(label="Account Details")
        account_menu.add_separator()
        account_menu.add_cascade(label="Logout")

        help_menu = Menu(my_menu, tearoff=False)
        my_menu.add_cascade(label="Help", menu=help_menu)

        exit_menu = Menu(my_menu, tearoff=False)
        my_menu.add_cascade(label="Exit", menu=exit_menu)
        exit_menu.add_cascade(label="Exit", command=self.exit_btn)

    def encode_image(self):
        self.Encode_Photo_Frame.destroy()
        self.Encode_Photo_Frame = LabelFrame(self.EncryptionFrame, bg='white', width=800, bd=10)
        self.Encode_Photo_Frame.place(x=190, y=80, height=500)
        self.path_image = filedialog.askopenfilename()
        try:
            self.load_image = Image.open(self.path_image)
            self.load_image.thumbnail(self.image_display_size, Image.ANTIALIAS)
            self.render = ImageTk.PhotoImage(self.load_image)
            img = Label(self.Encode_Photo_Frame, image=self.render)
            img.image = self.render
            img.place(x=0, y=0)
        except:
            pass

    def decode_image(self):
        self.Decode_Stego_Frame.destroy()
        self.Decode_Stego_Frame = LabelFrame(self.DecryptionFrame, bg='white', width=800, bd=10)
        self.Decode_Stego_Frame.place(x=190, y=80, height=500)
        self.decode_path_image = filedialog.askopenfilename()
        try:
            self.load_image = Image.open(self.decode_path_image)
            self.load_image.thumbnail(self.image_display_size, Image.ANTIALIAS)
            self.render = ImageTk.PhotoImage(self.load_image)
            img = Label(self.Decode_Stego_Frame, image=self.render)
            img.image = self.render
            img.place(x=0, y=0)
        except:
            pass

    def encrypt_data_into_image(self):
        # try:
            data = self.ent_encode_msg.get(1.0, "end-1c")
            # load the image
            img = cv2.imread(self.path_image)
            # break the image into its character level. Represent the characyers in ASCII.
            data = [format(ord(i), '08b') for i in data]
            _, width, _ = img.shape
            # algorithm to encode the image
            PixReq = len(data) * 3
            RowReq = PixReq / width
            RowReq = math.ceil(RowReq)
            count = 0
            charCount = 0
            # Step 3
            for i in range(RowReq + 1):
                # Step 4
                while (count < width and charCount < len(data)):
                    char = data[charCount]
                    charCount += 1
                    # Step 5
                    for index_k, k in enumerate(char):
                        if ((k == '1' and img[i][count][index_k % 3] % 2 == 0) or (
                                k == '0' and img[i][count][index_k % 3] % 2 == 1)):
                            img[i][count][index_k % 3] -= 1
                        if (index_k % 3 == 2):
                            count += 1
                        if (index_k == 7):
                            if (charCount * 3 < PixReq and img[i][count][2] % 2 == 1):
                                img[i][count][2] -= 1
                            if (charCount * 3 >= PixReq and img[i][count][2] % 2 == 0):
                                img[i][count][2] -= 1
                            count += 1
                count = 0
            cv2.imwrite("test1.png", img)
            # Display the success label.
            self.lbl_message = Label(self.EncryptionFrame, text='Steganography Successful',
                             font=('arial', 15, 'bold'), bg='white')
            self.lbl_message.place(x=450, y=805)

        # except:
        #     pass
        #     messagebox.showerror('Error', 'Give all the required field.')

    def decrypt(self):
        self.img = cv2.imread(self.decode_path_image)
        data = []
        stop = False
        for index_i, i in enumerate(self.img):
            i.tolist()
            for index_j, j in enumerate(i):
                if ((index_j) % 3 == 2):
                    # first pixel
                    data.append(bin(j[0])[-1])
                    # second pixel
                    data.append(bin(j[1])[-1])
                    # third pixel
                    if (bin(j[2])[-1] == '1'):
                        stop = True
                        break
                else:
                    # first pixel
                    data.append(bin(j[0])[-1])
                    # second pixel
                    data.append(bin(j[1])[-1])
                    # third pixel
                    data.append(bin(j[2])[-1])
            if (stop):
                break
        self.message = []
        # join all the bits to form letters (ASCII Representation)
        for i in range(int((len(data) + 1) / 8)):
            self.message.append(data[i * 8:(i * 8 + 8)])
        # join all the letters to form the message.
        self.message = [chr(int(''.join(i), 2)) for i in self.message]
        self.message = ''.join(self.message)
        self.message_label = Label(self.decode_frame_msg, text=self.message, bg='white',
                                   font=("arial", 20, 'bold'))
        self.message_label.place(x=0, y=0)
        self.result = Label(self.DecryptionFrame, text='Decode Successful.', font=('arial', 18, 'bold'), bg='white')
        self.result.place(x=350, y=600)

    def clear_btn(self):
        self.wn.destroy()
        DashBoard()

    def exit_btn(self):
        ask = messagebox.askyesno('Exit', 'Do you want to exit?')
        if ask == 1:
            exit()
        else:
            pass


DashBoard()
