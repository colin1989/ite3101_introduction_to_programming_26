def distance_from_zero(param:any):
    if isinstance(param, (int, float)):
        return abs(param)
    else:
        return "Nope"
