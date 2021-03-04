#frontend
from tkinter import *
import tkinter.messagebox
from tkinter import ttk 
import canteen_backend_2

color1="SkyBlue1"
color2="ghost white"

options=["NONE",
         "CHINESE DOSA","RAWA MASALA DOSA","CHOPSUEY DOSA","SADA DOSA",
         "VEG FRANKIE","PANEER FRANKIE","CHEESE FRANKIE","SCHEZWAN FRANKIE",
         "CHEESE SANDWICH","CHEESE CHILLI TOAST","VEG CLUB SANDWICH","GRILLED SANDWICH",
         "BHEL PURI","SEV PURI","DAHI PAPDI CHAAT","SAMOSA BHEL","RAGDA PURI",
         "PAV BHAJI","TAWA PULAO","MATAR PULAO","PANEER TIKKA BIRYANI",
         "PANEER TIKKA MASALA","PANEER SHAHI KORMA","PANEER TADKA",
         "PANEER GARLIC","VEG CRISPY","MANCHURIAN DRY","BUTTER NAAN","GARLIC NAAN","ROTI",
         "METHI PARATHA","PANEER PARATHA","ALOO PARATHA",
         "FRUIT SALAD","KHICHIYAMASALA PAPAD","BANANA MILKSHAKE","CHIKOO MILKSHAKE",
         "OREO SHAKE","LASSI","BUTTER MILK",
         "ORANGE JUICE","FRESH LIME JUICE","PINEAPPLE JUICE","TEA","COFFEE"]
        
