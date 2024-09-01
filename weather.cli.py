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


#Compute the average temperature for each city
def calculate_average_temperatures(weather_data):

    #getting main key names    
    first_data = weather_data[0]
    main_keys = []
    for key in first_data:
        main_keys.append(key)
    city = main_keys[0]
    temperature = main_keys[1]
    #print(keys)
    #print(city)
    #print(temperature)

    #intialize list of cities, and city temperature dict
    cities_list = []
    city_temeratures = {}
    #print(first_data)

    #intialize key variable for total temp and count
    total_temp = "total_temp"
    count = "count"
    

    #geting unique cities list and total temp and count
    for key_data in weather_data:
        if key_data[city] not in cities_list:
            cities_list.append(key_data[city])
            city_temeratures[key_data[city]] = {total_temp: key_data[temperature], count: 1}
        else:
            city_temeratures[key_data[city]][total_temp] += key_data[temperature]
            city_temeratures[key_data[city]][count] += 1

    #print(city_temeratures)
    #print(cities_list)
    
    average_temp = "average_temp"
    city_average_temeratures = {}

    #Calculate avarage temp for each city
    for city in cities_list:
        average_temperature = city_temeratures[city][total_temp] / city_temeratures[city][count]
        city_average_temeratures[city] = average_temperature
    #print(city_temeratures)

    return city_average_temeratures

#calculate_average_temperatures(weather_data)

def display_average_temperatures(average_temeratures):
    #print all the cities of average temperature
    print("Average Temperatures:")
    for city, average_tmp in average_temeratures.items():
        print(f"{city}: {average_tmp} °C")
    return

def list_all_cities(average_temeratures):
    #print all the cities
    print("Available Cities:")
    for city, average_tmp in average_temeratures.items():
        print(f"- {city}")
    return

def convert_temperatures_to_Fahrenheit_and_display(average_temeratures):
    #Convert temperatures to Fahrenheit and display
    for city, temp_celsius in average_temeratures.items():
        temp_fahrenheit = (temp_celsius * 9/5) + 32
        average_temeratures[city] = temp_fahrenheit
    
    print("Average Temperatures:")
    for city, temp_fahren in average_temeratures.items():
        print(f"{city}: {temp_fahren} °F")
    return

weather_data = weather_json_file()
average_temeratures_data = calculate_average_temperatures(weather_data)
#display_average_temperatures(average_temeratures_data)
#list_all_cities(average_temeratures_data)
convert_temperatures_to_Fahrenheit_and_display(average_temeratures_data)
