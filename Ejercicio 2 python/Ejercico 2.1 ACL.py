def mejor_puntuacion(scores):
    scores.sort(reverse=True)
    return sum(scores[:2])

scores = []
for i in range(3):
    scores.append(int(input(f"Ingrese el resultado de la partida {i+1}: ")))

print("El puntaje final es:", mejor_puntuacion(scores))
