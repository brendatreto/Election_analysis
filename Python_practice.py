# counties = ["Arapahoe", "Denver", "Jeffeson"]
# if counties[1] == "Denver":
#     print(counties[1])

# if counties [3] != "Jefferson":
#     print(counties[2])

# counties = ["Arapahoe", "Denver", "Jeffeson"]
# if "El Paso" in counties:
#     print("El Paso i in the list of counties.")
# else:
#     print("El Paso is not in the list of counties.")

# if "Arapahoe" in counties and "El Paso" not in counties:
#     print ("Only Arapahoe is in the list of counties")
# else:
#     print("Arapahoe is in the list of counties and El Paso is not in the list of counties")

# for county in counties:
#     print(county)

# for i in range(len(counties)):
#     print(counties[i])


# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county,voters in counties_dict.items():
#     print(f"{county} county has {voters:,} registered voters.")

#for county in counties_dict:
    #print(county)

# for county in counties_dict.keys():
#     print(county)

# for voters in counties_dict.values():
#     print(voters)

# for county in counties_dict:
#     print(counties_dict[county])

# for county in counties_dict:
#     print(counties_dict.get(county))

# for county,voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]
# for county_dict in voting_data:
#     print(
#         f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters.")

# for county_dict in voting_data:
#     print(county_dict)
# for i in range(len(voting_data)):
#     print(voting_data[i])

# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

# for county_dict in voting_data:
#     print(county_dict['registered_voters'])

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")

# candidate_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes:,} number of votes. "
#     f"The total number of votes in the election was {total_votes:,}."
#     f"You received {candidate_votes / total_votes *100:.2f}% of the total votes.")
# print(message_to_candidate)

# Import datetime class from datetime module
import datetime
# Use now() attribute to get present time
now = datetime.datetime.now()
#Print present time
print("The time right now is ", now)
