import matplotlib.pyplot as plt
# Dados para o gráfico de pizza
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']
explode = (0.1, 0, 0, 0)  # Destaca o primeiro segmento

# Criar o gráfico de pizza
plt.figure(figsize=(8, 8))  # Define o tamanho da figura
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

# Adicionar título
plt.title('Gráfico de Pizza Simples')

# Mostrar o gráfico
plt.axis('equal')  # Mantém o gráfico como um círculo
plt.show() 