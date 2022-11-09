#การคำนวณระยะห่าง
    #เมื่อสถานีอยู่สายเดียวกัน ระยะห่างระหว่างสถานีคือเลขลบกัน
    #เมื่อสถานีอยู่ต่างสาย ระยะห่างระหว่างสถานีคือเลขสถานีบวกกัน
    #ดังนั้นจึงควรแยกรับข้อมูลออกเป็นตัวแปร 4 ตัว คือรหัสและเลขสถานีของทั้งต้นทางและปลายทาง

#ส่วนเดิม หมายถึงสถานีดังต่อไปนี***
    # สยาม (C0)
    #ราชเทวี (N1) - หมอชิต (N8) ไม่มีส้วนต่อขยาย
    #ชิดลม (E1) - อ่อนนุช (E9)
    #ราชดำริ (S1) - วงเวียนใหญ่ (S8)
    #สนามกีฬาแห่งชาติ (W1)




print("Welcome to BTS Skytrain.")
print("Please enter your Beginning and Terminal station.")

startC = input("from")
startN = int(input("number"))
stopC = input("to")
stopN = int(input("number"))


Originalstart = startC == 'C' and startN == 0 \
                    or startC == 'N' and 1 <= startN <= 8 \
                    or startC == 'E' and 1 <= startN <= 9 \
                    or startC == 'S' and 1 <= startN <= 8 \
                    or startC == 'W' and startN == 1
Originalstop = stopC == 'C' and stopN == 0 \
                    or stopC == 'N' and 1 <= stopN <= 8 \
                    or stopC == 'E' and 1 <= stopN <= 9 \
                    or stopC == 'S' and 1 <= stopN <= 8 \
                    or stopC == 'W' and stopN == 1
Originalroute = Originalstart or Originalstop

Normprice = 0
#เดินทางในส่วนเดิม
if Originalroute :
    #เดินทางในส่วนตากสินถึงววญ
    if startC == "S" and stopC == "S" and startN >= 6 and stopN >= 6 :
        #คิดราคาช่วงตากสินถึงววญ
        Normprice = 16
    #ระยะทาง
    if startC == stopC :
        distance = abs(startN - stopN)
    elif startC != stopC :
        distance = startN + stopN
        #คิดราคา
        if distance == 0 :
            Normprice == 16
        if distance == 1 :
            Normprice = 16
        elif distance == 2 :
            Normprice = 23
        elif distance == 3 :
            Normprice = 26
        elif distance == 4 :
            Normprice = 30
        elif distance == 5 : 
            Normprice = 33
        elif distance == 6 :
            Normprice = 37
        elif distance >= 7 :
            Normprice = 44 

Extprice = 0
#มีการเดินทางส่วนต่อขยาย
Extendedstart = startC == 'E' and 10 <= startN <= 23 \
                    or startC == 'S' and 9 <= startN <= 12
Extendedstop = stopC == 'E' and 10 <= stopN <= 23 \
                    or stopC == 'S' and 9 <= stopN <= 12
Extendedroute = Extendedstart or Extendedstop 
#คิดราคาส่วนต่อขยาย
if Extendedroute :
    #ช่วงสำโรงเคหะ
    if startC == "E" and 15 <= startN <= 23 and stopC =="E" and 15 <= stopN <= 23 :
        Extprice = 0
    #ช่วงอื่นๆ
    else :
        Extprice = 15 
        #กรณีที่เดินทางจากส่วนต่อขยายเส้นนึง ไปจนถึงส่วนต่อขยายอีกเส้น
        if Extendedstart and Extendedstop :
            Extprice = Extprice + 44

Totalprice = Normprice + Extprice 
print(("Please pay") , Totalprice , ("Bath"))