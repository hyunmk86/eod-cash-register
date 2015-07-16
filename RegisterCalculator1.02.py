
# calculates all currency in the cash register and prints amount in each denomination
# you need to leave to meet desired amt in the cash register at the end of the day.

print "***Cash register calculator created by Brian Kim***"
print "-For suggestion and bug, email hyunmk86@gmail.com-"
print ""
print "Takes number of each denomination in the cash register and calculates amount "
print "you need to leave in the register per denomination for closing at the end of the day "
print "-Program designed to leave maximum coins and lower denomination-"
print ""
def calculate():


    pen = int(raw_input("input number of pennies : "))
    nick = int(raw_input("input number of nickels : "))
    dime = int(raw_input("input number of dimes : "))
    quart = int(raw_input("input number of quarters : "))
    one = int(raw_input("input number of one dollar bills : "))
    five = int(raw_input("input number of five dollar bills : "))
    ten = int(raw_input("input number of ten dollar bills : "))
    twenty = int(raw_input("input number of twenty dollar bills : "))

    takeoutpen = pen
    takeoutnick = nick
    takeoutdime = dime
    takeoutquart = quart
    takeoutone = one
    takeoutfive = five
    takeoutten = ten
    takeouttwenty = twenty


    total = (1 * pen) + (5 * nick) + (10 * dime) + (25 * quart) + (100 * one)\
        + (500 * five) + (1000 * ten) + (2000 * twenty)

    # 15000 * .01 is the amount you want to leave in your cash register
    remain = total - 15000

    remainder = remain

    while remainder > 0:

        if twenty != 0 and remainder >= 2000:
            remainder -= 2000
            twenty -= 1
        elif ten != 0 and remainder >= 1000:
            remainder -= 1000
            ten -= 1
        elif five != 0 and remainder >= 500:
            remainder -= 500
            five -= 1
        elif one != 0 and remainder >= 100:
            remainder -= 100
            one -= 1
        elif quart != 0 and remainder >= 25:
            remainder -= 25
            quart -= 1
        elif dime != 0 and remainder >= 10:
            remainder -= 10
            dime -= 1
        elif nick != 0 and remainder >= 5:
            remainder -= 5
            nick -= 1
        elif pen != 0 and remainder >= 1:
            remainder -= 1
            pen -= 1
        elif remainder != 0:
            print "Cant make it to $150"
            break
        total = 1 * pen + 5 * nick + 10 * dime + 25 * quart + 100 * one + 500 * five + 1000 * ten + 2000 * twenty
    print ""
    print "You should have.."
    print ""
    print "Pennnies: %s" % pen
    print "Nickels: %s" % nick
    print "Dimes: %s" % dime
    print "Quarters: %s" % quart
    print "Ones: %s" % one
    print "Fives: %s" % five
    print "Tens: %s" % ten
    print "Twenties: %s" % twenty
    print ""
    print "In your register"
    print ""
    print "Total: %s" % str(total*.01)
    print ""


    if takeouttwenty != twenty:
        print "Take out: " + str(takeouttwenty - twenty) + " Twenties"
    if takeoutten != ten:
        print "Take out: " + str(takeoutten - ten) + " Tens"
    if takeoutfive != five:
        print "Take out: " + str(takeoutfive - five) + " Fives"
    if takeoutone != one:
        print "Take out: " + str(takeoutone - one) + " Ones"
    if takeoutquart != quart:
        print "Take out: " + str(takeoutquart - quart) + " Quarters"
    if takeoutdime != dime:
        print "Take out: " + str(takeoutdime - dime) + " Dimes"
    if takeoutnick != nick:
        print "Take out: " + str(takeoutnick - nick) + " Nickels"
    if takeoutpen != pen:
        print "Take out: " + str(takeoutpen - pen) + " Pennies"
    again = raw_input("Again? y/n : ")
    if again == 'y':
        return calculate()
    else:
        pass

print calculate()