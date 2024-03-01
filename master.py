import os
import shutil
import datetime

def backup_hours_dat():
    if not os.path.exists('archives'):
        os.makedirs('archives')

    current_date = datetime.datetime.now().strftime("%d_%m_%y_%H_%M")
    backup_file_name = f"{current_date}.dat.bkp"
    
    try:
        shutil.copy('hours.dat', os.path.join('archives', backup_file_name))
    except:
        print("Backup of hours.dat unable to be made.")
        
def start_tracking():
    start_time = datetime.datetime.now()
    print(f"Tracking started at {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

    return start_time

def stop_tracking(start_time):
    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time
    total_hours = elapsed_time.total_seconds() / 3600

    print(f"Tracking stopped at {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Hours worked: {int(total_hours)} hours {int((total_hours % 1) * 60)} minutes")

    save_hours(start_time.strftime('%Y-%m-%d'), elapsed_time.total_seconds() / 3600,end_time)

def save_hours(date, hours,end_time):
    with open('hours.dat', 'a') as file:
        file.write(f"{date}: {int(hours)} hours {int((hours % 1) * 60)} minutes // {start_time.strftime('%H:%M')} - {end_time.strftime('%H:%M')}\n")

def query_hours():
    entries_per_day = {}
    total_hours_per_day = {}

    try:
        with open('hours.dat', 'r') as file:
            lines = file.readlines()
            
            if lines[0].startswith("Rate: "):
                lines.pop(0)
                
            for line in lines:
                wanted, unwanted = line.split(' // ')
                date, hours = wanted.split(': ')
                hours = int(hours.split()[0]) + int(hours.split()[2]) / 60

                if date in entries_per_day:
                    entries_per_day[date] += 1
                    total_hours_per_day[date] += hours
                else:
                    entries_per_day[date] = 1
                    total_hours_per_day[date] = hours
    except FileNotFoundError:
        print("No tracking data found.")
        return

    for date in sorted(entries_per_day.keys()):
        print(f"[{date}] {int(total_hours_per_day[date])} hours and {int((total_hours_per_day[date] % 1) * 60)} minutes across {entries_per_day[date]} sessions")
        
def query_hours_rates():

    with open('hours.dat', 'r') as file:
        first_line = file.readline().strip()
        if first_line.startswith("Rate: "):
            try:
                rate = float(first_line.replace("Rate: ", ""))
            except:
                print("Invalid rate datatype.")
                return
        else:
            print("No rate set.")
            return

    total_earning = 0.0
    entries_per_day = {}
    total_hours_per_day = {}

    try:
        with open('hours.dat', 'r') as file:
            lines = file.readlines()
            
            if lines[0].startswith("Rate: "):
                lines.pop(0)
                
            for line in lines:
                wanted, unwanted = line.split(' // ')
                date, hours = wanted.split(': ')
                hours = int(hours.split()[0]) + int(hours.split()[2]) / 60

                if date in entries_per_day:
                    entries_per_day[date] += 1
                    total_hours_per_day[date] += hours
                else:
                    entries_per_day[date] = 1
                    total_hours_per_day[date] = hours
    except FileNotFoundError:
        print("No tracking data found.")
        return

    for date in sorted(entries_per_day.keys()):
        print(f"[{date}] {int(total_hours_per_day[date])} hours and {int((total_hours_per_day[date] % 1) * 60)} minutes across {entries_per_day[date]} sessions [£{int(total_hours_per_day[date])*rate} @ {rate}]")
        total_earning += int(total_hours_per_day[date])*rate
    print(f"[Total Earnings: £{total_earning}]")
        
def query_hours_monthly():
    entries_per_month = {}
    total_hours_per_month = {}

    try:
        with open('hours.dat', 'r') as file:
            lines = file.readlines()
            
            if lines[0].startswith("Rate: "):
                lines.pop(0)
                
            for line in lines:
                wanted, unwanted = line.split(' // ')
                date, hours = wanted.split(': ')
                year_month = date[:-3]
                hours = int(hours.split()[0]) + int(hours.split()[2]) / 60

                if year_month in entries_per_month:
                    entries_per_month[year_month] += 1
                    total_hours_per_month[year_month] += hours
                else:
                    entries_per_month[year_month] = 1
                    total_hours_per_month[year_month] = hours
    except FileNotFoundError:
        print("No tracking data found.")
        return

    for year_month in sorted(entries_per_month.keys()):
        print(f"[{year_month}] {int(total_hours_per_month[year_month])} hours and {int((total_hours_per_month[year_month] % 1) * 60)} minutes across {entries_per_month[year_month]} sessions")

def query_hours_monthly_rates():

    with open('hours.dat', 'r') as file:
        first_line = file.readline().strip()
        if first_line.startswith("Rate: "):
            try:
                rate = float(first_line.replace("Rate: ", ""))
            except:
                print("Invalid rate datatype.")
                return
        else:
            print("No rate set.")
            return

    total_earning = 0.0
    entries_per_month = {}
    total_hours_per_month = {}

    try:
        with open('hours.dat', 'r') as file:
            lines = file.readlines()
            
            if lines[0].startswith("Rate: "):
                lines.pop(0)
                
            for line in lines:
                wanted, unwanted = line.split(' // ')
                date, hours = wanted.split(': ')
                year_month = date[:-3]
                hours = int(hours.split()[0]) + int(hours.split()[2]) / 60

                if year_month in entries_per_month:
                    entries_per_month[year_month] += 1
                    total_hours_per_month[year_month] += hours
                else:
                    entries_per_month[year_month] = 1
                    total_hours_per_month[year_month] = hours
    except FileNotFoundError:
        print("No tracking data found.")
        return

    for year_month in sorted(entries_per_month.keys()):
        print(f"[{year_month}] {int(total_hours_per_month[year_month])} hours and {int((total_hours_per_month[year_month] % 1) * 60)} minutes across {entries_per_month[year_month]} sessions [£{int(total_hours_per_month[year_month])*rate} @ {rate}]")
        total_earning += int(total_hours_per_month[year_month])*rate
    print(f"[Total Earnings: £{total_earning}]")
    
def update_rate(rate_value):

    with open('hours.dat', 'r') as file:
        lines = file.readlines()

    if lines[0].startswith("Rate: "):
        lines[0] = f"Rate: {rate_value}\n"
    else:
        for i in range(len(lines) - 1, 0, -1):
            lines[i] = lines[i - 1]

        lines[0] = f"Rate: {rate_value}\n"

    with open('hours.dat', 'w') as file:
        file.writelines(lines)

def delete_rate():
    
    with open('hours.dat','r') as file:
        lines = file.readlines()

    if lines[0].startswith("Rate: "):
        lines[0] = "Rate: None\n"

    with open('hours.dat', 'w') as file:
        file.writelines(lines)

def help_message():
    print("--- Command List ---\n\n<<< track start\nStarts the tracker.\n\n<<< track stop\nStops the tracker.\n\n<<< track query\nLists total hours worked across each day, and session count.\n\n<<< track query -m\nLists total hours worked across each month, and session count.\n\n--------------------")

if __name__ == "__main__":
    backup_hours_dat()
    while True:
        command = input(">>> ")

        if command == 'track start':
            start_time = start_tracking()
        elif command == 'track stop':
            stop_tracking(start_time)
        elif command.startswith('track query'):
            if '-m' in command:
                if '-r' in command:
                    query_hours_monthly_rates()
                else:
                    query_hours_monthly()
            else:
                if '-r' in command:
                    query_hours_rates()
                else:
                    query_hours()
        elif command == 'help':
            help_message()
        elif command.startswith("rate set "):
            try:
                update_rate(float(command.replace("rate set ","")))
            except:
                print("Invalid rate datatype.")
        elif command == "rate delete":
            delete_rate()
        else:
            print("Invalid command. Try again, or type 'help'")
