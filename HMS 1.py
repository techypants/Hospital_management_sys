import tkinter as tk
from PIL import ImageTk,Image
import tkinter.messagebox as messagebox
from tkinter import ttk
from tkinter import StringVar,END
from datetime import datetime
import tkinter.font as tkfont

import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="dbmsproj"
)
# ..
# messagebox.showerror("Error", "Please fill in all fields.")

# import databaseconnection
# import dbconnection
# Connect to the database and retrieve the data
conn2 = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="tkinterprac"
)


class login:

    def __init__(self):
    

        self.root=tk.Tk()
        self.root.geometry("1000x550")
        self.root.title("login")
        self.root.configure(bg="#dfe080")

        
        self.frame = tk.Frame(self.root,width=600,height=300)
        # root.config(bg="#ebf097")
        self.frame.config(bg="#ebf097")
        self.frame.place(relx=0.5,rely=0.5)
        self.frame2=tk.Button(self.root)
        # self.frame2 = ScrollableFrame(self.frame2)
        self.frame3=tk.Frame(self.root,height=100,width=10)
        self.frame3.config(bg="white")
        
        # self.frame3.place(relx=0.6,rely=0.4)
        # scrollable_frame = ScrollableFrame(self.frame3)
        # scrollable_frame.pack(side=tk.TOP)

        # add some widgets to the scrollable frame
        # for i in range(50):
        #     tk.Label(scrollable_frame.frame, text=f'Label {i}').pack()
        
        # loginframe=====================================
        self.loginframe=tk.Frame(self.root,width=600,height=300,highlightbackground="#ebf097", highlightthickness=20 )
        self.titlog=tk.Label(self.loginframe,text="Login",font=("helvetica",20,"bold"), bg="#eff0bd")
        self.titlog.place(relx=0.05,rely=0.05)
        # self.loginframe.pack(expand=True)
        self.loginframe.config(bg="#eff0bd")
        self.loginframe.place(relx=0.33,rely=0.5,anchor="center")
        #========================================================================
        #RECEPTION FRAME
        # self.recep=tk.Frame(self.root2,bg='white',width=600,height=300)
        # self.recep.place(relx=0.1,rely=0.1)
        
        
        # create account FRAME------------------------------------
        self.createacc=tk.Frame(self.root,width=600,height=300)


        # Create the UI elements
        self.login=tk.Button(self.loginframe,text="login",command=self.recep)
        self.login.place(relx=0.8,rely=0.8)
        self.emp_id_label = tk.Label(self.createacc, text="Employee ID")
        self.emp_id_label.place(relx=0.05,rely=0.1)
        self.emp_id_entry = tk.Entry(self.createacc)
        self.emp_id_entry.place(relx=0.05,rely=0.16)

        self.emp_name_label = tk.Label(self.createacc, text="Employee Name")
        self.emp_name_label.place(relx=0.05,rely=0.25)
        self.emp_name_entry = tk.Entry(self.createacc)
        self.emp_name_entry.place(relx=0.05,rely=0.32)

        self.age_label = tk.Label(self.createacc, text="Age")
        self.age_label.place(relx=0.05,rely=0.4)
        self.age_entry = tk.Entry(self.createacc)
        self.age_entry.place(relx=0.05,rely=0.48)

        self.gender_label = tk.Label(self.createacc, text="Gender")
        self.gender_label.place(relx=0.05,rely=0.55)
        self.gender_entry = tk.Entry(self.createacc)
        self.gender_entry.place(relx=0.05,rely=0.64)

        self.post_label = tk.Label(self.createacc, text="Post")
        self.post_label.place(relx=0.05,rely=0.7)
        self.post_entry = tk.Entry(self.createacc)
        self.post_entry.place(relx=0.05,rely=0.80)

        self.department_label = tk.Label(self.createacc, text="Department")
        self.department_label.place(relx=0.45,rely=0.1)
        self.department_entry = tk.Entry(self.createacc)
        self.department_entry.place(relx=0.45,rely=0.16)

        self.hosp_id_label = tk.Label(self.createacc, text="Hospital ID")
        self.hosp_id_label.place(relx=0.45,rely=0.25)
        self.hosp_id_entry = tk.Entry(self.createacc)
        self.hosp_id_entry.place(relx=0.45,rely=0.32)

        self.phone_label = tk.Label(self.createacc, text="Phone")
        self.phone_label.place(relx=0.45,rely=0.4)
        self.phone_entry = tk.Entry(self.createacc)
        self.phone_entry.place(relx=0.45,rely=0.48)
        
        
        self.email_label = tk.Label(self.createacc, text="Email")
        self.email_label.place(relx=0.45,rely=0.55)
        self.email_entry = tk.Entry(self.createacc)
        self.email_entry.place(relx=0.45,rely=0.64)
        
        self.join_date_label = tk.Label(self.createacc, text="Join Date")
        self.join_date_label.place(relx=0.45,rely=0.7)
        self.join_date_entry = tk.Entry(self.createacc)
        self.join_date_entry.place(relx=0.45,rely=0.8)
        
        self.create_button = tk.Button(self.createacc, text="Create Account", command=self.create_account)
        self.create_button.place(relx=0.8,rely=0.48)
       # # password
        
        
        # =======================================================================
        #LOGIN FRAME
        self.username=tk.Label(self.loginframe,text="Enter Username",font=("arial",10),width=15, fg="black", bg="#dfe080")
        # self.username.config(highlightbackground="#487fd9")
        # self.username.config(highlightbackground="#487fd", highlightthickness=2, bd=0)
        self.username.place(relx=0.1,rely=0.25)
        self.usernamein=tk.Entry(self.loginframe)
        self.usernamein.place(relx=0.1,rely=0.32)
       # password
        self.password=tk.Label(self.loginframe,text="Enter Password",font=("arial",10),width=15, fg="black", bg="#dfe080")
        self.password.config(highlightbackground="#487fd9")
        self.password.place(relx=0.1,rely=0.38)
        self.passwordin=tk.Entry(self.loginframe,show="*")
        self.passwordin.place(relx=0.1,rely=0.45)
        # # email 
        # self.email=tk.Label(self.loginframe,text="Enter email",font=("arial",10),width=15, fg="black", bg="#dfe080")
        # self.email.config(highlightbackground="#487fd9")
        # self.email.place(relx=0.1,rely=0.52)
        # self.emailin=tk.Entry(self.loginframe)
        # self.emailin.place(relx=0.1,rely=0.59)
        # #creating button to store values in database
        bool=False
        

        self.submitbutton=tk.Button(self.loginframe,text="Submit",command=self.login2)
        self.crtaccbutton=tk.Button(self.loginframe,text="create account",command=self.logtocrt)
        self.logbutton=tk.Button(self.createacc,text="login page",command=self.crttolog)
        self.logbutton.place(relx=0.8,rely=0.65)
        self.submitbutton.place(relx=0.15,rely=0.7)
        
        self.crtaccbutton.place(relx=0.15,rely=0.9)
        # self.yob=tk.Button(self.loginframe,text="get users",command=self.getusers)
        # self.yob2=tk.Button(self.loginframe,text="remove users",command=self.removeusers)
        # self.yob=tk.Button(self.loginframe,)
        # self.yob.place(relx=0.15,rely=0.8)
        # self.yob2.place(relx=0.25,rely=0.9)
        # self.frame = tk.Frame(self.root,width=600,height=300)
        # # root.config(bg="#ebf097")
        # self.frame.config(bg="#ebf097")
        # self.frame.place(relx=0.5,rely=0.5)
        
        # ------------------------------
        
          # hide the createacc initially
    #111111111111111111111111111111111111111111111111111111111111111111111
    def recep(self):
        self.recep = tk.Tk()
        self.recep.title('reception')
        self.recep.geometry('1500x800')
        self.recep.config(bg='white')
        #buttons frame
        # 1 staff
        self.bframe=tk.Frame(self.recep,width=1500,height=40,bg='grey')
        self.bframe.place(relx=0,rely=0.00)
        
        
        options = ["staff","Doctor", "nurse", "Ward Boy","peon","sweeper"]
        selected_option = tk.StringVar()
        selected_option.set(options[0])
        self.stafflab=tk.Label(self.bframe,text="Staff",font=(15),bg="white")
        self.stafflab.place(relx=0.024,rely=0.18,height=29)
        self.staff_dropbut = tk.OptionMenu(self.bframe, selected_option, *options, command=self.staff_select)
        self.staff_dropbut.place(relx=0.055,rely=0.15,width=20)
        # self.doc.place(relx=0.01,rely=0.01)
        
        # 2 billing 
       
        options = ["pharma bill", "rooms bill", "equipment bill"]
        selected_option = tk.StringVar()
        selected_option.set("amenities")
        self.bill_lab=tk.Label(self.bframe,text="amenities",font=(15),bg="white")
        self.bill_lab.place(relx=0.09,rely=0.18,height=29)
        self.bill_dropbut = tk.OptionMenu(self.bframe, selected_option, *options, command=self.bill_select)
        self.bill_dropbut.place(relx=0.147,rely=0.15)
         
        # 3 services diseases
        
        options = ["services","COVID-19","Malaria","Dengue Fever","Tuberculosis","Diabetes","Hypertension","Gastritis","Chikungunya"]
        selected_option = tk.StringVar()
        selected_option.set(options[0])
        self.serv_lab=tk.Label(self.bframe,text="services",font=(15),bg="white")
        self.serv_lab.place(relx=0.25,rely=0.18,height=29)
        self.serv_dropbut = tk.OptionMenu(self.bframe, selected_option, *options, command=self.diseases_select)
        self.serv_dropbut.place(relx=0.3,rely=0.15)
        
        # Avail dropbox
        
        # self.avail_lab=tk.Label(self.bframe,text='staff available')
        # # self.availbut=tk.Button(self.bframe,,command=self.pat_form)
        # self.avail_lab.place(relx=0.35,rely=0.2)
        options = ["doctors available", "nurse available","rooms avaiable"]
        selected_option = tk.StringVar()
        # selected_option.set(options[0])
                
        
        #------------------ Create the pform frame------------------------------
 
        self.disbutton=tk.Button(self.recep,text="patient symptoms",command=self.dis_info)
        self.disbutton.place(relx=0.537,rely=0.05)
        self.disbutton=tk.Button(self.recep,text="patient symptoms",command=self.dis_info)
        self.disbutton.place(relx=0.537,rely=0.05)
        self.guestbutton=tk.Button(self.recep,text="guest form",command=self.guest_form)
        self.guestbutton.place(relx=0.488,rely=0.05)
        
        self.pform = tk.Frame(self.recep, width=900, height=450, bg="#B0B7C0")
        self.pform.place(relx=0.01,rely=0.08)
        

        custom_font = tkfont.Font(size=20)
        self.name = tk.Label(self.pform, text="name",font=(20))
        self.name.place(relx=0.1,rely=0.1)
        
        self.doctor = tk.Label(self.pform, text='doctor',font=(20))
        self.doctor.place(relx=0.1,rely=0.2)
        
        self.age_label = ttk.Label(self.pform, text="Age:",font=(20))
        self.age_label.place(relx=0.1,rely=0.3)
        
        self.gender = tk.Label(self.pform, text='gender',font=(20))
        self.gender.place(relx=0.5,rely=0.1)
        
        self.contact = tk.Label(self.pform, text='contacts',font=(20))
        self.contact.place(relx=0.5,rely=0.2)
        
        self.address_label = ttk.Label(self.pform, text="Address:",font=(20))
        self.address_label.place(relx=0.5,rely=0.3)
        
        self.submit_button = ttk.Button(self.pform, text="Submit", command=self.insert_pat)
        self.submit_button.place(relx=0.4,rely=0.4)
        
        self.name_entry = tk.Entry(self.pform, width=20)
        self.name_entry.configure(font=custom_font)
        self.name_entry.place(relx=0.2,rely=0.1)
        
        self.doctor_entry = ttk.Entry(self.pform, width=20)
        self.doctor_entry.place(relx=0.2,rely=0.2)
        self.doctor_entry.configure(font=custom_font)
        
        self.age_entry = ttk.Entry(self.pform, width=20)
        self.age_entry.configure(font=custom_font)
        self.age_entry.place(relx=0.2,rely=0.3)
         
        self.gender_combo = ttk.Combobox(self.pform, values=["Male", "Female", "Other"], state="readonly",height=50)
        self.gender_combo.place(relx=0.6,rely=0.1)
        
        self.contact_entry = ttk.Entry(self.pform, width=20)
        self.contact_entry.configure(font=custom_font)
        self.contact_entry.place(relx=0.6,rely=0.2)
        
        self.address_entry = ttk.Entry(self.pform, width=20)
        self.address_entry.configure(font=custom_font)
        self.address_entry.place(relx=0.6,rely=0.3)

        
        # Create the room frame
        self.room = tk.Frame(self.recep, width=500, height=450)
        self.room.config(bg='blue')
        # self.room.place(relx=0.61, rely=0.055)
        self.avail=tk.Frame(self.recep, width=500, height=450)
        self.avail.config(bg='#bdccde')
        cur = conn.cursor()
        query = "select count(*) from doctors where shift=%s"
        values = ("morning",)  # Pass the parameter value directly, not inside query
        cur.execute(query, values)
        res = cur.fetchall()
        cur.close()
        
        
        self.avail.place(relx=0.61, rely=0.055)
        self.avdoc_list=tk.Listbox(self.avail,bg="#9dc9fa",width=70,height=40,font=(15))
        self.avdoc_list.place(relx=0,rely=0.2)
        
        self.avnurse_list=tk.Listbox(self.avail,bg="white",width=70,height=40,font=(15))
        # self.avnurse_list.place(relx=0,rely=0.2)
        
        self.docbut=tk.Button(self.avail,text="doctors",command=lambda:self.avail_doc())
        self.docbut.place(relx=0.8,rely=0.2)
  
        self.nursebut=tk.Button(self.avail,text="Nurses",command=lambda:self.avail_nurse())
        self.nursebut.place(relx=0.9,rely=0.2)
        
        self.availdocno = tk.Label(self.recep, text=res, font=("Arial", 50, "bold"),bg="#9dc9fa")
        self.availdocno.place(relx=0.75,rely=0.2)
        self.availdoc=tk.Label(self.recep,text="available doctors",font=(10),bg="#9dc9fa")
        self.availdoc.place(relx=0.725,rely=0.29)
        cur = conn.cursor()
        query = "select count(*) from nurses where shift=%s"
        values = ("morning",)  # Pass the parameter value directly, not inside query
        cur.execute(query, values)
        res = cur.fetchall()
        cur.close()
        self.availnurseno = tk.Label(self.recep, text=res, font=("Arial", 50, "bold"),bg="#9dc9fa")
        self.availnurseno.place(relx=0.65,rely=0.32)
        self.availnurse=tk.Label(self.recep,text="available nurses",font=(10),bg="#9dc9fa")
        self.availnurse.place(relx=0.625,rely=0.4)
        cur = conn.cursor()
        query = "select count(*) from patients"
        # values = ("morning",)  # Pass the parameter value directly, not inside query
        cur.execute(query)
        res = cur.fetchall()
        cur.close()
        self.availpatno = tk.Label(self.recep, text=res, font=("Arial", 50, "bold"),bg="#9dc9fa")
        self.availpatno.place(relx=0.85,rely=0.32)
        self.availpat=tk.Label(self.recep,text="patient counts",font=(10),bg="#9dc9fa")
        self.availpat.place(relx=0.825,rely=0.4)
        #333333333333333333333333333333333333333333333333333333333333333333333
        
        # Create a Canvas widget inside the room frame for scrolling
        # self.room_canvas = tk.Canvas(self.room, bg='white')
        # self.room_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        
        # self.room_content_frame = tk.Frame(self.room_canvas, bg='white')
        # self.room_canvas.create_window((0, 0), window=self.room_content_frame, anchor=tk.NW)
        
        # create the patients current frame
        
        # self.currpat = tk.Frame(self.recep, width=500, height=450)
        # self.currpat.config(bg='white')
        # self.currpat.place(relx=0.61, rely=0.055)
        self.currpat=tk.Frame(self.recep,width=1482.5,height=250,bg="white")
        self.currpat.place(relx=0.005,rely=0.65)
        # docsavail=tk.Label()
        # Create a Canvas widget inside the room frame for scrolling
        # self.currpat_canvas = tk.Canvas(self.currpat,width=1400.5,height=250,bg="white")
        # self.currpat_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # # Create a Scrollbar widget for the room Canvas
        # self.currpat_scrollbar = ttk.Scrollbar(self.currpat, orient=tk.VERTICAL, command=self.currpat_canvas.yview)
        # self.currpat_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # # Configure the room Canvas to use the Scrollbar
        # self.currpat_canvas.configure(yscrollcommand=self.currpat_scrollbar.set)
        # self.currpat_canvas.bind('<Configure>', self.on_currpat_canvas_configure)

        # Create a frame inside the room Canvas to hold the content
        self.currpat_content_frame = tk.Frame(self.currpat, bg='white')
        self.pat_list=tk.Listbox(self.currpat)
        self.pat_list.place(relx=0,rely=0,width=1482.5,height=250)
        
        # self.currpat_canvas.create_window((0, 0), window=self.currpat_content_frame, anchor=tk.NW)
        # Add content to the room frame
        # self.add_room_content()
        self.add_currpat_content()
        # self.pat_form()
        self.recep.mainloop()
        
    # def
    def avail_doc(self):
        import datetime
        
        # Create the doctors frame
        # self.doctors_frame = tk.Frame(self.recep, width=900, height=450)
        # self.doctors_frame.place(relx=0.005, rely=0.055)
        self.doctors_frame=tk.Tk()
        self.doctors_frame.geometry("1500x200")
        # Create the doctors treeview
        columns = ("EmpID", "Name", "Contact", "Email", "Age", "Salary", "Designation", "Dept", "Speciality", "Shift", "Address", "JoiningDate", "Gender", "LicenceNo", "Experience", "Languages")
        doctors_treeview = ttk.Treeview(self.doctors_frame, columns=columns, show="headings")
        doctors_treeview.place(relx=0, rely=0)
        
        # Set column headings
        doctors_treeview.heading("EmpID", text="EmpID")
        doctors_treeview.heading("Name", text="Name")
        doctors_treeview.heading("Contact", text="Contact")
        doctors_treeview.heading("Email", text="Email")
        doctors_treeview.heading("Age", text="Age")
        doctors_treeview.heading("Salary", text="Salary")
        doctors_treeview.heading("Designation", text="Designation")
        doctors_treeview.heading("Dept", text="Dept")
        doctors_treeview.heading("Speciality", text="Speciality")
        doctors_treeview.heading("Shift", text="Shift")
        doctors_treeview.heading("Address", text="Address")
        doctors_treeview.heading("JoiningDate", text="Joining Date")
        doctors_treeview.heading("Gender", text="Gender")
        doctors_treeview.heading("LicenceNo", text="Licence No")
        doctors_treeview.heading("Experience", text="Experience")
        doctors_treeview.heading("Languages", text="Languages")
        
        # Set column widths
        doctors_treeview.column("EmpID", width=60)
        doctors_treeview.column("Name", width=120)
        doctors_treeview.column("Contact", width=120)
        doctors_treeview.column("Email", width=150)
        doctors_treeview.column("Age", width=50)
        doctors_treeview.column("Salary", width=80)
        doctors_treeview.column("Designation", width=100)
        doctors_treeview.column("Dept", width=100)
        doctors_treeview.column("Speciality", width=100)
        doctors_treeview.column("Shift", width=80)
        doctors_treeview.column("Address", width=150)
        doctors_treeview.column("JoiningDate", width=100)
        doctors_treeview.column("Gender", width=70)
        doctors_treeview.column("LicenceNo", width=100)
        doctors_treeview.column("Experience", width=80)
        doctors_treeview.column("Languages", width=100)
        
        # Get the current system time
        current_time = datetime.datetime.now().time()
        
        # Fetch data from the "doctors" table in MySQL
        cur = conn.cursor()
        query = "SELECT EmpID, Name, Contact, Email, Age, Salary, Designation, Dept, Speciality, Shift, Address, JoiningDate, Gender, LicenceNo, Experience, Languages FROM doctors"
        cur.execute(query)
        data = cur.fetchall()
        
        # Insert the fetched data into treeview
        for item in data:
            shift = item[9]  # Shift column is at index 9
            values = item
        
            # Check if the shift is "morning" and current time is before 12:00 PM
            if shift == "morning" and current_time < datetime.time(hour=12):
                doctors_treeview.insert("", tk.END, values=values, tags=("green",))
            else:
                doctors_treeview.insert("", tk.END, values=values)
        
        # Configure tag to apply green color to rows
        doctors_treeview.tag_configure("green", background="green")
        
        cur.close()


        # conn2 = mysql.connector.connect(
        #     host="localhost",
        #     user="root",
        #     password="root",
        #     database="dbmsproj"
        # )
        # cur=conn2.cursor()
        # cur2=conn2.cursor()
        # query2="desc doctors"
        # cur2.execute(query2)
        # resc=cur2.fetchall()
        
        # query="select empid,name,contact,email,age,salary,languages from doctors"
        # cur.execute(query)
        # records=cur.fetchall()
        # self.root2 = tk.Tk()
        # self.root.title("Employee Records")
        
        # # Create a style object
        # style = ttk.Style()
        
        # # Configure the style to set the background color and padding of the Treeview
        # style.configure("Treeview", background="red", padding=10)
        
        # # Create a frame to contain the Treeview widget
        # frame = tk.Frame(self.root2)
        # frame.pack(fill='both', expand=True)
        
        # # Create a Treeview widget
        # tree = ttk.Treeview(frame, style="Treeview")
        # tree['columns'] = ('Emp_id', 'Doc_name', 'Contact', 'Email', 'Age', 'Charging_fee', 'Designation',
        #                    'Department', 'Speciality', 'Shift', 'Address', 'Gender',
        #                     'Languages','Licence_Experience')

        # # Adjust the padding of the columns
        # tree.column('#0', stretch=tk.NO, minwidth=0, width=0)  # Hide the first (default) column
        # tree.column('Emp_id', minwidth=0, width=100)  # Set the width of the Emp_id column
        # tree.heading('Emp_id', text='Emp_id')
        # tree.heading('Doc_name', text='Doc_name')
        # tree.heading('Contact', text='Contact')
        # tree.heading('Email', text='Email')
        # tree.heading('Age', text='Age')
        # # tree.heading('Charging_fee', text='Charging_fee')
        # # tree.heading('Designation', text='Designation')
        # # tree.heading('Department', text='Department')
        # # tree.heading('Speciality', text='Speciality')
        # # tree.heading('Shift', text='Shift')
        # # tree.heading('Address', text='Address')
        # # tree.heading('Joining_date', text='Joining_date')
        # tree.heading('Gender', text='Gender')
        # # tree.heading('Licence_Experience', text='Licence_Experience')
        # # tree.heading('Languages', text='Languages')
        
        # # Set narrow width for columns
        # column_width = 80  # Adjust this value to make columns narrower
        
        # for column in tree['columns']:
        #     tree.column(column, width=column_width, anchor='w')
        
        # # Add records to the Treeview
        # for record in records:
        #     tree.insert("", tk.END, values=record)
        
        # # Pack the Treeview widget
        # tree.pack(fill='both', expand=True)
        # cur.close()
        # cur2.close()
        # self.root2.mainloop()
    # def avail_doc(self):
    #     # self.avnurse.place_forget()
    #     self.avdoc_list.place(relx=0,rely=0.2)
    #     current_time = datetime.now().time()
    #     hour =current_time.hour
    #     cur=conn.cursor()
    #     query="select * from doctors where shift=%s"
    #     if hour < 12:
    #         self.avdoc_list.configure(bg="white")
    #         # time_label.config(text="Good Morning!")
    #         time="morning"
    #         value=(time,)
    #         cur.execute(query,value)
    #         res=cur.fetchall()

    #         for i in res:
    #             # print(i)55625C
    #             self.avdoc_list.insert(tk.END, "Emp_id: " + str(i[0]))
    #             self.avdoc_list.insert(tk.END, "Doc name: " + i[1])
    #             self.avdoc_list.insert(tk.END, "Contact: " + str(i[2]))
    #             self.avdoc_list.insert(tk.END, "Email: " + i[3])
    #             self.avdoc_list.insert(tk.END, "Age: " + str(i[4]))
    #             self.avdoc_list.insert(tk.END, "Charging fee: "+str(i[5]/10))
    #             self.avdoc_list.insert(tk.END, "Designation: " + str(i[6]))
    #             self.avdoc_list.insert(tk.END, "Department : " + i[8])
    #             self.avdoc_list.insert(tk.END, "specaility : " + i[9])
    #             self.avdoc_list.insert(tk.END, "shift : " + i[10])
    #             self.avdoc_list.insert(tk.END, "Address : " + i[11])
    #             self.avdoc_list.insert(tk.END, "joining date : " + str(i[12]))
    #             self.avdoc_list.insert(tk.END, "Gender : " + str(i[13]))
    #             self.avdoc_list.insert(tk.END, "Licence Experience : " + str(i[15]))
    #             self.avdoc_list.insert(tk.END, "languages : " + str(i[16]))
    #             self.avdoc_list.insert(tk.END, "")
           
    #     elif hour >= 12 and hour < 18:
    #             self.avdoc_list.configure(bg="white")
    #             time="evening"
    #             value=(time,)
    #             cur.execute(query,value)
    #             res=cur.fetchall()
    #             for i in res:
    #                 self.avdoc_list.insert(tk.END, "Emp_id: " + str(i[0]))
    #                 self.avdoc_list.insert(tk.END, "Doc name: " + i[1])
    #                 self.avdoc_list.insert(tk.END, "Contact: " + str(i[2]))
    #                 self.avdoc_list.insert(tk.END, "Email: " + i[3])
    #                 self.avdoc_list.insert(tk.END, "Age: " + str(i[4]))
    #                 self.avdoc_list.insert(tk.END, "Charging fee: "+str(i[5]/10))
    #                 self.avdoc_list.insert(tk.END, "Designation: " + str(i[6]))
    #                 self.avdoc_list.insert(tk.END, "Department : " + i[8])
    #                 self.avdoc_list.insert(tk.END, "specaility : " + i[9])
    #                 self.avdoc_list.insert(tk.END, "shift : " + i[10])
    #                 self.avdoc_list.insert(tk.END, "Address : " + i[11])
    #                 self.avdoc_list.insert(tk.END, "joining date : " + str(i[12]))
    #                 self.avdoc_list.insert(tk.END, "Gender : " + str(i[13]))
    #                 self.avdoc_list.insert(tk.END, "Licence Experience : " + str(i[15]))
    #                 self.avdoc_list.insert(tk.END, "languages : " + str(i[16]))
    #                 self.avdoc_list.insert(tk.END, "")
    #     cur.close()
    def avail_nurse(self):
        conn2 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="dbmsproj"
        )
        cur=conn2.cursor()
        cur2=conn2.cursor()
        query2="desc doctors"
        cur2.execute(query2)
        resc=cur2.fetchall()
        
        query="select * from nurses"
        cur.execute(query)
        records=cur.fetchall()
        self.root2 = tk.Tk()
        self.root.title("Employee Records")
        
        # Create a style object
        style = ttk.Style()
        
        # Configure the style to set the background color and padding of the Treeview
        style.configure("Treeview", background="red", padding=10)
        
        # Create a frame to contain the Treeview widget
        frame = tk.Frame(self.root2)
        frame.pack(fill='both', expand=True)
        
        # Create a Treeview widget
        tree = ttk.Treeview(frame, style="Treeview")
        tree['columns'] = ('Emp_id', 'Doc_name', 'Contact', 'Email', 'Age', 'Charging_fee', 'Designation',
                           'Department', 'Speciality', 'Shift', 'Address', 'hospitals served',
                            'Joining_date','Gender')

        # Adjust the padding of the columns
        tree.column('#0', stretch=tk.NO, minwidth=0, width=0)  # Hide the first (default) column
        tree.column('Emp_id', minwidth=0, width=100)  # Set the width of the Emp_id column
        tree.heading('Emp_id', text='Emp_id')
        tree.heading('Doc_name', text='Doc_name')
        tree.heading('Contact', text='Contact')
        tree.heading('Email', text='Email')
        tree.heading('Age', text='Age')
        tree.heading('Charging_fee', text='Charging_fee')
        tree.heading('Designation', text='Designation')
        tree.heading('Department', text='Department')
        tree.heading('Speciality', text='Speciality')
        tree.heading('Shift', text='Shift')
        tree.heading('Address', text='Address')
        tree.heading('hospitals served', text='hospitals served')
        tree.heading('Joining_date', text='Joining_date')
        tree.heading('Gender', text='Gender')
        
        # Set narrow width for columns
        column_width = 80  # Adjust this value to make columns narrower
        
        for column in tree['columns']:
            tree.column(column, width=column_width, anchor='w')
        
        # Add records to the Treeview
        for record in records:
            tree.insert("", tk.END, values=record)
        
        # Pack the Treeview widget
        tree.pack(fill='both', expand=True)
        cur.close()
        cur2.close()
        self.root2.mainloop()
        
    def dis_info(self):
        self.pdisframe=tk.Frame(self.recep,bg="pink", width=900, height=450)
        self.pdisframe.place(relx=0.01,rely=0.08)
        self.close = tk.Button(self.pdisframe, text='x', font=('bold'), bg="red",width=2,command=lambda:self.pdisframe.place_forget())
        self.close.place(relx=0.97, rely=0)
        def add_patient_info():
            # Retrieve input values from the entry fields
            did = did_entry.get()
            days = days_entry.get()
            ill_date = ill_date_entry.get()
            medicines_taken = medicines_entry.get()
            symptoms = symptoms_entry.get()
            add_details = add_details_entry.get()
            
            # Connect to the MySQL database
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="dbmsproj"
            )
            
            # Create a cursor object to execute SQL queries
            cursor = db.cursor()
            
            # Insert the values into the patient_info table
            query = "INSERT INTO patient_info (did, days, ill_date, medicines_taken, symptoms, add_details) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (did, days, ill_date, medicines_taken, symptoms, add_details)
            cursor.execute(query, values)
            
            # Commit the changes to the database
            db.commit()
            
            # Close the cursor and database connection
            cursor.close()
            db.close()
            
            # Clear the entry fields
            did_entry.delete(0, tk.END)
            days_entry.delete(0, tk.END)
            ill_date_entry.delete(0, tk.END)
            medicines_entry.delete(0, tk.END)
            symptoms_entry.delete(0, tk.END)
            add_details_entry.delete(0, tk.END)

        # Create the Tkinter window
        cursor2=conn.cursor()
        query="select count(*) from patients"
        cursor2.execute(query)
        res=cursor2.fetchall()
        count=(res[0][0])
        # cursor2.close()
        patcount=tk.Label(self.pdisframe,text=("current patient count: ",count))
        patcount.place(relx=0,rely=0)
        # Create labels and entry fields for input
        did_label = tk.Label(self.pdisframe, text="DID:")
        did_label.place(relx=0.1,rely=0.1)
        did_entry = tk.Entry(self.pdisframe,text=count)
        did_entry.place(relx=0.2,rely=0.1)

        days_label = tk.Label(self.pdisframe, text="Days:")
        days_label.place(relx=0.1,rely=0.2)
        days_entry = tk.Entry(self.pdisframe)
        days_entry.place(relx=0.2,rely=0.2)

        ill_date_label = tk.Label(self.pdisframe, text="Ill Date:")
        ill_date_label.place(relx=0.1,rely=0.3)
        ill_date_entry = tk.Entry(self.pdisframe)
        ill_date_entry.place(relx=0.2,rely=0.3)

        medicines_label = tk.Label(self.pdisframe, text="Medicines Taken:")
        medicines_label.place(relx=0.45,rely=0.1)
        medicines_entry = tk.Entry(self.pdisframe)
        medicines_entry.place(relx=0.6,rely=0.1)

        symptoms_label = tk.Label(self.pdisframe, text="Symptoms:")
        symptoms_label.place(relx=0.45,rely=0.2)
        symptoms_entry = tk.Entry(self.pdisframe)
        symptoms_entry.place(relx=0.6,rely=0.2)

        add_details_label = tk.Label(self.pdisframe, text="Additional Details:")
        add_details_label.place(relx=0.45,rely=0.3)
        add_details_entry = tk.Entry(self.pdisframe)
        # add_details_entry.configure(height=400)
        add_details_entry.place(relx=0.6,rely=0.3)

        # # Create a button to add patient info
        add_button = tk.Button(self.pdisframe, text="Add", command=add_patient_info)
        add_button.place(relx=0.4,rely=0.4)
        showdisframe=tk.Frame(self.pdisframe,width=900,height=400)
        showdisframe.place(relx=0.17,rely=0.5)
        query="select q.id,q.name,ill_date,days,medicines_taken,symptoms,add_details from patient_info p join  patients q where q.id=p.did;"
        cur=conn.cursor()
        cur.execute(query)
        records=cur.fetchall()
        tree = ttk.Treeview(showdisframe, style="Treeview")
        tree['columns'] = ('patient id','patient name', 'days ill','date since', 'medicines taken', 'symptoms', 'other details')
                           
                           

        # Adjust the padding of the columns
        tree.column('#0', stretch=tk.NO, minwidth=0, width=0)  # Hide the first (default) column
        tree.column('patient id', minwidth=0, width=150)  # Set the width of the Emp_id column
        tree.heading('patient name', text='patient name')
        # tree.heading('patient id', text='patient id')
        tree.heading('days ill', text='days ill')
        tree.heading('date since', text='date since')
        tree.heading('medicines taken', text='medicines taken')
        tree.heading('symptoms', text='symptoms')
        tree.heading('other details', text='other details')
   
        
        # Set narrow width for columns
        column_width = 80  # Adjust this value to make columns narrower
        
        for column in tree['columns']:
            tree.column(column, width=column_width, anchor='w')
        tree.column('other details', width=150, anchor='w')
        
        # Add records to the Treeview
        for record in records:
            tree.insert("", tk.END, values=record)
        
        # Pack the Treeview widget
        tree.pack(fill='both', expand=True)
        cur.close()
  
    def login2(self):
        username = self.usernamein.get()
        password = self.passwordin.get()
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="dbmsproj"
        )
        cursor = connection.cursor()
        
        # Execute the SQL query to check the credentials
        query = "SELECT * FROM employee WHERE emp_name = %s AND email = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        print(":yes")
        if result:
            # Credentials are authorized, change the frame
            print("Good")
            button=tk.Button(self.loginframe,text="proceed to reception",font=(20),command=self.recep)
            button.place(relx=0.6,rely=0.4)
            
            # TODO: Add code to show the new frame or perform any other actions
        else:
            # Invalid credentials, display an error message
            print("Bad")
            # TODO: Add code to display an error message or perform any other actions
    
        cursor.close()
        connection.close()

    
            # Update the time label every second
            # time_label.after(1000, update_time)
    def diseases_select(self, value):
        self.dis_frame = tk.Frame(self.recep, width=900, height=450)
        self.dis_frame.place(relx=0.005, rely=0.055)
        self.close = tk.Button(self.dis_frame, text='x', font=('bold'), bg="white", width=2, command=lambda: self.dis_frame.place_forget())
        self.close.place(relx=0.97, rely=0)
        dislabel=tk.Label(self.dis_frame,text=("disease record: ",value),font=(30))
        dislabel.place(relx=0,rely=0)
        ser_tree = ttk.Treeview(self.dis_frame, columns=("Disease Name", "Patient ID", "Diagnosis Date", "Treatment", "Status"), show="headings")
        ser_tree.place(relx=0.2, rely=0.2)
        
        # Set the column headings
        ser_tree.heading("Disease Name", text="Disease Name")
        ser_tree.heading("Patient ID", text="Patient ID")
        ser_tree.heading("Diagnosis Date", text="Diagnosis Date")
        ser_tree.heading("Treatment", text="Treatment")
        ser_tree.heading("Status", text="Status")
        
        # Set the column widths
        ser_tree.column("Disease Name", width=150)
        ser_tree.column("Patient ID", width=80)
        ser_tree.column("Diagnosis Date", width=100)
        ser_tree.column("Treatment", width=200)
        ser_tree.column("Status", width=80)
        
        print("Selected item:", value)
        query = "SELECT * FROM diseases WHERE disease_name = %s"
        cur2 = conn.cursor()
        cur2.execute(query, (value,))
        res = cur2.fetchall()
        
        for row in res:
            ser_tree.insert("", tk.END, values=(row[1], row[0], row[2], row[3], row[4]))
        
        cur2.close()
 
    def staff_select(self, value):
        self.staff_frame = tk.Frame(self.recep, width=900, height=450)
        self.staff_frame.place(relx=0.005, rely=0.055)
        
        self.close = tk.Button(self.staff_frame, text='x', font='bold', bg="white", width=2, command=lambda: self.staff_frame.place_forget())
        self.close.place(relx=0.97, rely=0)
        
        ser_treeview = ttk.Treeview(self.staff_frame, columns=("emp_id", "emp_name", "age", "gender", "post", "department", "phone", "email", "join_date"), show="headings")
        ser_treeview.place(relx=0, rely=0.2)
        
        # Set column headings
        ser_treeview.heading("emp_id", text="Emp ID")
        ser_treeview.heading("emp_name", text="Emp Name")
        ser_treeview.heading("age", text="Age")
        ser_treeview.heading("gender", text="Gender")
        ser_treeview.heading("post", text="Post")
        ser_treeview.heading("department", text="Department")
        ser_treeview.heading("phone", text="Phone")
        ser_treeview.heading("email", text="Email")
        ser_treeview.heading("join_date", text="Join Date")
        
        # Set column widths
        ser_treeview.column("emp_id", width=70)
        ser_treeview.column("emp_name", width=120)
        ser_treeview.column("age", width=50)
        ser_treeview.column("gender", width=70)
        ser_treeview.column("post", width=80)
        ser_treeview.column("department", width=120)
        ser_treeview.column("phone", width=100)
        ser_treeview.column("email", width=150)
        ser_treeview.column("join_date", width=90)
        
        print("Selected item:", value)
        query = ""
        cur2 = conn.cursor()
        if value == 'staff':
            query = "select * from employee"
            cur2.execute(query)
        else:
            query = "select * from employee where post=%s"
            cur2.execute(query, (value,))
        res = cur2.fetchall()
        
        # Insert data into treeview
        for row in res:
            # Remove the 7th element (Hospital ID) from the row tuple
            row_without_hosp_id = row[:6] + row[7:]
            ser_treeview.insert("", tk.END, values=row_without_hosp_id)
        
        cur2.close()

    def guest_form(self):
        def submit_form():
            # Retrieve the input values from the form fields
            gid = gid_entry.get()
            gname = gname_entry.get()
            pid = pid_entry.get()
            pname = pname_entry.get()
            
            # Connect to MySQL
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="dbmsproj"
            )
            
            # Create a cursor object to execute SQL queries
            cursor = conn.cursor()
            
            # Insert the values into the guestpatient table
            query = "INSERT INTO guestpatient (gid, gname, pid, pname) VALUES (%s, %s, %s, %s)"
            values = (gid, gname, pid, pname)
            cursor.execute(query, values)
            
            # Commit the changes to the database
            conn.commit()
            
            # Close the cursor and database connection
            cursor.close()
            conn.close()
            
            # Clear the form fields
            gid_entry.delete(0, tk.END)
            gname_entry.delete(0, tk.END)
            pid_entry.delete(0, tk.END)
            pname_entry.delete(0, tk.END)
        
            
            # Perform any further actions, such as saving the data to the database
        
        # Create the Tkinter window
        window = tk.Tk()
        window.title("Guest Patient Form")
        window.configure(bg="#c3dae6")
        # Create the form fields
        
        
        gid_label = tk.Label(window, text="Guest ID:")
        gid_label.grid(row=1, column=0, padx=10, pady=5)
        gid_entry = tk.Entry(window)
        gid_entry.grid(row=1, column=1, padx=10, pady=5)
        
        gname_label = tk.Label(window, text="Guest Name:")
        gname_label.grid(row=2, column=0, padx=10, pady=5)
        gname_entry = tk.Entry(window)
        gname_entry.grid(row=2, column=1, padx=10, pady=5)
        
        pid_label = tk.Label(window, text="Patient ID:")
        pid_label.grid(row=3, column=0, padx=10, pady=5)
        pid_entry = tk.Entry(window)
        pid_entry.grid(row=3, column=1, padx=10, pady=5)
        
        pname_label = tk.Label(window, text="Patient Name:")
        pname_label.grid(row=4, column=0, padx=10, pady=5)
        pname_entry = tk.Entry(window)
        pname_entry.grid(row=4, column=1, padx=10, pady=5)
        
        submit_button = tk.Button(window, text="Submit", command=submit_form)
        submit_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        
        # Start the Tkinter event loop
        window.mainloop()


    def calculate_totalmeds(self):
        cur2=conn.cursor()
        self.total_label.place(relx=0.2,rely=0.1,width=600)
        selected_items = self.medslist.curselection()
        if selected_items:
            total = 0
            for index in selected_items:
                med_info = self.medslist.get(index)
                med_name = med_info.split("\t")[0]
                cur2.execute("SELECT price FROM meds WHERE name = %s", (med_name,))
                prices = cur2.fetchall()
                if prices:
                    total += prices[0][0]
            self.total_price.set(f"Total Price: {total}")
        else:
            self.total_price.set("Total Price: 0")
        self.total_label.config(text=self.total_price.get())  # Update the total label text
    
    def calculate_totalroom(self):
        cur2=conn.cursor()
        self.total_label.place(relx=0.2,rely=0.1,width=600)
        selected_items = self.roomlist.curselection()
        if selected_items:
            total = 0
            for index in selected_items:
                room_info = self.roomlist.get(index)
                room_name = room_info.split("\t")[0]
                cur2.execute("SELECT price FROM rooms WHERE category = %s", (room_name,))
                prices = cur2.fetchall()
                if prices:
                    total += prices[0][0]
            self.total_price.set(f"Total Price: {total}")
        else:
            self.total_price.set("Total Price: 0")
        self.total_label.config(text=self.total_price.get())
    def calculate_totalequip(self):
        cur2=conn.cursor()
        self.total_label.place(relx=0.2,rely=0.1,width=600)
        selected_items = self.equiplist.curselection()
        if selected_items:
            total = 0
            for index in selected_items:
                eqp_info = self.equiplist.get(index)
                eqp_name = eqp_info.split("\t")[0]
                cur2.execute("SELECT price FROM equipment WHERE  name= %s", (eqp_name,))
                prices = cur2.fetchall()
                if prices:
                    total += prices[0][0]
            self.total_price.set(f"Total Price: {total}")
        else:
            self.total_price.set("Total Price: 0")
        self.total_label.config(text=self.total_price.get())
   
    def bill_select(self,value):
        connection = mysql.connector.connect(
          host="localhost",
            user="root",
            password="root",
            database="dbmsproj"
        )        
        cursor=connection.cursor()

        self.bill_frame = tk.Frame(self.recep, width=900, height=450)
        self.bill_frame.place(relx=0.005, rely=0.055)
        self.close = tk.Button(self.bill_frame, text='x', font=('bold'), bg="white",width=2,command=lambda:self.bill_frame.place_forget())
        self.close.place(relx=0.97, rely=0)
        if(value=='pharma bill'):
            self.medslist=tk.Listbox(self.bill_frame,width=200,height=40,bg="white",fg="black",font=('bold',10),selectmode='multiple')
            self.medslist.place(relx=0,rely=0.2)
            # self.display_meds()
            
            submit_button = tk.Button(self.bill_frame, text="Submit", command=lambda:self.calculate_totalmeds())
            submit_button.place(relx=0.8,rely=0.15)
            self.total_price = StringVar()
            self.total_price.set("Total Price: 0")
            self.total_label = tk.Label(self.bill_frame, text=self.total_price,font=(40))
            
            # self.total_label.place(relx=0.5,rely=0.6,width=100)
            
        
            # cursor.execute("SELECT name, price FROM meds")
            # meds = cursor.fetchall()
            
        
            cursor.execute("SELECT name, price,description FROM meds")
            meds = cursor.fetchall()
            for med in meds:
                # med_info = f"{med[0]}"+"  "+f"{med[1]}"+"  "+f"{med[2]}"
                med_info = f"{med[0]}\t   \t{med[1]}\t   \t{med[2]}"#"\t\t{med[3]}"
                self.medslist.insert(END, med_info)
                # self.medslist.insert(END, med_info)
            cur2=connection.cursor()
            selected_items = self.medslist.curselection()
            
            
        elif(value=='equipment bill'):
            self.equiplist=tk.Listbox(self.bill_frame,width=200,height=40,bg="white",fg="black",font=('bold',15),selectmode='multiple')
            self.equiplist.place(relx=0,rely=0.2)
            submit_button = tk.Button(self.bill_frame, text="Submit", command=lambda:self.calculate_totalequip())
            submit_button.place(relx=0.8,rely=0.15)
            self.total_price = StringVar()
            self.total_price.set("Total Price: 0")
            self.total_label=tk.Label(self.bill_frame,text=self.total_price)
            # self.total_label = tk.Label(self.bill_frame, textvariable=self.total_price)
            self.total_label = tk.Label(self.bill_frame, text=self.total_price,font=(40))
            
            
        
            cursor.execute("SELECT name,price,treatment_used FROM equipment")
            equips = cursor.fetchall()
            for eqp in equips:
                eqp_info = f"{eqp[0]}\t   \t{eqp[1]}\t  \t{eqp[2]}"
                self.equiplist.insert(END, eqp_info)
                # self.medslist.insert(END, med_info)
            cur2=connection.cursor()
            selected_items = self.equiplist.curselection()
        elif(value=='rooms bill'):
            self.roomlist=tk.Listbox(self.bill_frame,width=200,height=40,bg="white",fg="black",font=('bold',15),selectmode='multiple')
            self.roomlist.place(relx=0,rely=0.2)
            submit_button = tk.Button(self.bill_frame, text="Submit", command=lambda:self.calculate_totalroom())
            submit_button.place(relx=0.8,rely=0.15)
            self.total_price = StringVar()
            self.total_price.set("Total Price: 0")
            self.total_label = tk.Label(self.bill_frame, text=(self.total_price.get))
            # self.total_label.place(relx=0.5,rely=0.6)
            cursor.execute("SELECT name, price FROM equipment")
            meds = cursor.fetchall()
            
        
            cursor.execute("SELECT Category,PricePerBed FROM rooms")
            rooms = cursor.fetchall()
            for room in rooms:
                room_info = f"{room[0]}\t \t{room[1]}"  #\t{room[2]}\t  \t{room[3]}\t  \t{room[4]}\t  \t{room[5]}"
                self.roomlist.insert(END, room_info)
                # self.medslist.insert(END, med_info)
            cur3=connection.cursor()
            selected_items = self.roomlist.curselection()
       
        
       
    def bill_select2(self,value):
        print("Selected item:", value)
        self.bill_frame = tk.Frame(self.recep, width=900, height=450)
        self.bill_frame.place(relx=0.005, rely=0.055)
        self.close = tk.Button(self.bill_frame, text='x', font=('bold'), bg="white",width=2,command=lambda:self.bill_frame.place_forget())
        self.close.place(relx=0.97, rely=0)

        ser_list=tk.Listbox(self.bill_frame,width=200,height=40,bg="white",font=('bold',10))
        ser_list.place(relx=0,rely=0.2)
        print("Selected item:", value)
        query=""
        cur2=conn.cursor()
        if value=='billing':
            query="select * from bills"
            cur2.execute(query)
        else:
            query="select * from employee where =%s"
            cur2.execute(query,(value,))
        res=cur2.fetchall()
        for row in res:
            ser_list.insert(tk.END, "bill_id: " + str(row[0]))
            ser_list.insert(tk.END, "patient_name: " + row[1])
            ser_list.insert(tk.END, "patient_age: " + str(row[2]))
            ser_list.insert(tk.END, "doctor_fee: " + row[3])
            ser_list.insert(tk.END, "medicine_cost: " + row[4])
            ser_list.insert(tk.END, "room_charge: "+row[5])
            ser_list.insert(tk.END, "total_bill: " + str(row[6]))
            ser_list.insert(tk.END, "created_at : " + row[7])
            # ser_list.insert(tk.END, "email : " + row[8])
            # ser_list.insert(tk.END, "join_date: " + str(row[9]))
            ser_list.insert(tk.END, "")
            # print(row)
        cur2.close()
    def insert_pat(self):
            name =self.name_entry.get()
            gender = self.gender_combo.get()
            doctor_assigned = self.doctor_entry.get()
            contact_number = self.contact_entry.get()
            age = self.age_entry.get()
            address = self.address_entry.get()
            self.name_entry.delete(0, tk.END)
            self.gender_combo.set('')
            self.doctor_entry.delete(0, tk.END)
            self.contact_entry.delete(0, tk.END)
            self.age_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="dbmsproj"
            )
            cursor = db.cursor()
            
            # SQL query to insert a new record
            sql = "INSERT INTO patients (name, gender, doctor_assigned, contact_number, age, address) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (name, gender, doctor_assigned, contact_number, age, address)


        
       
    #================================
            
    def add_pform_content(self):
        # Example content added to the pform frame
        
        q="select * from rooms"#'show tables'
        cur=conn.cursor()
        cur.execute(q)
        res=cur.fetchall()
        # cnt=0
        for i in res:
            label=tk.Label(self.pform_content_frame,text=i,bg="white" )
            # label.place(relx=0.1,rely=(cnt+1)/10)
            label.pack(pady=5)
            # cnt=cnt+1
        cur.close()

    def on_pform_canvas_configure(self, event):
        # Update the scrollable region of the pform Canvas
        self.pform_canvas.configure(scrollregion=self.pform_canvas.bbox('all'))


    def on_room_canvas_configure(self, event):
        # Update the scrollable region of the room Canvas
        self.room_canvas.configure(scrollregion=self.room_canvas.bbox('all'))
    def add_currpat_content(self):
        
        conn2 = mysql.connector.connect(
             host="localhost",
             user="root",
             password="root",
             database="dbmsproj"
         )
        
         
        query="select empid,name,contact,email,age,salary,languages from doctors"
        cur=conn2.cursor()
        cur.execute(query)
        records=cur.fetchall()
        # self.root2 = tk.Tk()
        # self.root.title("Employee Records")
        # self.root2=tk.Frame(self.recep,width=1200,height=400)
        # self.root2.place(relx=0.1,rely=0.7)
        self.patients_frame = tk.Frame(self.currpat, width=1200, height=450)
        self.patients_frame.place(relx=0.005, rely=0.055)
        
        # self.close = tk.Button(self.patients_frame, text='x', font='bold', bg="white", width=2, command=lambda: self.patients_frame.place_forget())
        # self.close.place(relx=0.97, rely=0)
        
        columns = ("id", "name", "age", "gender", "contact_number", "address", "registration_date","doctor id","doctor")
        patients_treeview = ttk.Treeview(self.patients_frame, columns=columns, show="headings")
        patients_treeview.place(relx=0, rely=0)
        
        # Set column headings
        patients_treeview.heading("id", text="ID")
        patients_treeview.heading("name", text="Name")
        patients_treeview.heading("age", text="Age")
        patients_treeview.heading("gender", text="Gender")
        patients_treeview.heading("contact_number", text="Contact Number")
        patients_treeview.heading("address", text="Address")
        patients_treeview.heading("registration_date", text="Registration Date")
        patients_treeview.heading("doctor id", text="doctor id")
        patients_treeview.heading("doctor", text="doctor")
        
        # Set column widths
        patients_treeview.column("id", width=50)
        patients_treeview.column("name", width=120)
        patients_treeview.column("age", width=50)
        patients_treeview.column("gender", width=70)
        patients_treeview.column("contact_number", width=120)
        patients_treeview.column("address", width=150)
        patients_treeview.column("registration_date", width=100)
        patients_treeview.column("doctor id", width=100)
        patients_treeview.column("doctor", width=100)
        # Fetch data from the "patients" table in MySQL
        cur = conn.cursor()
        query = "SELECT * FROM patients"
        cur.execute(query)
        data = cur.fetchall()
        
        # Insert the fetched data into treeview
        for item in data:
            patients_treeview.insert("", tk.END, values=item)
        
        cur.close()

            

    def on_currpat_canvas_configure(self, event):
        # Update the scrollable region of the pform Canvas
        self.currpat_canvas.configure(scrollregion=self.currpat_canvas.bbox('all'))
        
    #222222222222222222222222222222222222222222222222222222222222222222222
    def create_account(self):
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="root",
          database="dbmsproj"
        ) 
        mycursor = mydb.cursor()

         #defining SQL query
        sql = "INSERT INTO employee (emp_id, emp_name, age, gender, post, department, hosp_id, phone, email, join_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        flag=True
        emp_id = self.emp_id_entry.get()
        emp_name = self.emp_name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()
        post = self.post_entry.get()
        department = self.department_entry.get()
        hosp_id = self.hosp_id_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        join_date = self.join_date_entry.get()
        
        # Add necessary constraints/validation here
        if not emp_id or not emp_name or not age or not gender or not post or not department or not hosp_id or not phone or not email or not join_date:
            showerror=("Please fill in all fields.")
            # self.mess1agebox.place(relx=0.8,rely=0.6)
            # self.createacc.after(3000,lambda:messagebox.place_forget())
            messagebox.showinfo("error", showerror)
            flag=False
        # Additional constraints can be added here
        if not emp_id.isdigit():
            showerror=("Employee ID must be a numeric value.")
            # self.messagebox=tk.Label(self.createacc,text=showerror)
            # self.messagebox.place(relx=0.8,rely=0.6)
            # self.createacc.after(3000,lambda:messagebox.place_forget())
            messagebox.showinfo("error", showerror)
            flag=False
            
        if not age.isdigit() or int(age) < 18 or int(age) > 100:
            showerror=("Age must be a numeric value between 18 and 100.")
            # self.messagebox=tk.Label(text=showerror)
            # self.createacc.after(3000,lambda:messagebox.place_forget())
            messagebox.showinfo("error", showerror)
            flag=False
    
        # If all constraints are satisfied, perform further actions
        # For example, you can save the employee details to a database or display a success message
        if(flag):
            messagebox.showinfo("Success", "Account created successfully!")
            val=(emp_id,emp_name,age,gender,post,department,hosp_id,phone,email,join_date)
            mycursor.execute(sql,val)
            mydb.commit()
    def getusers(self):
        global cursor
        self.frame2.place(relx=0.7,rely=0.2)
        self.yob.place_forget()
        self.yob2.place_forget()
        self.yob2.place(relx=0.27,rely=0.8)
        cursor = conn.cursor()
        text="select * from logins2"#input("enter query: ")
        cursor.execute(text)
        table_data = cursor.fetchall()
        # cursor.execute("desc hospital")
        # table_data = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        
        # Create the column name row
        for i in range(len(column_names)):
            label = tk.Label(self.frame2, text=column_names[i], borderwidth=1, relief="solid")
            label.grid(row=1, column=i)
        # Create a for loop to create the table
        for i in range(len(table_data)):
            for j in range(len(table_data[i])):
                label = tk.Label(self.frame2, text=table_data[i][j], borderwidth=0, relief="solid")
                label.grid(row=i+2, column=j)
        # Close the database connection
        cursor.close()
        conn.close()
    def removeusers(self):
        # self.frame2.place_forget()
        self.frame2.place_forget()
        self.yob.place(relx=0.15,rely=0.8)
        self.yob2.place_forget()
            
    def logtocrt(self):
        self.loginframe.place_forget()
        self.root.config(bg="#abed9a")
        self.frame.config(bg="#79bd68")
        self.createacc.place(relx=0.33,rely=0.5,anchor="center")
    def crttolog(self):
        self.createacc.place_forget()
        self.root.config(bg="#dfe080")
        self.frame.config(bg="#ebf097")
        self.loginframe.place(relx=0.33,rely=0.5,anchor="center")

    def store_data(self):
        #creating database connection
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="root",
          database="tkinterprac"
        )
        #creating cursor object
        mycursor = mydb.cursor()

        #defining SQL query
        sql = "INSERT INTO logins2 (username password) VALUES (%s, %s)"

        #getting values from input boxes
        username = self.usernamein.get()
        password = self.passwordin.get()
        email = self.emailin.get()
        self.u=tk.Label(self.frame,text=username)
        self.u.place(relx=0.5,rely=0.5)
        self.p=tk.Label(self.frame,text=password)
        self.p.place(relx=0.5,rely=0.6)
        self.e=tk.Label(self.frame,text=email)
        self.e.place(relx=0.5,rely=0.7)
        #executing SQL query with values
        val = (username, password)
        mycursor.execute(sql, val)

        #committing changes
        mydb.commit()
        self.usernamein.delete(0,'end')
        self.passwordin.delete(0,'end')
        self.emailin.delete(0,'end')
        
        #printing success message
        # print("Data inserted successfully")
        mycursor.close()

app = login()
app.root.mainloop()
