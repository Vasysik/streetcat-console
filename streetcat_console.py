import cam_viewer
import json

with open('streetcat_viewer/cams.json', 'r') as cams:
    cams_json = json.loads(cams.read())

while(True):
    print("Cats Cams:")
    for key in cams_json.keys(): print(key)
    
    print("Enter camera name: ", end="")
    cam_name = input()
    print("Cam number: ", end="")
    cam_number = input()

    player = cam_viewer.playback(command = "ffplay", 
                        parameters = "", 
                        cams_json = cams_json,
                        cam_name = cam_name, 
                        cam_number = int(cam_number),
                        use_text = True,
                        fontfile = "./CALIBRI.TTF")
    player[0].wait()
    print(player[1])