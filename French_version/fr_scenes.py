"""Fantasy Fight Project. A simple fight game with fantasy characters.

This file contains the game text scenes displayed throughout the game.
"""

__version__ = 0.3
__author__ = "Sophie Blanchard"
__start_date__ = "03-17-2020"
__last_update__ = "05-17-2020"

import random

import pygame

pygame.init()

# Game scenes (ordered)
# GAME INTRO
title = "Fantasy Fight\n"
story = "Fantasy Fight est une modeste aventure textuelle.\n\n~~~HISTOIRE~~~\n\nVous entrez dans les Royaumes Oubliés, " \
        "un monde fantastique où les héros s'affrontent pour le pouvoir et la gloire.\n\n~~~BUT DU JEU~~~\n\n" \
        "Votre objectif est de défaire autant d'ennemis que vous le pourrez et de gagner ainsi une renommée éternelle !"
rules = "~~~REGLES DU JEU~~~\n\nVous allez créer un personnage et recevrez un peu d'argent (ou pas si vous n'avez pas" \
        " de chance !) afin d'acheter de l'équipement.\nVous pouvez choisir de jouer un Rakshasa, un Illithid, un" \
        " Tieflin, un Banshee ou un Githzerai.\nDe votre race de personnage vont dépendre vos points de vie, votre force," \
        " votre intelligence et votre pouvoir spécial.\nVous pourrez acheter des armes, des armures et des sorts. " \
        "Vous pourrez aussi vendre de l'équipement placé dans votre inventaire. En revanche vous ne pourrez vendre les" \
        " éléments que vous avez équipés pour le combat. Pensez à vous déséquiper si vous souhaitez revendre ces éléments."\
        "\nPuis vous combattrez d'autres personnages jusqu'à ce que vous mourriez ou que vous décidiez de vous retirer. "\
        "\nChaque ennemi tué vous rapporte des points d'expériences et de l'or. Quand vous aurez gagné assez d'expérience, "\
        "vous passerez au niveau supérieur et vos capacités s'amélioreront.\n"
tips = "~~~CONSEILS POUR LE COMBAT~~~\n\nAvant de démarrer le combat, sachez que :\n- Vous pouvez blesser votre ennemi "\
       "avec votre arme, votre pouvoir ou votre sort si vous en avez acheté un.\n- Il y a plusieurs sortes d'armes, " \
       "générant plus ou moins de dommages. Votre force vous donne des points de dégâts supplémentaires lorsque vous " \
       "utilisez votre arme.\n- Il y a également plusieurs sorts, générant plus ou moins de dommages. Votre intelligence " \
       "vous donne des points de dégâts supplémentaires lorsque vous utilisez un sort.\n- Votre pouvoir est à double" \
       " tranchant : il peut faire beaucoup de dégâts mais a une grande propension à l'échec.\n- Il existe toujours un risque "\
        "que votre coup (ou celui de votre adversaire) échoue.\n\n~~~METTRE FIN AU JEU~~~\n\nVous pouvez quitter le "\
    "jeu à tout moment.\nAttention ! Ce jeu NE SAUVEGARDE PAS votre personnage ni votre progression.\nBon courage"\
        " et amusez-vous bien !"

# CHARACTER CREATION
enter_name = "C'est parti !\n\nEntrez le nom de votre personnage (vous ne pourrez plus le modifier alors n'écrivez "\
             "de bêtises que si vous le souhaitez vraiment) : \n"
enter_gender = "Etes vous de sexe féminin, masculin ou autre ?\nIndiquez votre réponse ci-dessous. (Seuls les termes 'femme', " \
               "'homme' ou 'autre' sont acceptés.)\n"
enter_race = "\nMaintenant choisissez votre race !\n~ Les Githzerais sont agiles et furtifs, mais pas très intelligents. " \
             "Ils ont une bonne constitution mais manquent de force.\n~ Les Banshees sont très intelligents mais" \
             " pas vraiment endurants et ils manquent clairement de force.\n~ Les Tieflins sont" \
             " complètement crétins mais très forts et bien bâtis.\n~ Les Illithids sont intelligents à la folie " \
             "mais plutôt frêles.\n~ Les Rakshasas sont très forts et résistants, mais à peu près aussi stupides" \
             " que les Tieflins.\nMerci d'entrer votre choix ci-dessous. (Seuls les termes 'Githzerai', 'Banshee', " \
             "'Tieflin', 'Illithid' ou 'Rakshasa' sont acceptés.)\n"

# ENDING
endgame = "~~~Game over~~~\nMerci d'avoir joué !\n\n~~~CREDITS~~~\nConception, art" \
          " & programmation : \nAphios\n"
credits = "Réalisé avec Python 3.7 and Pygame 1.9.6\n\nMusique :\n'The Descent' by Kevin MacLeod\nLink: "\
          "https://incompetech.filmmusic.io/song/4490-the-descent\nLicense: "\
          "http://creativecommons.org/licenses/by/4.0/\n\n'Crossing the Chasm' by Kevin MacLeod\n"\
          "Link: https://incompetech.filmmusic.io/song/3562-crossing-the-chasm\nLicense: "\
          "http://creativecommons.org/licenses/by/4.0/\n\n'Killers' by Kevin MacLeod\n"\
          "Link: https://incompetech.filmmusic.io/song/3952-killers\nLicense: "\
          "http://creativecommons.org/licenses/by/4.0/\n\n'The Path of the Goblin King' by Kevin MacLeod"\
          "\nLink: https://incompetech.filmmusic.io/song/4503-the-path-of-the-goblin-king\nLicense: "\
          "http://creativecommons.org/licenses/by/4.0/\n"
credits2 = "Sons :\n\nArgent, sort, victoire, défaite et inventaire :\nLittle Robot Sound Factory : " \
           "www.littlerobotsoundfactory.com\nCoup : artisticdude"

# STATS
view_stats = "Voulez-vous consulter vos statistiques et votre équipement ?\n"

# SHOP
go_shop = "Voulez-vous vous rendre à la boutique pour acheter ou vendre de l'équipement ?"
bazaar = "-- Bazar du Combattant --"
shop_menu = "Souhaitez-vous acheter, vendre ou sortir de la boutique ?\nIndiquez votre réponse ci-dessous \n(seuls les " \
            "termes 'Acheter', 'Vendre' ou 'Sortir' sont acceptés)."
no_sell = "Vous n'avez rien à vendre.\n"
inventory_choose = "Indiquez ci-dessous le nom d'une de vos possessions (ou 'Rien')."
already_yours = "Vous possédez déjà cet objet.\n"
which_stock = "Quels stocks souhaitez-vous regarder ? (Merci de choisir \nentre 'Armures', 'Sorts' ou 'Armes')\n"
shop_stocks = "\nVoici pour les objets à vendre. Ecrivez ci-dessous \nle nom de l'objet que vous souhaitez " \
              "acquérir, ou bien 'Rien'."

# EQUIP
go_equip = "Voulez-vous vous équiper avant de débuter le combat ?\n"
your_pack = "Regardons dans votre sac !\n"
no_equip = "Vous n'avez rien à équiper !\n"
re_equip = "C'est fait ! Souhaitez-vous équiper autre chose ?\n"

# FIGHT
enter_arena = "Vous rencontrez votre adversaire dans l'arène... \n"
last_level = "Vous avez atteint le dernier niveau et défait tous vos ennemis !\n"
fight_again = "Souhaitez-vous combattre un autre adversaire ?\n"