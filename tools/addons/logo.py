"""This module provides a function that prints the logo's application."""

import os

from colorama import Fore as F


def show_logo() -> None:
    """Print the application logo.

    Args:
        None

    Returns:
        None
    """
    logo = """   _,.-------.,_
             ,;~'             '~;,
           ,;                     ;,
          ;                         ;
         ,'                         ',
        ,;                           ;,
        ; ;                         ; ;           
        | ;   ______       ______   ; |         
        |  `/         .           \'  |         
        |  ~  ,-~~~^~, | ,~^~~~-,  ~  |          
        |   |        }:{        |   |            
        |   l       / | \       !   |             
        .~  (__,.--       --.,__)  ~.                        
        |     ---;' / | \ `;---     |                        
         \__.       \/^\/       .__/                         
          V| \                 / |V                          
           | |T~\___!___!___/~T| |                   
           | |`IIII_I_I_I_IIII'| |                                                                                                                                                          
           |  \,III I I I III,/  |
            \   `~~~~~~~~~~'    /            
              \   .       .   /              
                \.    ^    ./
                  ^~~~^~~~^

               GITHUB:https://github.com/P0CK3T2       
               POWERED BY P0CK3T2

  """

    print(f"{F.RED}{logo}")
    print("├─── DOS TOOL")
    print("├─── AVAILABLE METHODS")
    print("├─── LAYER 7: HTTP | HTTP-PROXY | SLOWLORIS | SLOWLORIS-PROXY")
    if os.name != "nt":
        print("├─── LAYER 4: SYN-FLOOD")
        print("├─── LAYER 2: ARP-SPOOF | DISCONNECT")
    print("├───┐")
