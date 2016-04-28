# Compute Totals Here
# calc.py
# Salar Gohar, June 2015

from datetime import datetime

def store_exp(file_name = "exp.log", new_day = True):
    while(True):

        file_obj = open(file_name, 'a+')
        time_now = datetime.now().strftime("%d / %m:")

        try:
            if new_day:
                cur_exp = raw_input("Enter Amount For %s $ " % time_now)
            else:
                cur_exp = raw_input("Enter Additional Amount For %s $ " % time_now)

        except EOFError:
            file_obj.close()
            print("\n** Ending Session **\n")
            return

    
        if new_day:
            cur_entry = time_now + " $ " + str(cur_exp) + "\n"
            file_obj.write(cur_entry)
        else:
            content = file_obj.readlines()
            prev_total = float(content[-1].split("$")[1])
            cur_exp = str(float(cur_exp) + float(prev_total))
            cur_entry = time_now + " $ " + str(cur_exp) + "\n"
            content.pop()
            file_obj.close()
            file_obj = open(file_name, 'w')
            
            for con in content:
                file_obj.write(con)

            file_obj.write(cur_entry)
    
        file_obj.close()
    

def calc_bal(file_name = "exp.log", per_day = 25):
    file_obj = open(file_name)
    days = file_obj.readlines()

    benchmark = len(days) * per_day
    exp_yet = 0

    for day in days:
        split_day = day.split("$")
        exp_for_day = float(split_day[1])
        print("For %s The Balace was: $ %.2f" % (split_day[0], per_day - exp_for_day))
        exp_yet += exp_for_day
    
    overall_balance = benchmark - exp_yet

    print("\nOverall Balance: $ %.2f" % overall_balance)
    return overall_balance


def exp_check(req_exp, file_name = "exp.log", per_day = 25):
    cur_bal = calc_bal(file_name, per_day)
    take_exp = cur_bal - req_exp

    print("Balance would be: $ %.2f" % take_exp)

if __name__ == "__main__":
    #store_exp()
    #store_exp(new_day = False)
    calc_bal("exp.log", 25)
    exp_check(14.92)
