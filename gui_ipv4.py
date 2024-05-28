from os import startfile
import tkinter as tk
from tkinter import Frame, Label, Tk, ttk
from tkinter import PhotoImage
from tkinter.constants import CENTER, FALSE, LEFT, RIDGE, RIGHT, TRUE

from tkinter.messagebox import showinfo
from tkinter import messagebox
from typing import Text

from datetime import datetime

from ipv4 import IPV4 
import random


ip = ""
mask = ""
clicked_the_check_button = 0

nid = ""
bc = ""
first_ip = ""
last_ip = ""
    
# Fenster:window
window = tk.Tk()
window.geometry("500x750+400+100")
window.resizable(FALSE, FALSE)
window.title('Netzberechnung')


# icon = PhotoImage(file="./pics/bin.png")
# window.iconphoto(True, icon)

def bin2dez(bin):
    # bin2dez wandelt eine Binärzahl in eine Dezimalzahl um
    
    # Horner-Schema:   
    # der Wert der ersten Ziffer als Anfangswert nehmen
    # danach schrittweise das Ergebnis aus dem vorigen Schritt mit 2 multipliziert
    # und die nächste Ziffer addieren bis alle Ziffern aufgebraucht sind.
   
    ergebnis_dez = 0

    # for zahl in bin:  TIPP von Hr. Mörl:
        # eleganter als for i in range(len(bin)):
    for ziffer in bin:
        if ziffer != '1' and ziffer != '0':
            # Falscheingabe?
            raise TypeError('Binärzahl hat falsches Format')
        ergebnis_dez = ergebnis_dez * 2 + int(ziffer)
    return ergebnis_dez

def createIP(ip):
    # teilt eine 32er Zeichenkette in 4 Oktette und wandelt die einzelnen Oktette in eine Dezimalzahl 
    
    okt_1 = ip[0:8]
    okt_2 = ip[8:16]
    okt_3 = ip[16:24]
    okt_4 = ip[24:32]

    okt_1 = bin2dez(okt_1)
    okt_2 = bin2dez(okt_2)
    okt_3 = bin2dez(okt_3)
    okt_4 = bin2dez(okt_4)

    ges_Okt = str(okt_1) + "." + str(okt_2) + "." + str(okt_3) + "." + str(okt_4)
    
    return ges_Okt

def createMask(cidr):
    
    # Anhand von der Zahl nach "/" (Eingabe des users) 
    # werden so viele  1er erstellt und der Rest mit Nullen aufgefüllt (32-Ziffern)

    if cidr < 0 or cidr > 32:
        print("falsche Eingabe der Maske")
        
    cidr1 = 32-cidr

    mask = ""
    # Erstellen der Einser anhand der cidr
    while cidr > 0:
        mask = mask + "1"
        cidr -= 1
    
    # Erstellen der Nullen anhand von 32-cidr
    while cidr1 > 0:
        mask = mask + "0"
        cidr1 -= 1
    
    # 
    maske = createIP(mask)
    
    return mask   

def createRandomAdress(ran_ip, ran_cidr):
    # es werden 4 Oktette erstellt und zu einer IP-Adresse zusammengeführt

    okt1 = str(random.randint(0,255))
    okt2 = str(random.randint(0,255))
    okt3 = str(random.randint(0,255))
    okt4 = str(random.randint(0,255))

    ran_ip = okt1 + "." + okt2 + "." + okt3 + "." + okt4

    # es wird ein cidr erstellt, um eine Maske zu berechnen
    ran_cidr = random.randint(4,30) # ein cidr zw. /4 und /30
    ran_cidr = createMask(ran_cidr)
    ran_mask = createIP(ran_cidr)

    return ran_ip, ran_mask 

def newExercise():
    msg_box = messagebox.askquestion("neue Übung", "Wollen Sie eine neue Übung starten?")
    if msg_box == "yes":
        new()

# def sent_adress():
    
#     print(admin_ip.get())
#     print(admin_mask.get())
   
#     # adresse = IPV4(admin_ip.get(), admin_mask.get())

#     label_ip["text"] = admin_ip
#     label_mask["text"] = admin_mask

#     # nid = adresse.get_nid()
#     # bc = adresse.get_bc()
#     # first_ip = adresse.get_first()
#     # last_ip = adresse.get_last()



