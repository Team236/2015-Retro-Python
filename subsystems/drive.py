import wpilib
from wpilib.command import Subsystem
from robotmap import DriveMap, JoystickMap

class Drive(Subsystem):
    def __init__(self, robot):
        super().__init__()
        self.robot = robot

        self.leftFrontMotor = wpilib.Talon(DriveMap.PWM_LEFT_FRONT)
        self.leftBackMotor = wpilib.Talon(DriveMap.PWM_LEFT_BACK)

        self.rightFrontMotor = wpilib.Talon(DriveMap.PWM_RIGHT_FRONT)
        self.rightBackMotor = wpilib.Talon(DriveMap.PWM_RIGHT_BACK)

        self.leftEncoder = wpilib.Encoder(DriveMap.DIO_ENCODER_LEFT_A, DriveMap.DIO_ENCODER_LEFT_B)
        self.rightEncoder = wpilib.Encoder(DriveMap.DIO_ENCODER_RIGHT_A, DriveMap.DIO_ENCODER_RIGHt_B)

    def initDefaultCommand(self):
        self.setDefaultCommand(DriveWithJoysticks(self.robot))

    def setLeftSpeed(self, speed):
        self.leftFrontMotor.set(speed)
        self.leftBackMotor.set(speed)

    def setRightSpeed(self, speed):
        self.rightFrontMotor.set(-speed)
        self.rightBackMotor.set(-speed)

    def setSpeeds(self, leftSpeed, rightSpeed):
        self.setLeftSpeed(leftSpeed)
        self.setRightSpeed(rightSpeed)

    def stop(self):
        self.setLeftSpeed(0)
        self.setRightSpeed(0)

    def getLeftEncoder(self):
        return self.leftEncoder.get()

    def getRightEncoder(self):
        return self.rightEncoder.get()

    def zeroEncoders(self):
        self.leftEncoder.reset()
        self.rightEncoder.reset()
