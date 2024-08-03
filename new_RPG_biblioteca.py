import os
import time
import random
import msvcrt
import copy
from RPG_Objetos import Warrior,Rogue,Mage,Paladin,Priest,Hunter,Hunker,Slunker,Flunker,Character,Monster,Items,Weapon,Battle,start_battle,pocao,bomba

def print_attribut(attribut):
    numbers = '1234567890'
    form_word = ''
    aux_word = ''
    i = 0

    attribut = str(attribut)

    while i < len(attribut):

        sort_num = random.choice(numbers)
        form_word += sort_num
        time.sleep(0.05)
        os.system('cls')
        print(form_word)
        
        if sort_num == attribut[i]:
            aux_word += sort_num
            i += 1
            
        else:
            form_word = aux_word
            continue

def roll_dice(attribut):
    dice_result = random.randrange(1,21)
    test_result = dice_result + attribut

    print_attribut(test_result)
    if dice_result == 20:
        print('Acerto Crítico!!!')
    elif dice_result == 1:
        print('Erro crítico!!!')
    else:
        print(f'O resultado do dado foi {test_result}')
    return test_result

def print_loading(rep):
    for i in range(rep):
        print('Loading')
        time.sleep(0.5)
        os.system('cls')
        print('Loading.')
        time.sleep(0.5)
        os.system('cls')
        print('Loading..')
        time.sleep(0.5)
        os.system('cls')
        print('Loading...')
        time.sleep(0.5)
        os.system('cls')

def class_inf():
    while True:
        print('As classes de RPG.py definem o seu estilo de jogo, cada uma possui atributos, quantidade vida e ataque, e vantagens próprias ')
        print('Classes disponíveis:')
        print('- Guerreiro / Warrior')
        print('- Ladino / Rogue')
        print('- Mago / Mage')
        print('- Caçador / Hunter')
        print('- Sacerdote / Priest')
        print('- Paladino / Paladin')
        choice = input('Escolha uma classe para verificar suas informações ou aperte "S" para voltar a criação de personagem: ').lower()
        while choice != 's':
            if choice == 'guerreiro' or choice == 'warrior':
                print('Warrior: Guerreiros são fortes e resistentes, possuem bastante vida e ataque e são ótimos para batalhas corpo-a-corpo')
                pause = msvcrt.getch()
                break
            elif choice == 'ladino' or choice == 'rogue':
                print('Rogue: Ladinos são ágeis e furtivos, possuem bastante destreza e dano e são ótimos enganadores')
                pause = msvcrt.getch()
                break
            elif choice == 'mago' or choice == 'mage':
                print('Mage: Magos são inteligentes e sábios, possuem um alto dano mágico. Perfeito para pulverizar seu oponente')
                pause = msvcrt.getch()
                break
            elif choice == 'caçador' or choice == 'hunter':
                print('Hunter: Caçadores são espertos e atentos, possuem ótimas miras e sempre andam com suas armadilhas')
                pause = msvcrt.getch()
                break
            elif choice == 'sacerdote' or choice == 'priest':
                print('Priest: Sacerdotes são sábios e pacientes, possuem poderes de cura incríveis e uma ótima resistência')
                pause = msvcrt.getch()
                break
            elif choice == 'paladino' or choice == 'paladin':
                print('Paladin: Paladinos são fiéis e ótimos em combate, além de terem bastante dano e vida tambem conseguem se curar')
                pause = msvcrt.getch()
                break
            else:
                print('Opção digitada é inválida, digite o nome de uma das classes')
                pause = msvcrt.getch()
                break
        break

