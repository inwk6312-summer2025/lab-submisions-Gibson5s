from netmiko import Netmiko

devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
        "port": "22"
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",
        "username": "student",
        "password": "Meilab123",
        "port": "22"
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

for device in devices:
    try:
        net_connect = Netmiko(**device)
        output = net_connect.send_command("show version")
        net_connect.disconnect()

        # Search for line that includes uptime
        for line in output.splitlines():
            if "uptime is" in line:
                print(f"{device['ip']} => {line.strip()}")
                break
        else:
            print(f"{device['ip']} => Uptime information not found.")
    except Exception as e:
        print(f"Failed to connect to {device['ip']}: {e}")
