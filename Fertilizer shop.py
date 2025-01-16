item_dict={}
f = open("E:\\fertilizerandinsecticide.txt","r")
while True:
  item=f.readline()
  if item=="\n":
      break
  qntt=f.readline()
  uprc= f.readline()
  item= item[:len(item)-1]
  qntt=int(qntt[:len(qntt)-1])
  uprc=float(uprc[:len(uprc)-1])
  item_dict[item]=[qntt,uprc]
f.close()


"""
item_dict= {
    "napa":[500,1.5],
    "napa extra":[1200,2.50],
    "seclo":[28000,5.75],
    "fenadin":[3000,1.50],
    "ace plus":[50,3.75],
    "Paracitamol":[280,6.70]
    }

"""

def present_data():
    print(28*"*")
    print("Fertilizer & Insecticide")
    print(28*"*")
    print(28*"=")
    print("Available insecticide:")
    print(28*"=")
    for x in item_dict:
        print(x, (20-len(x))*" ",
              (6-len(str(item_dict[x][0])))*" ",item_dict[x][0])
    print(28*"_")
#present_data()

def dec_quant(item, amount):
    item_dict[item][0]-=amount

def inc_quant(item, amount):
    item_dict[item][0]+=amount
def receive_order():
    while True:
        item= input("item(type'x' to stop):")
        if item=='x':
            break
        amnt= int(input("amount:"))
        if item not in item_dict:
            print("new item found")
            uprice=float(input("enter the unique price"))
            item_dict[item]=[amnt,uprice]
            continue
        inc_quant(item,amnt)
    #present_data()
def process_demand():
    demand_list=[]
    while True:
        item= input("item(type'x' to stop):")
        if item=='x':
            break
        if item not in item_dict:
            print("Sorry! The item is not available.")
            continue
        amnt= int(input("amount:"))
        if amnt>item_dict[item][0]:
            print (f"Total {item_dict[item][0]} pcs availabe!")
            continue
        dec_quant(item,amnt)
        demand_list+=[item,amnt,
                      item_dict[item][1],
                      amnt*item_dict[item][1]],
    print(40*"=")
    print("** Payment receipt **".center(40))
    print(40*"=")
    print("Item name",3*" ","Quantity","Uprice","S.total")
    print(40*"_")
    tprice=0
    for x in demand_list:
      tprice+=x[3]
      print(x[0].title(),(14-len(x[0]))*" ",
            (5-len(str(x[1])))*" ",x[1],
            (6-len(str("%.2f"%x[2])))*" ","%.2f"%x[2],
            (6-len(str("%.2f"%x[3])))*" ","%.2f"%x[3])
    print(40*"_")
    tprice="%.2f"%tprice
    print("Total price:",(24-len(str(tprice)))*" ",tprice)
    print(40*"_")
    #present_data()


while True:
    present_data()
    print("Choose an option: ")
    print("Type '1': To process demand")
    print("Type '2': To receive order")
    print("Type '3': To exit the program")
    choice=input("choice: ")
    if choice =='1':
        process_demand()
    elif choice=='2':
        receive_order()
    elif choice=='3':
        break
    else:
        continue
f = open("E:\\fertilizerandinsecticide.txt","w")
for x in item_dict:
    f.write(x+"\n")
    f.write((str(item_dict[x][0]))+"\n")
    f.write((str(item_dict[x][1]))+"\n")
f.write("\n")
f.close()
