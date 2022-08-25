# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

# Obs: pygame é um módulo desenvolvido para criar jogos. Para este exercícios poderíamos utilizar muitos outros que funcionariam também.
