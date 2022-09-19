import random

class couponCode:
    list1 = []

    def generateCoupon(num):

        for i in range(num):
            coupon = random.randint(1, 100)
            if coupon not in couponCode.list1:
                couponCode.list1.append(coupon)


num = int(input("Enter any number:"))
print("total random number needed to have all distinct numbers are :")
couponCode.generateCoupon(num)
print(couponCode.list1)