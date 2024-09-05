import os
import json

file_name = "weather.json"

"""''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
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

"""''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
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


    #geting unique cities list and total temp and count
    for key_data in weather_data:
        if key_data[city] not in cities_list:
            cities_list.append(key_data[city])
            city_temeratures[key_data[city]] = [key_data[temperature]]
        else:
            city_temeratures[key_data[city]] += [key_data[temperature]]

    #print(city_temeratures)
    #print(cities_list)
    """
    city_temeratures = {'New York': [30, 28], 'Los Angeles': [25, 26], ...}
    """
    
    #Calculate avarage temp for each city
    city_average_temeratures = {}
    for city, temeratures in city_temeratures.items():
        average_temp = sum(temeratures) / len(temeratures)
        city_average_temeratures[city] = average_temp

        #print(len(temeratures))
        #print(temeratures)
    #print(city_average_temeratures)
    """
    city_average_temeratures = {'New York': 29.0, 'Los Angeles': 25.5, ...}
    """
    return city_average_temeratures

"""''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
#calculate_average_temperatures(weather_data)
def display_average_temperatures(average_temeratures_data, city_name=None, all_cities=False):

    #initialze data to write on json
    output_avg_data = {}

    #print all the cities of average temperature
    if all_cities:
        output_avg_data = average_temeratures_data
        """output_avg_data = {'New York': 29.0, 'Los Angeles': 25.5, ...}"""        

    #print only the specifi city of average temperature
    else: 
        if city_name in average_temeratures_data:
            #print(city)
            output_avg_data[city_name] = average_temeratures_data[city_name]
            #print(output_avg_data)
            """output_avg_data = {'New York': 29.0} """

        else:
            print(f"Error: {city_name} is not in the file")
            return
            
    #print the output on terminal
    print("Average Temperatures")
    for city, average_tmp in output_avg_data.items():
        print(f"{city}: {average_tmp} °C")

"""''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
#List all cities for which weather data is available
def list_all_cities(average_temeratures):
    #print all the cities
    print("Available Cities:")
    for city, average_tmp in average_temeratures.items():
        print(f"- {city}")
    return

"""''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
#Convert temperatures to Fahrenheit and display
def convert_temperatures_to_Fahrenheit_and_display(average_temeratures_data, city_name=None, all_cities=False):
    #initialze data to write on json
    output_avg_data = {}

    #Convert temperatures to Fahrenheit and
    for city, temp_celsius in average_temeratures_data.items():
        temp_fahrenheit = (temp_celsius * 9/5) + 32
        output_avg_data[city] = temp_fahrenheit

    #print all cities display
    if all_cities:
        output_avg_data = output_avg_data
        """output_avg_data = {'New York': 84.2, 'Los Angeles': 77.9, ...]"""

    #print only the specifi city of average temperature 
    else:
        if city_name in average_temeratures_data:
            output_avg_data[city_name] = average_temeratures_data[city_name]
            """output_avg_data {'New York': 84.2}"""

        else:
            print(f"Error: {city_name} is not in the file")
            return
        
    #print the output on terminal
    print("Average Temperatures")
    for city, average_tmp in output_avg_data.items():
        print(f"{city}: {average_tmp} °C")
    return

city_name = "New York"
weather_data = weather_json_file()
#calculate_average_temperatures(weather_data)
average_temeratures_data = calculate_average_temperatures(weather_data)
#print(average_temeratures_data)
display_average_temperatures(average_temeratures_data, all_cities=True)
#list_all_cities(average_temeratures_data)
#convert_temperatures_to_Fahrenheit_and_display(average_temeratures_data, all_cities=True)
