#return multiple values
def miles_to_run(minimum_miles):
   week_1 = minimum_miles + 2
   week_2 = minimum_miles + 4
   week_3 = minimum_miles + 6
   return [week_1, week_2, week_3]
 
print(miles_to_run(2))
