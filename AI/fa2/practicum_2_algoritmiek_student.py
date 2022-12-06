#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Final assignment 2: algoritmiek

(c) 2019 Hogeschool Utrecht,
Tijmen Muller (tijmen.muller@hu.nl)

Opdracht:
Beantwoord onderstaande vragen en werk onderstaande functies uit.
Voeg commentaar toe om je code toe te lichten.

Je kunt je functies testen met het gegeven raamwerk door het bestand
uit te voeren (of met behulp van `pytest`, als je weet hoe dat werkt).
Lever je werk in op Canvas als alle tests slagen.

Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""

# TODO: Vul hier je naam, klas en studentnummer in.
naam = "Bas van Dijk"
klas = "TICT-ICT-V10"
studentnummer = 1832998

"""
1.  Sorteeralgoritme

    Hieronder staat de pseudocode van een sorteeralgoritme:
    1. Startend vanaf het begin van een lijst, vergelijk elk element met zijn volgende buur.
    2. Als het element groter is dan zijn volgende buur, verwissel ze van plaats.
    3. Doorloop zo de lijst tot het eind.
    4. Als er verwisselingen zijn geweest bij stap 2., ga naar stap 1.

    1a. Handmatig toepassen
        Gegeven is de lijst l = [ 4, 3, 1, 2 ]. Geef de waardes die deze
        lijst aanneemt bij álle tussenstappen bij toepassing van
        bovenstaand sorteeralgoritme.
"""
#       TODO: Schrijf een loop voor het wisselen van elementen van klein naar groot.
"""

    1b. Implementatie
        Implementeer het sorteeralgoritme in Python in een functie
        hieronder genaamd my_sort(lst).

    1c. Best en worst case
        -   Stel je hebt een lijst met de waarden 1, 2 en 3. Bij welke
            volgorde van de waarden in de lijst is het sorteeralgoritme
            het snelste klaar (best-case scenario)?
            Hoeveel vergelijkingen (zoals beschreven in stap 1. van de
            pseudocode) zijn nodig geweest?
"""
#           TODO: Optimalizeer loop, check of lijst gesorteerd is.
"""


        -   Bij welke volgorde van de waarden in de lijst is het
            sorteeralgoritme het minst snel klaar (worst-case scenario)?
            Hoeveel vergelijkingen zijn nodig geweest?
"""
#           TODO: Groot naar klein -> Klein naar groot
"""


        -   Stel je hebt een lijst met de waarden 1 tot en met 4.
            Wat is nu het best-case scenario?
            Hoeveel vergelijkingen zijn er nodig?
            En wat is nu het worst-case scenario?
            Hoeveel vergelijkingen zijn er nodig?
"""
#           TODO: Best-case: al gesorteerd, 4 vergelijkingen.
#                 Worst-case: reverse gesorteerd, 7 vergelijkingen.
"""


        -   (Optioneel) Stel je hebt een lijst met de waarden 1 tot en met n
            (je weet nu dus niet precies hoeveel waarden er in de lijst
            zitten, het zijn er 'n').
            Wat is nu het best-case scenario?
            Hoeveel vergelijkingen zijn er nodig?
            En wat is nu het worst-case scenario?
            Hoeveel vergelijkingen zijn er nodig?
"""
#           TODO: [geef hier je antwoord]
"""
"""


def my_sort(lst):
    """
    Sorteer gegeven lijst volgens het algoritme zoals beschreven in de pseudocode.

    1. Startend vanaf het begin van een lijst, vergelijk elk element met zijn volgende buur.
    2. Als het element groter is dan zijn volgende buur, verwissel ze van plaats.
    3. Doorloop zo de lijst tot het eind.
    4. Als er verwisselingen zijn geweest bij stap 2., ga naar stap 1.

    Zorg dat de gegeven lijst niet verandert, maar geef een nieuwe, gesorteerde variant van de lijst terug.

    Args:
        lst (list): Een lijst met elementen van gelijk type, bijvoorbeeld gehele getallen.

    Returns:
        list: Een nieuwe, gesorteerde variant van lijst `lst`.
    """
    lst_sorted = lst[:]
    srtd = False

    for _ in lst:
        # srtd wordt True als lijst gesorteerd is.
        if not srtd:
            swap = 0  # Tel de swaps, als er 0 swaps gebeurd zijn is de lijst gesorteerd.
            for i, em in enumerate(lst_sorted):
                # Als het element rechts groter is dan het huidige element
                # en het huidige element is niet het einde van de lijst:
                #     Wissel huidige element met element rechts ervan.
                if i < len(lst_sorted) -1 and em > lst_sorted[i + 1]:
                    lst_sorted[i], lst_sorted[i + 1] = lst_sorted[i + 1], lst_sorted[i]
                    swap += 1 
            else:
                if swap == 0:
                    srtd = True
    return lst_sorted


