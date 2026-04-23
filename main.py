# Create an empty dictionary called 'robots'
robots = {}

# prompt the user for name
name = input("Enter robot name: ")

# PROMPT user for 'zone' (Downtown, Suburbs, Industrial)
zone = input("Enter robot zone (Downtown, Suburbs, Industrial): ")
#         VALIDATE that 'zone' is correct; RE-PROMPT if not
while zone not in ["Downtown", "Suburbs", "Industrial"]:
    print("Invalid zone. Please try again.")
    zone = input("Enter robot zone (Downtown, Suburbs, Industrial): ")

#         STORE 'name' as key and 'zone' as value in 'robots'
robots[name] = zone

#     PROMPT user for 'total_distance' (5-500)
total_distance = float(input("Enter total distance (5-500): "))
#     VALIDATE 'total_distance' is within range; RE-PROMPT if not
while total_distance < 5 or total_distance > 500:
    print("Invalid distance. Please try again.")
    total_distance = float(input("Enter total distance (5-500): "))

#     CREATE an empty dictionary 'cargo_weights'
cargo_weights = {}
#     FOR each 'name' in 'robots':
for name in robots:
    #         PROMPT for 'weight' (1-50 kg)
    weight = float(input(f"Enter cargo weight for {name} (1-50 kg): "))
    #         VALIDATE 'weight' is within range; RE-PROMPT if not
    while weight < 1 or weight > 50:
        print("Invalid weight. Please try again.")
        weight = float(input(f"Enter cargo weight for {name} (1-50 kg): "))
    #         STORE 'weight' in 'cargo_weights' linked to 'name'
    cargo_weights[name] = weight

#     PROMPT for 'weather' (Clear, Rain, Storm)
#     VALIDATE 'weather' is valid; RE-PROMPT if not
    
#     IF distance > 300 OR any weight > 50 OR weather is "Storm":
#         PRINT "🚨 Deployment Unsafe!"
#     ELSE:
#         FOR each 'name' in 'robots':
#             PRINT name, zone, and weight
#         PRINT "🤖 Robots Ready for Delivery!"
# END
