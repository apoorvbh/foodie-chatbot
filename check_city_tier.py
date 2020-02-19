def initialize_app():
    return CheckCityTier()

class CheckCityTier:
    tier_1_cities = ['bangalore', 'chennai', 'delhi', 'hyderabad', 'kolkata', 'mumbai', 'ahmedabad', 'pune']
    tier_2_cities = ['agra', 'ajmer', 'aligarh', 'amravati', 'amritsar', 'asansol', 'aurangabad', 'bareilly', 'belgaum', 
    'bhavnagar', 'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner', 'bilaspur', 'bokaro steel city', 'chandigarh', 'coimbatore',
    'nagpur', 'cuttack', 'dehradun', 'dhanbad', 'bhilai', 'durgapur', 'erode', 'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur', 
    'gulbarga', 'guntur', 'gwalior', 'gurgaon', 'guwahati', 'hamirpur', 'hubli–dharwad', 'indore', 'jabalpur', 'jaipur', 'jalandhar', 
    'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kakinada', 'kannur', 'kanpur', 'kochi', 'kolhapur', 'kollam', 
    'kozhikode', 'kurnool', 'ludhiana', 'lucknow', 'madurai', 'malappuram', 'mathura', 'goa', 'mangalore', 'meerut', 'moradabad', 
    'mysore', 'nanded', 'nashik', 'nellore', 'noida', 'patna', 'pondicherry', 'purulia', 'prayagraj', 'raipur', 'rajkot', 'rajahmundry', 
    'ranchi', 'rourkela', 'salem', 'sangli', 'shimla', 'siliguri', 'solapur', 'srinagar', 'thiruvananthapuram', 'thrissur', 
    'tiruchirappalli', 'tiruppur', 'ujjain', 'bijapur', 'vadodara', 'varanasi', 'vasai-virar city', 'vijayawada', 
    'vellore', 'warangal', 'surat', 'visakhapatnam']

    def __init__(self):
        self.valid_cities = []
        self.valid_cities.extend(CheckCityTier.tier_1_cities)
        self.valid_cities.extend(CheckCityTier.tier_2_cities)
    
    def check_city_tier(self, city):
        return (city.lower() in self.valid_cities)

