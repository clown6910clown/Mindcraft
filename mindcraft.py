import pygame
import math
import random
from pygame import mixer

# display
pygame.init()
WIDTH, HEIGHT = 1000, 700
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('MINDCRAFT')

# Font
LETTER_FONT = pygame.font.SysFont('Times New Roman', 40)
WORD_FONT = pygame.font.SysFont('Times New Roman', 60)
TITLE_FONT = pygame.font.SysFont('Comic Sans', 60)
title = TITLE_FONT.render('MINDCRAFT', 1, "RED")


# Background 
background_image = pygame.image.load('background.jpg')

#loading of images
images = []
for i in range(7):
    image = pygame.image.load('mindcraft' + str(i) + '.png')
    images.append(image)

#button
RADIUS = 30
GAP = 15
letters = [[400,550, chr(39), True],[475,550, chr(32), True],[550,550, chr(46), True],]
start_x = round((WIDTH - (GAP + RADIUS * 2) * 13) / 2)
start_y = 400
A = 65
for i in range(26):
    x = start_x + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = start_y + ((GAP + (RADIUS * 2)) * (i // 13))
    letters.append([x, y, chr(A + i), True])

# game variables
MINDCRAFT_status = 0
guessed = []
words = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia","Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Democratic Republic of the Congo" ,"Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czechia", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda","Saint Lucia","Samoa", "San Marino", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"]
word = random.choice(words)
word = word.upper()

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# blit -> block transfer used to copy element of one surface to another
def draw():
    window.blit(background_image, (0, 0))
    window.blit(title, (WIDTH / 2 - title.get_width() / 2, 20))
    # drawing keys
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(window, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, "BLACK")
            window.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))
            
    # Drawing words
    display_word = ''
    for letter in word:
        if letter in guessed:
            display_word += letter + ' '
        else:
            display_word += '_ '
        text = WORD_FONT.render(display_word, 1, BLACK)
        window.blit(text, (350, 200))
    window.blit(images[MINDCRAFT_status], (30, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    window.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    window.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(1000)


def display_intro(message,xyz):
    window.fill(WHITE)
    title = TITLE_FONT.render(message, 1, BLACK)
    window.blit(title, (WIDTH / 2 - title.get_width() / 2, HEIGHT / 2 - title.get_height() / 2))
    ah_shit = mixer.Sound(xyz)
    ah_shit.play()
    pygame.display.update()


def main():
    # Setting loop
    global MINDCRAFT_status
    FPS = 60
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():  #returns a list of events that gonna be proceed
            pygame.display.update()
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        distance = math.sqrt((x - mouse_x) ** 2 + (y - mouse_y) ** 2)
                        if distance < RADIUS:
                            letter[3] = False  #4 element of a letter points to visibility  
                                                #and we set it to false after guessing
                            guessed.append(ltr)
                            if ltr not in word:
                                MINDCRAFT_status += 1
                                oof = mixer.Sound('oof.mp3')
                                oof.play()
                            else:
                                wow = mixer.Sound('Puk Sound (Part-1) -- Duck Puk Sound Effect.mp3')
                                wow.play()
        draw()
        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            epic_sax = mixer.Sound('Cristiano-Ronaldo-Siuuu-Sound-Effect.mp3')
            epic_sax.play()
            display_message('You WON')
            pygame.time.delay(1)
            display_intro('Do you want to play?')
            break

        if MINDCRAFT_status == 6:
            display_message('You LOST')
            not_fine = mixer.Sound('not_really_fine.mp3')
            not_fine.play()
            pygame.time.delay(1)
            display_intro('Do you want to play?','WhatsApp Ptt 2024-04-30 at 10.30.26.mp3')
            break


run_game = True
while run_game:
    display_intro('Do you want to play?','WhatsApp Ptt 2024-04-30 at 10.30.26.mp3')
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            main()
            # game variables
            MINDCRAFT_status = 0
            guessed = []
            words = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Democratic Republic of the Congo" ,"Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czechia", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Samoa", "San Marino", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"]
            word = random.choice(words)
            word = word.upper()
            for letter in letters:
                letter[3] = True
        elif event.type == pygame.QUIT:
            run_game = False

pygame.quit()
