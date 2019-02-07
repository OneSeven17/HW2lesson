def calculate_trip_length (liters_per_100km, liters_in_tank):
    """
    >>> calculate_trip_length (12, 60) # doctest: +ELLIPSIS
    5.0...
    """

    trip_length = liters_in_tank / liters_per_100km
    return trip_length