def hotel_cost(num_nights):
    # Assuming hotel cost per night is £100
    return num_nights * 100

def plane_cost(city_flight):
    # Assuming flight costs for different cities
    if city_flight == "London":
        return 200
    elif city_flight == "Paris":
        return 300
    elif city_flight == "New York":
        return 500
    else:
        return 0

def car_rental(rental_days):
    # Assuming daily car rental cost is £50
    return rental_days * 50

def holiday_cost(num_nights, city_flight, rental_days):
    total_hotel_cost = hotel_cost(num_nights)
    total_plane_cost = plane_cost(city_flight)
    total_car_rental_cost = car_rental(rental_days)
    
    return total_hotel_cost + total_plane_cost + total_car_rental_cost

def main():
    # Get user inputs
    city_flight = input("Enter the city you will be flying to (London, Paris, New York): ")
    num_nights = int(input("Enter the number of nights you will be staying at the hotel: "))
    rental_days = int(input("Enter the number of days for which you will be hiring a car: "))
    
    # Calculate holiday cost
    total_cost = holiday_cost(num_nights, city_flight, rental_days)
    
    # Print holiday details
    print("\nHoliday Details:")
    print("Flight to", city_flight, ":", plane_cost(city_flight))
    print("Hotel cost for", num_nights, "nights:", hotel_cost(num_nights))
    print("Car rental cost for", rental_days, "days:", car_rental(rental_days))
    print("Total holiday cost:", total_cost)

if __name__ == "__main__":
    main()