def print_introduction(char : Character):
    os.system('cls')
    print('Ano 16XX reino de PY, um lugar de guerra e destruição')
    time.sleep(4.0)
    print('Você é um morador do burgo de Flask, o maior centro comercial do reino de PY')
    time.sleep(4.0)
    print('Recentemente o mundo está presenciando a maior guerra já registrada em sua história')
    time.sleep(4.0)
    print('O exército dos guerreiros Django está dominando grande parte do continente e não vão parar até estabelerecerem a sua tirania')
    time.sleep(4.0)
    print('Em breve eles chegarão em sua cidade, e todos do exército de Flask estão preocupados com o resultado desse acontecimento\n')
    time.sleep(6.0)
    print('Aperte qualquer botão para prosseguir')
    pause = msvcrt.getch()
    os.system('cls')
    while True:
        print('Dia 1')
        time.sleep(5.0)
        print('São 4 horas da manhã e você acorda assustado com uma batida na porta')
        time.sleep(5)
        print('A lua está cheia lá fora, o brilho dela ilumina a sua janela')
        time.sleep(5)
        print('um silêncio quase perfeito toma conta do seu quarto')
        time.sleep(5)
        print('Ir até a porta?')
        time.sleep(1.5)
        print('\nEscolha um número referente a uma das opções abaixo:\n'
              '[1] Abrir a porta\t\tLivre\n'
              f'[2] Espiar pela janela\t\tPercepção(+{char.perception})\n'
              '[3] Voltar a dormir\t\tLivre\n')
        Choice = msvcrt.getch()
        match Choice.decode():
            case '1':
                print('Você anda cautelosamente até sua porta')
                time.sleep(5)
                print('Ao abrir a porta você olha para os lados e não vê nada muito especial')
                time.sleep(4)
                print('Porém ao olhar para baixo você enxerga uma carta em sua frente')
                time.sleep(4)
                print('Ao abrir a carta você encontra uma mensagem assinada pelo chefe do exército de Flask')
                time.sleep(5)
                print('Nela, ele ordena que todos os moradores retirem-se da cidade o mais rápido possível')
                time.sleep(5)
                print('O exercíto de Django se aproxima e logo todo o local será tomado por guerra e destruição')
                time.sleep(6)
                print('Você não parece ter muita opção...')
                time.sleep(4)
                print('Não é a primeira vez que as guerras pertubam a sua vida e nem será a última')
                time.sleep(5)
                print('Pegue seus pertences mais importantes e saia de sua casa o mais rápido possível')
                time.sleep(5)
                print('Aperte qualquer botão para prosseguir')
                pause = msvcrt.getch()
                return True
            case '2':
                result = char.class_action(char.perception,10)
                match result:
                    case 'CriticError':
                        print('Você tenta espiar pela janela mas está morto de sono')
                        time.sleep(3)
                        print('Você não consegue ver nada lá fora')
                        time.sleep(3)
                    case 'CriticHit':
                        print('Você espia atentamente pela janela')
                        time.sleep(3)
                        print('Do outro lado da sua porta um homem de capuz preto aguarda pacientimente por você')
                        time.sleep(3)
                        print('De algum modo você sente que não é a primeira vez que você o vê')
                        time.sleep(4)
                    case 'Error':
                        print('Você espia pela sua janela')
                        time.sleep(3)
                        print('Não parece haver nada de especial lá fora')
                        time.sleep(3)
                    case 'Hit':
                        print('Você espia pela sua janela')
                        time.sleep(3)
                        print('Do outro lado da sua porta não a ninguêm te esperando, apenas uma carta em frente a ela')
                        time.sleep(3)
                while True:
                    print('Abrir a porta?\n')
                    print('[1] Abrir')
                    print('[2] Voltar a dormir')
                    Choice = msvcrt.getch()
                    if Choice.decode() == '1':
                        print('Você anda cautelosamente até sua porta')
                        time.sleep(5)
                        print('Ao abrir a porta você olha para os lados e não vê nada muito especial')
                        time.sleep(4)
                        print('Porém ao olhar para baixo você enxerga uma carta em sua frente')
                        time.sleep(4)
                        print('Ao abrir a carta você encontra uma mensagem assinada pelo chefe do exército de Flask')
                        time.sleep(5)
                        print('Nela, ele ordena que todos os moradores retirem-se da cidade o mais rápido possível')
                        time.sleep(5)
                        print('O exercíto de Django se aproxima e logo todo o local será tomado por guerra e destruição')
                        time.sleep(6)
                        print('Você não parece ter muita opção...')
                        time.sleep(4)
                        print('Não é a primeira vez que as guerras pertubam a sua vida e nem será a última')
                        time.sleep(5)
                        print('Pegue seus pertences mais importantes e saia de sua casa o mais rápido possível')
                        time.sleep(5)
                        print('Aperte qualquer botão para prosseguir')
                        pause = msvcrt.getch()
                        return True
                    elif Choice.decode() == '2':
                        print('Você ignora a batida na porta, fecha os olhos e volta para o seu sono profundo...')
                        time.sleep(4)
                        os.system('cls')
                        break
                    else:
                        print('Opção inválida, escolha uma opção entre 1,2 ou 3')
                        print('Aperte qualquer botão para prosseguir')
                        pause = msvcrt.getch()
                        os.system('cls')
                        continue
            case '3':
                print('Você ignora a batida na porta, fecha os olhos e volta para o seu sono profundo...')
                time.sleep(4)
                os.system('cls')
                continue
            case _:
                print('Opção inválida, escolha uma opção entre 1,2 ou 3')
                print('Aperte qualquer botão para prosseguir')
                pause = msvcrt.getch()
                os.system('cls')
                continue

