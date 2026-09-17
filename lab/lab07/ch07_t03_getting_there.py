def hotel_cost(nights: int) -> int:
    return 140 * nights

def plane_ride_cost(city: str) -> int:
    if "Charlotte" == city:
        return 183
    elif "Tampa" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    elif "Los Angeles" == city:
        return 475