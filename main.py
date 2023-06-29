from datetime import datetime

class Resource:
    def __init__(self, id, name, energy_consumption, standby_power):
        self.id = id
        self.name = name
        self.energy_consumption = energy_consumption
        self.standby_power = standby_power

# Create a list of resources with their respective energy consumption in watts and standby power in watts
resources = [
    Resource(1, "Resource 1", 25, 5),
    Resource(2, "Resource 2", 200, 10),
    Resource(3, "Resource 3", 1000, 50),
    # Add more resources as needed
]

def calculate_runtime(start_time, end_time):
    runtime = (end_time - start_time).total_seconds() / 3600
    return runtime

def calculate_energy_consumption(resource, runtime):
    return resource.energy_consumption * runtime

def calculate_energy_wastage(resource, runtime):
    return resource.standby_power * runtime

def display_energy_consumption(resource, runtime):
    energy_consumption = calculate_energy_consumption(resource, runtime)
    energy_wastage = calculate_energy_wastage(resource, runtime)
    print(f"Resource ID: {resource.id}")
    print(f"Resource Name: {resource.name}")
    print(f"  Energy Consumption: {energy_consumption} watt-hours")
    print(f"  Energy Wastage: {energy_wastage} watt-hours")

# Get the resource ID from the user
resource_id = int(input("Enter the resource ID: "))

# Find the resource with the specified ID
selected_resource = None
for resource in resources:
    if resource.id == resource_id:
        selected_resource = resource
        break

# If a resource with the specified ID is found, proceed to capture start and end times
if selected_resource:
    start_time = datetime.now()
    input(f"Press Enter to start using Resource ID {selected_resource.id}: {selected_resource.name}")
    end_time = datetime.now()
    runtime = calculate_runtime(start_time, end_time)

    # Call the function to display energy consumption and wastage for the selected resource
    display_energy_consumption(selected_resource, runtime)
else:
    print("Resource not found.")

