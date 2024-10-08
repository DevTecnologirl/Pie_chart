#importando matplotlib
import matplotlib.pyplot as plt

#Criando conjunto de dados
labels = 'Carros', 'Motos', 'Onibus', 'Caminhoes'
sizes = [40, 30, 20, 15]

#Criando representação área de plotagem 
fig1, ax1 = plt.subplots()

#Criando grafico
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
shadow=True, startangle=90)

#O grafico fica em formato circular 
ax1.axis('equal')

#mostra o grafico
plt.show()