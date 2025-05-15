import yaml
from jinja2 import Environment, FileSystemLoader

# Load YAML data
with open("data-task9.yml") as file:
    topology = yaml.safe_load(file)

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("template-task9.j2")

# Generate configs with detailed output
for router, data in topology["routers"].items():
    config = template.render(router=router, data=data)
   
    # Write to file
    filename = f"{router}_config.txt"
    with open(filename, "w") as f:
        f.write(config)

    # Print detailed info
    print(f"\n--- Configuration for {router} ---")
    print(f"Hostname: {router}")
    print(f"Loopback: {data['loopback']}")
    print("Interfaces:")
    for iface, props in data["interfaces"].items():
        print(f"  {iface}: {props['ip']} ({props['description']})")
    print(f"Config written to: {filename}")