# def adminMode():
#     admin_window = tk.Tk()
#     admin_window.geometry("300x200")
#     admin_window.title("Eingabe IP & MASKE")

#     admin_ip_Frame = ttk.Frame(admin_window)
#     admin_ip_Frame.pack()

#     admin_ip_label =  ttk.Label(admin_ip_Frame, text="IP:", font="consolas, 20")
#     admin_ip_label.pack()

#     admin_ip_entry = ttk.Entry(admin_ip_Frame, textvariable=admin_ip, font="consolas, 15",)
#     admin_ip_entry.pack(fill='x',pady=5, side=LEFT)
#     admin_ip_entry.focus()

#     admin_mask_Frame = ttk.Frame(admin_window)
#     admin_mask_Frame.pack()

#     admin_mask_label =  ttk.Label(admin_mask_Frame, text="Maske:", font="consolas, 20")
#     admin_mask_label.pack()

#     admin_ip_entry = ttk.Entry(admin_mask_Frame, textvariable=admin_mask, font="consolas, 15",)
#     admin_ip_entry.pack(fill='x',pady=5, side=LEFT)
#     admin_ip_entry.focus()


#     admin_button_frame = ttk.Frame(admin_window)
#     admin_button_frame.pack()

#     # admin sent button
#     admin_sent_button = ttk.Button(admin_button_frame, text="übertragen", command=sent_adress)
#     admin_sent_button.pack(pady=10)

#     admin_window.mainloop()
    

def endExercise():
    msg_box = messagebox.askquestion("Übung beenden?", "sind Sie sicher, dass die Übung beenden möchten?")
    if msg_box == "yes":
        window.destroy()

def showSolution():
    msg_box = messagebox.askquestion("Lösung", "Wollen Sie die Lösungen anzeigen?")
    if msg_box == "yes":
        with open("statistik.txt", "a") as file:
            file.write("Lösung benutzt\n")
        aktivateSolution()     

def showMessageLabel():
    
    check_list = [0,0,0,0]
    soll_list = [1,1,1,1]
    stats = 0.00

    if user_nid.get() != nid:
        nid_solution_label["text"] = "die eingegebene NID ist nicht korrekt"
        check_list[0] = 0
        stats += 0.0 
    else:
        nid_solution_label["text"] = "sehr gut gemacht!"
        check_list[0] = 1
        stats += 0.25
    
    if user_bc.get() != bc:
        bc_solution_label["text"] = "der eingegebene BC ist nicht korrekt"
        check_list[1] = 0
        stats += 0.0 
    else:
        bc_solution_label["text"] = "sehr gut gemacht!"
        check_list[1] = 1
        stats += 0.25
    
    if user_first.get() != first_ip:
        first_solution_label["text"] = "die eingegebene ERSTE ADRESSE ist nicht korrekt"
        check_list[2] = 0
        stats += 0.0
    else:
        first_solution_label["text"] = "sehr gut gemacht!"
        check_list[2] = 1
        stats += 0.25
    
    if user_last.get() != last_ip:
        last_solution_label["text"] = "die eingegebene LETZTE ADRESSE ist nicht korrekt"
        check_list[3] = 0
        stats += 0.0
    else:
        last_solution_label["text"] = "sehr gut gemacht!"
        check_list[3] = 1
        stats += 0.25

    stats = stats * 100
    with open("statistik.txt", "a") as file:
        file.write(str(stats) + " %\n")
    
    if check_list == soll_list:
        # msg = f'User_NID: {user_nid.get()} richtig ist {nid}\nUser BC: {bc_entry.get()} richtig ist {bc}\nUser 1.: {first_entry.get()} richtig ist {first_ip}\nUser L.: {last_entry.get()} richtig ist {last_ip}'
        msg = "Super gemacht! Sie haben alles richtig berechnet" 
        showinfo(
            title='Glückwunsch',
            message=msg
        )
        
