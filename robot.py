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
        super().__init__()
        self.drive = Drive(self)
        self.oi = OI(self)

        self.DriveWithJoysticks = DriveWithJoysticks(self)

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def disabledInit(self):
        self.DriveWithJoysticks.cancel()

    def disabledPeriodic(self):
        pass

    def teleopInit(self):
        self.DriveWithJoysticks.start()

    def disabledInit(self):
        self.DriveWithJoysticks.cancel()

if __name__ == '__main__':
    wpilib.run(Robot)
