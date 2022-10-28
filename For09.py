def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    s=0
    l=[]
    for i in range(10):
        s+=price
        l.append(s)
    return l
print(main(2.25))