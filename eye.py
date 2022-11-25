class Eye:
    def __init__(self, type):
        self.type = type
        optic_neuritis = []
        color_vision = []
        self.optic_neuritis = optic_neuritis
        self.color_vision = color_vision

    def setOpticNeuritis(self, optic_neuritis):
        self.optic_neuritis.append(optic_neuritis)

    def setColorVision(self, color_vision):
        self.color_vision.append(color_vision)