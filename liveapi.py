import requests

def fetch_data(api_url, params):
    try:
        # Make the API request
        response = requests.get(api_url, params=params)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        return data
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error occurred: {req_err}")
    except ValueError as json_err:
        print(f"JSON decoding error: {json_err}")

def display_data(data):
    if data:
        print("Weather Data:")
        print(f"Location: {data.get('name', 'N/A')}")
        print(f"Temperature: {data.get('main', {}).get('temp', 'N/A')}°C")
        print(f"Condition: {data.get('weather', [{}])[0].get('description', 'N/A')}")
        print(f"Humidity: {data.get('main', {}).get('humidity', 'N/A')}%")
    else:
        print("No data to display.")

def main():
    # Example API URL and parameters
    api_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': input("Enter city name: "),
        'appid': 'e567421e68fb8cfe4980d5d6d6b26a9d',  # Replace with your actual API key
        'units': 'imperial'  # Use 'imperial' for Fahrenheit
    }
    
    # Fetch data from API
    data = fetch_data(api_url, params)
    
    # Display the fetched data
    display_data(data)

if __name__ == "__main__":
    main()
    
    
    #e567421e68fb8cfe4980d5d6d6b26a9d - api key

