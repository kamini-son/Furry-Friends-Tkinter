# Imports all classes, functions, and constants from the tkinter library.
from tkinter import * 
# ttk - stylist interpreter
#  Imports themed widget classes from the ttk module of tkinter.
from tkinter import ttk 
# Imports classes for handling images from the Python Imaging Library (PIL). 
from PIL import Image,ImageTk
# used for generating random numbers and interacting with the operating system
import random,os
# class from the tkinter library, which is used to display various types of messages.
from tkinter import messagebox
#  module, which provides functions to create temporary files and directories.
import tempfile
# from the time module, which is used to format time strings.
from time import strftime
# variables for colors
col0="purple"
col1="white"

# main class encapsulates entire application
class Bill_App:
    # constructor method,tkinter root window
    def __init__(self,root):
        # instance variable
        self.root = root
        self.root.geometry("1525x800+0+0")
        # w,h,x,y
        self.root.title("Pet Care")

        # VARIABLES
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        # random- module, randint- function
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.c_pname=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()

        # Type of Pet
        self.Category=["Select Option","Cat","Dog"]
        # For Cat
        self.SubCatCat=["Cat Toys","Cat Food"]
        # Cat Toys
        self.CatToys=["Mouse","Stick","Scratchers"]
        self.price_Mouse=300
        self.price_Stick=200
        self.price_Scratcher=800
        # Cat Food
        self.CatFood=["Gravy","Biscuits","Tuna"]
        self.price_Gravy=500
        self.price_Biscuits=300
        self.price_Tuna=1000

        # For Dog
        self.SubCatDog=["Dog Toys","Dog Food"]
        # Dog Toys
        self.DogToys=["Puzzles","Ball","Bone"]
        self.price_Puzzle=500
        self.price_Ball=100
        self.price_Bone=300
        # Dog Food
        self.DogFood=["Dry Food","Chewy Food","Meat and Bone"]
        self.price_Dry=1000
        self.price_Chewy=1200
        self.price_Meat=1500

        # Header
        lbl_title= Label(self.root,text="Furry Friends!",font=("times new roman",30,"bold"),bg=col1,fg=col0)
        lbl_title.place(x=0,y=0,width=1530,height=45)

        #Creating frames for layout
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg=col1)
        Main_Frame.place(x=0,y=175,width=1530,height=6200)

        def time():
                string= strftime('%H:%M:%S %p')
                # method
                lbl.config(text = string)
                lbl.after(1000,time) #1000=1sec

        lbl = Label(lbl_title, font=('times new roman',16,'bold'),background="white",foreground=col0)
        lbl.place(x=0,y=0,width=120,height=45)
        time()

        # Images
        # Image-1
        # open() method from pil 
        img=Image.open("image/cat1.jpeg")
        img=img.resize((500,150),Image.LANCZOS)
        # converts the resized image (img) into a tkinter-compatible PhotoImage object
        self.photoimg=ImageTk.PhotoImage(img)
        
        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=45,width=500,height=130)

        # Image-2
        img1=Image.open("image/dog.jpeg")
        img1=img1.resize((500,150),Image.LANCZOS) 
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lbl_img1=Label(self.root,image=self.photoimg1)
        lbl_img1.place(x=500,y=45,width=500,height=130)

        # Image-3
        img2=Image.open("image/cat2.jpeg")
        img2=img2.resize((500,150),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lbl_img2=Label(self.root,image=self.photoimg2)
        lbl_img2.place(x=1000,y=45,width=500,height=130)

    # MAIN FRAME
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg=col1)
        Main_Frame.place(x=0,y=175,width=1530,height=620)
        
        # Customer LabelFrame
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg=col1,fg=col0)
        Cust_Frame.place(x=10,y=5,width=350,height=200)

        self.lbl_mob=Label(Cust_Frame,text="Mobile no.",font=("aria",12,"bold"),bg=col1,bd=4)
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phone,font=("arial",10,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)

        self.lblCustName=Label(Cust_Frame,font=('arial',12,'bold'),bg=col1,text="Customer Name",bd=4)
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("arial",10,'bold'),width=24)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblEmail=Label(Cust_Frame,font=('arial',12,'bold'),bg=col1,text='Email',bd=4)
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=('arial',10,'bold'),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        
        self.lblEmail=Label(Cust_Frame,font=('arial',12,'bold'),bg=col1,text='Pet Name',bd=4)
        self.lblEmail.grid(row=3,column=0,sticky=W,padx=5,pady=2)

        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_pname,font=('arial',10,'bold'),width=24)
        self.txtEmail.grid(row=3,column=1,sticky=W,padx=5,pady=2)

        # Product LabelFrame
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg=col1,fg=col0)
        Product_Frame.place(x=10,y=220,width=350,height=250)
           
        #Category, Type of Pet
        self.lblCategory=Label(Product_Frame,font=('arial',12,'bold'),bg=col1,text='Select Pet',bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,values=self.Category,font=('arial',10,'bold'),width=24,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

        #Subcategory, select toys or food
        self.lblSubCategory=Label(Product_Frame,font=('arial',12,'bold'),bg=col1,text="Category",bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.ComboSubCategory=ttk.Combobox(Product_Frame,values=[""],state="readonly",font=('arial',10,'bold'),width=24)
        self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)

        #Product Name
        self.lblproduct=Label(Product_Frame,font=('arial',12,'bold'),bg=col1,text="Product Name",bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.ComboProduct=ttk.Combobox(Product_Frame,textvariable=self.product,state="readonly",font=('arial',10,'bold'),width=24)
        self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)

        #Price
        self.lblPrice=Label(Product_Frame,font=('arial',12,'bold'),bg=col1,text="Price",bd=4)
        self.lblPrice.grid(row=3,column=0,sticky=W,padx=5,pady=2)

        self.ComboPrice=ttk.Combobox(Product_Frame,state="readonly",textvariable=self.prices,font=('arial',10,'bold'),width=24)
        self.ComboPrice.grid(row=3,column=1,sticky=W,padx=5,pady=2)

        #Qty
        self.lblQty=Label(Product_Frame,font=('arial',12,'bold'),bg=col1,text="Qty",bd=4)
        self.lblQty.grid(row=4,column=0,sticky=W,padx=5,pady=2)

        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=('arial',10,'bold'),width=26)
        self.ComboQty.grid(row=4,column=1,sticky=W,padx=5,pady=2)


        #Search
        Search_Frame=Frame(Main_Frame,bd=2,bg=col1)
        Search_Frame.place(x=380,y=15,width=500,height=40)

        self.lblBill=Label(Search_Frame,font=('arial',12,'bold'),bg=col0,fg=col1,text="Bill Number")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("arial",10,"bold"),width=24)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=('arial',10,'bold'),bg=col0,fg=col1,width=10,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)

        #Bill Area
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg=col1,fg=col0)
        RightLabelFrame.place(x=380,y=45,width=480,height=440)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg=col1,fg=col0,font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y) #the side where we want scrollbar and have to fill y axis
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        
        #Right Side Frame(image)
        RightFrame = Frame(Main_Frame,bd=5)
        RightFrame.place(x=875,y=10,width=650,height=500)

        #Image-4
        img_13=Image.open("image/dog1.jpeg")
        img_13=img_13.resize((650,500),Image.LANCZOS)
        self.photoimg_13=ImageTk.PhotoImage(img_13)

        lbl_img_13=Label(RightFrame,image=self.photoimg_13)
        lbl_img_13.place(x=10,y=0,width=650,height=500)

    # FOOTER
        #Bill Counter Labelframe
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill counter",font=("times new roman",12,"bold"),bg=col1,fg=col0)
        Bottom_Frame.place(x=0,y=485,width=1520,height=125)

        self.lblSubTotal= Label(Bottom_Frame,font=('arial',12,"bold"),bg=col1,text="Sub Total",bd=4)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.EntrySubTotal=ttk.Entry(Bottom_Frame,textvariable=self.total,font=('arial',10,"bold"),width=24)
        self.EntrySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)


        self.lbl_tax=Label(Bottom_Frame,font=('arial',12,"bold"),bg=col1,text="Gov Tax",bd=4)
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=('arial',10,"bold"),width=24)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblAmountTotal=Label(Bottom_Frame,font=("arial",12,"bold"),bg=col1,text="Total",bd=4)
        self.lblAmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtAmountTotal=ttk.Entry(Bottom_Frame,textvariable=self.total,font=('arial',10,"bold"),width=24)
        self.txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #Button Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg=col1)
        Btn_Frame.place(x=320,y=25)

        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add To Cart",font=("arial",13,"bold"),bg=col0,fg=col1,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.Btngenerate_bill=Button(Btn_Frame,height=2,command=self.gen_bill,text="Generate Bill",font=("arial",13,"bold"),bg=col0,fg=col1,width=15,cursor="hand2")
        self.Btngenerate_bill.grid(row=0,column=1)

        self.BtnSave=Button(Btn_Frame,height=2,command=self.save_bill,text="Save Bill",font=("arial",13,"bold"),bg=col0,fg=col1,width=15,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)

        self.BtnPrint=Button(Btn_Frame,height=2,command=self.iprint,text="Print",font=("arial",13,"bold"),bg=col0,fg=col1,width=15,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

        self.BtnClear=Button(Btn_Frame,height=2,command=self.clear,text="Clear",font=("arial",13,"bold"),bg=col0,fg=col1,width=15,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit =Button(Btn_Frame,height=2,command=self.root.destroy,text="Exit",font=("arial",13,"bold"),bg=col0,fg=col1,width=15,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)

        self.welcome()

        self.l=[]
    #FUNCTION DECLARATION
    def welcome(self):
        self.textarea.delete(1.0,END) #First we have to delete content
        self.textarea.insert(END,"\t\t Welcome to FURRY FRIENDS :)\n")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phone.get()}")
        self.textarea.insert(END,f"\n E-mail ID:{self.c_email.get()}")
        self.textarea.insert(END,f"\n Pet Name:{self.c_pname.get()}")


        self.textarea.insert(END,"\n==================================================")
        self.textarea.insert(END,f"\n PRODUCTS\t\t\tQTY\t\tPrice")
        self.textarea.insert(END,"\n==================================================\n")


    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n 
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please select the Product Name")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l))-(self.prices.get()))*Tax)/100)))))


    def gen_bill(self):
        if not self.l:
            messagebox.showerror("Error", "Please Add To Cart Product")
            return

        bill_text = ""
        bill_text += "\t\t Welcome to FURRY FRIENDS :)\n"
        bill_text += f"\n Bill Number: {self.bill_no.get()}"
        bill_text += f"\n Customer Name: {self.c_name.get()}"
        bill_text += f"\n Phone Number: {self.c_phone.get()}"
        bill_text += f"\n E-mail ID: {self.c_email.get()}"
        bill_text += f"\n Pet Name: {self.c_pname.get()}"
        bill_text += "\n=================================================="
        bill_text += "\n PRODUCTS\t\t\tQTY\t\tPrice"
        bill_text += "\n==================================================\n"

        for i in range(len(self.l)):
            bill_text += f"\n {self.product.get()}\t\t\t{self.qty.get()}\t\t{self.l[i]}"

        bill_text += "\n=================================================="
        bill_text += f"\n Sub Amount:\t\t\t{self.sub_total.get()}"
        bill_text += f"\n Tax Amount:\t\t\t{self.tax_input.get()}"
        bill_text += f"\n Total Amount:\t\t\t{self.total.get()}"
        bill_text += "\n=================================================="

        self.textarea.delete(1.0, END)
        self.textarea.insert(END, bill_text)

    def iprint(self):
        q=self.textarea.get(1.0,"end-1c") #to get all of the data in q
        filename=tempfile.mktemp('.txt') #the format txt ,html etc.
        open(filename,'w').write(q)
        os.startfile(filename,"print") #we will pass the filename



    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you Want to save the bill?")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open("Bills/"+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill no:{self.bill_no.get()} Saved Successfully")
            f1.close()        


    def find_bill(self):
        found="no"
        for i in os.listdir("Bills/"): #it will split from directory in file manager
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'Bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=='no':
            messagebox.showerror("Error","Invalid Bill Number.")

    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_email.set("")
        self.c_pname.set("")
        self.c_phone.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set('')
        self.welcome()





    def Categories(self,event=""):
        if self.Combo_Category.get()=="Cat":
            self.ComboSubCategory.config(values=self.SubCatCat)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Dog":
            self.ComboSubCategory.config(values=self.SubCatDog)
            self.ComboSubCategory.current(0)

    def Product_add(self,event=""):
        if self.ComboSubCategory.get()=="Cat Toys":
            self.ComboProduct.config(values=self.CatToys)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Cat Food":
            self.ComboProduct.config(values=self.CatFood)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Dog Toys":
            self.ComboProduct.config(values=self.DogToys)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Dog Food":
            self.ComboProduct.config(values=self.DogFood)
            self.ComboProduct.current(0)


    def price(self, event=""):
    # CatToys
        if self.ComboProduct.get() == "Mouse":
            self.prices.set(self.price_Mouse)
            self.qty.set(1)

        if self.ComboProduct.get() == "Stick":
            self.prices.set(self.price_Stick)
            self.qty.set(1)

        if self.ComboProduct.get() == "Scratchers":
            self.prices.set(self.price_Scratcher)
            self.qty.set(1)

        # CatFood
        if self.ComboProduct.get() == "Gravy":
            self.prices.set(self.price_Gravy)
            self.qty.set(1)

        if self.ComboProduct.get() == "Biscuits":
            self.prices.set(self.price_Biscuits)
            self.qty.set(1)

        if self.ComboProduct.get() == "Tuna":
            self.prices.set(self.price_Tuna)
            self.qty.set(1)

        # DogToys
        if self.ComboProduct.get() == "Puzzles":
            self.prices.set(self.price_Puzzle)
            self.qty.set(1)

        if self.ComboProduct.get() == "Ball":
            self.prices.set(self.price_Ball)
            self.qty.set(1)

        if self.ComboProduct.get() == "Bone":
            self.prices.set(self.price_Bone)
            self.qty.set(1)

        # DogFood
        if self.ComboProduct.get() == "Dry Food":
            self.prices.set(self.price_Dry)
            self.qty.set(1)

        if self.ComboProduct.get() == "Chewy Food":
            self.prices.set(self.price_Chewy)
            self.qty.set(1)

        if self.ComboProduct.get() == "Meat and Bone":
            self.prices.set(self.price_Meat)
            self.qty.set(1)



if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()