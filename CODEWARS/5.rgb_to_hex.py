def rgb(r, g, b):
    # your code here :
    
    return (((f"{r:02x}" if r >=0 else "00") if r <= 255 else "ff") + ((f"{g:02x}" if g >= 0 else "00") if g <= 255 else "ff") + ((f"{b:02x}" if b >= 0 else "00") if b <= 255 else "ff")).upper()