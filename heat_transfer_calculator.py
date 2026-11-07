import sys
import matplotlib.pyplot as plt


def generate_thickness(start_thickness, end_thickness, step_size):
    thickness_values = []
    current_thickness = start_thickness

    while current_thickness <= end_thickness:
        thickness_values.append(current_thickness)
        current_thickness += step_size

    return thickness_values


def temperature_difference_and_heat_transfer_rate(
    thermal_conductivity,
    wall_area,
    wall_thickness,
    inside_temperature,
    outside_temperature
):
    temperature_difference = inside_temperature - outside_temperature

    heat_transfer = (
        thermal_conductivity * wall_area * temperature_difference
    ) / wall_thickness

    return temperature_difference, heat_transfer


def save_results(results):
    with open("heat_transfer_data.csv", "w") as file:
        file.write("thickness,heat_transfer_rate\n")

        for t, Q in results:
            file.write(str(t) + "," + str(Q) + "\n")


def read_results():
    retrieved_data = []

    with open("heat_transfer_data.csv", "r") as file:
        next(file)

        for line in file:
            values = line.strip().split(",")

            thickness = float(values[0])
            heat_transfer = float(values[1])

            retrieved_data.append((thickness, heat_transfer))

    return retrieved_data


try:
    thermal_conductivity = float(input("Enter thermal conductivity (k): "))
    wall_area = float(input("Enter wall area (A): "))

    start_thickness = float(input("Enter starting thickness: "))
    end_thickness = float(input("Enter ending thickness: "))
    step_size = float(input("Enter step size: "))

    inside_temperature = float(input("Enter inside temperature (T1): "))
    outside_temperature = float(input("Enter outside temperature (T2): "))

except ValueError:
    print("Invalid physical input. Program terminated!")
    sys.exit()


if (
    start_thickness > 0
    and end_thickness > 0
    and step_size > 0
    and start_thickness <= end_thickness
    and wall_area > 0
    and thermal_conductivity > 0
):

    thickness_values = generate_thickness(
        start_thickness, end_thickness, step_size
    )

    results = []

    for thickness in thickness_values:

        temperature_difference, heat_transfer = (
            temperature_difference_and_heat_transfer_rate(
                thermal_conductivity,
                wall_area,
                thickness,
                inside_temperature,
                outside_temperature
            )
        )

        results.append((thickness, heat_transfer))

        print("Temperature difference:", temperature_difference)
        print("Heat transfer rate:", heat_transfer)

    print("Calculated results:", results)

    save_results(results)

    retrieved_data = read_results()

    print("Retrieved data:", retrieved_data)

    thickness_values = [item[0] for item in retrieved_data]
    heat_transfer_values = [item[1] for item in retrieved_data]

    plt.plot(thickness_values, heat_transfer_values, marker="o")
    plt.xlabel("Wall Thickness")
    plt.ylabel("Heat Transfer Rate")
    plt.title("Wall Thickness vs Heat Transfer Rate")
    plt.grid(True)
    plt.show()

else:
    print("Invalid input. Please run again!")
    

    
    
    
       


