'''
Coding Challenge 5: Farmer Problem Statement
Mahesh is a farmer and owns 80 acres of land. His land is equally divided into 5 segments. He grows
tomatoes in the 1st segment, potatoes in the 2nd segment, cabbage in the 3rd segment, sunflower in
the 4th segment and sugarcane in the 5th segment. He is converting his land from chemical-driven
farming to chemical-free farming. Mahesh starts with the conversion of vegetables into chemical-free
produce. He spends the first 6 months doing the same. He then converts the sunflower land bank
into chemical-free farming. This takes him another 4 months. Finally, he converts sugarcane into
chemical-free farming over the next 4 months. He gets a yield of the following for tomatoes. 30% of
his tomato land gives him 10 tonne yield per acre. The remaining 70% of his tomato land gives him
12 tonnes yield per acre. The selling price of tomato is Rs. 7 per Kg. The yield of potatoes is 10 tonnes
per acre. He sells each kg at Rs. 20. The yield of cabbage is 14 tonnes per acre. He sells each kg at Rs.
24. The yield of sunflowers is 0.7 tonnes per acre. He sells each kg at Rs. 200. The yield of sugarcane
is 45 tonnes per acre. He sells each tonne at Rs. 4,000. All the crops are sowed at the same time.
Mahesh gets the above yield at the above-mentioned rate in one crop cycle across his entire land of
80 acres.
What is
a. The overall sales achieved by Mahesh from the 80 acres of land.
b. Sales realisation from chemical-free farming at the end of 11 months
'''

# Total land details
total_land = 80
segments = 5
land_per_segment = total_land / segments  # 16 acres each

# TOMATO 
tomato_land = land_per_segment
tomato_yield = (0.3 * tomato_land * 10) + (0.7 * tomato_land * 12)  # tonnes
tomato_sales = tomato_yield * 1000 * 7  # Rs (kg * price)

# POTATO 
potato_land = land_per_segment
potato_yield = potato_land * 10  # tonnes
potato_sales = potato_yield * 1000 * 20

# CABBAGE
cabbage_land = land_per_segment
cabbage_yield = cabbage_land * 14  # tonnes
cabbage_sales = cabbage_yield * 1000 * 24

#  SUNFLOWER 
sunflower_land = land_per_segment
sunflower_yield = sunflower_land * 0.7  # tonnes
sunflower_sales = sunflower_yield * 1000 * 200

# SUGARCANE 
sugarcane_land = land_per_segment
sugarcane_yield = sugarcane_land * 45  # tonnes
sugarcane_sales = sugarcane_yield * 4000  # price per tonne

# a) Overall sales from 80 acres
total_sales = (
    tomato_sales +
    potato_sales +
    cabbage_sales +
    sunflower_sales +
    sugarcane_sales
)

# b) Chemical-free sales at end of 11 months
# (Vegetables + Sunflower only)
chemical_free_sales_11_months = (
    tomato_sales +
    potato_sales +
    cabbage_sales +
    sunflower_sales
)

# Output
print(f"Overall sales from 80 acres = Rs. {total_sales}")
print(f"Chemical-free sales at end of 11 months = Rs. {chemical_free_sales_11_months}")



