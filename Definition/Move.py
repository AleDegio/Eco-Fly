"""
calculation of finger-palm distance
"""
import Leap, sys, time, math
from threading import Thread
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
from djitellopy.tello import Tello


class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    tello = Tello(host='192.168.10.1', port=8889)
    tello.connect()
    commandTime = time.clock()
    takeoff = False

    if takeoff == False:
        tello.takeoff ()
        takeoff = True


    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()


        position={"Thumb":0,"Index":0,"Middle":0,"Ring":0,"Pinky":0}

        # Get hand
        for hand in frame.hands:
            # Get center hand
            Center = hand.palm_position
            print Center
            
            if Center[1] <= 60:
                self.tello.land()
            elif(Center[1] >= 300 and Center[1] <= 350 and Center[0] >= -90 and Center[0] <= 150):   
                self.tello.move_up(30)
            elif(Center[1] >= 100 and Center[1] <= 150 and Center[0] >= -90 and Center[0] <= 150):
                self.tello.move_down(30)
            if(Center[0] >= -140 and Center[0] <= -90 and Center[1] >= 150 and Center[1] <= 300):
                self.tello.move_left(30)
            if(Center[0] >= 150 and Center[0] <= 200 and Center[1] >= 150 and Center[1] <= 300):
                self.tello.move_right(30)   
            if(Center[2] >= -150 and Center[2] <= -100 and Center[0] >= -90 and Center[0] <= 150 and Center[1] >= 150 and Center[1] <= 300):
                self.tello.move_forward(30)
            if(Center[2] >= 100 and Center[2] <= 150 and Center[0] >= -90 and Center[0] <= 150 and Center[1] >= 150 and Center[1] <= 300):
                self.tello.move_back(30)

            
            #time.sleep(2)
            '''
            # Get fingers
            for finger in hand.fingers:
                bone = finger.bone(3)
                position[self.finger_names[finger.type]]=math.sqrt(pow((bone.next_joint[0]-Center[0]),2)+pow((bone.next_joint[1]-Center[1]),2)+pow((bone.next_joint[2]-Center[2]),2))
        for k,v in position.items():
            print k,v
            
        '''
            
               

        
         
        


def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
       