import wpilib

class MoveDistance(wpilib.command):
    '''Set a distance (ft) for the robot to go (linear)'''
    def __init__(self, robot, distance):
        self.robot = robot
        self.goal = distance
        self.robot.drive.zeroEncoders()

    def execute(self):
        avgDistance = (self.robot.drive.getLeftEncoder() + self.robot.drive.getRightEncoder()) / 2
        self.robot.drive.setSpeeds(0.5, 0.5)

    def isFinished(self):
        if avgDistance >= goal:
            return True
        return False

    def end(self):
        robot.drive.stop()
