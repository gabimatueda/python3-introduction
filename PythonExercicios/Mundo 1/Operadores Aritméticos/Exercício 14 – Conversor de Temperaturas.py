celsius = float(input('Informe a temperatura em °C:'))
fahrenheit = ((9 * celsius) / 5) + 32
kelvin = celsius + 273
print('A temperatura de {}°C corresponde a {}°F e {}K'. format(celsius, fahrenheit, kelvin))