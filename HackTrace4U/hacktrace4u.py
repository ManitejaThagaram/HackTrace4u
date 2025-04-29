import requests
import csv
import datetime
from colorama import Fore, Style

# Your API key
API_KEY = "c2ad438495198ef94085680ac69c6b5f"

# Fallback offline telecom data
offline_db = {
    "+91": {"country": "India", "carrier": "Generic Carrier", "region": "Unknown"},
    "+1": {"country": "USA", "carrier": "Generic US Carrier", "region": "Unknown"},
    "+44": {"country": "UK", "carrier": "Generic UK Carrier", "region": "Unknown"},
}

# Save to CSV or Text File
def save_to_file(results):
    with open("location_lookup_results.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(results)
    print(Fore.GREEN + "[+] Results saved to 'location_lookup_results.csv'")

# Google Maps Link Generation
def generate_maps_link(location):
    base_url = "https://www.google.com/maps/search/"
    return base_url + location.replace(" ", "+")

# Date and Time Logging
def log_lookup_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

# Real Lookup via API
def real_lookup(phone_number):
    try:
        url = f"http://apilayer.net/api/validate?access_key={API_KEY}&number={phone_number}&country_code=&format=1"
        response = requests.get(url)
        data = response.json()

        if data["valid"]:
            result = [
                log_lookup_time(), 
                data['international_format'], 
                data['country_name'], 
                data['location'], 
                data['carrier'], 
                data['line_type']
            ]
            print(Fore.CYAN + "\n[+] Real Lookup Success")
            print(Fore.YELLOW + f"  Number      : {data['international_format']}")
            print(Fore.YELLOW + f"  Country     : {data['country_name']}")
            print(Fore.YELLOW + f"  Location    : {data['location']}")
            print(Fore.YELLOW + f"  Carrier     : {data['carrier']}")
            print(Fore.YELLOW + f"  Line Type   : {data['line_type']}")
            maps_link = generate_maps_link(data['location'])
            print(Fore.GREEN + f"  Google Maps : {maps_link}")
            save_to_file(result)
        else:
            print(Fore.RED + "\n[-] Invalid phone number or not found in API.")
            offline_lookup(phone_number)
    except Exception as e:
        print(Fore.RED + "\n[!] Real lookup failed, using offline data...")
        offline_lookup(phone_number)

# Offline Lookup for Unknown Numbers
def offline_lookup(phone_number):
    for code, info in offline_db.items():
        if phone_number.startswith(code):
            result = [
                log_lookup_time(), 
                phone_number, 
                info['country'], 
                info['region'], 
                info['carrier'], 
                'Offline'
            ]
            print(Fore.CYAN + "\n[+] Offline Lookup Success")
            print(Fore.YELLOW + f"  Number      : {phone_number}")
            print(Fore.YELLOW + f"  Country     : {info['country']}")
            print(Fore.YELLOW + f"  Region      : {info['region']}")
            print(Fore.YELLOW + f"  Carrier     : {info['carrier']}")
            print(Fore.GREEN + "  Google Maps : Not available for offline data.")
            save_to_file(result)
            return
    print(Fore.RED + "\n[-] No offline data found for this number.")

# Menu System for Multiple Lookups
def menu():
    while True:
        print(Fore.MAGENTA + "\n=== HackTrace4U | Phone Number Tracker ===")
        print(Fore.CYAN + "1. Lookup a phone number")
        print(Fore.CYAN + "2. Exit")
        choice = input(Fore.YELLOW + "Enter choice (1/2): ")
        
        if choice == '1':
            number = input(Fore.YELLOW + "Enter phone number with country code (e.g., +919876543210): ")
            real_lookup(number)
        elif choice == '2':
            print(Fore.GREEN + "Exiting HackTrace4U...")
            break
        else:
            print(Fore.RED + "Invalid option. Please try again.")

# --- Main ---
if __name__ == "__main__":
    menu()
