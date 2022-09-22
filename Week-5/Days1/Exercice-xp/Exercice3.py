class Song:
    def __init__(self,lyrics):
        pass
    def sing_me_a_song(self,lyrics):
        for i in lyrics:
            print(i)

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song(lyrics=["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])