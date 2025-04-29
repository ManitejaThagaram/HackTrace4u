from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to capture the location data
@app.route('/capture_location', methods=['POST'])
def capture_location():
    if request.method == 'POST':
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        ip_address = request.remote_addr
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Save the captured data to a file
        with open('captured_locations.txt', 'a') as f:
            f.write(f"Timestamp: {timestamp}, IP: {ip_address}, Latitude: {latitude}, Longitude: {longitude}\n")

        # Return a message or a new page
        return f"Location captured: {latitude}, {longitude}. Thanks for visiting!"

if __name__ == '__main__':
    app.run(debug=True)
