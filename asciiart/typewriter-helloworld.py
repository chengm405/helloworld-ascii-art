import sys
import time

def typewriter_effect(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  

hello_world_text = """
H   H  EEEEE  L      L       OOO      W   W   OOO   RRRR   L      DDDD   !!
H   H  E      L      L      O   O     W W W  O   O  R   R  L      D   D  !!
HHHHH  EEEE   L      L      O   O     W W W  O   O  RRRR   L      D   D  !!
H   H  E      L      L      O   O     W W W  O   O  R   R  L      D   D   
H   H  EEEEE  LLLLL  LLLLL   OOO       W W    OOO   R   R  LLLLL  DDDD   !!
"""

typewriter_effect(hello_world_text, delay=0.05) 

