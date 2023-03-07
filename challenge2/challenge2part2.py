import math

prices = [
        437,309,628,198,675,637,549,133,370,570,681,396,215,349,699,203,66,86,56,438,680,555,434,432,399,239,403,595,512,630,
        641,660,665,553,462,286,579,353,523,202,287,647,155,291,443,448,369,209,358,220,84,429,677,206,419,301,179,615,454,
        158,627,119,60,633,242,583,643,601,500,210,248,363,135,535,611,97,392,52,475,101,477,518,509,300,484,688,670,385,
        496,294,537,360,446,126,51,68,276,580,273,557,463,67,338,697,526,664,694,304,285,337,270,689,356,145,280,107,343,
        659,409,459,205
    ]

def get_prices_input(message):
    """ Ignore this function you don't need to understand or change it """
    if "testInput" in message:
        testInputString = message.split("testInput")[1].rstrip().lstrip()
        pricesTestingInput = testInputString.split(",")
        return [int(k) for k in pricesTestingInput]
    return prices


def problem2_4(message):
    prices = get_prices_input(message)
    mostExpensivePrice = 0

    return str(mostExpensivePrice)


def problem2_5(message):
    prices = get_prices_input(message)
    totalCost = 0


    return str(totalCost)


def problem2_6(message):
    prices = get_prices_input(message)
    totalCost = 0


    return str(totalCost)