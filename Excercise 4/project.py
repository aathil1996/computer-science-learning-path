destinations = [['Paris' , 'France'], ['Shanghai', 'China'], ['Los Angeles', 'USA'], ['São Paulo' , 'Brazil'], ['Cairo' , 'Egypt']]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  destination_index = destination.index()
  return destination_index

print(get_destination_index(Los Angeles, USA))
  