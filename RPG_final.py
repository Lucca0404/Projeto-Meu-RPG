from RPG_Objetos import Warrior,Rogue,Mage,Paladin,Priest,Hunter,Hunker,Slunker,Flunker,Character,Monster,Items,Weapon,Battle,start_battle
from abc import ABC,abstractmethod
from time import sleep
from os import system
from msvcrt import getch
from new_RPG_biblioteca import print_introduction,print_attribut,print_loading,roll_dice,change_char,map, create_protagonist, chapter_one,chapter_one_map

def main() -> None:
    def print_logo():
        system('cls')
        sleep(4)
        print('       ########        ')
        print('     ############      ')
        print('    ########     #    ')
        print('    ##  ###  ##  #     ')
        print('    ######       #     ')
        print('     ###       ##      ')
        print('       ########         ')
        sleep(4)
        print('\nLucca Games presents.')
        sleep(5)
        system('cls')

    def print_menu():
        print('##### ##### #####    ##### ## ##    #####   #####')
        print('#   # #   # #        #   #  ###    ##   ## ##   ##')
        print('##### ##### #  ##    #####   #    ##     ###     ##')
        print('#  #  #     #   #    #       #     ##   ## ##   ##')
        print('#   # #     #####  # #       #      #####   #####')
        print('\nO enigma de PY\n\n')
        print('Aperte "S" para iniciar o jogo')
        print('Aperte "Q" para fechar o jogo')

    print_logo()
    while True:
        print_menu()
        player_choice = getch().lower()
        if player_choice.decode() == 'q':
            break
        elif player_choice.decode() == 's':
            system('cls')
            print_loading(2)
            protagonist = create_protagonist()
            print_loading(1)
            print('Gostaria de ver a introdução do jogo?\n \
                  [1] Ver introduçõa\n\
                  [2] Pular introdução\n')
            choice = getch().lower()
            if choice.decode() == '1':
                print_introduction(protagonist)
            elif choice.decode() == '2':
                system('cls')
                chapter_one()
                sleep(3)
                chapter_one_map()
                print('O jogo acabou por aqui, o resto ainda está em desenvolvimento')
                exit()
            else:
                system('cls')
                print('Opção digitada é inválida')
                continue
        else:
            system('cls')
            print('Opção digitada é inválida')
            continue
        
if __name__ == '__main__':
    main()
    