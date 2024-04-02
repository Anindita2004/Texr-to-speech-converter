#libraries
import pyttsx3
import customtkinter as ctk

#initialization
root=ctk.CTk()
root.title("Text To Speech Project")
speaker=pyttsx3.init('sapi5')
font = ("consolas",20)
last_played=""


#config
root.configure(fg_color="#121212")#change this for background colour
root.geometry("500x500")#change this to change the window size
root.resizable(0,0)#change this to make the window resizable

#config
voices=speaker.getProperty('voices')
speaker.setProperty('voice',voices[1].id)#change voice
speaker.setProperty('rate',125)#change speed
#functions
def play():#play audio
    global textbox,errorlabel,speaker,last_played
    #read text
    text=textbox.get("0.0","end")
    text=text.strip()
    if text:
        #play
        speaker.say(text)
        speaker.runAndWait()
        last_played=text
    else:
        #if no text
        errorlabel.place(relx=0.5,rely=0.05,anchor=ctk.CENTER)
        root.after(1000,errorlabel.place_forget)

def save():#save audio
    global textbox,errorlabel,speaker
    
    #read text
    text=textbox.get("0.0","end")
    text=text.strip()
    if text:
        export_file_type = [('MP3', '*.mp3')]
        #exportfile location
        export_file = ctk.filedialog.asksaveasfile(filetypes=export_file_type,defaultextension=export_file_type).name
        if export_file:
            #save
            speaker.save_to_file(text,export_file)
            speaker.runAndWait()
    else:
        #if no text
        errorlabel.place(relx=0.5,rely=0.05,anchor=ctk.CENTER)
        root.after(1000,errorlabel.place_forget)

def playnew():
    global last_played
    text=textbox.get("0.0","end")
    text=text.strip()
    #save whole text
    temp=text
    #new text get
    text = text.replace(last_played, '', 1)
    if text:
        #play
        speaker.say(text)
        speaker.runAndWait()
        last_played=temp
    else:
        #if no text
        errorlabel.place(relx=0.5,rely=0.05,anchor=ctk.CENTER)
        root.after(1000,errorlabel.place_forget)
    

#gui
screenwidth=root.winfo_width()
screenheight=root.winfo_height()
textbox=ctk.CTkTextbox(master=root,
                       font=font,
                       width=screenwidth/1.4,
                       height=screenheight/1.6,
                       wrap="word")#this is not reactive
playbutton=ctk.CTkButton(root,
                        text="Play",
                        width=130,height=40,
                        fg_color="#018786",
                        font=font,
                        hover_color="#005958",
                        command=play)#button to play audio
savebutton=ctk.CTkButton(root,
                        text="Save",
                        width=130,height=40,
                        fg_color="#018786",
                        font=font,
                        hover_color="#005958",
                        command=save)#button to save audio
playnewbutton=ctk.CTkButton(root,
                      text="Play New",
                      width=130,height=40,
                      fg_color="#018786",
                      font=font,
                      hover_color="#005958",
                      command=playnew)
errorlabel=ctk.CTkLabel(root,
                        font=font,
                        bg_color="#ff0033",
                        text="Enter Text!"
                        )#if no text show error


#place
textbox.place(relx=0.5,rely=0.43,anchor=ctk.CENTER)#text box placement
playbutton.place(relx=0.19,rely=0.9,anchor=ctk.CENTER)#playbutton placement
savebutton.place(relx=0.5,rely=0.9,anchor=ctk.CENTER)#savebutton placement
playnewbutton.place(relx=0.81,rely=0.9,anchor=ctk.CENTER)#playnewbutton placement

root.mainloop()
speaker.stop()
