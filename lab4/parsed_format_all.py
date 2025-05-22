from netmiko import Netmiko

# List of routers (update IPs accordingly)
routers = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
        "port": 22
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",  # Update for second router
        "username": "student",
        "password": "Meilab123",
        "port": 22
    },
    {
	"device_type": "cisco_ios",
	"ip": "192.168.1.103",
	"username": "student",
	"password": "Meilab123",
	"port": "22",
    },
    {
	"device_type": "cisco_ios",
	"ip": "192.168.1.104",
	"username": "student",
	"password": "Meilab123",
	"port": "22",
    }
]

# Loop through each router
for device in routers:
    print(f"\nConnecting to {device['ip']}...\n{'-'*50}")
    net_connect = Netmiko(**device)

    # Use TextFSM parsing
    output = net_connect.send_command("show ip interface brief", use_textfsm=True)
    net_connect.disconnect()

    print(f"Interfaces on {device['ip']}:")
    for interface in output:
        print(interface['interface'])
    print("-" * 50)
