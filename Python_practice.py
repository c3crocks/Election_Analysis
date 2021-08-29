# # # # counties = ["Arapahoe","Denver","Jefferson"]
# # # # # counties.insert(2,"Lucknow")
# # # # # counties.insert(counties.index("Arapahoe"),"Bangalore")
# # # # # #counties.append("El Paso")
# # # # # #counties.remove("El Paso")
# # # # # #counties[2]="Mumbai"
# # # # # y=len(counties)
# # # # # print(y)
# # # # # print((counties[:y]))

# # # # # counties_dict = {}
# # # # # counties_dict["Araphoe"] = 422829
# # # # # counties_dict["Denver"] = 546558
# # # # # counties_dict["Jefferson"] = 462168



# # # # # print(counties_dict["Jefferson"])
# # # # # print(counties_dict.items())

# # # # voting_data = []
# # # # voting_data.append ({"county": "Arapahoe", "registered_voters": "422829"})
# # # # voting_data.append ({"county": "Denver", "registered_voters":"463353"})
# # # # voting_data.append ({"county": "Jefferson", "registered_voters":"432438"})
# # # # voting_data.insert(2,{"county": "El Paso", "registered_voters": "461149"})
# # # # voting_data.remove({"county": "Arapahoe", "registered_voters": "422829"})
# # # # voting_data.remove({"county": "Denver", "registered_voters": "463353"})
# # # # voting_data.insert(3,{"county": "Denver", 70"registered_voters": "463353"})
# # # # voting_data.append({"county": "Arapahoe", "registered_voters": "422829"})

# # # # # print(voting_data)

# counties = ["El Paso","Arapahoe","Denver","Jefferson"]
# # # # if "El Paso" in counties:

# # # #    print(counties[1])
# # # # else:
# # # #     print(counties[0])

# # # # temperature = int(input("What is the temperature outside? "))

# # # # if temperature > 80:
# # # #     print("Turn on the AC.")
# # # # else:
# # # #     print("Open the windows.")

# # # # #What is the score?
# # # # score = int(input("What is the score? "))

# # # # #Determine the Grade
# # # # if score >= 90:
# # # #     print("Your grade is A")
# # # # elif score >=80:
# # # #     print("Your grade is B")
# # # # elif score >=70:
# # # #     print("Your grade is C")
# # # # elif score >=60:
# # # #     print("Your grade is D")
# # # # else:
# # # #     print("Your grade is F")

# # # if "Arapahoe" in counties and "El Paso" not in counties:
# # #    print("Only Arapahoe is in the list of counties.")
# # # else:
# # #     print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")


# # for county in counties:
# #     print(county)

# # for num in range(7):
# #     print(num)

# for i in range(len(counties)):
#     print(counties[i])

voting_data = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county_dict in voting_data:
    for value in voting_data.values():
        print(value)