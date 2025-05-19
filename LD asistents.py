import csv

def iegut_ievadi():
    print("Ķīmijas LD asistents – Titrēšana")
    tilpums = float(input("Ievadi titrējamā šķidruma tilpumu (ml): "))
    konc = float(input("Ievadi koncentrāciju (mol/l): "))
    return tilpums, konc

def simulēt_datus(tilpums):
    dati = [["Laiks (s)", "pH", "Tilpums (ml)"]]
    for i in range(4):
        laiks = i * 10
        tilp = round(i * tilpums / 3, 2)
        ph = round(2.5 + 2.3 * i, 2)
        dati.append([laiks, ph, tilp])
    return dati

def saglabat_csv(dati, faila_nosaukums="rezultati.csv"):
    with open(faila_nosaukums, "w", newline="") as f:
        rakstitajs = csv.writer(f)
        rakstitajs.writerows(dati)
    print(f"Dati saglabāti failā {faila_nosaukums}")

def galvena():
    tilpums, konc = iegut_ievadi()
    dati = simulēt_datus(tilpums)
    saglabat_csv(dati)

if __name__ == "__main__":
    galvena()