def linear_search_recursive(lst, target):
    """
    Zoek een element in de gegeven lijst door middel van recursief lineair zoeken.

    Zorg dat de inhoud van de gegeven lijst niet verandert.

    Args:
        lst (list):     Een lijst met elementen van gelijk type, bijvoorbeeld gehele getallen.
        target (int):   Het gezochte element.

    Returns:
        bool: Of het element in de lijst voorkomt.
    """
    srch = lst[:]  # Maak een kopie van de lijst, zodat originele lst niet aangepast wordt. 
    
    # Als er geen elementen in de lijst zitten, is het target element niet gevonden in de lijst.
    if len(srch) == 1:
        return False
    # Als het eerste element de target is, dan is de target gevonden.
    elif srch[0] == target:
        return True
    # Als het eerste element niet de target is, dan weghalen en recursief in de functie stoppen.
    return linear_search_recursive(srch[1:], target)


def binary_search_recursive(lst, target):
    """
    (Optioneel) Zoek een element in de gegeven lijst door middel van recursief binair zoeken.

    Je mag ervan uit gaan dat de gegeven lijst al gesorteerd is.
    Zorg dat de inhoud van de gegeven lijst niet verandert.

    Args:
        lst (list):     Een lijst met elementen van gelijk type, bijvoorbeeld gehele getallen.
        target (int):   Het gezochte element.

    Returns:
        bool: Of het element in de lijst voorkomt.
    """
    srch = lst[:]  # kopie van lijst maken
    
    # Als er nog maar 1 element over is, checken of dat de target is.
    if len(srch) == 1:
        return True if srch[0] == target else False
        
    # deel de lijst in twee
    midindex = len(srch) // 2
    mid = srch[midindex]

    # bepaal in welk van de twee delen de target zich zou moeten bevinden. 
    if mid == target:
        return True
    elif mid > target:
        # Linker helft van de lijst 
        return binary_search_recursive(srch[:midindex], target)
    # Rechter helft van de lijst
    return binary_search_recursive(srch[midindex:], target)


"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import random


def test_id():
    assert naam != "", "Je moet je naam nog invullen!"
    assert studentnummer != -1, "Je moet je studentnummer nog invullen!"
    assert klas != "", "Je moet je klas nog invullen!"


def test_my_sort():
    lst_test = random.choices(range(-99, 100), k=6)
    lst_copy = lst_test.copy()
    lst_output = my_sort(lst_test)

    assert lst_copy == lst_test, "Fout: my_sort(lst) verandert de inhoud van lijst lst"
    assert lst_output == sorted(lst_test), \
        f"Fout: my_sort({lst_test}) geeft {lst_output} in plaats van {sorted(lst_test)}"


def test_linear_search_recursive():
    for _ in range(10):
        lst_test = random.sample(range(20), 6)
        target = random.randrange(20)
        found = target in lst_test
        lst_copy = lst_test.copy()

        outcome = linear_search_recursive(lst_test, target)
        assert lst_copy == lst_test, "Fout: linear_search_recursive(lst, target) verandert de inhoud van lijst lst"
        assert outcome == found, \
            f"Fout: linear_search_recursive({lst_test}, {target}) geeft {outcome} in plaats van {found}"


def test_binary_search_recursive():
    for _ in range(10):
        lst_test = sorted(random.sample(range(20), 6))
        target = random.randrange(20)
        found = target in lst_test
        lst_copy = lst_test.copy()

        outcome = binary_search_recursive(lst_test, target)
        assert outcome == found, \
            f"Fout: binary_search_recursive({lst_test}, {target}) geeft {outcome} in plaats van {found}"
        assert lst_copy == lst_test, "Fout: binary_search_recursive(lst, target) verandert de inhoud van lijst lst"


def __main():
    """ Test alle functies. """
    # Noodzakelijk voor gekleurde tekst binnen een Windows terminal
    import os
    os.system("")

    try:
        print("\x1b[32m")   # Groene tekstkleur
        test_id()

        test_my_sort()
        print("Je functie my_sort() werkt goed!")

        test_linear_search_recursive()
        print("Je functie linear_search_recursive() werkt goed!")

        test_binary_search_recursive()
        print("Je functie binary_search_recursive() werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("Lever je werk nu in op Canvas...")

    except AssertionError as ae:
        print("\x1b[31m")   # Rode tekstkleur
        if not ae:
            print("Je code veroorzaakt onderstaande AssertionError:")
            raise ae
        else:
            print(ae)

    print("\x1b[0m")    # Reset tekstkleur


if __name__ == '__main__':
    __main()
