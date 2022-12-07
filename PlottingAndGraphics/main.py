import matplotlib.pyplot as plt



suv_miles_per_gallon = 10
sedan_miles_per_gallon = 20

miles_driven_per_year = 10_000

suv_gallons_per_year = miles_driven_per_year / suv_miles_per_gallon
sedan_gallons_per_year = miles_driven_per_year / sedan_miles_per_gallon

print(f'SUVs use {suv_gallons_per_year} gallons per year currently')
print(f'Sedans use {sedan_gallons_per_year} gallons per year currently')


new_suv_miles_per_gallon = 20
new_sedan_miles_per_gallon = 50

new_suv_gallons_per_year = miles_driven_per_year / new_suv_miles_per_gallon
new_sedan_gallons_per_year = miles_driven_per_year / new_sedan_miles_per_gallon

print(f'new SUVs use {new_suv_gallons_per_year} gallons per year currently')
print(f'new Sedans use {new_sedan_gallons_per_year} gallons per year currently')

print(f'net savings in fuel used per year in old vs new SUVs: {suv_gallons_per_year - new_suv_gallons_per_year }')
print(f'net savings in fuel used per year in old vs new sedans: {sedan_gallons_per_year - new_sedan_gallons_per_year}')

future_sedan_miles_per_gallon = 100

future_sedan_gallons_per_year = miles_driven_per_year / future_sedan_miles_per_gallon
print(f'future Sedans use {future_sedan_gallons_per_year} gallons per year currently')


miles_per_gallon_range = range(10, 101)
gallons_used = []
gallons_saved = []
for mpg in miles_per_gallon_range:
    gallons_used.append(miles_driven_per_year / mpg)
    gallons_saved.append(suv_gallons_per_year - ( miles_driven_per_year / mpg ) )

plt.plot(miles_per_gallon_range, gallons_used, label="gallons used")
plt.plot(miles_per_gallon_range, gallons_saved, label="gallons saved")
plt.xlabel("Miles per Gallon")

plt.legend()
plt.show()
