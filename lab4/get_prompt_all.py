from netmiko import Netmiko

# List of device dictionaries
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",  # Router 1
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",  # Router 2
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",  # Router 3
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    },
        {
        "device_type": "cisco_ios",
        "ip": "192.168.1.104",  # Router 4
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    }

]

# Loop through each device and print the prompt
for device in devices:
    try:
        print(f"\nConnecting to {device['ip']}...")
        net_connect = Netmiko(**device)
        print(f"Default prompt: {net_connect.find_prompt()}")
        
        net_connect.send_command_timing("disable")
        print(f"After 'disable': {net_connect.find_prompt()}")
        
        net_connect.enable()
        print(f"After 'enable': {net_connect.find_prompt()}")
        
        net_connect.disconnect()
    except Exception as e:
        print(f"Failed to connect to {device['ip']}: {e}")

