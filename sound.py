import pygame as pg
import simpleaudio as sa

class Sound:
    def __init__(self, game):
        self.game = game
        self.path = 'resources/sound/'
        self.shotgun = sa.WaveObject.from_wave_file(self.path + 'shotgun.wav')
        self.npc_pain = sa.WaveObject.from_wave_file(self.path + 'npc_pain.wav')
        self.npc_death = sa.WaveObject.from_wave_file(self.path + 'npc_death.wav')
        self.npc_shot = sa.WaveObject.from_wave_file(self.path + 'npc_attack.wav')
        self.player_pain = sa.WaveObject.from_wave_file(self.path + 'player_pain.wav')
        self.theme = sa.WaveObject.from_wave_file(self.path + 'theme.wav')
