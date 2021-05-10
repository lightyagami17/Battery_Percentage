import psutil

battery = psutil.sensors_battery();
plugged = battery.power_plugged

percent = battery.percent

plugged = "Plugged In" if plugged else "Not Plugged In"
print(f"{str(round(percent))}% | {plugged}")