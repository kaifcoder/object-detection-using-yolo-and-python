import detect
print('''
source -> 

0 # webcam
img.jpg        # image
vid.mp4        # video
path/          # directory
path/*.jpg     # glob
'https://youtu.be/Zgi9g1ksQHc'  # YouTube
'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
''')
s = input('enter source = ')
t = int(input('''
Enter option =>
1. Count People
2. Traffic
'''))
if t == 2:
    detect.run(source=s,
               classes=[1, 2, 3, 5], line_thickness=1, conf_thres=0.25)
if t == 1:
    l = input('''want to enter any limit ? y/n''')
    if l == "Y" or l == "y":
        lim = int(input("enter the limit => "))
        detect.run(source=s,
                   classes=[0], line_thickness=1, conf_thres=0.25, limitpeople=lim)
    else:
        detect.run(source=s,
                   classes=[0], line_thickness=1, conf_thres=0.25)