def check_clicked():

    global clicked_the_check_button
    clicked_the_check_button += 1

    with open("statistik.txt", "a") as file:
        file.write(str(clicked_the_check_button)+". Versuch: ")
    
    
    # ------------------ check NID ----------------------
    checked = 0

    # hier wird überprüft, ob eine Eingabe mit 3 Punkten eingegeben wurde 
    count = 0
    for char in user_nid.get():
        if char == ".":
            count += 1
    
    if count == 3: 
        # hier wird überprüft, ob die einzelnen Werte zwischen den Punkten  (".") kleiner 0 oder größer 255 sind
        a,b,c,d = user_nid.get().split(".")
        
        # ist dies der Fall, so wird ein Ausgabefester mit einer Fehlermeldung aufgehen
        if int(a)<0 or int(a)>255:
            showinfo(title="falsche Eingabe",message=f"Fehlerhafte Eingabe im 1.Oktett der NID")
        else:
            checked += 1
        if int(b)<0 or int(b)>255:
            showinfo(title="falsche Eingabe",message=f"Fehlerhafte Eingabe im 2.Oktett der NID")
        else:
            checked += 1
        if int(c)<0 or int(c)>255:
            showinfo(title="falsche Eingabe",message=f"Fehlerhafte Eingabe im 3.Oktett der NID")
        else:
            checked += 1
        if int(d)<0 or int(d)>255:
            showinfo(title="falsche Eingabe",message=f"Fehlerhafte Eingabe im 4.Oktett der NID")
        else:
            checked += 1
    elif user_nid.get() == "":
        showinfo(title="falsche Eingabe",message=f"bitte geben Sie die NID ein")
    else:
        showinfo(title="falsche Eingabe",message=f"Ihre Eingabe der Netzadresse ist Fehlerhaft")

    	# ------------------ check BC ----------------------    

    count = 0
    for char in user_bc.get():
        if char == ".":
            count += 1
    
    if count == 3: 
        # hier wird überprüft, ob die einzelnen Werte zwischen den Punkten  (".") kleiner 0 oder größer 255 sind
        e,f,g,h = user_bc.get().split(".")
        
        # ist dies der Fall, so wird ein Ausgabefester mit einer Fehlermeldung aufgehen
        if int(e)<0 or int(e)>255:
            showinfo(title="falsche Eingabe",message=f"Fehlerhafte Eingabe im 1.Oktett der BC")

        else:
            checked += 1
        if int(f)<0 or int(f)>255:
            showinfo(title="falsche Eingabe",message=f"Fehlerhafte Eingabe im 2.Oktett der BC")
        else:
            checked += 1
        if int(g)<0 or int(g)>255:
            showinfo(title="falsche Eingabe",message=f"Fehlerhafte Eingabe im 3.Oktett der BC")
        else:
            checked += 1
        if int(h)<0 or int(h)>255:
            showinfo(title="falsche Eingabe",message=f"Fehlerhafte Eingabe im 4.Oktett der BC")
        else:
            checked += 1
    elif user_bc.get() == "":
        showinfo(title="falsche Eingabe",message=f"bitte geben Sie die BC ein")
    else:
        showinfo(title="falsche Eingabe",message=f"Ihre Eingabe des Breodcasts ist Fehlerhaft")

    # ------------------ check first ----------------------

    count = 0
    for char in user_first.get():
        if char == ".":
            count += 1
    
    if count == 3:
        # hier wird überprüft, ob die einzelnen Werte zwischen den Punkten  (".") kleiner 0 oder größer 255 sind
        i,j,k,l = user_first.get().split(".")
        
        # ist dies der Fall, so wird ein Ausgabefester mit einer Fehlermeldung aufgehen
        if int(i)<0 or int(i)>255:
            showinfo(title="falsche Eingabe",message=f"Fehlerhafte Eingabe im 1.Oktett der erste Adresse")
        else:
            checked += 1        
        if int(j)<0 or int(j)>255:
            showinfo(title="falsche Eingabe",message=f"Fehlerhafte Eingabe im 2.Oktett der erste Adresse")
        else:
            checked += 1        
        if int(k)<0 or int(k)>255:
            showinfo(title="falsche Eingabe",message=f"Fehlerhafte Eingabe im 3.Oktett der erste Adresse")
        else:
            checked += 1        
        if int(l)<0 or int(l)>255:
            showinfo(title="falsche Eingabe",message=f"Fehlerhafte Eingabe im 4.Oktett der erste Adresse")
        else:
            checked += 1    
    elif user_first.get() == "":
        showinfo(title="falsche Eingabe",message=f"bitte geben Sie die erste Adresse ein")
    else:
        showinfo(title="falsche Eingabe",message=f"Ihre Eingabe der ersten Adresse ist Fehlerhaft")

    # ------------------ check last ----------------------

    count = 0
    for char in user_last.get():
        if char == ".":
            count += 1
    
    if count == 3:
        # hier wird überprüft, ob die einzelnen Werte zwischen den Punkten  (".") kleiner 0 oder größer 255 sind
        m,n,o,p = user_last.get().split(".")
        
        # ist dies der Fall, so wird ein Ausgabefester mit einer Fehlermeldung aufgehen
        if int(m)<0 or int(m)>255:
            showinfo(title="falsche Eingabe",message=f"Fehlerhafte Eingabe im 1.Oktett der letzten Adresse")
        else:
            checked += 1        
        if int(n)<0 or int(n)>255:
            showinfo(title="falsche Eingabe",message=f"Fehlerhafte Eingabe im 2.Oktett der letzten Adresse")
        else:
            checked += 1        
        if int(o)<0 or int(o)>255:
            showinfo(title="falsche Eingabe",message=f"Fehlerhafte Eingabe im 3.Oktett der letzten Adresse")
        else:
            checked += 1        
        if int(p)<0 or int(p)>255:
            showinfo(title="falsche Eingabe",message=f"Fehlerhafte Eingabe im 4.Oktett der letzten Adresse")
        else:
            checked += 1    
    elif user_last.get() == "":
        showinfo(title="falsche Eingabe",message=f"bitte geben Sie die letzte Adresse ein")
    else:
        showinfo(title="falsche Eingabe",message=f"Ihre Eingabe der letzten Adresse ist Fehlerhaft")

    if checked == 16:
        showMessageLabel()
    



    # nid_solution_label["text"] = nid
    # bc_solution_label["text"] = bc 
    # first_solution_label["text"] = first_ip 
    # last_solution_label["text"] = last_ip

    # check_list = [0,0,0,0]
    # soll_list = [1,1,1,1]

    # if user_nid.get() != nid:
    #     nid_solution_label["text"] = "die eingegebene NID ist nicht korrekt"
    #     check_list[0] = 0
    # else:
    #     nid_solution_label["text"] = "sehr gut gemacht!"
    #     check_list[0] = 1
    
    # if user_bc.get() != bc:
    #     bc_solution_label["text"] = "der eingegebene BC ist nicht korrekt"
    #     check_list[1] = 0
    # else:
    #     bc_solution_label["text"] = "sehr gut gemacht!"
    #     check_list[1] = 1
    
    # if user_first.get() != first_ip:
    #     first_solution_label["text"] = "die eingegebene ERSTE ADRESSE ist nicht korrekt"
    #     check_list[2] = 0
    # else:
    #     first_solution_label["text"] = "sehr gut gemacht!"
    #     check_list[2] = 1
    
    # if user_last.get() != last_ip:
    #     last_solution_label["text"] = "die eingegebene LETZTE ADRESSE ist nicht korrekt"
    #     check_list[3] = 0
    # else:
    #     last_solution_label["text"] = "sehr gut gemacht!"
    #     check_list[3] = 1
        
