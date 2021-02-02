# Per creare il grafico, prima di tutto importando il modulo matplotlib.pyplot
import matplotlib.pyplot as plt
# definisco i valori di x
x = [2, 5, 7]
#definisco i valori di y
y = [1, 9, 4]
# rappresento i punti sul grafico
plt.plot(x, y)
# do un nome all’asse delle x
plt.xlabel('x - axis')
# do un nome all’asse delle y
plt.ylabel('y - axis')
#do un titolo al mio grafico
plt.title('Grafico Fulgione')
# mostro il grafico che ho creato
plt.show()
