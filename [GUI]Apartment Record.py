__author__ = "Teeraphat Kullanankanjana"
__version__ = "Prototype 0.0.0"

from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from datetime import date


def on_click():
    try:
        room_number, room_price, elect_price, water_price, service, year = e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get()
        month_name, internet_number = combo1.get(), combo2.get()
        if int(room_number) < 0 or int(room_price) < 0 or int(elect_price) < 0 or int(water_price) < 0 or \
                int(service) < 0 or int(year) < 0 or int(internet_number) < 0 or month_name not in month_list_TH:
            msg.showerror("แจ้งเตือน", "บันทึกรายการล้มเหลว\nการป้อนค่าไม่ถูกต้อง\nกรุณาลองใหม่")
        else:
            file_name = "ใบแจ้งหนี้เดือน" + str(month_name) + str(year) + ".txt"
            fo = open(str(file_name), "w+", encoding="utf-8")
            fo.write("\t\t\tใบแจ้งหนี้/ใบเสร็จรับเงิน\nหมายเลขห้อง: " + str(room_number) + "\t\t\t\t\t"+"ยอดชำระเดือน: "+str(month_name)+" "+str(year)+"\nลงวันที่บันทึก: "+str(date.today().strftime("%b-%d-%Y"))+"\n")
            fo.write("____________________\n")
            fo.write("รายการที่ต้องชำระ\n")
            fo.write("ลำดับที่\t\t\tรายการ\t\t\t\t\t\tราคา(บาท)\n")
            fo.write("1\t\t\t\tค่าห้อง"+"\t\t\t\t\t\t"+str(room_price)+"\n")
            fo.write("2\t\t\t\tค่าไฟฟ้า"+"\t\t\t\t\t\t"+str(elect_price)+"\n")
            fo.write("3\t\t\t\tค่าไฟฟ้า"+"\t\t\t\t\t\t"+str(water_price)+"\n")
            fo.write("4\t\t\t\tค่าบริการ"+"\t\t\t\t\t\t"+str(water_price)+"\n")
            fo.write("5\t\t\t\tค่าอินเตอร์เน็ต"+"\t\t\t\t\t"+str(int(internet_number)*250)+"\n")
            fo.write("____________________\nรวมทั้งสิ้น "+str(int(room_price)+int(elect_price)+int(water_price)+int(service)+int(internet_number)*250)+" บาท\n")
            fo.close()
            msg.showinfo("แจ้งเตือน", "บันทึกรายการเสร็จสิ้น")
    except(ValueError or TypeError):
        msg.showerror("พบข้อผิดพลาด", "บันทึกรายการล้มเหลว\nการป้อนค่าไม่ถูกต้อง\nกรุณาลองใหม่")


root = Tk()
root.title("Recorder")
root.resizable(width=FALSE, height=FALSE)
month_list_TH = ("มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน",
                 "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม")
number_internet_list = ("0", "1", "2", "3", "4",
                        "5", "6", "7", "8", "9", "10")
L1 = LabelFrame(root).grid()
L2 = LabelFrame(root).grid()
L3 = LabelFrame(root).grid()
Label(L1, text="\nข้อมูลทั่วไป").grid(row=0, sticky=W)
Label(L1, text="หมายเลขห้อง").grid(row=1, sticky=W)
Label(L1, text="กรุณาเลือกเดือนที่ชำระ").grid(row=2, sticky=W)
Label(L1, text="ปีที่ต้องชำระ").grid(row=3, sticky=W)
Label(L2, text="\nรายการค่าชำระ").grid(row=4, sticky=W)
Label(L2, text="1.ค่าห้อง(บาท)").grid(row=5, sticky=W)
Label(L2, text="2.ค่าไฟฟ้า(บาท)").grid(row=6, sticky=W)
Label(L2, text="3.ค่าน้ำ(บาท)").grid(row=7, sticky=W)
Label(L2, text="4.ค่าบริการ(บาท)").grid(row=8, sticky=W)
Label(L2, text="5.ค่าอินเตอร์เน็ต(ใบ)").grid(row=9, sticky=W)

e1 = Entry(L1)
e1.grid(row=1, column=1)  # room number
e6 = Entry(L1)
e6.grid(row=3, column=1)  # year
e2 = Entry(L2)
e2.grid(row=5, column=1)  # room price
e3 = Entry(L2)
e3.grid(row=6, column=1)  # elect price
e4 = Entry(L2)
e4.grid(row=7, column=1)  # water price
e5 = Entry(L2)
e5.grid(row=8, column=1)  # service

combo1 = ttk.Combobox(L1, textvariable="month_list_TH", width=17)
combo1["values"] = month_list_TH
combo1.grid(row=2, column=1)

combo2 = ttk.Combobox(L1, textvariable=number_internet_list, width=17)
combo2["values"] = number_internet_list
combo2.grid(row=9, column=1)

b1 = Button(L3, text="\nบันทึกรายการ\n", command=on_click).grid(row=10)
root.mainloop()
