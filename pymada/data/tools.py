"""tools
"""

rulers = {}
rulers["distance"] = {}
rulers["range"] = {}

rulers["distance"][1] = 7.625
rulers["distance"][2] = 12.48
rulers["distance"][3] = 18.48
rulers["distance"][4] = 24.48
rulers["distance"][5] = 30.48

rulers["range"]["red"] = 30.48
rulers["range"]["blue"] = 18.65
rulers["range"]["black"] = 12.3

maneuver = {}
maneuver["distance"] = {}
maneuver["yaw"] = {}
for speed in [0, 1, 2, 3, 4]:
    maneuver["distance"][speed] = [6.85 for notch in range(speed)]
    maneuver["yaw"][speed] = [20 for notch in range(speed)]
    for quantity in ["distance", "yaw"]:
        if maneuver[quantity][speed] == []:
            maneuver[quantity][speed] = [0.0]
