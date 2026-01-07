class Transaction:

    transaction_counter = 0
    def __init__(self,trans_Month,trans_Type,trans_Amount):
        
        self.trans_Month = int(trans_Month)   
        self.trans_Type = int(trans_Type)
        Transaction.transaction_counter += 1
        self.trans_Amount = float(trans_Amount)
        self.trans_Id = Transaction.transaction_counter
    def add_trans(self):
        self.trans_Detail={
            'Month':self.trans_Month,
            'Trans_Type':self.trans_Type,
            'Trans_Amount':self.trans_Amount}
        self.f={self.trans_Id:self.trans_Detail}
        #pocess = {trans_ID+1:j for r,j in tprocess}
        return self.f

        
    
# z = int(input("Enter Amount of transection"))
# x = input("Enter Your Transection Type")
# y = eval(input("Enter Amount of transection"))



budget = 0
tra = {}
while True:
    con = int(input("Welcome to Expense Tracker\nPress 1 for Add transection \nPress 2 for Montly Report\nPress 3 Budget Check"))
    if con ==1:
        x = int(input("Enter Month"))
        y = int(input("Enter Trans Type. Press 1 for Add budget 2 for Expense "))
        z = float(input("Enter Trans Amount"))
        if y==1:
            
            d = Transaction(x,y,z)
            new_trans = dict(d.add_trans())
            tra.update(new_trans)
            budget = budget + z
        elif y==2:
            if budget < 0:
                d = Transaction(x,y,z)
                new_trans = dict(d.add_trans())
                tra.update(new_trans)
                budget = budget - z
            else:
                print("Unsufficient Budget")
        else:
            con = int(input("Press 1 for continue"))
        con = int(input("Press 0 for Exite"))
        if con == 0:
            break
    if con ==2:
        print(tra)
        for x,y in tra.items():
            print(f'---------\nTransection ID :{x}\n-------------')
            for i,j in y.items():
                print(f' {i}:{j}\n') 
                
        con = int(input("Press 0 for Exite"))
        if con == 0:
            break
    if con ==3:
        print(f'Your Balance is {budget}')
         
                
        con = int(input("Press 0 for Exite"))
        if con == 0:
            break

    
    
