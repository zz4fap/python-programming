def mod2Name():
   print('Este é o módulo: mod2: Video')
   
video_device = {
   "name" : "NVIDIA GTX1080",
   "id" : 2,
   "file" : "/dev/vdo",
   "addr" : 0xCCDD
}

class Video:   
   def play(self):
      print("Playing video")