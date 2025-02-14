age = 10
is_vip = False

if is_vip:
    print("welcome VIP! enjoy exclusive access and free drinks")
elif age >= 25:
    print("entry granted,plus free drinks")
elif age >= 18 and age < 25:
    print("entry granted, but no free drink")
else:
    print("this event is not for you,entry not granted")

