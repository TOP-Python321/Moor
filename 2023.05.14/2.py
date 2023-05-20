def taxi_cost(distance: int, waiting_time=0) -> int | None:
    """
    Returns the cost of the trip and the waiting time (if any) 
    if the distance is > 0. If the distance == 0, 
    returns the fine, the start and the waiting time (if any). 
    Otherwise returns None
    """
    start = 80
    fine = 80
    price_per_distance = distance * 6  // 150
    price_per_waiting = waiting_time * 3

    total = start + price_per_distance + price_per_waiting
    
    if distance == 0:
        total = start + fine + price_per_waiting
    elif distance < 0:
        total = None
    
    return total 
    
    
# print(taxi_cost(0, 12))
# 196

# print(taxi_cost(-90, 21))
# None

# print(taxi_cost(2160, 8))
# 188