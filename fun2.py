def vac_feedback(vac, efficacy):
    print(f"{vac} vaccine is having {efficacy}% efficacy")
    if(efficacy > 50) and (efficacy < 75):
        print("Seems not so effective and might need more trials")
    elif(efficacy > 75) and (efficacy < 90):
        print("Can consider this vaccine")
    elif efficacy > 90:
        print("Sure, will take a shot of this")
    else:
        print("phuk kya the abhey")

vac_feedback("Pfizer", 95)
vac_feedback(efficacy=45, vac="unknown")

