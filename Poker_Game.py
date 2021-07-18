'''
This is the implementation of a "Poker Game" system that shows the best hand from the lot.
It starts off by letting the user enter an integer input (between 1 and 10) to select the number of players they'd
like to play with. Once selected, The best hand from the lot is shown

'''

# Below are all the imports used in the program, 'random' has been used for shuffling deck before distributing
# numpy is imported to get unique values from a list

import random
#from itertools import islice
import numpy as np
#from collections import Counter

# Below are the 2 Dictionaries used in the program to form each card. The first one consists of each possible rank and the second one consists of each possible suit
# The Rank 10 has been used as 1 in this case. The value is still 10 but it will be seen as 1 when seeing it in card form

Ranks = { "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "1": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
Suits = {"Clubs": "C", "Diamonds": "D", "Spades": "S", "Hearts": "H"}



''' 
Below are all the functions used for the sub operations such as:
1) finding the best hand 
2) sorting each hand by ascending value of Card Rank
3) assigning Hand Rank to each Hand

'''


# Comments, Rename and Testing, Best Hand


# This is the function that conducts the operation to verify if the hand is a Royal Flush
# As Royal Flush is the most superior hand, it is assigned with the Number 1 Rank

# Royal Flush -> Rank 1

def Check_Royal_Flush(array):
    
    if Check_Flush(array): # First for the operation to proceed, it has to verify if it is a flush 
        royal_values = [14,13,12,11,10] # These are the Rank Values of the cards that are in a Royal Flush
        royal_append = []
        for i in range(len(array)):
            royal_append.append(Ranks.get(array[i][0])) # As the cards in the hand are in string format, it is added to a new list by taking the integer from the String. I.E 7 from '7C'
        
        for i in royal_values:
            if i not in royal_append: # Once all the values in royal_append are added(Integer values of each card in the hand), we loop through royal_values and check if any of the values are not in royal_append
                return False     #Appropriate message shown for failure
            
        return True
    return False


# This is the function that conducts the operation to verify if the hand is a Straight Flush
# it is assigned with the 2nd Rank

# Straight Flush -> Rank 2

def Check_Straight_Flush(array):
    
    if not Check_Royal_Flush(array): # If Hand is as such, it is a Royal Flush but also a Straight Flush hence in this instance, if this appears, it will not be classified as a Straight Flush
        if Check_Straight(array) and Check_Flush(array): # If any other hand, first will be checked if it is a Straight and a Flush, only then will it be a Straight Flush
            return True
    
    return False


    
    
# This is the function that conducts the operation to verify if the hand is a Four Of A Kind
# it is assigned with the 3rd Rank
                                
# Four Of A Kind -> Rank 3
   
def Check_Four_Of_A_Kind(array):
    if not Check_Flush(array) and not Check_Straight(array): # The operation is conducted further only if it's not a Flush or Straight
        unique_values = []
        four_occurences = []
        for i in array: 
            unique_values.append(Ranks.get(i[0])) #looped through the input array, take the integer from the string and added its rank value from the dictionary to another array i.e new2
            x = np.array(unique_values)
            for i in np.unique(x): # Use of numpy to take only the unique values from new2
      
                if unique_values.count(i)==4: # .count to check how many occurences of each value in the hand. If 4, then it is added to a new list
            
                    if i not in four_occurences: # Added if not already in the list 
                        four_occurences.append(i)
            
            # since a hand consists of only 5 cards in 5 Card Stud, it is possible to only have one value for Four Of A Kind hence the length of the new list needs to be 1
            if len(four_occurences)==1:
                
                return True
    
    return False


# This is the function that conducts the operation to verify if the hand is a Full House
# it is assigned with the 4th Rank
                                
# Full House -> Rank 4

def Check_Full_House(array):
    new_array=[]
    for i in array: #looped through the input array, take the integer from the string and added its rank value from the dictionary to another array i.e new_array
        new_array.append(Ranks.get(i[0]))
    
    
    unique_values = []
    multiple_occurences=[]
    x = np.array(new_array)
    for i in np.unique(x): # Use of numpy to take only the unique values from new
        
        if new_array.count(i)==2 or new_array.count(i)==3: #  .count to check how many occurences of each value in the hand. If 2 or 3, then it is added to a new list. I.E count2
            unique_values.append(i)
        
    
    
    if len(unique_values)==2: # The operation proceeds then and checks if length of count2 is 2 because if it is a full house, it will consists of only 2 different ranks. Eg -> 5 and 6
        
        for i in unique_values:
            if new_array.count(i)==2: # If .count of any of the 2 elements is 2, it is added to the first position of a new list 
                multiple_occurences.insert(0,i)
            elif new_array.count(i)==3:
                multiple_occurences.insert(1,i) # If .count of any of the 2 elements is 3, it is added to the second position of a new list 
    
        # The ablove operation is done to specifically position the 2 elements to later verify if its a full house
    
    
    # if length of the new list is 2, it is verified whether the count of  the first element of  the list in the hand is 2 and the second element is 3
    # If yes, it is a full house
    
    if len(multiple_occurences)==2:
        if new_array.count(multiple_occurences[0])==2 and new_array.count(multiple_occurences[1])==3:
            #print(count3)
            return True
        
        
    return False


# This is the function that conducts the operation to verify if the hand is a Flush
# it is assigned with the 5th Rank
                                
# Flush -> Rank 5

def Check_Flush(array):
    for i in range(len(array)-1):
        if array[i][1] != array[i+1][1]: # Loop through the array and check if The Suit of Each card is not equal, if not, returns False . Eg-> array[0] -> "6C"......array[0][1]-> "C"[The Suit]
            return False
    return True
               
                                

# This is the function that conducts the operation to verify if the hand is a Straight
# it is assigned with the 6th Rank

# Straight -> Rank 6

def Check_Straight(array):
    
        for i in range(len(array)-1):
            if Ranks.get(array[i][0])+1 != Ranks.get(array[i+1][0]): # Loops through the list and checks if each new element is incremented by 1 from the previous element
                return False
        return True

# This is the function that conducts the operation to verify if the hand is Three Of A Kind
# it is assigned with the 7th Rank

# Three Of A Kind -> Rank 7
    

def Three_Of_A_Kind(array):
    
    if Check_Full_House(array) and not Check_Four_Of_A_Kind(array): # If hand is a Full House or Four Of A Kind, it will return False. This is because both cases will have 3 occurences of some rank 
        return False
    else:
        unique_values = []
        multiple_occurences = []
        for i in array:
            unique_values.append(Ranks.get(i[0]))
            x = np.array(unique_values)
            for i in np.unique(unique_values):
      
                if unique_values.count(i)==3: # THe rest is similar to the Four Of A Kind operation, only the .count is specified to verify if value is 3 instead of 4
            
                    if i not in multiple_occurences:
                        multiple_occurences.append(i)
            
            if len(multiple_occurences)==1:
                
                return True

    return False


# This is the function that conducts the operation to verify if the hand is Two Pairs
# it is assigned with the 8th Rank

# Two Pairs  -> Rank 8  

def Check_Two_Pairs(array):
        
    if not Check_Full_House(array): # It can be a full house as the elements of the 2nd pair can consist of 3 occurences hence returned false if it is a full house
        unique_values = []
        multiple_occurences = []
        for i in array:
            unique_values.append(Ranks.get(i[0]))
            x = np.array(unique_values)
            for i in np.unique(unique_values):
      
                if unique_values.count(i)==2: # If.count of that element is 2, means it is a pair and is added to a new list
            
                    if i not in multiple_occurences:
                        multiple_occurences.append(i)
            
    
        if len(multiple_occurences)==2: # If length of new list is 2, means there are 2 pairs
            
            return True
    
    return False
        

    
# This is the function that conducts the operation to verify if the hand is One Pair
# it is assigned with the 9th Rank
    
#  One Pair ->  Rank 9 

def Check_Pair(array):
        
    if not Check_Full_House(array) and not Check_Two_Pairs(array):# It can be a full house as the elements of the 2nd pair can consist of 3 occurences or Two Pairs, hence returned false if it is a full house or Two Pairs

        
        unique_values = []
        multiple_occurences = []
        for i in array:
            unique_values.append(Ranks.get(i[0]))
            x = np.array(unique_values)
            for i in np.unique(unique_values):
      
                if unique_values.count(i)==2: # If.count of that element is 2, means it is a pair and is added to a new list
            
                    if i not in multiple_occurences:
                        multiple_occurences.append(i)
            
    
        if len(multiple_occurences)==1: # If length of new list is 1, means there is 1 pair
           
            return True
       
    
    return False


# This is the function that assigns a rank to each hand

def Check_Hand(hand):
    
    if Check_Royal_Flush(hand):
        
        return 1
    
                                
    if Check_Straight_Flush(hand):
        
        return 2
                                
    if Check_Four_Of_A_Kind(hand):
        
        return 3
                                
    if Check_Full_House(hand):
      
        return 4
                                
    if Check_Flush(hand):
        
        return 5
               
    if Check_Straight(hand):
        
        return 6
                                
    if Three_Of_A_Kind(hand):
        
        return 7
    
    if Check_Two_Pairs(hand):
        
        return 8
    
    if Check_Pair(hand):
        
        return 9
    
   
    return 10 # If none of the above, the hand is a High Card hence the lowest rank
                                
    



# This is the function that conducts the operation to sort each hand by rank

def Sort_Hand(hand):
    for i in range(len(hand)-1):
        for j in range(i+1, len(hand)):
            if Ranks.get(hand[i][0]) > Ranks.get(hand[j][0]):
                temp= hand[i]
                hand[i] = hand[j]
                hand[j] = temp

    return hand
                
                



def Main():
        i = 0
        j = 0
        Hands = []
        best_Hand = []
        Individual = []
        


    
        Players = int(input("How many Players(1-10): "))
        
        
        if Players >= 1 and Players <= 10:
            
           # po = []
            #for i in range(int(Players*5/5)):
             #   po.append(5)
        
            for i in Ranks.keys():
                for j in Suits.values():
                    Individual.append(i+j)
                
            random.shuffle(Individual)
            x = 5
            number_of_participants = Players
            list_of_lists = [Individual[i:i+x] for i in range(0, len(Individual), x)]


            for i in range(number_of_participants):
                #print(list_of_lists[i])
            
                print('{} -> {}'.format(Sort_Hand(list_of_lists[i]),Check_Hand(list_of_lists[i])))
                best_Hand.append(Check_Hand(list_of_lists[i]))

            print('\n')
            print('{} is the best hand!'.format(min(best_Hand)))
            print("\n")
            print("Please Enter '0' If You'd To Exit\n")
            Main()
              
        elif Players == 0:
            print("\nHave A Good Day!\n")
            
        else:
            print("\nMaximum Number Of Players is 10!\n")
            Main()


if __name__ == "__main__":
    Main()
