import math
#Takes a list of RGB integer decimal values (in that order) and returns a
#hexadecimal string in the form of "#RRGGXBB"
def hexstring(color):
    hexcode = "#"
    
    for dec in color:
        rgb = hex(dec)
        hex_dig = rgb[2:] 
        if len(hex_dig)==1:
            hex_dig = '0' + hex_dig
        hexcode += hex_dig
        
    return hexcode
    
def make_hue(rdns):
    pi = math.pi
    red = 0
    green = 0
    blue = 0
    
    while rdns > 2*pi:
        rdns -= 2*pi
    while rdns < 0:
        rdns += 2*pi
        
    if rdns >= 0 and rdns <= 2*pi/3:
            red = 255
    elif rdns > 2*pi/3 and rdns < pi:
            redratio = (rdns - (pi/3))/(pi/3)
            red = int(round(225*redratio))
    elif rdns > 5*pi/3 and rdns < 2*pi:
            redratio = ((pi) - rdns)/(pi/3)
            red = int(round(225*redratio))
    
            
    if rdns >= 2*pi/3 and rdns <= 4*pi/3:
            green = 255
    elif rdns > pi/3 and rdns < 2*pi/3:
            greenratio = (rdns - (5*pi/3))/(pi/3)
            green = int(round(225*greenratio))
    elif rdns > 4*pi/3 and rdns < 5*pi/3:
            greenratio = ((5*pi/3) - rdns)/(pi/3)
            green = int(round(225*greenratio))

            
    if (rdns >= 4*pi/3 and rdns <= 2*pi):
            blue = 255
    elif rdns > pi and rdns < 4*pi/3:
            blueratio = (rdns - (pi/3))/(pi/3)
            blue = int(round(225*blueratio))
    elif rdns > 0 and rdns < pi/3:
            blueratio = ((pi/3) - rdns)/(pi/3)
            blue = int(round(225*blueratio))

            
    hue = [red, green, blue]
            
    return hue