def aktivateSolution():
    nid_solution_label["text"] = nid
    bc_solution_label["text"] = bc 
    first_solution_label["text"] = first_ip 
    last_solution_label["text"] = last_ip
    
def startExercise():
    global ip
    global mask

    ip, mask = createRandomAdress(ip, mask)
    
    with open("statistik.txt", "a") as file:
        file.write("\n\nÜbung vom "+str(datetime.now())+"\n")
    with open("statistik.txt", "a") as file:
        file.write("IP: " + ip + "\n")
    with open("statistik.txt", "a") as file:
        file.write("Maske: " + mask + "\n")

    adresse = IPV4(ip, mask)
    global nid
    global bc
    global first_ip
    global last_ip
    
    nid = adresse.get_nid()
    bc = adresse.get_bc()
    first_ip = adresse.get_first()
    last_ip = adresse.get_last()

    return ip, mask

def new():
    global ip
    global mask

    nid_entry.delete(0,"end")
    bc_entry.delete(0,"end")
    first_entry.delete(0,"end")
    last_entry.delete(0,"end")
    
    nid_solution_label["text"] = ""
    bc_solution_label["text"] = ""
    first_solution_label["text"] = "" 
    last_solution_label["text"] = ""
    
    
    ip, mask = startExercise()
    adresse = IPV4(ip, mask)

    label_ip["text"] = ip
    label_mask["text"] = mask

