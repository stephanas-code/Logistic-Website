from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

def calculate_dimensional_weight(length_cm, width_cm, height_cm, dimensional_factor):
    """
    Calculate the dimensional weight of a package based on its dimensions in centimeters and the dimensional factor.
    """
    dimensional_weight = (length_cm * width_cm * height_cm) / dimensional_factor
    return dimensional_weight

def calculate_base_shipping_cost(actual_weight, dimensional_weight, rate_per_unit_weight):
    """
    Calculate the base shipping cost based on actual weight, dimensional weight, and rate per unit weight.
    """
    base_shipping_cost = rate_per_unit_weight * max(actual_weight, dimensional_weight)
    return base_shipping_cost

def calculate_total_shipping_cost(base_shipping_cost, destination_based_shipping_cost):
    """
    Calculate the total shipping cost by adding the base shipping cost and the destination-based shipping cost.
    """
    total_shipping_cost = base_shipping_cost + destination_based_shipping_cost
    return total_shipping_cost

# Example values
length_cm = 30  # in centimeters
width_cm = 20  # in centimeters
height_cm = 15  # in centimeters
actual_weight = 10  # in pounds
dimensional_factor_cm = 5000  # specific to the carrier, varies by region
rate_per_unit_weight = 2.0  # in dollars per pound
destination_based_shipping_cost = 50.99  # Example additional cost based on the destination

# Calculate dimensional weight
dimensional_weight = calculate_dimensional_weight(length_cm, width_cm, height_cm, dimensional_factor_cm)

# Calculate base shipping cost
base_shipping_cost = calculate_base_shipping_cost(actual_weight, dimensional_weight, rate_per_unit_weight)

# Calculate total shipping cost
total_shipping_cost = calculate_total_shipping_cost(base_shipping_cost, destination_based_shipping_cost)



