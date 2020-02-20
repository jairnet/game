# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

rules = {
        'Piedra-Tijera': (1,0),
        'Piedra-Papel': (0,1),
        'Piedra-Lagarto': (1,0),
        'Piedra-Spock': (0,1),
        'Piedra-Piedra': (0,0),
        'Papel-Tijera': (0,1),
        'Papel-Piedra': (1,0),
        'Papel-Lagarto': (0,1),
        'Papel-Spock': (1,0),
        'Papel-Papel': (0,0),
        'Tijera-Papel': (1,0),
        'Tijera-Piedra': (0,1),
        'Tijera-Lagarto': (1,0),
        'Tijera-Spock': (0,1),
        'Tijera-Tijera': (0,0),
        'Lagarto-Tijera': (0,1),
        'Lagarto-Papel': (1,0),
        'Lagarto-Piedra': (0,1),
        'Lagarto-Spock': (1,0),
        'Lagarto-Lagarto': (0,0),
        'Spock-Tijera': (1,0),
        'Spock-Papel': (0,1),
        'Spock-Piedra': (1,0),
        'Spock-Lagarto': (0,1),
        'Spock-Spock': (0,0)
    }
