from netmiko import ConnectHandler

# Define multiple routers (update IPs as per your topology)
r1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",
    "username": "student",
    "password": "Meilab123",
    "port": 22
}
r2 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.102",  # Updated IP for the second router
    "username": "student",
    "password": "Meilab123",
    "port": 22
}

# List of routers
routers = [r1, r2]

# Loop through each router
for device in routers:
    print(f"\nConnecting to {device['ip']}...\n{'-'*50}")
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show interface description")
    net_connect.disconnect()
    
    print(output)
    print("-" * 100)
