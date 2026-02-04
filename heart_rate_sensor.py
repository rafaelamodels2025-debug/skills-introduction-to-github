class StressDetector:
    def detect(self, heart_rate, accel):
        if heart_rate > 100:
            return True
        return Falseclass HeartRateSensor:
    def read(self):
        return 75