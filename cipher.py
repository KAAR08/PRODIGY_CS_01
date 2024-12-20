import tkinter as tk
from customtkinter import *
from CTkMessagebox import CTkMessagebox
from PIL import Image


#App properties

app = CTk()
app.geometry("1000x768")
app.resizable(0,0)
app.title("EncDec")


#Images used in the App
 
header_img_data = Image.open("static/hder.jpg")
side_img_data = Image.open("static/bg2.jpg")
message_data = Image.open("static/th (1).jpeg")
enc_image = Image.open("static/lo1.png")
dec_image = Image.open("static/dec.png")


header_img = CTkImage(dark_image=header_img_data, light_image=header_img_data, size=(1000,84))
side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(500, 684))
message_icon = CTkImage(dark_image=message_data, light_image=message_data, size=(35,35))
enc_icon = CTkImage(dark_image=enc_image, light_image=enc_image, size=(17,17))
dec_icon = CTkImage(dark_image=dec_image, light_image=dec_image, size=(17,17))



#Header
CTkLabel(master=app, text="Aziizkaar@Prodigy", font=("Arial Bold", 24), text_color="#ffffff", justify="right", image=header_img).pack()
CTkLabel(master=app, text="",  image=side_img).pack(expand=True, side="left")


#main frame
frame = CTkFrame(master=app, width=500, height=684, fg_color="#ffffff")
frame.pack_propagate(0)
frame.pack(expand=True, side="right")

CTkLabel(master=frame, text="EncDec App", text_color="#000000",  justify="center", font=("Arial Bold", 24)).pack( pady=(50, 15), padx=(25, 0))
CTkLabel(master=frame, text="Encrypt and decrypt text messages effortlessly.\nThe Caesar cipher, a classic encryption technique, \nat your fingertips.", text_color="#5E5E5E",  justify="center", font=("Arial Bold", 16)).pack(padx=(25, 0))

#Shift frame
shift_frame = CTkFrame(master=frame, width=250, height=20, fg_color="#ffffff")
shift_frame.pack(pady=(5,5))
shift_label = CTkLabel(master=shift_frame, text="Shift", text_color="blue", justify="left", anchor="w", font=("Arial Bold", 16, "italic")).pack( padx=(5, 2), anchor="w")
shift_entry = CTkEntry(master=shift_frame,width=30, height=20, fg_color="#EEEEEE", text_color="#000000")
shift_entry.pack(anchor="e", padx=(0, 0), pady=(0,8))

#Textbox
CTkLabel(master=frame, text="Enter the Message ", text_color="blue", anchor="center", justify="left", font=("Arial Bold", 16), image=message_icon, compound="right").pack(anchor="center", pady=(0, 0), padx=(25, 0))
message_entry = CTkTextbox(master=frame, width=400, height=100, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
message_entry.pack(anchor="center", padx=(0, 25))



#Functions to call
def encrypt():
    encrypted_message =""
    actual_message = str(message_entry.get("1.0", "end-1c")) #Gets value entered the text box.
    
    #Tries to convert shift value from shift entry to int, raises exception if not possible.
    try:
        shift_string = shift_entry.get()
        shift = int(shift_string)
        
    except Exception as e:
        err = CTkMessagebox(title="Error", 
                        message="Invalid shift input!", 
                        icon="cancel", 
                        option_1="Retry", 
                        option_2="Cancel")
        
        if err.get()=="Retry":
            shift_entry.delete(0, tk.END)
    
    #Checks if the text box for message entry is empty and value entered as shift      
    if  actual_message != "":
        if shift > 0 and shift <= 10:
            
            CTkMessagebox(title="Success", message="Encryption successful!", 
                  icon="check", 
                  option_1="OK")
            message_title.configure(text="Encrypted Message")
            
            #Iterates through the characters in the message, and checks the alpha for shifting, not alpha, value is taken the way it is.
            for character in actual_message:
                if not character.isalpha():
                    encrypted_message += character
                else:
                   character_code = ord(character)
                   ciphered_character = chr(character_code + shift)
                   encrypted_message += ciphered_character
            message_body.configure(text=encrypted_message)            
            
            
        #Message that notifies the valid input as shift pops
        else:
            CTkMessagebox(title="Information", 
                  message="Number of shifts should neither be negative nor exceed 10.")
            shift_entry.delete(0, tk.END)

    else:
        CTkMessagebox(title="Warning", 
                        message="Message can't be empty", 
                        icon="warning", 
                        option_1="Retry")
        message_title.configure(text=" ")
        message_body.configure(text=" ")

           
        
            
    
    

     


def decrypt():
    decrypted_message =""
    actual_message = str(message_entry.get("1.0", "end-1c"))
    
    try:
        shift_string = shift_entry.get()
        shift = int(shift_string)
        
    except Exception as e:
        err = CTkMessagebox(title="Error", 
                        message="Invalid shift input!", 
                        icon="cancel", 
                        option_1="Retry", 
                        option_2="Cancel")
        
        if err.get()=="Retry":
            shift_entry.delete(0, tk.END)
            
    if  actual_message != "":
        if shift > 0 and shift <= 10:
            
            CTkMessagebox( title="Success", message="Decryption successful!", 
                  icon="check", 
                  option_1="OK")
            message_title.configure(text="Decrypted Message")
            
            for character in actual_message:
                if not character.isalpha():
                    decrypted_message += character
                else:
                   character_code = ord(character)
                   deciphered_character = chr(character_code - shift)
                   decrypted_message += deciphered_character
                   
            message_body.configure(text=decrypted_message)            
            
            

        else:
            CTkMessagebox(title="Information", 
                  message="Number of shifts should neither be negative nor exceed 10.")
            shift_entry.delete(0, tk.END)

    else:
        CTkMessagebox(title="Warning", 
                        message="Message can't be empty", 
                        icon="warning", 
                        option_1="Retry")
        message_title.configure(text=" ")
        message_body.configure(text=" ")



#Buttons frame
button_frame = CTkFrame(master=frame, width=500, height=50)

#Encryption button and its properties
CTkButton(master=frame, text="Encrypt", fg_color="#E44982", hover_color="#C73267", font=("Arial Bold", 13), text_color="#ffffff", width=150, image=enc_icon, compound="right", command=encrypt).pack(anchor="center", pady=(10, 7), padx=(0, 0))
CTkLabel(master=frame, text="---------------or--------------", font=("Arial", 12), text_color="blue", anchor="center").pack(anchor="center")

#Decryption button and its properties
CTkButton(master=frame, text="Decrypt", font=("Arial Bold", 13), text_color="#ffffff", width=150, image=dec_icon, compound="right", command=decrypt).pack(anchor="center", pady=(10, 0), padx=(0, 0),)

# Final message appears here
message_title = CTkLabel(master=frame, text=" ", text_color="#000000",  justify="center", font=("Arial Bold", 22))
message_title.pack(anchor="center", pady=(20,5))

message_body = CTkLabel(master=frame, text=" ", text_color="black", justify="left", font=("Arial", 15), wraplength=400)
message_body.pack()


app.mainloop()