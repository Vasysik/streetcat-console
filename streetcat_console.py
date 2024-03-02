import cam_viewer
import json

with open('streetcat_viewer/cams_list.json', 'r') as cams:
    cams_json = json.loads(cams.read())
command = "connect"
debug = True

if debug:
    print("Commands:\nconnect\ndata\nurl\ntime")
    command = input("\nEnter command: ")

def cams_list():
    print("\nCats Cams:")
    for key in cams_json.keys(): print(cams_json[key]["title"], "-", key)
    cam_group = input("\nEnter camera name: ")
    cam_id = input("Cam ID: ")
    return [cam_group, cam_id]

while(True):
    responce = ""
    if command == "connect":
        cam = cams_list()
        player = cam_viewer.playback(command = "ffplay", 
                            parameters = "",
                            cams_json = cams_json,
                            cam_group = cam[0], 
                            cam_id = int(cam[1]),
                            use_title = True,
                            font_file = "./CALIBRI.TTF",
                            custom_title = cams_json[cam[0]]["title"] + " - " + cam[1])
        responce = player[1]
        print(f"\n{responce}")
        try: player[0].wait()
        except: None
        print(f"\nCam {cam[0]} {cam[1]} is closed")
    elif command == "data":
        cam = cams_list()
        data = cam_viewer.cam_data(cams_json, cam[0], int(cam[1]))
        print(f"\nURL: {data[0]}\nEnabled: {data[1]}\nResponce: {data[2]}\n")
    elif command == "url":
        url = input("\nEnter URL: ")
        print(f"Available: {cam_viewer.url_available(url)}")
    elif command == "time":
        input("\nPress enter to display time...")
        print(f"Current time: {cam_viewer.current_time()}")
    else: 
        print("Command does not exist!!!\nSetting the command to connect...")
        command = "connect"