import RPi.GPIO as gpio
import time as t

class GPIOControl():

    MOT_A_IN1 =17
    MOT_A_IN2 =22
    MOT_A_IN3 =23
    MOT_A_IN4 =24

    MOT_B_IN1 =26
    MOT_B_IN2 =19
    MOT_B_IN3 =13
    MOT_B_IN4 =27

    PWM_VALUE =25
    PWM_VALUE_CORR =23
    SLEEP_TIME = 1
    def __init__(self):
        gpio.setmode(gpio.BCM)
        #MOTORDRIVER A
        gpio.setup(self.MOT_A_IN1, gpio.OUT)
        self.MOT_A_IN1_PWM = gpio.PWM(self.MOT_A_IN1, self.PWM_VALUE)
        self.MOT_A_IN1_PWM.start(0)

        gpio.setup(self.MOT_A_IN2, gpio.OUT)
        self.MOT_A_IN2_PWM = gpio.PWM(self.MOT_A_IN2, self.PWM_VALUE)
        self.MOT_A_IN2_PWM.start(0)

        gpio.setup(self.MOT_A_IN3, gpio.OUT)
        self.MOT_A_IN3_PWM = gpio.PWM(self.MOT_A_IN3, self.PWM_VALUE)
        self.MOT_A_IN3_PWM.start(0)

        gpio.setup(self.MOT_A_IN4, gpio.OUT)
        self.MOT_A_IN4_PWM = gpio.PWM(self.MOT_A_IN4, self.PWM_VALUE)
        self.MOT_A_IN4_PWM.start(0)

        #MOTORDRIVER B
        gpio.setup(self.MOT_B_IN1, gpio.OUT)
        self.MOT_B_IN1_PWM = gpio.PWM(self.MOT_B_IN1, self.PWM_VALUE)
        self.MOT_B_IN1_PWM.start(0)

        gpio.setup(self.MOT_B_IN2, gpio.OUT)
        self.MOT_B_IN2_PWM = gpio.PWM(self.MOT_B_IN2, self.PWM_VALUE)
        self.MOT_B_IN2_PWM.start(0)

        gpio.setup(self.MOT_B_IN3, gpio.OUT)
        self.MOT_B_IN3_PWM = gpio.PWM(self.MOT_B_IN3, self.PWM_VALUE)
        self.MOT_B_IN3_PWM.start(0)

        gpio.setup(self.MOT_B_IN4, gpio.OUT)
        self.MOT_B_IN4_PWM = gpio.PWM(self.MOT_B_IN4, self.PWM_VALUE)
        self.MOT_B_IN4_PWM.start(0)

    def wait(self):
        self.MOT_A_IN1_PWM.start(0)#gpio.output(self.MOT_A_IN1, False)
        self.MOT_A_IN2_PWM.start(0)#gpio.output(self.MOT_A_IN2, False)
        self.MOT_A_IN3_PWM.start(0)#gpio.output(self.MOT_A_IN3, False)
        self.MOT_A_IN4_PWM.start(0)#gpio.output(self.MOT_A_IN4, False)

        self.MOT_B_IN1_PWM.start(0)#gpio.output(self.MOT_B_IN1, False)
        self.MOT_B_IN2_PWM.start(0)#gpio.output(self.MOT_B_IN2, False)
        self.MOT_B_IN3_PWM.start(0)#gpio.output(self.MOT_B_IN3, False)
        self.MOT_B_IN4_PWM.start(0)#gpio.output(self.MOT_B_IN4, False)
        #print("Wait thread going to sleep for {} seconds :)".format(self.SLEEP_TIME))
        t.sleep(self.SLEEP_TIME)
        #gpio.cleanup()

    def forward(self):
        self.MOT_A_IN1_PWM.start(self.PWM_VALUE_CORR)#gpio.output(self.MOT_A_IN1, True)
        self.MOT_A_IN2_PWM.start(0)#gpio.output(self.MOT_A_IN2, False)
        self.MOT_A_IN3_PWM.start(0)#gpio.output(self.MOT_A_IN3, False)
        self.MOT_A_IN4_PWM.start(self.PWM_VALUE)#gpio.output(self.MOT_A_IN4, True)
        self.MOT_B_IN1_PWM.start(self.PWM_VALUE)#gpio.output(self.MOT_B_IN1, True)
        self.MOT_B_IN2_PWM.start(0)#gpio.output(self.MOT_B_IN2, False)
        self.MOT_B_IN3_PWM.start(0)#gpio.output(self.MOT_B_IN3, False)
        self.MOT_B_IN4_PWM.start(self.PWM_VALUE_CORR)#gpio.output(self.MOT_B_IN4, True)
        #print("Forward thread going to sleep for {} seconds :)".format(self.SLEEP_TIME))
        t.sleep(self.SLEEP_TIME)
        #gpio.cleanup()

    def right(self):
        self.MOT_A_IN1_PWM.start(self.PWM_VALUE)#gpio.output(self.MOT_A_IN1, False)
        self.MOT_A_IN2_PWM.start(0)#gpio.output(self.MOT_A_IN2, False)
        self.MOT_A_IN3_PWM.start(self.PWM_VALUE)#gpio.output(self.MOT_A_IN3, False)
        self.MOT_A_IN4_PWM.start(0)#gpio.output(self.MOT_A_IN4, True)

        self.MOT_B_IN1_PWM.start(0)#gpio.output(self.MOT_B_IN1, False)
        self.MOT_B_IN2_PWM.start(self.PWM_VALUE)#gpio.output(self.MOT_B_IN2, False)
        self.MOT_B_IN3_PWM.start(0)#gpio.output(self.MOT_B_IN3, False)
        self.MOT_B_IN4_PWM.start(self.PWM_VALUE)#gpio.output(self.MOT_B_IN4, True)
        #print("Right thread going to sleep for {} seconds :)".format(self.SLEEP_TIME))
        t.sleep(self.SLEEP_TIME)
        #gpio.cleanup()

    def left(self):
        self.MOT_A_IN1_PWM.start(0)#gpio.output(self.MOT_A_IN1, True)
        self.MOT_A_IN2_PWM.start(self.PWM_VALUE)#gpio.output(self.MOT_A_IN2, False)
        self.MOT_A_IN3_PWM.start(0)#gpio.output(self.MOT_A_IN3, False)
        self.MOT_A_IN4_PWM.start(self.PWM_VALUE)#gpio.output(self.MOT_A_IN4, False)

        self.MOT_B_IN1_PWM.start(self.PWM_VALUE)#gpio.output(self.MOT_B_IN1, True)
        self.MOT_B_IN2_PWM.start(0)#gpio.output(self.MOT_B_IN2, False)
        self.MOT_B_IN3_PWM.start(self.PWM_VALUE)#gpio.output(self.MOT_B_IN3, False)
        self.MOT_B_IN4_PWM.start(0)#gpio.output(self.MOT_B_IN4, False)
        #print("Left thread going to sleep for {} seconds :)".format(self.SLEEP_TIME))
        t.sleep(self.SLEEP_TIME)
        #gpio.cleanup()

    def reverse(self):
        self.MOT_A_IN1_PWM.start(0)#gpio.output(self.MOT_A_IN1, False)
        self.MOT_A_IN2_PWM.start(self.PWM_VALUE)#gpio.output(self.MOT_A_IN2, True)
        self.MOT_A_IN3_PWM.start(self.PWM_VALUE)#gpio.output(self.MOT_A_IN3, True)
        self.MOT_A_IN4_PWM.start(0)#gpio.output(self.MOT_A_IN4, False)

        self.MOT_B_IN1_PWM.start(0)#gpio.output(self.MOT_B_IN1, False)
        self.MOT_B_IN2_PWM.start(self.PWM_VALUE)#gpio.output(self.MOT_B_IN2, True)
        self.MOT_B_IN3_PWM.start(self.PWM_VALUE)#gpio.output(self.MOT_B_IN3, True)
        self.MOT_B_IN4_PWM.start(0)#gpio.output(self.MOT_B_IN4, False)
        #print("Reverse thread going to sleep for {} seconds :)".format(self.SLEEP_TIME))
        t.sleep(self.SLEEP_TIME)
        #gpio.cleanup()

#if __name__ == "__main__":
#        #obj = GPIOControl()
#        while True:
#            prompt = input()
#            if prompt == "w":
#                obj = GPIOControl()
#                print("Forward")
#                obj.forward()
#            elif prompt == "a":
#                obj = GPIOControl()
#                print("Left")
#                obj.left()
#            elif prompt == "s":
#                obj = GPIOControl()
#                print("Reverse")
#                obj.reverse()
#            elif prompt == "d":
#                obj = GPIOControl()
#                print("Right")
#                obj.right()
#            else:
#                obj = GPIOControl()
#                print("Wait")
#                obj.wait()
#            gpio.cleanup()
