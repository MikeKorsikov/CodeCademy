# |Unit testing
# Exceptions
sale_instruments = ['Violin', 'Conga', 'Clavinet']

print('The following ' + str(len(sale_instruments)) + ' instruments are on sale:')
print(sale_instruments[0])
print(sale_instruments[1])
print(sale_instruments[2])
print(TypeError.__bases__)

###

instrument_catalog = {
  'Marimba': 1999,
  'Kora': 499,
  'Flute': 899
}

def print_instrument_price(instrument):
  if instrument in instrument_catalog:
    print('The price of a ' + instrument + ' is ' + str(instrument_catalog[instrument]))
  else:
    raise KeyError(f'{instrument} is not found in instrument catalog!')

print_instrument_price('Marimba')
print_instrument_price('Flute')
print_instrument_price('Piano')

###