def saveStats(stats):
    statistic = stats * 100
    stats_text = str(statistic)

    with open("statistik.txt", "a") as file:
        file.write(stats_text)

# speichere die User-Eingaben
user_nid = tk.StringVar()
user_bc = tk.StringVar()
user_first = tk.StringVar()
user_last = tk.StringVar()

admin_ip = tk.StringVar()
admin_mask = tk.StringVar()

# Netzberechnung frame
netzberechnung = ttk.Frame(window)
netzberechnung.pack(padx=10,pady=10,fill='x',expand=True)

ip, mask = startExercise()

#memo an mich: genauere Ausrichtung der Entrys 
# NID -----------------------------------------------------------------
random_frame = ttk.Frame(netzberechnung)
random_frame.pack()

text_ip = ip
label_ip = ttk.Label(random_frame, text=text_ip, font="consolas, 30")
label_ip.pack()

text_mask = mask
label_mask = ttk.Label(random_frame, text=text_mask+"\n", font="consolas, 30")
label_mask.pack()


# NID -----------------------------------------------------------------
nid_bool = FALSE

nid_frame = ttk.Frame(netzberechnung)
nid_frame.pack()

nid_label = ttk.Label(nid_frame, text="Netzadresse: ", justify="left", font="consolas, 15")
nid_label.pack(pady=5, fill='x')

nid_entry = ttk.Entry(nid_frame,textvariable=user_nid, font="consolas, 20",)
nid_entry.pack(fill='x',pady=5, side=LEFT)
nid_entry.focus()

nid_solution_label = ttk.Label(netzberechnung, text="")
nid_solution_label.pack()



# BC ------------------------------------<-----------------------------
bc_frame = ttk.Frame(netzberechnung)
bc_frame.pack()

bc_label = ttk.Label(bc_frame, text="Broadcast: ", justify="left", font="consolas, 15")
bc_label.pack(pady=5, fill='x', expand=True)

bc_entry = ttk.Entry(bc_frame,textvariable=user_bc, font="consolas, 20",)
bc_entry.pack(fill='x',expand=True, pady=5,  side=LEFT)
bc_entry.focus()

bc_solution_label = ttk.Label(netzberechnung, text="")
bc_solution_label.pack()

# First Adress -----------------------------------------------------------------
first_frame = ttk.Frame(netzberechnung)
first_frame.pack()

first_label = ttk.Label(first_frame, text="1. Adresse: ", justify="left", font="consolas, 15")
first_label.pack(pady=5, fill='x', expand=True)

first_entry = ttk.Entry(first_frame,textvariable=user_first, font="consolas, 20",)
first_entry.pack(fill='x',expand=True, pady=5,  side=LEFT)
first_entry.focus()

first_solution_label = ttk.Label(netzberechnung, text="")
first_solution_label.pack()

# Last Adress -----------------------------------------------------------------
last_frame = ttk.Frame(netzberechnung)
last_frame.pack()

last_label = ttk.Label(last_frame, text="Letzte Adresse: ", justify="left", font="consolas, 15")
last_label.pack(pady=5, fill='x', expand=True)

last_entry = ttk.Entry(last_frame,textvariable=user_last, font="consolas, 20",)
last_entry.pack(fill='x',expand=True, pady=5,  side=LEFT)
last_entry.focus()

last_solution_label = ttk.Label(netzberechnung, text="")
last_solution_label.pack()

# BUTTONS-----------------------------------------------------------------------

button_frame1 = ttk.Frame(netzberechnung)
button_frame1.pack()

button_frame2 = ttk.Frame(netzberechnung)
button_frame2.pack()

button_frame3 = ttk.Frame(netzberechnung)
button_frame3.pack()

# neu button
check_button = ttk.Button(button_frame1, text="neu", command=newExercise)
check_button.pack(pady=10,side="left")

# check button
check_button = ttk.Button(button_frame1, text="check", command=check_clicked)
check_button.pack(pady=10)

# Lösung button
check_button = ttk.Button(button_frame2, text="Lösung", command=showSolution)
check_button.pack(pady=10, side="left")

# Beenden button
check_button = ttk.Button(button_frame2, text="Beenden", command=endExercise)
check_button.pack(pady=10)

# # AdminMode button
# check_button = ttk.Button(button_frame3, text="Admin", command=adminMode)
# check_button.pack(pady=10)




# ----------------------------------------------------------------------------

window.mainloop()