itemlist=dict.fromkeys(options,0)
#print(itemlist)
class Student:
    
    def __init__(self,root):
        self.root=root
        self.root.title("Canteen ")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg=color1)
        SAPID=StringVar()
        username=StringVar()
        stream=StringVar()
        course=StringVar()
        year=StringVar()
        password=StringVar()
        mobile=StringVar()
        address=StringVar()
        #functions
        def iExit():
            iExit=tkinter.messagebox.askyesno("Canteen","Confrim if you want to exit")
            if iExit>0:
                root.destroy()
            return

        def clearData():
            self.txtSAPID.delete(0,END)
            self.txtuser.delete(0,END)
            self.txtstream.delete(0,END)
            self.txtyear.delete(0,END)
            #self.txtpass.delete(0,END)

        def addData():
            if(len(SAPID.get())!=0):
                countt=0
                for i in itemlist.keys():
                    if i ==password.get():
                        itemlist[i]+=1
                        countt=itemlist[i]
                canteen_backend_2.addStdRec(SAPID.get(),username.get(),stream.get(),year.get(),password.get(),countt)
                studentlist.delete(0,END)
                studentlist.insert(END,(SAPID.get(),username.get(),stream.get(),year.get(),password.get()))
                for i in itemlist.keys():
                    if i ==password.get():
                        itemlist[i]+=1
                        
            #    print(itemlist)
             
        def DisplayData():
            studentlist.delete(0,END)
            for row in canteen_backend_2.viewData():
                studentlist.insert(END,row,str(""))

        def StudentRec(event):
            global sd
            searchStd=studentlist.curselection()[0]
            sd=studentlist.get(searchStd)

            self.txtSAPID.delete(0,END)
            self.txtSAPID.insert(END,sd[1])
            self.txtuser.delete(0,END)
            self.txtuser.insert(END,sd[2])
            self.txtstream.delete(0,END)
            self.txtstream.insert(END,sd[3])
            self.txtyear.delete(0,END)
            self.txtyear.insert(END,sd[4])
            
        def DeleteData():
            if(len(SAPID.get())!=0):
                canteen_backend_2.deleteRec(sd[0])
                clearData()
                DisplayData()

        def searchDatabase():
            studentlist.delete(0,END)
            for row in canteen_backend_2.searchData(SAPID.get()):
                studentlist.insert(END,row,str(""))

        



       
        

        #frames
        
        
        
        MainFrame=Frame(self.root,bg=color1)
        MainFrame.grid()

        TitFrame=Frame(MainFrame,bd=2,padx=54,pady=8,bg=color2,relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit=Label(TitFrame,font=('arial',40, 'bold'),text="CANTEEN",bg=color2)
        self.lblTit.grid()

        ButtonFrame=Frame(MainFrame,bd=2,width=1350,height=70,padx=18,pady=10,bg=color2,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame=Frame(MainFrame,bd=1,width=1300,height=70,padx=20,pady=20,bg=color1,relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT=LabelFrame(DataFrame,bd=1,width=1000,height=600,padx=20,bg=color2,relief=RIDGE,font=('arial',20, 'bold'),text="student info\n")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT=LabelFrame(DataFrame,bd=1,width=450,height=300,padx=31,pady=3,bg=color2,relief=RIDGE,font=('arial',20, 'bold'),text="ORDER LOGS:\n")
        DataFrameRIGHT.pack(side=RIGHT)


        #dropdownmenu
        
        password.set("NONE")
        combo=ttk.Combobox(DataFrameLEFT,values=options,width=15,textvariable=password)
        combo.grid(row=4,column=1,columnspan = 2, sticky = 'NSWE', padx = 5, pady = 5)
        
        
        #labels
        self.lblSAPID=Label(DataFrameLEFT,font=('arial',20, 'bold'),text="SAP ID:",padx=2,pady=2,bg=color2)
        self.lblSAPID.grid(row=0,column=0,sticky=W)
        self.txtSAPID=Entry(DataFrameLEFT,font=('arial',20, 'bold'),textvariable=SAPID,width=39)
        self.txtSAPID.grid(row=0,column=1)

        self.lbluser=Label(DataFrameLEFT,font=('arial',20, 'bold'),text="Username:",padx=2,pady=2,bg=color2)
        self.lbluser.grid(row=1,column=0,sticky=W)
        self.txtuser=Entry(DataFrameLEFT,font=('arial',20, 'bold'),textvariable=username,width=39)
        self.txtuser.grid(row=1,column=1)

        self.lblstream=Label(DataFrameLEFT,font=('arial',20, 'bold'),text="Stream:",padx=2,pady=2,bg=color2)
        self.lblstream.grid(row=2,column=0,sticky=W)
        self.txtstream=Entry(DataFrameLEFT,font=('arial',20, 'bold'),textvariable=stream,width=39)
        self.txtstream.grid(row=2,column=1)

        self.lblyear=Label(DataFrameLEFT,font=('arial',20, 'bold'),text="Year:",padx=2,pady=2,bg=color2)
        self.lblyear.grid(row=3,column=0,sticky=W)
        self.txtyear=Entry(DataFrameLEFT,font=('arial',20, 'bold'),textvariable=year,width=39)
        self.txtyear.grid(row=3,column=1)

        self.lblpass=Label(DataFrameLEFT,font=('arial',20, 'bold'),text="Your Order:",padx=2,pady=2,bg=color2)
        self.lblpass.grid(row=4,column=0,sticky=W)

        val=canteen_backend_2.findRecc()

        self.lblrecc=Label(DataFrameLEFT,font=('arial',20, 'bold'),text="Recomended Order:",padx=2,pady=2,bg=color2)
        self.lblrecc.grid(row=5,column=0)
        self.lblfind=Label(DataFrameLEFT,font=('arial',20, 'bold'),text=val,padx=2,pady=2,bg=color2)
        self.lblfind.grid(row=5,column=1)
        

        #scroll
        scrollbar=Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='NS')

        scrollbar1=Scrollbar(DataFrameRIGHT,orient='horizontal')
        scrollbar1.grid(row=1,column=0,sticky='WE')

        studentlist=Listbox(DataFrameRIGHT,width=41,height=16,font=('arial',12, 'bold'),yscrollcommand=scrollbar.set,xscrollcommand=scrollbar1.set)
        studentlist.bind('<<ListboxSelect>>',StudentRec)
        studentlist.grid(row=0,column=0,padx=8)
        scrollbar.config(command=studentlist.yview)
        scrollbar1.config(command=studentlist.xview)
        
        

        
        
        #Button
        self.btnAddData=Button(ButtonFrame,text="Add New",font=('arial',20, 'bold'),height=1,width=10,bd=4,command=addData)
        self.btnAddData.grid(row=0,column=0)

        self.btnDisplay=Button(ButtonFrame,text="Display",font=('arial',20, 'bold'),height=1,width=10,bd=4,command=DisplayData)
        self.btnDisplay.grid(row=0,column=1)

        self.btnClear=Button(ButtonFrame,text="Clear",font=('arial',20, 'bold'),height=1,width=10,bd=4,command=clearData)
        self.btnClear.grid(row=0,column=2)

        self.btnDelete=Button(ButtonFrame,text="Delete",font=('arial',20, 'bold'),height=1,width=10,bd=4,command=DeleteData)
        self.btnDelete.grid(row=0,column=3)

        self.btnSearch=Button(ButtonFrame,text="Search",font=('arial',20, 'bold'),height=1,width=10,bd=4,command=searchDatabase)
        self.btnSearch.grid(row=0,column=4)

        
        self.btnExit=Button(ButtonFrame,text="Exit",font=('arial',20, 'bold'),height=1,width=10,bd=4,command=iExit)
        self.btnExit.grid(row=0,column=6)

       
        
        

if __name__=="__main__":
    
    root=Tk()
    
    application=Student(root)
    root.mainloop()
