#use of if and else and elif
#weather and moods of Prajwal and Ami
weather = input("Enter the weather :" )
weather_1 = "Summer"
weather_2 = "Spring"
weather_3 = "Rainy"
weather_4 = "Winter"


if str(weather) == str(weather_1) :
    print("Prajwal and Ami are annoyed because it is very hot")
elif str(weather) == str(weather_2) :
    print("Prajwal and Ami are happy because they love greenery")
elif str(weather) == str(weather_3) :
    print("Prajwal and Ami are sad because they cannot go out and Ami hates thunder and there are frequent power cuts")
elif str(weather) == str(weather_4) :
    print("Prajwal and Ami love cool weather to cuddle and sleep warmly in the arms of each other")

else :
    print("Prajwal and Ami have not experienced this weather yet")
    
    #Output gives weather and mood according to the input of the user
