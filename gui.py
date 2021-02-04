from tkinter import *
from PIL import Image,ImageTk 
from tkinter import filedialog
import NLP
import readPdf 
import sendMail
import Autocopy

root = Tk()
root.title("Sentiment Analyser")
root.iconbitmap('icon.ico')
root.geometry('500x310')
root.resizable(False, False)



# canvas = Canvas(root,height=70,width=70,bg='#f0b71a')
# canvas.pack()

# frame 
frame = LabelFrame(root,padx=50,pady=50,bd=3,relief='solid')
frame.pack(padx=10,pady=10)




def mainPage(frame):
    # Name 
    labelName = Label(frame,text='Enter Your Name',foreground='#000000',font=('calibiri',10,'bold'))
    labelName.grid(row=0,column=0,stick=W)
    global EnterName
    EnterName = Entry(frame,width=50,border=2,font=('calibiri',10))
    EnterName.grid(row=1,column=0,columnspan=3,stick=W)

    EnterName.focus()

    # password
    labelPass = Label(frame,text='Password',foreground='#000000',font=('calibiri',10,'bold'))
    labelPass.grid(row=2,column=0,stick=W)
    global EnterPass 
    EnterPass = Entry(frame,show='*',width=50,border=2,font=('calibiri',10))
    EnterPass.grid(row=3,column=0,columnspan=3,stick=W)


    btnLogin = Button(frame, text='Get IN', padx=40,pady=10,background='#423f3e',foreground='#ffffff',relief='solid',bd=0.7,command=lambda: login(frame) )
    btnLogin.grid(row=5,column=2,pady=7,sticky=E)

    #exit button to quit.
    btnExit = Button(frame,text='Exit Analyser',command=root.quit)
    btnExit.grid(row=6,column=2,sticky=E,pady=40,columnspan=2)
    


# login function 
def login(frame):
    passw = EnterPass.get()
    if passw == "123chris":
        frame.forget()
        secondPage()
    else:
        EnterPass.delete(0,"end") 

# Menu 3. opens the text file section.....
def OpenTextFile(f):
    f.forget()

    frame = LabelFrame(root,padx=90,pady=130,bd=3,relief='solid')
    frame.pack(padx=10,pady=10)

    labelWhichFile = Label(frame,text='Which file you want to upload...?',font=('calibiri',15,'bold','underline'))
    labelWhichFile.grid(row=0,column=0,columnspan= 3)

    t= StringVar()
    t.set("txt")
    
    def clicked(value):
        global v
        v = value
        

    Radiobutton(frame,text='Text File',variable=t,value="txt",font=('calibiri',10,'bold'),command= lambda: clicked(t.get())).grid(row=1,column=0 ,pady=20)
    Radiobutton(frame,text='Doc File',variable=t,value="docx",font=('calibiri',10,'bold'),command= lambda: clicked(t.get())).grid(row=1,column=1)
    Radiobutton(frame,text='PDF File',variable=t,value="pdf",borderwidth=5,font=('calibiri',10,'bold'),command= lambda : clicked(t.get())).grid(row=1,column=2)

    lblrecommend = Label(frame,text='***Use txt and Doc files majorly***',font=(7),fg='Red').grid(row=2,column=0,columnspan=3)
    
    
    def open(val):
        
        frame.filename = filedialog.askopenfilename(initialdir="",title='Select a file',filetypes=((val+" Files", "*."+val), ("All Files", "*.*")))
        #reading pdf and extracting text
        if val == 'pdf':
            NLP.extractedText(readPdf.pdftoText(frame.filename))
            btnOpenImage.configure(bg='green',state ='normal')
        
        #reading doc file and extracting text
        if val == 'docx':
            NLP.extractedText(readPdf.doctoText(frame.filename)) 
            btnOpenImage.configure(bg='green',state ='normal')                

        # print(frame.filename)
        if  val == 'txt':
            NLP.nameF(frame.filename)
            btnOpenImage.configure(bg='green',state ='normal')
    
    btnOpenFile = Button(frame,padx=100,pady=10,background='#423f3e',foreground='#ffffff',text='Select a file',command=lambda: open(v)).grid(row=3,column=0,columnspan=3)
    
    btnOpenImage = Button(frame,padx=90,pady=10,text='Open the Graph',command=lambda: openImage(frame),state='disabled')
    btnOpenImage.grid(row=4,column=0,columnspan=3,pady=10)
    
    def backpage(f):
        f.destroy()
        secondPage()
    
    btnBack = Button(frame,text='<-Back',command=lambda: backpage(frame)).grid(row=5,column=3,pady=30,sticky=E)

# menu Open copy paste

