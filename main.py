
garums = float(input("garums:"))
platums = float(input("platums:"))
augstums = float(input("augstums:"))
skaits = int(input("sKAITS:"))
tips = input(":")

  
def materialaUzskaite(tips, izmers1, izmers2, skaits):
    if tips == "Finieris":
      print(izmers1, izmers2)
    if tips == "Liste":
      print(izmers1)
    if tips  == "Sturis":
      print("Vērtības nav svarīgas")
    return None


materialaUzskaite(tips, garums, platums, augstums)
