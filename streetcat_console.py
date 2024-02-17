import cam_viewer
import json

with open('streetcat_viewer/cams.json', 'r') as cams:
    cams_json = json.loads(cams.read())
command = "connect"
debug = True

if debug:
    print("Commands:\nconnect\ndata\nurl\ntime")
    command = input("\nEnter command: ")

def cams_list():
    print("\nCats Cams:")
    for key in cams_json.keys(): print(key)
    cam_name = input("\nEnter camera name: ")
    cam_number = input("Cam number: ")
    return [cam_name, cam_number]

while(True):
    responce = ""
    if command == "connect":
        cam = cams_list()
        player = cam_viewer.playback(command = "ffplay", 
                            parameters = "", 
                            cams_json = cams_json,
                            cam_name = cam[0], 
                            cam_number = int(cam[1]),
                            use_text = True,
                            font_file = "./CALIBRI.TTF")
        responce = player[1]
        print(responce)
        player[0].wait()
        print(f"\nCam {cam[0]} {cam[1]} is closed")
    elif command == "data":
        cam = cams_list()
        data = cam_viewer.cam_data(cams_json, cam[0], int(cam[1]))
        print(f"\nURL: {data[0]}\nEnabled: {data[1]}\nResponce: {data[2]}\n")
    elif command == "url":
        url = input("\nEnter URL: ")
        print(f"Available: {cam_viewer.url_available(url)}\n")
    elif command == "time":
        input("\nPress enter to display time...")
        print(f"Current time: {cam_viewer.current_time()}")
    else: 
        print("Command does not exist!!!\nSetting the command to connect...")
        command = "connect"