def OpenAutocopy(f):
    f.forget()
    root.geometry('530x460')
    frame = LabelFrame(root,padx=90,pady=130,bd=3,relief='solid')
    frame.pack(padx=5,pady=5)

    labelAutoCopy = Label(frame,text='AutoCopy Module',font=('calibiri',15,'bold','underline'))
    labelAutoCopy.grid(row=0,column=0,columnspan=3)

    labelFileName = Label(frame,text='Enter the file Name in which you want to copy?',font=('calibiri',9,'bold')).grid(row=1,column=0, pady=10,stick=W)
    EnterFileName = Entry(frame,width=50,border=2)
    EnterFileName.grid(row=2,column=0,pady=2,stick=W)

    labeltime = Label(frame,text='Enter the time in Seconds you want to copy',font=('calibiri',9,'bold')).grid(row=3,column=0, pady=10,stick=W)
    Entertime = Entry(frame,width=10,border=2)
    Entertime.grid(row=4,column=0,pady=2,stick=W)

    def copy(): # to start the copy module
        file = EnterFileName.get()
        time = int(Entertime.get())
        Autocopy.copypaste(file,time)


    btnStart = Button(frame,padx=100,pady=10,background='#423f3e',foreground='#ffffff',text='Start Module',command=copy).grid(row=5,column=0,pady=9,stick=EW)
    
    

    def backpage(f):
        f.destroy()
        secondPage()
    btnBack = Button(frame,text='<-Back',command=lambda: backpage(frame)).grid(row=6,column=3,pady=30,sticky=E)





# This button opens the Analysed Image...
def openImage(f):
    global analysedImage
    f.forget()
    root.geometry('530x550')
    imgFrame = Label(root,bd=3,relief='solid')
    imgFrame.pack()
    analysedImage = ImageTk.PhotoImage(Image.open('C:\\Users\\shrestha\\Desktop\\sentiment proj\\AnalysedImage.png'))
    labelImage = Label(imgFrame,image=analysedImage).pack()

    frame2 = LabelFrame(root).pack()
    labelEmail = Label(frame2,text='Get this graph to your E-mail',font=('calibiri',9,'bold')).pack(anchor=NW,pady=5)
    global askForEmail
    frame3 = LabelFrame(root).pack(fill = X)
    askForEmail = Entry(frame3,width=50,border=2,font=('calibiri',10),relief='solid')
    askForEmail.insert("0",'enter your E-mail Address...')    
    def clear_Placeholder(e):
        askForEmail.delete("0","end")
    askForEmail.bind("<FocusIn>",clear_Placeholder)     
    askForEmail.pack(padx=5,side=LEFT)

    btnSend = Button(frame3,width = 10, text='Send',background='#423f3e',foreground='#ffffff',command=lambda: Mail(askForEmail.get()))
    btnSend.pack(padx=5,fill= X)
    
    def Mail(emailID):
        sendMail.send(emailID)


def secondPage():

    root.geometry('530x450')
    global Secondframe
    Secondframe = LabelFrame(root,padx=50,pady=50,bd=3,relief='solid')
    Secondframe.pack(padx=10,pady=10)

    # intro label
    intro = 'WELCOME TO ANALYSE THE SENTIMENTS'
    labelIntro = Label(Secondframe,text=intro,font=('calibiri',15,'bold','underline'))
    labelIntro.grid(row=0,column=0,sticky=W+E)

    # greeting the user
    labelHello = Label(Secondframe,text='Hello '+EnterName.get()+' What you want to anayse?',font=('calibiri',10,'bold'))
    labelHello.grid(row=1,column=0,pady=10)

    # tweeter Button 
    btnTweet = Button(Secondframe,text='Analyse Tweets',padx=50,pady=10,relief='solid')
    btnTweet.grid(row =2,columnspan=3,pady=10)

    # Copy and Paste module
    btnCopyPaste = Button(Secondframe,text='Copy n Paste',padx=50,pady=10,relief='solid',command=lambda: OpenAutocopy(Secondframe))
    btnCopyPaste.grid(row =3,columnspan=3,pady=10)

    # Analyse Text , Doc and Pdf
    btnDoc = Button(Secondframe,text='Doc Pdf Text',padx=50,pady=10,relief='solid',command=lambda: OpenTextFile(Secondframe))
    btnDoc.grid(row =4,columnspan=3,pady=10)

    # record Audio 
    btnRecord = Button(Secondframe,text='Record Audio',padx=50,pady=10,relief='solid')
    btnRecord.grid(row =5,columnspan=3,pady=10)
    
    # exit 
    btnExit = Button(Secondframe,text='Log Out',command=lambda: logout(Secondframe))
    btnExit.grid(row=6,column=0,sticky=E)

def logout(f):
    f.destroy()
    f = LabelFrame(root,padx=50,pady=50,bd=3,relief='solid')
    f.pack(padx=10,pady=10)
    root.geometry('500x310')
    mainPage(f)


mainPage(frame)
root.mainloop()



