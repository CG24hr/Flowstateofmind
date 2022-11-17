import matplotlib.pyplot as plt

#Monthly Sales - ยอดขายประจำเดือน
def monthlySales ():
  
  weekDay = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
  existingReport = [1500,2000,1000,1200,2100,1000,3000,1800,2500,2100,3400,1700,2600,3300,1500,2900,3100,1400,2500,1600,2700]
  week4Report = []
  dayCount = 0

  #เริ่มระบบสรุปยอดขาย
  print('Welcome to Sales Report')
  print('Enter Daily Sales Amount (Baht):')
  print()

  #วนรับข้อมูล
  while dayCount < 7:
    dailySales = int(input(weekDay[dayCount] + ':'))
    week4Report.append(dailySales)
    dayCount = dayCount + 1

  #รวมข้อมูลเป็น list รายเดือน
  monthlyReport = existingReport + week4Report

  #สรุปข้อมูลยอดรายเดือน
  print()
  print('Your Monthly Sales Report:')
  print('Total Sales:', sum(monthlyReport))
  print('Daily Average:', (sum(monthlyReport)/len(monthlyReport)))

  #รับข้อมูลเพื่อดูข้อมูลรายสัปดาห์
  print()
  infoWeekReport = int(input('Enter week number (1-4) to see more weekly details - Press 0 to Exit'))

  #วนรับข้อมูล
  while infoWeekReport != 0:
  
    #เงื่อนไขการดูข้อมูลรายสัปดาห์
    if 1<=infoWeekReport<=4:
      weekReport = monthlyReport[(infoWeekReport-1)*7:infoWeekReport*7]
      print('Week',infoWeekReport, 'Sales:', weekReport)
      print('Total Weekly Sales:', sum(weekReport))
      print('Daily Average:', (sum(weekReport)/len(weekReport)))
    else:
      print('Error: Please enter correct information')
  
    print()
    infoWeekReport = int(input('Enter week number (1-4) to see more weekly details - Press 0 to Exit'))

#Product Sales - วิเคราะห์สินค้า
def productSales():
  
  #ตัวแปร
  productList = []
  productTotal = 0
  productPercent = 0

  #อ่านข้อมูลและหาผลรวม
  with open('productReport.txt','r') as productReport:
    for itemNum_itemName_cnt in productReport:
      itemData=itemNum_itemName_cnt.split()
      productList.append(itemData)
      productTotal = productTotal + int(itemData[2])

  print(productList)
  print('Total Product Sales')
  print(productTotal)

  #Plot รายชื่อสินค้า / จำนวนสินค้าที่ขายได้
  productNameList = []
  sellList = []
  for item in productList :
    productNameList.append(item[1])
    sellList.append(int(item[2]))
  plt.plot(productNameList, sellList)
  plt.xticks(rotation = 'vertical')
  plt.show()


  #พิมพ์หัวข้อวิเคราะห์สัดส่วนยอดขาย
  print()
  print('Product Sales Ratio')

  for itemNum_itemName_cnt in productList:
    productPercent = int(itemNum_itemName_cnt[2]) / productTotal * 100
    print(itemNum_itemName_cnt[1], productPercent, '%')
  
  #สร้างเงื่อนไขเพื่อพิมพ์สินค้ายอดขายต่ำกว่ามาตรฐาน
  print()
  productBenchmark = int(input('Level of Underperforming Products?'))
  
  print()  
  print('Underperforming Products (Under', productBenchmark,  '% Sales)') 

  for itemNum_itemName_cnt in productList:
    productPercent = int(itemNum_itemName_cnt[2]) / productTotal * 100
    if productPercent < productBenchmark:
      print(itemNum_itemName_cnt[1],productPercent,'%')
  
  productReport.close()

###กำหนด Parameter
def member(totalPrice, rewardPoint):
  isMember = input('Member? (Y/N):')

  if isMember == 'Y':
    print('Membership Discount : 10% Off!')
    totalPrice = totalPrice * 0.9

    if totalPrice > 500 and totalPrice < 1000 :
      print('Price above 500 : Receive 50 Reward Points')
      rewardPoint = rewardPoint + 50

    elif totalPrice >= 1000 and totalPrice < 5000:
      print('Price above 1,000 : Receive 100 Reward Points')
      rewardPoint = rewardPoint + 100

    elif totalPrice >= 5000:
      print('Price above 5,000 : Receive 500 Reward Points')
      rewardPoint = rewardPoint + 500

    else:
      print('No Reward Points Added')

  else:
    print ('Not a Member')
   
  ###กำหนดค่าส่งกลับ
    return totalPrice, rewardPoint

###กำหนด Parameter
def dailyPromotion(totalPrice):
  purchasedDate = input('What is the day of the week?')

  if purchasedDate == 'Saturday':
    print('Saturday Discount : 20% Off!')
    totalPrice = totalPrice * 0.8

  elif purchasedDate == 'Sunday':
    print('Sunday Discount : 40% Off!')
    totalPrice = totalPrice * 0.6

  elif purchasedDate == 'Monday' or purchasedDate == 'Wednesday':
    print('Special Monday/Wednesday Promotion : 30% Off!')
    totalPrice = totalPrice * 0.7

  else:
    print('No Promotion')

    
  ###กำหนดค่าส่งกลับ
  return totalPrice
#Cashier - คิดเงิน
def cashier():

  rewardPoint = 0
  totalPrice = 0
  itemCount = 0

  print('Welcome to The System : Enter 0 when all the items are entered')

  itemCount = itemCount + 1
  price = int(input('Price '+str(itemCount)+':'))

  while price != 0:

    if itemCount==5:
      print('Special Promotion : Get 5th Item for Free!!')

    else:
      totalPrice = totalPrice + price

    itemCount = itemCount + 1
    price = int(input('Price '+str(itemCount)+':'))

  ###เรียก Parameter และกำหนดตัวแปรรับค่าคืน ของฟังก์ชัน member
  member (totalPrice, rewardPoint)

  ###เรียก Parameter และกำหนดตัวแปรรับค่าคืน ของฟังก์ชัน dailyPromotion
  totalPrice = dailyPromotion (totalPrice) 

  print('Please Pay', totalPrice,'Baht')
  print('Your Total Reward Point is', rewardPoint)
  
 
print('---Welcome to the POS System---')
mode = input('Press 1: Cashier Mode \nPress 2: Monthly Sales Report \nPress 3: Product Sales Report\nPress 0: Exit\n')

while mode != '0':
  if mode == '1':
    cashier()
  elif mode == '2':
    monthlySales()
  elif mode == '3':
    productSales()
  else:
    print('Error : Please enter correct information')
  
  
  print('---Welcome to the POS System---')
  mode = input('''Press 1: Cashier Mode 
Press 2: Monthly Sales Report 
Press 3: Product Sales Report
Press 0: Exit''')
  
print ('Have a nice day!')
  


