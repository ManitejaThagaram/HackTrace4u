# HackTrace4U 📍

HackTrace4U is a Python-based phone number location tracker tool.  
It can track a phone number using an API service or offline telecom database fallback.

Built to help with educational cybersecurity and ethical tracking purposes.

---

## Features 🚀
- Track phone number location via online telecom API.
- Generate Google Maps link for easy location viewing.
- Offline lookup support (if online fails).
- Save lookup results into a CSV file.
- Command-line menu system to lookup multiple numbers.
- Color-coded terminal output for better readability.
- Logs lookup time and date.

---

## Requirements ⚙️
- Python 3.7 or higher
- Required Python libraries:
  - `requests`
  - `colorama`

You can install them using:
```bash
pip install requests colorama

How to Use 🔥
Clone this repository:

bash
Copy
Edit
git clone https://github.com/ManitejaThagaram/HackTrace4U.git
cd HackTrace4U
Run the script:

bash
Copy
Edit
python hacktrace4u.py
Enter a phone number in international format (example: +919876543210).

View results directly in the terminal and saved in location_lookup_results.csv.

Example Output 🎯
yaml
Copy
Edit
[+] Real Lookup Success
  Number      : +919876543210
  Country     : India
  Location    : Hyderabad
  Carrier     : Airtel
  Line Type   : mobile
  Google Maps : https://www.google.com/maps/search/Hyderabad
Disclaimer ⚡
This tool is built for educational and ethical use only.
Unauthorized tracking or misuse of personal information is illegal and strictly discouraged.

License 📜
This project is licensed under the MIT License - see the LICENSE file for details.
