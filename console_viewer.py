import cam_viewer
import json

with open('cams.json', 'r') as file:
    cams_json = json.loads(file.read())

while(True):
    print("Cats Cams:")
    print(" Mr Fresh: fresh")
    print(" Mr Despair: despair")
    print(" Miss Sleeps: sleeps")
    print(" Mr Snack: snack")
    print(" Mr Shock: shock")
    print(" Mr Sonic: sonic")
    print(" Ducks: ducks")
    
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