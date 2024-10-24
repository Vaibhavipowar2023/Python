'''Q2. Write a program to find out whether a student is pass or fail, if it requires total 40%
and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user
'''

sub1 = int(input("Enter 1st subject marks :\n"))
sub2 = int(input("Enter 2nd subject marks :\n"))
sub3 = int(input("Enter 3rd subject marks :\n"))

if (sub1<33 or sub2<33 or sub3<33):
    print("you are fail because you have less than 33% in one subject")

elif(sub1+sub2+sub3)/3<40 :
        print("You are fail due to tatal percentage less thean 40")
else:
      print("You are pass")

