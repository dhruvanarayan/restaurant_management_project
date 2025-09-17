import string
import random
from .models import Coupon

def generate_coupon_code(length=10):
    """
    Generates a unique random alphanumeric string to be used as a coupon code.

    It continuously generates a new code until it finds one that is not
    already in the Coupon database.
    """
    characters = string.ascii_uppercase + string.digits
    while True:
        # Generate a random string of the specified length
        code = ''.join(random.choices(characters, k=length))
        
        # Check if a coupon with this code already exists
        if not Coupon.objects.filter(code=code).exists():
            # If it doesn't exist, we found a unique code
            break
            
    return code