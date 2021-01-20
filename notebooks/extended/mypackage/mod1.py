def mod1Name():
   print('Este é o módulo: mod1: Audio')
   
audio_device = {
   "name" : "Intel HDA",
   "id" : 0,
   "file" : "/dev/snd",
   "addr" : 0xAABB
}

class Audio:   
   def play(self):
      print("Playing audio")
   