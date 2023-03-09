def cost_delivery(quantity, *args, discount=0):
    first_delivery = 5
    last_delivery = 2
    cost = 0
    for i, _ in enumerate(range(0, quantity)):
        if i == 0:
            cost = first_delivery
        else:
            cost += last_delivery
    return cost - cost * discount