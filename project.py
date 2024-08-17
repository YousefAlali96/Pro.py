def est(f):
    x = 30000000000 / f
    if x > 11:
        t = 0
    elif x == 11:
        t = 0.0002
    elif x >= 10:
        t = 0.0009
    elif x > 9:
        t = 0.0012
    elif x == 9:
        t = 0.0015
    elif x > 8:
        t = 0.0022
    elif x == 8:
        t = 0.003
    elif x > 7:
        t = 0.0045
    elif x == 7:
        t = 0.006
    elif x > 6:
        t = 0.018
    elif x == 6:
        t = 0.03
    elif x > 5:
        t = 0.045
    elif x == 5:
        t = 0.055
    elif x > 4:
        t = 0.057
    elif x == 4:
        t = 0.06
    elif x > 3:
        t = 0.065
    elif x == 3:
        t = 0.07
    elif x > 2:
        t = 0.08
    elif x == 2:
        t = 0.09
    elif x > 1:
        t = 0.15
    elif x == 1:
        t = 0.2
    elif x > 0.9:
        t = 0.23
    elif x == 0.9:
        t = 0.25
    elif x > 0.8:
        t = 0.27
    elif x == 0.8:
        t = 0.3
    elif x > 0.7:
        t = 0.35
    elif x == 0.7:
        t = 0.4
    elif x > 0.6:
        t = 0.45
    elif x == 0.6:
        t = 0.5
    elif x > 0.5:
        t = 0.75
    elif x == 0.5:
        t = 0.8
    elif x > 0.4:
        t = 0.9
    elif x == 0.4:
        t = 1
    elif x > 0.3:
        t = 1.5
    elif x == 0.3:
        t = 2
    else:
        t = 3
    
    return t

def den(x):
    c = 0

    if x > 640:
        c = 0.03
    elif x > 500 and x <= 640:
        c = 0.032
    elif x > 300 and x <= 500:
        c = 0.04
    elif x > 200 and x <= 300:
        c = 0.085
    elif x > 150 and x <= 200:
        c = 0.17
    elif x > 128 and x <= 150:
        c = 0.23
    elif x > 90 and x <= 128:
        c = 0.32
    elif x > 60 and x <= 90:
        c = 0.48
    elif x > 30 and x <= 60:
        c = 0.85
    elif x > 0 and x <= 30:
        c = 2.3

    return c


def temp20(lamda):
    B = 0

    if lamda >= 10:
        B = 0.005
    elif lamda >= 7 and lamda < 10:
        B = 0.01
    elif lamda >= 5 and lamda < 7:
        B = 0.02
    elif lamda >= 4 and lamda < 5:
        B = 0.03
    elif lamda >= 3 and lamda < 4:
        B = 0.05
    elif lamda >= 2 and lamda < 3:
        B = 0.13
    elif lamda >= 1 and lamda < 2:
        B = 0.5

    return B


def temp5(lamda):
    B = 0

    if lamda >= 10:
        B = 0.01
    elif lamda >= 7 and lamda < 10:
        B = 0.02
    elif lamda >= 5 and lamda < 7:
        B = 0.04
    elif lamda >= 4 and lamda < 5:
        B = 0.06
    elif lamda >= 3 and lamda < 4:
        B = 0.1
    elif lamda >= 2 and lamda < 3:
        B = 0.26
    elif lamda >= 1 and lamda < 2:
        B = 1

    return B