def create_protagonist():
    Rpg_classes = ['mage','warrior','rogue','priest','paladin','hunter','mago','guerreiro','ladino','sacerdote','paladino','caçador']
    print('Crie seu personagem')
    global protagonist
    while True:
        Name = input('Escolha o seu nome: ')
        print(f'Tem certeza que seu nome será {Name}?')
        print('Aperte "E" para confirmar ou outro botão para voltar')
        Choice = msvcrt.getch().lower()
        if Choice.decode() != 'e':
            continue
        while True:
            print('Para ver as classes de RPG.py digite "inf"')
            Rpg_class = input('Escolha a sua classe: ').lower()
            if Rpg_class == 'inf':
                class_inf()
                os.system('cls')
                continue
            elif Rpg_class not in Rpg_classes:
                print('A classe digitada não existe')
                continue
            print(f'Tem certeza que sua classe será {Rpg_class}?')
            print('Aperte "E" para confirmar ou outro botão para voltar')
            Choice = msvcrt.getch().lower()
            if Choice.decode() != 'e':
                continue
            if Rpg_class == 'warrior' or Rpg_class == 'guerreiro':
                protagonist = Warrior()
                protagonist.name = Name
            elif Rpg_class == 'rogue' or Rpg_class == 'ladino':
                protagonist = Rogue()
                protagonist.name = Name
            elif Rpg_class == 'mage' or Rpg_class == 'mago':
                protagonist = Mage()
                protagonist.name = Name
            elif Rpg_class == 'hunter' or Rpg_class == 'caçador':
                protagonist = Hunter()
                protagonist.name = Name
            elif Rpg_class == 'priest' or Rpg_class == 'sacerdote':
                protagonist = Priest()
                protagonist.name = Name
            elif Rpg_class == 'paladin' or Rpg_class == 'paladino':
                protagonist = Paladin()
                protagonist.name = Name
            print(f'{protagonist.name} criado com sucesso')    
            time.sleep(3)
            return protagonist
        
def map(lines,collums):
    create_map = [
                '#'*collums if i == 0 or i == lines-1 else '#'+' '*(collums-2)+'#' for i in range(lines)
               ]
    return create_map
        
def change_char(string, new_char,*index):
    aux = 0
    for i in index:
        if aux == 0:
            new_string =string[:i] + new_char + string[i + 1:]
            aux+=1
        else:
            new_string = new_string[:i] + new_char + new_string[i + 1:]
    return new_string

def chapter_one():
    print('Você arruma sua mochila com suprimentos suficientes para a próxima semana')
    time.sleep(4)
    print('Além disso, talvez seja inteligente levar uma arma com você')
    time.sleep(3)
    print(f'{protagonist.name} obteve {protagonist.weapon.name}')
    time.sleep(3)
    print('Você sente o peso da mochila em suas costas')
    time.sleep(4)
    print('Provavelmente em pouco tempo sua casa será destrúida')
    time.sleep(4)
    print('Você lembra que trabalhou duro para tê-la')
    time.sleep(3)
    print('Abdicou de passar tempo com sua família e amigos')
    time.sleep(3)
    print('Tudo para ter um teto em cima de sua cabeça')
    time.sleep(3)
    print('Ter uma casa deveria ser o mínimo que você merece por se esforçar tanto')
    time.sleep(4)
    os.system('cls')
    print('Então por que você está nessa situação?')
    time.sleep(4)
    print('Isso é culpa sua?')
    time.sleep(3)
    print('Não tem como ser')
    time.sleep(3)
    os.system('cls')
    print('Não tem como ser.')
    time.sleep(3)
    os.system('cls')
    print('Não tem como ser..')
    time.sleep(3)
    os.system('cls')
    print('Não tem como ser...')
    time.sleep(3)
    os.system('cls')
    print('já está quase amanhecendo')
    time.sleep(3)
    print('Você decide que é melhor já ir andando...')
    return True

