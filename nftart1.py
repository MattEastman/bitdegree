#from PIL import Image
from PIL.Image import core as _imaging

group1 = [
  r"X:/Users/sug/Desktop/meNFT/Background/me1.jpg",
  r"X:/Users/sug/Desktop/meNFT/Background/me2.jpg",
  r"X:/Users/sug/Desktop/meNFT/Background/me3.jpg"
]
group2 = [
  r"X:/Users/sug/Desktop/meNFT/Background/me4.png"
]

#group3 = [
# r"C:/Users/pract/Desktop/Elephant/Head/head_base.png",
#  r"C:/Users/pract/Desktop/Elephant/Head/head_spray_1.png",
#  r"C:/Users/pract/Desktop/Elephant/Head/head_spray_2.png",
#  r"C:/Users/pract/Desktop/Elephant/Head/head_spray_3.png" #could add head_spray4
#]
#group4 = [
#  r"C:/Users/pract/Desktop/Elephant/Trunk/trunk_axe.png",
 # r"C:/Users/pract/Desktop/Elephant/Trunk/trunk_base.png",
#  r"C:/Users/pract/Desktop/Elephant/Trunk/trunk_knife.png",
 # r"C:/Users/pract/Desktop/Elephant/Trunk/trunk_laser.png"
#]

#group5 = [
 # r"C:/Users/pract/Desktop/Elephant/Tusks/tusks_base.png",
 # r"C:/Users/pract/Desktop/Elephant/Tusks/tusks_broken.png",
 # r"C:/Users/pract/Desktop/Elephant/Tusks/tusks_golden.png",
 # r"C:/Users/pract/Desktop/Elephant/Tusks/tusks_large.png"
#]

#group6 = [
#r"C:/Users/pract/Desktop/Elephant/Eyes/blue_eye_elephant.png",
 # r"C:/Users/pract/Desktop/Elephant/Eyes/red_eye_elephant.png"

#]
counter = 0


def createImage(a,b,counter):
  first = group1[a]
  second = group2[b]

# def createImage(a,b,c,d,e,f,counter):
#  first = group1[a]
#  second = group2[b]
 # third = group3[c]
 # fourth = group4[d]
 # fifth = group5[e]
 # sixth = group6[f]

  image01 = _imaging.open(first).convert("RGBA")
  image02 = _imaging.open(second).convert("RGBA")
 # image01 = Image.open(first).convert("RGBA")
 # image02 = Image.open(second).convert("RGBA")
#  image03 = Image.open(third).convert("RGBA")
#  image04 = Image.open(fourth).convert("RGBA")
 # image05 = Image.open(fifth).convert("RGBA")
#  image06 = Image.open(sixth).convert("RGBA")


 # intermediate = Image.alpha_composite(image01, image02)
  intermediate = _imaging.alpha_composite(image01, image02)
 # intermediate2 = Image.alpha_composite(intermediate,image03)
 # intermediate3 = Image.alpha_composite(intermediate2,image04)
 # intermediate4 = Image.alpha_composite(intermediate3,image05)
 # intermediate5 = Image.alpha_composite(intermediate4,image06)




  name = "C:/Users/sug/Desktop/meNFT/" + str(counter) + ".png"
  intermediate.save(name)
 # intermediate5.save(name)


for a in range(4):
  for b in range(4):
 #   for c in range(4):
#     for d in range(4):
 #       for e in range(4):
  #        for f in range(2):

     #       createImage(a,b,c,d,e,f,counter)
      #      counter = counter + 1
            
               createImage(a,b,counter)
               counter = counter + 1
            