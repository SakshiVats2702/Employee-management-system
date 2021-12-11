from tkinter import*
from tkinter import ttk
from tkinter import Frame
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

class Employee:
    def __init__(self, root):
       self.root=root
       self.root.geometry("1280x720+0+0")
       self.root.title('Employee Management System')

       # Variables
       self.var_dep = StringVar()
       self.var_name = StringVar()
       self.var_designation = StringVar()
       self.var_email = StringVar()
       self.var_address = StringVar()
       self.var_dob = StringVar()
       self.var_doj = StringVar()
       self.var_married = StringVar()
       self.var_idproofcomb = StringVar()
       self.var_idproof = StringVar()
       self.var_gender = StringVar()
       self.var_phone = StringVar()
       self.var_country = StringVar()
       self.var_salary = StringVar()

       lbl_title = Label(self.root, text='EMPLOYEE MANAGEMENT SYSTEM', font=('times new roman', 34, 'bold'),
                         fg='palevioletred3', bg='white')
       lbl_title.place(x=0, y=0, width=1280, height=50)

       # logo
       img_logo = Image.open(r"C:\Users\91787\Desktop\Perfect folder\logo2.jpeg")
       img_logo = img_logo.resize((45, 45), Image.ANTIALIAS)
       self.photo_logo = ImageTk.PhotoImage(img_logo)

       self.logo = Label(self.root, image=self.photo_logo)
       self.logo.place(x=190, y=0, width=45, height=45)

       # Image Frame
       img_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
       img_frame.place(x=0, y=50, width=1279, height=155)

       # 1st image
       img_1 = Image.open(r"C:\Users\91787\Desktop\Perfect folder\imagenew1.png")
       img_1 = img_1.resize((426, 151), Image.ANTIALIAS)
       self.photo1 = ImageTk.PhotoImage(img_1)

       self.img_1 = Label(img_frame, image=self.photo1)
       self.img_1.place(x=0, y=0, width=426, height=151)

       # 2nd image
       img_2 = Image.open(r"C:\Users\91787\Desktop\Perfect folder\image3.png")
       img_2 = img_2.resize((427, 151), Image.ANTIALIAS)
       self.photo2 = ImageTk.PhotoImage(img_2)

       self.img_2 = Label(img_frame, image=self.photo2)
       self.img_2.place(x=426, y=0, width=427, height=151)

       # 3rd image
       img_3 = Image.open(r"C:\Users\91787\Desktop\Perfect folder\imagenew1.png")
       img_3 = img_3.resize((424, 151), Image.ANTIALIAS)
       self.photo3 = ImageTk.PhotoImage(img_3)

       self.img_3 = Label(img_frame, image=self.photo3)
       self.img_3.place(x=852, y=0, width=424, height=151)

       # Main frame
       Main_frame = Frame(self.root, bd=3, relief=RIDGE, bg='hotpink3')
       Main_frame.place(x=5, y=205, width=1271, height=450)

       # upper Frame
       upper_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='white', text='Employee Information',
                                font=('times new roman', 16, 'bold'), fg='turquoise4')
       upper_frame.place(x=5, y=5, width=1250, height=210)

       # labels and Entry fields
       lbl_dep = Label(upper_frame, text='Department', font=('arial', 12, 'bold'), bg='lavenderblush1', fg='palevioletred4')
       lbl_dep.grid(row=0, column=0, padx=2, sticky=W)

       combo_dept = ttk.Combobox(upper_frame,textvariable=self.var_dep, font=('arial', 12, 'bold'), width=13,state='readonly')
       combo_dept['value'] = ('Select Department', 'HR', 'Software Engineer', 'Manager', 'Sales', 'Finance')
       combo_dept.current(0)
       combo_dept.grid(row=0, column=1, padx=2, pady=2, sticky=W)

       # Name
       lbl_Name = Label(upper_frame, font=('arial', 12, 'bold'), text='Name of Employee:', bg='lavenderblush1',fg='palevioletred4')
       lbl_Name.grid(row=0, column=2, padx=2, pady=2)

       txt_name = ttk.Entry(upper_frame,textvariable=self.var_name, width=15, font=('arial', 12, 'bold'))
       txt_name.grid(row=0, column=3, padx=2, pady=2)

       # lbl_Designation
       lbl_Designation = Label(upper_frame, font=('arial', 12, 'bold'), text='Designation:', bg='lavenderblush1',fg='palevioletred4')
       lbl_Designation.grid(row=1, column=0, sticky=W, padx=2, pady=2)

       txt_Designation = ttk.Entry(upper_frame, width=15,textvariable=self.var_designation,font=('arial', 12, 'bold'))
       txt_Designation.grid(row=1, column=1, sticky=W, padx=2, pady=2)

       # Email
       lbl_email = Label(upper_frame, font=('arial', 12, 'bold'), text='Email Address:', bg='lavenderblush1',fg='palevioletred4')
       lbl_email.grid(row=1, column=2, sticky=W, padx=2, pady=2)

       txt_email = ttk.Entry(upper_frame,textvariable=self.var_email, width=15, font=('arial', 12, 'bold'))
       txt_email.grid(row=1, column=3, padx=2, pady=2)

       # Address
       lbl_address = Label(upper_frame, font=('arial', 12, 'bold'), text='Address:', bg='lavenderblush1',fg='palevioletred4')
       lbl_address.grid(row=2, column=0, sticky=W, padx=2, pady=2)

       txt_address = ttk.Entry(upper_frame,textvariable=self.var_address, width=15, font=('arial', 12, 'bold'))
       txt_address.grid(row=2, column=1, padx=2, pady=2)

       # Married
       lbl_married_status = Label(upper_frame, font=('arial', 12, 'bold'), text='Marriage Status:', bg='lavenderblush1',fg='palevioletred4')
       lbl_married_status.grid(row=2, column=2, sticky=W, padx=2, pady=2)

       com_txt_married = ttk.Combobox(upper_frame,textvariable=self.var_married, state='readonly',font=('arial', 12, 'bold'), width=13)
       com_txt_married['value'] = ('Married', 'Unmarried')
       com_txt_married.current(0)
       com_txt_married.grid(row=2, column=3, sticky=W, padx=2, pady=2)

       # DOB
       lbl_dob = Label(upper_frame, font=('arial', 12, 'bold'), text='DOB:', bg='lavenderblush1',fg='palevioletred4')
       lbl_dob.grid(row=3, column=0, sticky=W, padx=2, pady=2)

       txt_dob = ttk.Entry(upper_frame,textvariable=self.var_dob, width=15, font=('arial', 12, 'bold'))
       txt_dob.grid(row=3, column=1, padx=2, pady=2)

       # Date of joining
       lbl_doj = Label(upper_frame, font=('arial', 12, 'bold'), text='Date of joining:', bg='lavenderblush1',fg='palevioletred4')
       lbl_doj.grid(row=3, column=2, sticky=W, padx=2, pady=2)

       txt_doj = ttk.Entry(upper_frame,textvariable=self.var_doj, width=15, font=('arial', 12, 'bold'))
       txt_doj.grid(row=3, column=3, padx=2, pady=2)

       # Id Proof

       com_txt_proof=ttk.Combobox(upper_frame,textvariable=self.var_idproofcomb, state='readonly',font=('arial', 12, 'bold'), width=13)
       com_txt_proof['value']=('Select ID Proof', 'Aadhar Card', 'PAN Card', 'Driving License')
       com_txt_proof.current(0)
       com_txt_proof.grid(row=4, column=0, sticky=W, padx=2, pady=2)

       txt_proof=ttk.Entry(upper_frame,textvariable=self.var_idproof, width=15,font=('arial',12,'bold'))
       txt_proof.grid(row=4,column=1,padx=2,pady=2)

       # Gender
       lbl_Gender = Label(upper_frame, font=('arial', 12, 'bold'), text='Gender:', bg='lavenderblush1',fg='palevioletred4')
       lbl_Gender.grid(row=4, column=2, sticky=W, padx=2, pady=2)

       com_txt_Gender = ttk.Combobox(upper_frame,  textvariable=self.var_gender, state='readonly',font=('arial', 12, 'bold'), width=13)
       com_txt_Gender['value'] = ('Select Gender', 'Male', 'Female', 'Other')
       com_txt_Gender.current(0)
       com_txt_Gender.grid(row=4, column=3, sticky=W, padx=2, pady=2)

       # Phone
       lbl_phone = Label(upper_frame, font=('arial', 12, 'bold'), text='Phone:', bg='lavenderblush1',fg='palevioletred4')
       lbl_phone.grid(row=0, column=4, sticky=W, padx=2, pady=2)

       txt_phone = ttk.Entry(upper_frame,textvariable=self.var_phone, width=15, font=('arial', 12, 'bold'))
       txt_phone.grid(row=0, column=5, padx=2, pady=2)

       # country
       lbl_country = Label(upper_frame, font=('arial', 12, 'bold'), text='Country:', bg='lavenderblush1',fg='palevioletred4')
       lbl_country.grid(row=1, column=4, sticky=W, padx=2, pady=2)

       txt_country = ttk.Entry(upper_frame, textvariable=self.var_country, width=15, font=('arial', 12, 'bold'))
       txt_country.grid(row=1, column=5, padx=2, pady=2)

       # CTC
       lbl_CTC = Label(upper_frame, font=('arial', 12, 'bold'), text='Salary(CTC):', bg='lavenderblush1',fg='palevioletred4')
       lbl_CTC.grid(row=2, column=4, sticky=W, padx=2, pady=2)

       txt_CTC = ttk.Entry(upper_frame,textvariable=self.var_salary, width=15, font=('arial', 12, 'bold'))
       txt_CTC.grid(row=2, column=5, padx=2, pady=2)

       # display image
       img_display = Image.open(r"C:\Users\91787\Desktop\Perfect folder\display image.jpg")
       img_display = img_display.resize((150, 169), Image.ANTIALIAS)
       self.photodisplay = ImageTk.PhotoImage(img_display)

       self.img_display = Label(upper_frame, image=self.photodisplay)
       self.img_display.place(x=860, y=0, width=150, height=169)

       # Button frame
       button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
       button_frame.place(x=1070, y=0, width=172, height=172)

       btn_add = Button(button_frame, text="SAVE",command=self.add_data, font=("arial", 15, "bold"), width=13,bg='deepskyblue3', fg='white')
       btn_add.grid(row=0, column=0, padx=1, pady=0)

       btn_update = Button(button_frame, text="UPDATE",command=self.update_data, font=("arial", 15, "bold"), width=13,bg='deepskyblue3', fg='white')
       btn_update.grid(row=1, column=0, padx=1, pady=0)

       btn_delete = Button(button_frame, text="DELETE",command=self.delete_data,font=("arial", 15, "bold"), width=13,bg='deepskyblue3', fg='white')
       btn_delete.grid(row=2, column=0, padx=1, pady=0)

       btn_clear = Button(button_frame, text="CLEAR",command=self.reset_data, font=("arial", 15, "bold"), width=13,bg='deepskyblue3', fg='white')
       btn_clear.grid(row=3, column=0, padx=1, pady=0)

       # down frame
       down_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='lavenderblush1', text='Employee Information Table', font=('times new roman', 16, 'bold'), fg='turquoise4')
       down_frame.place(x=5, y=225, width=1250, height=210)

       # Search frame
       search_frame = LabelFrame(down_frame, bd=2, relief=RIDGE, bg='thistle1', text='Search Employee Information', font=('times new roman', 14, 'bold'), fg='midnightblue')
       search_frame.place(x=0, y=0, width=1245, height=60)

       search_by = Label(search_frame, font=('arial', 12, 'bold'), text='Search By:', fg='white', bg='maroon4')
       search_by.grid(row=0, column=0, sticky=W, padx=3)

       # search
       self.var_com_search = StringVar()
       com_txt_search = ttk.Combobox(search_frame,textvariable=self.var_com_search, state="readonly", font=("arial", 12, "bold"), width=15)
       com_txt_search['value'] = ("Select Option", "Phone", "id_proof")
       com_txt_search.current(0)
       com_txt_search.grid(row=0, column=1, sticky=W, padx=4)

       self.var_search = StringVar()
       txt_search = ttk.Entry(search_frame,textvariable=self.var_search, width=15, font=("arial", 12, "bold"))
       txt_search.grid(row=0, column=2, padx=4)

       btn_search = Button(search_frame, text='Search',command=self.search_data, font=("arial", 12, "bold"), width=10,bg="purple4", fg="white")
       btn_search.grid(row=0, column=3, padx=5)

       btn_ShowAll = Button(search_frame, text='Show All',command=self.fetch_data, font=('arial', 12, 'bold'),width='10', bg='purple4', fg='white')
       btn_ShowAll.grid(row=0, column=4, padx=5)

       stayhome = Label(search_frame, text='WEAR MASK,YOUR SAFETY IS IN YOUR HANDS.',font=('times new roman',18, 'bold'), fg='white', bg='seagreen')
       stayhome.place(x=660, y=0, width=575, height=30)

       # *********** Employee Table ************
       # Table frame
       table_frame = Frame(down_frame, bd=3, relief=RIDGE, bg='lightblue2')
       table_frame.place(x=0, y=66, width=1246, height=110)

       scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
       scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

       self.employee_table = ttk.Treeview(table_frame, column=('dep', 'name', 'desig', 'email', 'add', 'married', 'dob', 'doj', 'idproofcomb', 'idproof', 'gender', 'phone','country', 'salary',), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

       scroll_x.pack(side=BOTTOM, fill=X)
       scroll_y.pack(side=RIGHT, fill=Y)

       scroll_x.config(command=self.employee_table.xview)
       scroll_y.config(command=self.employee_table.yview)

       self.employee_table.heading('dep', text='Department')
       self.employee_table.heading('name', text='Name')
       self.employee_table.heading('desig', text='Designation')
       self.employee_table.heading('email', text='EMail')
       self.employee_table.heading('add', text='Address')
       self.employee_table.heading('married', text='Married Status')
       self.employee_table.heading('dob', text='DOB')
       self.employee_table.heading('doj', text='DOJ')
       self.employee_table.heading('idproofcomb', text='Id Type')
       self.employee_table.heading('idproof', text='ID PROOF')
       self.employee_table.heading('gender', text='Gender')
       self.employee_table.heading('phone', text='Phone')
       self.employee_table.heading('country', text='Country')
       self.employee_table.heading('salary', text='Salary')

       self.employee_table['show']='headings'

       self.employee_table.column('dep', width=70)
       self.employee_table.column('name', width=70)
       self.employee_table.column('desig', width=70)
       self.employee_table.column('email', width=70)
       self.employee_table.column('add', width=70)
       self.employee_table.column('married', width=70)
       self.employee_table.column('dob', width=70)
       self.employee_table.column('doj', width=70)
       self.employee_table.column('idproofcomb', width=70)
       self.employee_table.column('idproof', width=70)
       self.employee_table.column('gender', width=70)
       self.employee_table.column('phone', width=70)
       self.employee_table.column('country', width=70)
       self.employee_table.column('salary', width=70)

       self.employee_table.pack(fill=BOTH, expand=1)
       self.employee_table.bind("<ButtonRelease>",self.get_cursor)

       self.fetch_data()

       # ****Function Declarations****
    def add_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
           messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                conn= mysql.connector.connect(host='localhost', username='root', password='Karwasatya@2702',database='employee1')
                my_cursor = conn.cursor()
                my_cursor.execute('insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_name.get(),
                                                                                                        self.var_designation.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_married.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_doj.get(),
                                                                                                        self.var_idproofcomb.get(),
                                                                                                        self.var_idproof.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_country.get(),
                                                                                                        self.var_salary.get()
                                                                                                      ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Employee has been added!', parent=self.root)
            except Exception as es:
                messagebox.showerror('Error', f'Due To:{str(es)}', parent=self.root)

       # fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='Karwasatya@2702',database='employee1')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from employee')
        data = my_cursor.fetchall()
        if len(data) != 0:
           self.employee_table.delete(*self.employee_table.get_children())
           for i in data:
               self.employee_table.insert("", END, values=i)
           conn.commit()
        conn.close()

       # Get cursor
    def get_cursor(self,event=""):
        cursor_row = self.employee_table.focus()
        content = self.employee_table.item(cursor_row)
        data = content['values']

        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_designation.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_idproofcomb.set(data[8])
        self.var_idproof.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])

    def update_data(self):
        if self.var_dep.get() == '' or self.var_email.get() == '':
           messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                update = messagebox.askyesno('Update', 'Are you sure to update this data')
                if update > 0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='Karwasatya@2702',database='employee1')
                    my_cursor = conn.cursor()
                    my_cursor.execute('update employee set Department=%s,Name=%s,Designation=%s,Email=%s,Address=%s,Married_status=%s,DOB=%s,DOJ=%s,id_proof_type=%s,Gender=%s,Phone=%s,Country=%s,Salary=%s where id_proof=%s',(
                                                                                                                                                                                                                           self.var_dep.get(),
                                                                                                                                                                                                                           self.var_name.get(),
                                                                                                                                                                                                                           self.var_designation.get(),
                                                                                                                                                                                                                           self.var_email.get(),
                                                                                                                                                                                                                           self.var_address.get(),
                                                                                                                                                                                                                           self.var_married.get(),
                                                                                                                                                                                                                           self.var_dob.get(),
                                                                                                                                                                                                                           self.var_doj.get(),
                                                                                                                                                                                                                           self.var_idproofcomb.get(),
                                                                                                                                                                                                                           self.var_gender.get(),
                                                                                                                                                                                                                           self.var_phone.get(),
                                                                                                                                                                                                                           self.var_country.get(),
                                                                                                                                                                                                                           self.var_salary.get(),
                                                                                                                                                                                                                           self.var_idproof.get()
                                                                                                                                                                                                                           ))
                else:
                    if not update:
                       return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success', 'Data successfully updated', parent=self.root)
            except Exception as es:
                messagebox.showerror('Error', f'Due To:{str(es)}', parent=self.root)

       # Delete
    def delete_data(self):
        if self.var_idproof.get() == "":
            messagebox.showerror('Error', "All fields are required")
        else:
            try:
                delete = messagebox.askyesno('Delete','Are you sure to delete this data', parent=self.root)
                if delete > 0:
                   conn = mysql.connector.connect(host='localhost', username='root', password='Karwasatya@2702',database='employee1')
                   my_cursor = conn.cursor()
                   sql= 'delete from employee where id_proof=%s'
                   value = (self.var_idproof.get(),)
                   my_cursor.execute(sql, value)
                else:
                    if not delete:
                       return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('delete', 'Data successfully deleted', parent=self.root)
            except Exception as es:
                messagebox.showerror('Error', f'Due To:{str(es)}', parent=self.root)

       # reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_name.set("")
        self.var_designation.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_married.set("Married")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_idproofcomb.set("Select ID Proof")
        self.var_idproof.set("")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_salary.set("")

       # search
    def search_data(self):
        if self.var_com_search.get() == '' or self.var_search.get() == '':
            messagebox.showerror('Error','Please select option')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='Karwasatya@2702',database='employee1')
                my_cursor = conn.cursor()
                my_cursor.execute('select * from employee where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("", END, values=i)
                conn.commit
                conn.close()
            except Exception as es:
                 messagebox.showerror('Error', f'Due To:{str(es)}', parent=self.root)


if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()