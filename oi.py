import wpilib
from networktables import NetworkTable
from wpilib.buttons import JoystickButton, InternalButton
from wpilib import Joystick
from robotmap import DriveMap, JoystickMap

class OI:
    def __init__(self, robot):
        # Joysticks
        self.leftStick = wpilib.Joystick(JoystickMap.PORT_LEFT)
        self.rightStick = wpilib.Joystick(JoystickMap.PORT_RIGHT)
        self.controller = wpilib.Joystick(JoystickMap.PORT_CONTROLLER)

        self.smart_dashboard = NetworkTable.getTable("SmartDashboard")