def chapter_one_map():
    player_char = '8'
    item_char = '!'
    player_x = 5
    player_y = 2
    interact = 0
    map_number = 0

    house_high = 5
    house_large = 11
    house = map(house_high,house_large)
    house[0] = change_char(house[0],' ',4,5,6)
    house[3] = change_char(house[3],item_char,9)
    aux_house = copy.deepcopy(house)
    
    while map_number == 0:
        house = copy.deepcopy(aux_house)
        house[player_y] = change_char(house[player_y],player_char,player_x)
        print('Aperte "I" para interagir com o cenário')
        print(*house, sep='\n')
        move = msvcrt.getch().lower()
        
        match move.decode():
            case'w':
                if house[player_y-1][player_x] == ' ':
                    player_y -= 1
            case's':
                if house[player_y+1][player_x] == ' ':
                    player_y += 1
            case'd':
                if house[player_y][player_x+1] == ' ':
                    player_x += 1
            case'a':
                if house[player_y][player_x-1] == ' ':
                    player_x -= 1
            case'i':
                interact = 1

        if player_x == 4 and player_y == 0 or player_x == 5 and player_y == 0 \
        or player_x == 6 and player_y == 0:
            map_number+=1

        if (player_x == 8 and player_y == 3 or player_x == 9 and player_y == 2) and interact == 1 and aux_house[3][9] == '!':
            print(f'Você achou uma poção')
            protagonist.items.append(pocao)
            pause = msvcrt.getch()
            aux_house[3] = change_char(aux_house[3],' ',9)
        interact = 0
        os.system('cls')

    map_one_high = 15
    map_one_large = 101
    map_one = map(map_one_high,map_one_large)

    for draw in range(1,14):
        if draw == 4 or draw == 10:
            map_one[draw] = change_char(map_one[draw],'*',21,22,23,24,25,26,27,28,29,41,42,43,44,45,46,47,48,49,61,62,63,64,65,66,67,68,69)
        if draw == 5 or draw == 9:
            map_one[draw] = change_char(map_one[draw],'*',1,2,3,4,5,6,7,8,9)
            map_one[draw] = change_char(map_one[draw],'(',95)
        elif draw == 6 or draw == 7 or draw == 8:
            map_one[draw] = change_char(map_one[draw],'-',1,2,3,4,5,6,7,8)
            map_one[draw] = change_char(map_one[draw],'*',9)
            if draw != 7:
                map_one[draw] = change_char(map_one[draw],'=',94,95,96,97,98,99)
        else:
            map_one[draw] = change_char(map_one[draw],'*',21,29,41,49,61,69)
            map_one[draw] = change_char(map_one[draw],'(',95)

    map_one[2] = change_char(map_one[2],item_char,2)
    map_one[12] = change_char(map_one[12],item_char,55)

    enemy_char = 'm'
    strong_enemy_char = 'M'
    aux_map_one = copy.deepcopy(map_one)
    player_x = 11
    player_y = 7
    enemy_x = 50
    enemy_y = 7
    strong_enemy_x = 80
    strong_enemy_y = 3
    not_shift = 1

    Goblin = Slunker()
    Goblin.name = 'Goblin'
    Goblin.level = 1
    Goblin.give_attribut()
    Skull = Flunker()
    Skull.name = 'Skull'
    Skull.level = 2
    Skull.give_attribut()
    Imp = Flunker()
    Imp.name = 'Diabrete'
    Imp.level = 1
    Imp.give_attribut()

    while map_number == 1:
        map_one = copy.deepcopy(aux_map_one)
        map_one[player_y] = change_char(map_one[player_y],player_char,player_x)
        map_one[enemy_y] = change_char(map_one[enemy_y],enemy_char,enemy_x)
        map_one[strong_enemy_y] = change_char(map_one[strong_enemy_y],strong_enemy_char,strong_enemy_x)
        if not_shift:
            print('Aperte shift para correr')
        print('Objetivo: Vá até a ponte')
        print(*map_one, sep='\n')

        move = msvcrt.getch()
        enemy_move = random.randrange(0,4)
        strong_enemy_move = random.randrange(0,2)

        match move.decode():
            case'w':
                if map_one[player_y-1][player_x] == ' ':
                    player_y-=1
            case's':
                if map_one[player_y+1][player_x] == ' ':
                    player_y+=1
            case'd':
                if map_one[player_y][player_x+1] == ' ':
                    player_x+=1
            case'a':
                if map_one[player_y][player_x-1] == ' ':
                    player_x-=1
            case'i':
                interact = 1
            case'W':
                not_shift = 0
                if map_one[player_y-2][player_x] == ' ' and map_one[player_y-1][player_x] == ' ':
                    player_y-=2
                elif map_one[player_y-1][player_x] == ' ':
                    player_y-=1
            case'S':
                not_shift = 0
                if map_one[player_y+2][player_x] == ' ' and map_one[player_y+1][player_x] == ' ':
                    player_y+=2
                elif map_one[player_y+1][player_x] == ' ':
                    player_y+=1
            case'D':
                not_shift = 0
                if map_one[player_y][player_x+2] == ' ' and map_one[player_y][player_x+1] == ' ':
                    player_x+=2
                elif map_one[player_y][player_x+1] == ' ':
                    player_x+=1
            case'A':
                not_shift = 0
                if map_one[player_y][player_x-2] == ' ' and map_one[player_y][player_x-1] == ' ':
                    player_x-=2
                elif map_one[player_y][player_x-1] == ' ':
                    player_x-=1
            case'I':
                interact = 1

        match enemy_move:
            case 0:
                if map_one[enemy_y-1][enemy_x] == ' ' or map_one[enemy_y-1][enemy_x] == player_char:
                    enemy_y-=1
            case 1:
                if map_one[enemy_y+1][enemy_x] == ' ' or map_one[enemy_y+1][enemy_x] == player_char:
                    enemy_y+=1
            case 2:
                if map_one[enemy_y][enemy_x+1] == ' ' or map_one[enemy_y][enemy_x+1] == player_char:
                    enemy_x+=1
            case 3:
                if map_one[enemy_y][enemy_x-1] == ' ' or map_one[enemy_y][enemy_x-1] == player_char:
                    enemy_x-=1

        match strong_enemy_move:
            case 0:
                if player_y < strong_enemy_y:
                    if map_one[strong_enemy_y-1][strong_enemy_x] == ' ' or map_one[enemy_y-1][enemy_x] == player_char:
                        strong_enemy_y-=1
                else:
                    if map_one[strong_enemy_y+1][strong_enemy_x] == ' ' or map_one[enemy_y+1][enemy_x] == player_char:
                        strong_enemy_y+=1
            case 1:
                if player_x > strong_enemy_x:
                    if map_one[strong_enemy_y][strong_enemy_x+1] == ' ' or map_one[enemy_y][enemy_x+1] == player_char:
                        strong_enemy_x+=1
                else:
                    if map_one[strong_enemy_y][strong_enemy_x-1] == ' ' or map_one[enemy_y][enemy_x-1] == player_char:
                        strong_enemy_x-=1

        if (player_x == 3 and player_y == 2 or player_x == 2 and player_y == 3 or player_x == 2 and player_y == 1 or player_x == 1 and player_y == 2) and interact == 1 and aux_map_one[2][2] == '!':
            print(f'Você achou uma bomba')
            protagonist.items.append(bomba)
            pause = msvcrt.getch()
            aux_map_one[2] = change_char(aux_map_one[2],' ',2)

        if (player_x == 56 and player_y == 12 or player_x == 54 and player_y == 12 or player_x == 55 and player_y == 13 or player_x == 55 and player_y == 11) and interact == 1 and aux_map_one[12][55] == '!':
            print(f'Você achou uma poção')
            protagonist.items.append(pocao)
            pause = msvcrt.getch()
            aux_map_one[12] = change_char(aux_map_one[12],' ',55)

        if player_x == enemy_x and player_y == enemy_y:
            start_battle(protagonist,Goblin)
            enemy_x = 1
            enemy_y = 7
            enemy_char = '-'
        
        if player_x == strong_enemy_x and player_y == strong_enemy_y:
            start_battle(protagonist,Imp,Skull)
            strong_enemy_x = 2
            strong_enemy_y = 7
            strong_enemy_char = '-'

        if player_x == 99 and player_y == 7:
            return True
        interact = 0
        os.system('cls')

def chapter_two():
    pass