print("Programm zur Notenschnittberrechnung")
note=0
zeahler=0
summe=0
print("Tippen sie '-1' als abbruchparameiter ein")
while note != -1:
    zeahler=zeahler+1
    message= "Geben sie Ihre " + str(zeahler) + ". Note ein:"
    note=int(input(message))
    if note!= -1:
        summe = summe + note
    #print(summe)
print("Dein Notendurchschnitt ist:",summe/zeahler)