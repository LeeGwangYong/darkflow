class Position:
    def __init__(self, minX: int, minY: int, maxX: int, maxY: int):
        self.minX = minX
        self.minY = minY
        self.maxX = maxX
        self.maxY = maxY

    def __sub__(self, other):
        return abs(self.minX - other.minX) + abs(self.minY - other.minY) + abs(self.maxX - other.maxX) + abs(self.maxY - other.maxY)


class DetectedObject:
    def __init__(self, num: int, frame: int, confidence: float, position: Position):
        self.num = num
        self.frame = frame
        self.confidence = confidence
        self.position = position


class Segment:
    def __init__(self, frame: int, position: Position):
        self.frame = frame
        self.position = position


class Car:
    def __init__(self, num: int, segment: Segment):
        self.num = num
        self.previousSegment = segment
        self.isIllegal = False
        self.count = 0
        self.beginStoppedSegment = None
        self.endStoppedSegment = None

    def update(self, segment: Segment):
        if (self.previousSegment.position - segment.position) <= 10:
            if self.beginStoppedSegment is None:
                self.beginStoppedSegment = segment
            self.endStoppedSegment = segment
            self.isIllegal = (self.endStoppedSegment.frame - self.beginStoppedSegment.frame > 100)
        self.previousSegment = segment

