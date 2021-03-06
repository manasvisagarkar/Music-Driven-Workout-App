#!/usr/bin/env python3
from Scripts.exercise import Exercise
from datetime import datetime

class UserExercise:
    def __init__(self, exercise, rpm):
        self.exercise = exercise
        self.trials = []
        self.addTrial(rpm)

    def __repr__(self):
        string = "UserExercise: %s, max: %f rpm on %s\n\tTrials:" % \
         (self.exercise.name, self.maxRate[1], str(self.maxRate[0]))
        for time, rate in self.trials:
            string += "\n\t\t %f rpm on %s" % (rate, str(time))
        return string

    def __contains__(self, rpm):
        for time, rate in self.trials:
            if rate == rpm:
                return True
        return False

    def sameExercise(self, exercise):
        return self.exercise == exercise

    def combine(self, other):
        assert(self.exercise == other.exercise)
        self.trials += other.trials
        self.trials.sort()

    def addTrial(self, rpm):
        self.trials.append((datetime.now(),rpm))

    @property
    def maxRate(self):
        return(max(self.trials, key=lambda x: x[1]))

if __name__ == '__main__':
    ex = Exercise("Lunges", 30.0)
    uex = UserExercise(ex, 16.0)
    for i in [23.5,32.0,12.0]:
        uex.addTrial(i)
    print(uex)
    print(uex.maxRate)
