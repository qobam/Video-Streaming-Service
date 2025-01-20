%pip install tabulate
# import library
from tabulate import tabulate
data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
}
# isilah titik - titik di bawah ini

class User:
    
    def __init__(self, username, duration_plan, current_plan):
        self.username = username
        self.duration_plan = duration_plan
        self.current_plan = current_plan

    # untuk nge cek benefit dari masing - masing plan
    def check_benefit(self):
        table = [[True, True, True, "Bisa Stream"],
                 [True, True, True, "Bisa Download"],
                 [True, True, True, "Kualitas SD"],
                 [False, True, True, "Kualitas HD"],
                 [False, False, True, "Kualitas UHD"],
                 [1, 2, 4, "Number of Devices"],
                 ["3rd party Movie only", "Basic Plan Content + Sports", "Basic Plan + Standard Plan + PacFlix Original Series", "Jenis Konten"],
                 [120_000, 160_000, 200_000, "Harga"]]

        headers = ["Basic Plan", "Standard Plan", "Premium Plan", "Services"]
        print("PacFlix Plan List")
        print("")
        print(tabulate(table, headers))
        
    # untuk nge cek plan dari plan yang dipilih    
    def check_plan(self, username):
        for key, value in data.items():
            if key == self.username:
                print(value[0])
                print(f"{value[1]} Bulan")
                print("")
                
                try:
                    if value[0] == "Basic Plan":
                        table = [[True, "Bisa Stream"],
                         [True, "Bisa Download"],
                         [True, "Kualitas SD"],
                         [False, "Kualitas HD"],
                         [False, "Kualitas UHD"],
                         [1, "Number of Devices"],
                         ["3rd party Movie only", "Jenis Konten"],
                         [120_000, "Harga"]]

                        headers = ["Basic Plan", "Services"]
                        print(f"{value[0]} PacFlix Benefit List")
                        print("")
                        print(tabulate(table, headers))

                    elif value[0] == "Standard Plan":
                        table = [[True, "Bisa Stream"],
                         [True, "Bisa Download"],
                         [True, "Kualitas SD"],
                         [True, "Kualitas HD"],
                         [False, "Kualitas UHD"],
                         [2, "Number of Devices"],
                         ["Basic Plan + Sports (F1, Football, Basketball)", "Jenis Konten"],
                         [160_000, "Harga"]]

                        headers = ["Standard Plan", "Services"]
                        print(f"{value[0]} PacFlix Benefit List")
                        print("")
                        print(tabulate(table, headers))

                    elif value[0] == "Premium Plan":
                        table = [[True, "Bisa Stream"],
                         [True, "Bisa Download"],
                         [True, "Kualitas SD"],
                         [True, "Kualitas HD"],
                         [True, "Kualitas UHD"],
                         [4, "Number of Devices"],
                         ["Basic Plan + Standard Plan + PacFlix Original Series or Movies", "Jenis Konten"],
                         [200_000, "Harga"]]

                        headers = ["Premium", "Services"]
                        print(f"{value[0]} PacFlix Benefit List")
                        print("")
                        print(tabulate(table, headers))

                    else:
                        raise Exception("Plan didn't exists")
                except:
                    print("aaaa")
                    
    # function untuk upgrade plan
    def upgrade_plan(self, current_plan, new_plan):
    
        if new_plan != self.current_plan:
            if self.duration_plan > 12:
                if new_plan == "Basic Plan":
                    total = 120_000 - (120_000 * 0.05)
                    return total
                elif new_plan == "Standard Plan":
                    total = 160_000 - (160_000 * 0.05)
                    return total
                elif new_plan == "Premium Plan":
                    total = 200_000 - (200_000 * 0.05)
                    return total
                else:
                    raise Exception("Plan didn't exist")
            else:
                if new_plan == "Basic Plan":
                    total = 120_000
                    return total
                elif new_plan == "Standard Plan":
                    total = 160_000
                    return total
                elif new_plan == "Premium Plan":
                    total = 200_000
                    return total
user_1 = User("Shandy", 12, "Basic Plan")
user_1.check_benefit()
user_1.check_plan(user_1.username)
user_1.upgrade_plan(user_1.current_plan, "Standard Plan")
user_2 = User("Cahya", 24, "Standard Plan")
user_2.check_benefit()
user_2.check_plan(user_2.username)
user_2.upgrade_plan(user_2.current_plan, "Premium Plan")
# isi titik - titik di bawah ini

class NewUser:
    
    check_list = []
    
    def __init__(self, username):
        self.username = username
    
    # method to dictionary to list to easier use
    def convert_data_to_list(self, data):
        for data in data.values():
            for val in data:
                self.check_list.append(val)
                
        return self.check_list
        
    # method to pick plan 
    def pick_plan(self, new_plan, referral_code):
        if referral_code in self.check_list:
            if new_plan == "Basic Plan":
                total = 120_000 - (120_000 * 0.04)
                return total
            elif new_plan == "Standard Plan":
                total = 160_000 - (160_000 * 0.04)
                return total
            elif new_plan == "Premium Plan":
                total = 200_000 - (200_000 * 0.04)
                return total
            else:
                print("Plan doesn't exist")
        else:
            raise Exception("Referral Code doesn't exist")
faizal = NewUser("faizal_icikiwir")
faizal.convert_data_to_list(data)
faizal.pick_plan("Basic Plan", "shandy-2134")
faizal.pick_plan("Basic Plan", "indira-22gs")