
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




    total = float((.01 * pen) + (.05 * nick) + (.10 * dime) + (.25 * quart) + (1 * one)\
        + (5 * five) + (10 * ten) + (20 * twenty))
    # 150 is the amount you want to leave in your cash register
    remain = total - 150
    remainder = remain

    while remainder > 0:
        total = .01 * pen + .05 * nick + .10 * dime + .25 * quart + 1 * one + 5 * five + 10 * ten + 20 * twenty
        if twenty != 0 and remainder >= 20:
            remainder -= 20
            twenty -= 1
        elif ten != 0 and remainder >= 10:
            remainder -= 10
            ten -= 1
        elif five != 0 and remainder >= 5:
            remainder -= 5
            five -= 1
        elif one != 0 and remainder >= 1:
            remainder -= 1
            one -= 1
        elif quart != 0 and remainder >= .25:
            remainder -= .25
            quart -= 1
        elif dime != 0 and remainder >= .10:
            remainder -= .10
            dime -= 1
        elif nick != 0 and remainder >= .05:
            remainder -= .05
            nick -= 1
        elif pen != 0 and remainder >= .01:
            remainder -= .01
            pen -= 1

        elif remainder != 0:
            print ""
            print "Please take out " + str(total-150) + " from the register"
            break
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
    print "Total: %s" % str(total)
    print ""

    '''nickels: %s, dimes: %s, quarters: %s, ones: %s, five: %s, ten: %s, twenty: %s " % \
           (pen, nick, dime, quart, one, five, ten, twenty), "total: " + str(total)'''
    again = raw_input("Again? y/n : ")
    if again == 'y':
        return calculate()
    else:
        pass

print calculate()