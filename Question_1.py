#Task 1

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

crossover_destinations = our_routes.intersection(competitor_routes) #output: {'BKK', 'LHR', 'CDG', 'JFK'}

unique_destinations = our_routes.difference(competitor_routes) #output: {'LAX', 'DXB'}

unshared_destinations = our_routes.symmetric_difference(competitor_routes) #output: {'BKK', 'DXB', 'LAX', 'LHR'}
