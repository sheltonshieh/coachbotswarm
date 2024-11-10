import math
import struct


def usr(robot):
    robot.delay(3000)  # Initial delay for peripherals setup

    log = open("experiment_log.txt", "w")
    log.write("Starting an enhanced Coachbot program\n")
    log.flush()

    # Setting up initial variables
    exploration_radius = 0.5  # Radius for circular exploration
    steps = 36  # Number of steps for completing a circle
    angle_step = 360 / steps

    # Main exploration loop
    for loop in range(3):  # Repeat the exploration 3 times
        log.write("Starting loop %d\n" % (loop + 1))
        log.flush()

        # Circular movement
        for i in range(steps):
            # Move in a small circle
            angle = math.radians(i * angle_step)
            left_speed = 25 + 10 * math.sin(angle)
            right_speed = 25 - 10 * math.sin(angle)
            robot.set_vel(left_speed, right_speed)
            robot.delay(200)

        # Zig-zag movement
        for i in range(5):
            robot.set_led(100, 100, 0)  # Yellow LED for zig-zag phase
            robot.set_vel(30, -30)  # Turn right
            robot.delay(500)
            robot.set_vel(-30, 30)  # Turn left
            robot.delay(500)

        # Randomized behavior - setting random LED colors
        for i in range(3):
            r = robot.random_int(0, 100)
            g = robot.random_int(0, 100)
            b = robot.random_int(0, 100)
            robot.set_led(r, g, b)
            robot.delay(1000)

        # LED signal and pause before next loop
        robot.set_led(0, 0, 100)  # Set LED to blue to signal the end of a loop
        robot.delay(1500)

    # Final cleanup
    log.write("Finished running the enhanced example program\n")
    log.flush()
    log.close()  # Closing the log file

    # Stop the robot before ending
    robot.set_vel(0, 0)
    robot.set_led(0, 0, 0)  # Turn off LED
    return