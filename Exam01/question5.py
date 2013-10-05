def midi_to_freq(midi_num):
	x=(midi_num-69)/12.0

	freq=440.0*2**x

	return freq

frequency=midi_to_freq(81)

#print frequency