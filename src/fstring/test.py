from src.fstring.custom_temperature_formatter import Temperature

if __name__ == "__main__":
    input_temp = float(input("Enter temperature: "))
    temp = Temperature(input_temp)
    print(f"{temp:f}")
