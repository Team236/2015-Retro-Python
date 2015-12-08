import wpilib
from wpilib.command import Command
import oi

class DriveWithJoysticks(Command):
    '''Tank drive with left and right sticks'''
    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.drive)

    def execute(self):
        #leftSpeed = self.robot.oi.controller.getRawAxis(1)
        #rightSpeed = self.robot.oi.controller.getRawAxis(5)
        leftSpeed = self.robot.oi.leftStick.getY()
        rightSpeed = self.robot.oi.rightStick.getY()
        self.robot.drive.setLeftSpeed(leftSpeed)
        self.robot.drive.setRightSpeed(rightSpeed)

    def isFinished(self):
        return False # Run until interrupted

    def end(self):
        self.robot.drive.stop()
