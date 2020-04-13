class Temperature():
    def convertFahrenhiet(self,celsius):
        self.farenheit = str((celsius * 9/5) + 32) + '0'
        return self.farenheit

    def convertCelsius(self,farenhiet):
        self.celsius = str((farenhiet - 32) * 5/9) + '0'
        return self.celsius
    
temperature = Temperature()
print(temperature.convertFahrenhiet(25))