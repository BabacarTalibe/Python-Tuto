from time import sleep


light = input("Enter the traffic light color (red/green): ").strip().lower()
while light != "":
    if light == "red":
        print("stop the car")
        sleep(5)  # Simulate waiting for the light to change
        light = input("The light is now green. Enter the traffic light color (red/green): ").strip().lower()
    elif light == "green":
        print("Go ahead")
        break
    else:
        print("Invalid color, please enter red or green.")
        light = input("Enter the traffic light color (red/green): ").strip().lower()