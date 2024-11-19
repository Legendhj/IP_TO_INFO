import requests

def get_ip_location(ip_address):
    try:
        # Send a GET request to the ip-api service
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()
        
        if data["status"] == "success":
            print(f"IP Address: {data['query']}")
            print(f"Country: {data['country']}")
            print(f"Region: {data['regionName']}")
            print(f"City: {data['city']}")
            print(f"ZIP Code: {data['zip']}")
            print(f"Latitude: {data['lat']}")
            print(f"Longitude: {data['lon']}")
            print(f"Location : {data['lat']}, {data['lon']}")
            print(f"Org: {data.get('org')}")
            print(f"ISP: {data['isp']}")
        else:
            print(f"Error: {data['message']}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Input the IP address to locate
ip = input("Enter an IP address: ")
get_ip_location(ip)
