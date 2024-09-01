import os
import json

file_name = "weather.json"

#check json file and read
def weather_json_file():
    try:
        with open(file_name, "r") as weather_file:
            weather_data = json.load(weather_file)
        #print(weather_data)
        return weather_data

    except FileNotFoundError:
        print(f"Error: {os.path.basename(file_name)} file not exists.")
        return None

    except json.JSONDecodeError:
        print(f"Error: {os.path.basename(file_name)} is not a valied JSON file.")
        return None

    except Exception as error:
        print(f"Error: {error}")
        return None

weather_json_file()

#Compute the average temperature for each city
def calculate_average_temperatures(weather_data):
        
    first_data = weather_data[0]
    main_keys = []
    for key in first_data:
        main_keys.append(key)
    city = main_keys[0]
    temperature = main_keys[1]
    #print(keys)
    #print(city)
    #print(temperature)

    cities_list = []

    #print(first_data)

    for key_data in weather_data:
        if key_data[city] not in cities_list:
            cities_list.append(key_data[city])
        else:
            continue
    
    print(cities_list)
        #city = key_data["city"]
        #temperature = key_data["temperature"]
        #print(city)
        #print(temperature)   
    return

weather_data = weather_json_file()

calculate_average_temperatures(weather_data)
