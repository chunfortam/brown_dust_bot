import numpy as np
import cv2
import time
import os
import win32api, win32con
import pyautogui
import chilimangoes

def click((x,y)):
    print("Clicking at %d ,%d" % (x,y))
    (my_x,my_y) = win32api.GetCursorPos()
    win32api.SetCursorPos((x,y))
    print(my_x,my_y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    win32api.SetCursorPos((my_x,my_y))

def templates_list(path):
    files = os.listdir(path)
    templates = []
    for file in files:
        template_path = os.path.join(path,file)
        print(template_path)
        template = cv2.imread(template_path,cv2.IMREAD_COLOR)
        templates.append((file,template))
    return templates
def screen_record():
    print(win32api.EnumDisplayMonitors())
    last_time = time.time()
    templates = templates_list("D:\IdeaProjects\\brown_dust_bot\\templates\\done")
    while(True):
        # 800x600 windowed mode
        #printscreen =  np.array(ImageGrab.grab(bbox=(10,50,450,850)))
        time.sleep(1)
        pyautogui.screenshot = chilimangoes.grab_screen
        pyautogui.pyscreeze.screenshot = chilimangoes.grab_screen
        printscreen = np.array(pyautogui.screenshot())
        ##printscreen = printscreen[:1080,:1920,:]
        printscreen = cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB)
        ##cv2.imshow("test",printscreen)
        ##cv2.waitKey(0)
        ##cv2.destroyAllWindows()

        look_for_matching(printscreen,templates)
        #cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        #if cv2.waitKey(25) & 0xFF == ord('q'):
            #cv2.destroyAllWindows()
            #break
def look_for_matching(screen,templates):
    test_target = screen
    for filename,template in templates:
        (tW, tH) = template.shape[:2]
        result = cv2.matchTemplate(template,test_target,cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
       ## print("best match for %s is %f" % (filename,max_val))
        if max_val >= 0.90:
            x = max_loc[0] + tW /2
            y = max_loc[1] + tH /2
            print("Matching of template %s found with confident %f" % (filename,max_val))
            ##print("Max location at (%d,%d)" % max_loc)
            click((-1920 + x, y))
            #cv2.rectangle(test_target, max_loc, (x + tH, y + tW), (0,255,255), 2)
            #cv2.imshow("debug",test_target)
            #cv2.imshow("template",template)
            #cv2.waitKey(0)
            break
        ##click((-408,943))

#qtemplates = templates_list("D:\IdeaProjects\\brown_dust_bot\\templates")
#test_screen =cv2.imread("D:\IdeaProjects\\brown_dust_bot\gameplay_3.jpg",cv2.IMREAD_COLOR)
#look_for_matching(test_screen,templates)
screen_record()

