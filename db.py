import json
class DataBase:
    def insert(self,name,email,password):
        self.name=name
        self.email=email
        self.password=password
        with open('db.json','r') as rf :
            users=json.load(rf)
            if self.email in users:
             return 0
            else:
               users[self.email]=[self.name,self.password]
        with open('db.json','w') as wf:
           json.dump(users,wf,indent=4)
           return 1
        
    def Search(self,email,password):
       self.password=password
       self.email=email
       with open("db.json",'r') as rf:
          users=json.load(rf)
          if (self.email in users) :
               if email[1]==self.password:
                 return 1
               else :
                 return 1
          else:
                return 1
                  
