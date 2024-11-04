import math
import struct


def usr(robot):
    robot.delay(3000)  # ensures that the camera and all other peripherals are up and running before your code begins
    # any set up variables or code before looping can go here
    log = open("experiment_log.txt", "w")

    log.write("Starting a simple Coachbot program\n")
    log.flush()

    write_str = "I am robot " + str(robot.virtual_id())
    log.write(write_str)
    log.flush()

    while True:
        for i in range(2):
            robot.delay()
            # your looping code here

            # set the robot's LED to green
            robot.set_led(0, 100, 0)

            # move forward for 1 second
            robot.set_vel(25, 25)
            robot.delay(1000)

            # move backwards for 1 second
            robot.set_vel(-25, -25)
            robot.delay(1000)

            # set the robot's LED to blue
            robot.set_led(0, 0, 100)

            # turn right for 1 second
            robot.set_vel(25, -25)
            robot.delay(1000)

            # turn left for 1 second
            robot.set_vel(-25, 25)
            robot.delay(1000)

            # set the robot's LED to red
            robot.set_led(100, 0, 0)
            robot.delay(1500)

            log.write("Finished running the simple example program\n")
            log.flush()

        # clean up before ending the experiment
        log.close()  # closing the log file
        return
