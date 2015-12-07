#!/usr/bin/env python3
import wpilib
import networktables
from wpilib.command import Scheduler

from oi import OI
# Import Subsystems
from subsystems.drive import Drive
# Import Commands
from commands.drivewithjoysticks import DriveWithJoysticks

class Robot(wpilib.IterativeRobot):
    def robotInit(self):
        self.drive = Drive(self)
        self.oi = OI(self)

        # Commands
        self.DriveWithJoysticks = DriveWithJoysticks(self)

    def operatorControl(self):
        self.drive.setSafetyEnabled(True)

        self.DriveWithJoysticks.start()

        while self.isOperatorControl() and self.isEnabled():
            wpilib.Timer.delay(.005)

    def disabled(self):
        self.DriveWithJoysticks.cancel()

        while self.isDisabled():
            wpilib.Timer.delay(0.01)

    def autonomous(self):
        while self.isAutonomous() and self.isEnabled():
            wpilib.Timer.delay(0.01)

if __name__ == '__main__':
    wpilib.run(Robot)
