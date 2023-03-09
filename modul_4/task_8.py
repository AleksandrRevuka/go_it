def game(terra, power):
    for particles in terra:
        for particle in particles:
            if power >= particle:
                power += particle
            else:
                break
    return power
