
class BasePasswordManager:
     #Holds all of the user's old passwords
    def __init__(self):
        self.old_passwords=[]

    #returns the users's latest password
    def get_password(self):
        if(self.old_passwords!=[]):
            last = len(self.old_passwords)-1
            return self.old_passwords[last]
        else:
            return -1   #if no password exists

    #checks whether the string is equal to the current password
    def is_correct(self,password):
        return password == self.get_password()
    
class PasswordManager(BasePasswordManager):
    def __init__(self):
        super().__init__()

    #sets the user's password
    def set_password(self,new_password):
        new_password = str(new_password) #all passwords are strings

        if self.is_correct(new_password):
            print("Your new password is same as the current password\n") #if newpassword is same as current password
        
        elif self.get_level(new_password)==-1: #checks whether a password is valid
            print("Enter a valid password\n")
            
        elif len(new_password)>=6 and (" " not in new_password):
            
            if (self.old_passwords==[]):
                self.old_passwords.append(new_password)  #first password
                print("Password set successfully!!\n")
                
            else:
                 #if the old password already has the highest security level,new password
                 #must be of the highest security level for a successful password change
                
                if self.get_level()==self.get_level(new_password)==2:
                    self.old_passwords.append(new_password)
                    print("Password set successfully!!\n")
                    
                elif self.get_level()<self.get_level(new_password):
                    self.old_passwords.append(new_password)
                    print("Password set successfully!!\n")

                else:
                    print("Your new password should be stronger than the current one\n")

        else:
            print("New Password should have atleast 6 charecters and no spaces in it\n")


    #returns the security level of the password
    def get_level(self,password=None):
        if password==None:
            password = super().get_password()

        if " " in password:
            print("No space allowed\n")
            
        elif password.isalpha() or password.isnumeric():  
            return 0  #only alphabets or only numbers
        
        elif password.isalnum():  
            return 1  #alphanumeric passwords
        
        elif len([x for x in password if x.isdigit()]) and len([x for x in password if x.isalpha()]) : 
            return 2  #alphanumeric password with special charecters
        
        else:
            return -1

pw1 = PasswordManager()

pw1.set_password("hello")       #password must have atleat 6 charecters
pw1.set_password("helloWorld")  #level 0 password
pw1.set_password("123456")      #level 0 password hence should not be accepted
pw1.set_password("hello1234")   #level 1 password
pw1.set_password("#hello12456") #level 2 password
pw1.set_password("hello12334")  #level 1 password should not be accepted
pw1.set_password("@hello12345") #level2 password must be accepted 
pw1.set_password("#!@$$!@")     #invalid password - only special charecters