import unittest
import Poker_Game

'''
This file contains all the test cases for each of the functions used in the program
All the values of the hand is sorted because the Sort_Hand function sorts it before comparing hands
'''
class TestCalc(unittest.TestCase):

# Testing For Royal Flush

    # Base Case -> True (Standard)
    def test_Royal_Flush_1(self):
        result = Poker_Game.Check_Royal_Flush(["1H", "JH", "QH", "KH", "AH"])
        self.assertEqual(result, True)

    # False Case
    def test_Royal_Flush_2(self):
        result = Poker_Game.Check_Royal_Flush(["1H", "3H", "JH", "KH", "AH"])
        self.assertEqual(result, False)

    # Correct rank but diff suit (The rank is of the exact same order of a Royal Flush but suits are different)
    def test_Royal_Flush_3(self):
        result = Poker_Game.Check_Royal_Flush(["1C", "JH", "QH", "KH", "AH"])
        self.assertEqual(result, False)

    # Straight Flush (Straight Flush isn't a Royal Flush -> The Order has to be of the Royal Flush Order)
    def test_Royal_Flush_4(self):
        result = Poker_Game.Check_Royal_Flush(["4H", "5H", "6H", "7H", "8H"])
        self.assertEqual(result, False)





# Testing For Straight Flush

     # Base Case -> True (Standard)
    def test_Straight_Flush_1(self):
        result = Poker_Game.Check_Straight_Flush(["2H", "3H", "4H", "5H", "6H"])
        self.assertEqual(result, True)

    # False Case
    def test_Straight_Flush_2(self):
        result = Poker_Game.Check_Straight_Flush(["1H", "3H", "5H", "7H", "9H"])
        self.assertEqual(result, False)

    # Case where it's not a Flush
    def test_Straight_Flush_3(self):
        result = Poker_Game.Check_Straight_Flush(["2C", "3H", "4H", "5H", "6H"])
        self.assertEqual(result, False)

    # Royal Flush is true but as there is a higher rank that the hand applies to, It's been set to False as it is of a higher rank i.e Royal Flush
    def test_Straight_Flush_4(self):
        result = Poker_Game.Check_Straight_Flush(["1H", "JH", "QH", "KH", "AH"])
        self.assertEqual(result, False)






# Testing For Four Of A Kind

     # Base Case -> True (Standard)
    def test_Four_Of_A_Kind_1(self):
        result = Poker_Game.Check_Four_Of_A_Kind(["4H", "4C", "4D", "4S", "5H"])
        self.assertEqual(result, True)

     # Three Of A Kind -> False Case
    def test_Four_Of_A_Kind_2(self):
        result = Poker_Game.Check_Four_Of_A_Kind(["4H", "4C", "4D", "7H", "9H"])
        self.assertEqual(result, False)


     # False Case
    def test_Four_Of_A_Kind_3(self):
        result = Poker_Game.Check_Four_Of_A_Kind(["4H", "5C", "6D", "7H", "9H"])
        self.assertEqual(result, False)

        




# Testing For Full House

     # Base Case -> True (Standard)
    def test_Check_Full_House_1(self):
        result = Poker_Game.Check_Full_House(["4H", "4C", "4D", "5S", "5H"])
        self.assertEqual(result, True)

     # False Case
    def test_Check_Full_House_2(self):
        result = Poker_Game.Check_Full_House(["4H", "4C", "4D", "7H", "9H"])
        self.assertEqual(result, False)






# Testing For Flush

     # Base Case -> True (Standard)
    def test_Check_Flush_1(self):
        result = Poker_Game.Check_Flush(["2H", "4H", "6H", "1H", "KH"])
        self.assertEqual(result, True)

     # False Case
    def test_Check_Flush_2(self):
        result = Poker_Game.Check_Flush(['2S', '3D', '4S', '6S', '8S'])
        self.assertEqual(result, False)

     # Straight Flush -> there is a higher rank that the hand applies to hence it will show true here but it will show the higher rank when evaluating rank of hand i.e Straight Flush
     
    def test_Check_Flush_3(self):
        result = Poker_Game.Check_Flush(["4H", "5H", "6H", "7H", "8H"])
        self.assertEqual(result, True)
        




# Testing For Straight

     # Base Case -> True (Standard)
    def test_Check_Check_Straight_1(self):
        result = Poker_Game.Check_Straight(["4D", "5C", "6H", "7H", "8S"])
        self.assertEqual(result, True)

     # False Case
    def test_Check_Check_Straight_2(self):
        result = Poker_Game.Check_Straight(['2S', '3D', '4S', '6S', '8S'])
        self.assertEqual(result, False)

     # Straight Flush -> there is a higher rank that the hand applies to hence it will show true here but it will show the higher rank i.e Straight Flush
     
    def test_Check_Check_Straight_3(self):
        result = Poker_Game.Check_Straight(["4H", "5H", "6H", "7H", "8H"])
        self.assertEqual(result, True)






