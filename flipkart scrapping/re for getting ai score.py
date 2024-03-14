import re

my_string = "**Opinion Score: 4/5** Based on customer reviews on Amazon, the Exide 150Ah Instabrite Inverter Battery is a generally well-received product with high ratings for its performance and durability. Customers praise its long backup time, even during power outages, and its ability to power multiple devices simultaneously. The battery is also said to be easy to install and maintain. However, some users have mentioned that the battery may require frequent topping up, which can be a minor inconvenience. Overall, the Exide 150Ah Instabrite Inverter Battery is a reliable and efficient option for those in need of a UPS battery."
match = re.search(r"(score|Score|SCORE):\s*(\d+)", my_string)  # Pattern to capture digits after "score:"
if match:
    number_after_score = match.group(2)
    print(number_after_score)  # Output: 456
else:
    print("Number not found in the expected format")
