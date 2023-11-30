products = ["K1565_2017_ST7745", "T2432_2019_FE84",
            "T8551_2018_XA413", "T3345_2019_JK142",
            "Y51372_2019_HJ2", "Y76715_2017_AB3",
            "E98144_2018_21T", "T7733_2020_CE55",
            "E7614_2021_XZA784", "E9722_2017_MHE67",
            "Y82018_2020_FI95", "T61287_2021_IA293",
            "E9152_2019_TY5", "T774_2021_OB672"]

ordercode = input("Give the order code:\n")
ordercode = ordercode.upper()

#for-loop checks the new list for given by user order code and
# when found adds the right product info to use_order list,
# after it prints year of the right product:
for product in products:
    item = product.split("_")
    if ordercode == item[0]:
        print(f"Year of the order code: {item[1]}")
        break