# Testing For Three Of A Kind

     # Base Case -> True (Standard)
    def test_Three_Of_A_Kind_1(self):
        result = Poker_Game.Three_Of_A_Kind(["3H", "3D", "3C", "7H", "8H"])
        self.assertEqual(result, True)

     # False Case
    def test_Three_Of_A_Kind_2(self):
        result = Poker_Game.Three_Of_A_Kind(["3H", "3D", "7H", "8H", "1C"])
        self.assertEqual(result, False)

     # Four Of A Kind -> there is a higher rank that the hand applies to hence it will show False  i.e Four Of A Kind
     
    def test_Three_Of_A_Kind_3(self):
        result = Poker_Game.Three_Of_A_Kind(["3H", "3D", "3C", "3S", "8H"])
        self.assertEqual(result, False)

    # Full House -> there is a higher rank that the hand applies to hence it will show i.e Full House
     
    def test_Three_Of_A_Kind_3(self):
        result = Poker_Game.Three_Of_A_Kind(["2S", "2H", "3H", "3D", "3C"])
        self.assertEqual(result, False)
        





# Testing For Two Pairs

     # Base Case -> True (Standard)
    def test_Check_Two_Pairs_1(self):
        result = Poker_Game.Check_Two_Pairs(["2S", "2H", "3H", "3D", "5C"])
        self.assertEqual(result, True)

     # False Case
    def test_Check_Two_Pairs_2(self):
        result = Poker_Game.Check_Two_Pairs(["3H", "3D", "7H", "8H", "1C"])
        self.assertEqual(result, False)

     # Full House -> there is a higher rank that the hand applies to hence it will show False i.e Full House
     
    def test_Check_Two_Pairs_3(self):
        result = Poker_Game.Check_Two_Pairs(["2S", "2H", "3H", "3D", "3C"])
        self.assertEqual(result, False)







# Testing For One Pair

     # Base Case -> True (Standard)
    def test_Check_Pair_1(self):
        result = Poker_Game.Check_Pair(["2H", "2D", "3C", "5S", "6H"])
        self.assertEqual(result, True)

     # False Case
    def test_Check_Pair_2(self):
        result = Poker_Game.Check_Pair(["2H", "3D", "5C", "9S", "1H"])
        self.assertEqual(result, False)

     # Full House -> there is a higher rank that the hand applies to hence it will show False i.e Full House
     
    def test_Check_Pair_3(self):
        result = Poker_Game.Check_Pair(["3H", "3D", "3C", "2S", "2H"])
        self.assertEqual(result, False)

    # Two Pairs -> there is a higher rank that the hand applies to hence it will show False i.e Two Pairs
    def test_Check_Pair_4(self):
        result = Poker_Game.Check_Pair(["2H", "2D", "3C", "3S", "4H"])
        self.assertEqual(result, False)






# Testing For Checking Hand Rank

    # Test for Royal Flush Hand Rank
    def test_Check_Hand(self):
        result = Poker_Game.Check_Hand(["1H", "JH", "QH", "KH", "AH"])
        self.assertEqual(result,1)

    # Test for Straight Flush Rank
    def test_Check_Hand_2(self):
        result = Poker_Game.Check_Hand(["2H", "3H", "4H", "5H", "6H"])
        self.assertEqual(result, 2)

     
    # Test for Four Of A Kind Hand Rank
    def test_Check_Hand_3(self):
        result = Poker_Game.Check_Hand(["3H", "3D", "3C", "3S", "2H"])
        self.assertEqual(result, 3)

    # Test for Full House Hand Rank
    def test_Check_Hand_4(self):
        result = Poker_Game.Check_Hand(["2H", "2D", "2C", "3S", "3D"])
        self.assertEqual(result, 4)

    # Test for Flush Hand Rank
    def test_Check_Hand_5(self):
        result = Poker_Game.Check_Hand(["2H", "3H", "5H", "9H", "1H"])
        self.assertEqual(result, 5)

    # Test for Straight Hand Rank
     
    def test_Check_Hand_6(self):
        result = Poker_Game.Check_Hand(["3H", "4D", "5C", "6S", "7H"])
        self.assertEqual(result, 6)

    # Test for Three Of A Kind Hand Rank
    def test_Check_Hand_7(self):
        result = Poker_Game.Check_Hand(["2H", "2D", "2C", "6S", "7H"])
        self.assertEqual(result, 7)

    # Test for Two Pairs Hand Rank
    def test_Check_Hand_8(self):
        result = Poker_Game.Check_Hand(["2H", "2D", "3C", "3S", "1H"])
        self.assertEqual(result, 8)

    # Test for One Pair Hand Rank
     
    def test_Check_Hand_9(self):
        result = Poker_Game.Check_Hand(["3H", "3D", "1C", "JS", "QH"])
        self.assertEqual(result, 9)

    # Test for High Card Hand Rank
    def test_Check_Hand_10(self):
        result = Poker_Game.Check_Hand(["2H", "5D", "1C", "KS", "AH"])
        self.assertEqual(result, 10)

    
    # Test for High Card Hand Rank
    def test_Check_Hand_11(self):
        result = Poker_Game.Check_Hand(["3C", "5D", "7C", "8S", "9H"])
        self.assertEqual(result, 10)



if __name__ == "__main__":
    unittest.main()
