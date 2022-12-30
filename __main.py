"""
Project Password Generator

Valt te verdelen in meerdere mini projecten:
1. Password Generator
    1. Hoeveel letters (DONE)
    2. Hoofdletters/kleine letters (DONE)
    3. Speciale tekens (DONE)
    4. (Optioneel:) Vraag zin als input en convert dat tot leesbaar wachtwoord met bovenstaande categorieen
2. Overzicht per wachtwoord
    1. Naam website/app/notitie
    2. Map
    3. Link
    4. Gebruikersnaam
    5. Wachtwoord (onzichtbaar maken/bolletjes)
    6. Notities
    7. Optie tot bewerken/verwijderen/kopieren/delen?
    8. Overige: Maak favoriet;  geef aan of wachtwoord altijd ingevuld moet worden voor bekijken item; ntb
3. Overzicht startmenu
    1. Mappen op alphabetische volgorde
    2. Losse items op alphabetische volgorde
4. Maak database voor alle items per gebruiker
5. Beveiliging
    1. Hoofdwachtwoord/Biometrische gegevens
    2. Random keren vragen om invullen wachtwoord
    3. Ntb
    4. Creeer inloggegevens
6. Integratie bovenstaande items
7. Maak het mooi
8. Convert tot Android app
"""

from PW_Generator import PW_Gen



def main():
    reshuffle_bool = False
    generator_class = PW_Gen.Generator(reshuffle_bool)
    password = generator_class.run()

    print("Your final password is: {}.\n".format(password))


if __name__ == '__main__':
    main()