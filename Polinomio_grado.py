def poli(t,s):
    fig = plt.figure(figsize = (10,6), dpi = 175)
    grado = int(input("¿Cuántos polinomios de usaran para el ajuste?"))
    for i in range(grado):
        tendencia = np.poly1d(np.polyfit(t,s,(i+1)));
        plt.plot(t,tendencia(t), "--", linewidth = 2)
    exactitud = r2_score(s, tendencia(t))*100
    print("El polinomio de grado {} tiene una exactitud de {}%".format(grado,exactitud))
    
    plt.plot(t,s, c = "k", label = "Datos")

    titulo = input("Título de la gráfica: ")
    plt.title("{}".format(titulo), fontsize = 40)
    xlab = input("Eje x: ")
    ylab = input("Eje y: ")
    plt.xlabel("{}".format(xlab), fontsize = 20)
    plt.ylabel("{}".format(ylab), fontsize = 20)
    plt.legend()
    plt.grid()
    
    resp = int(input("¿Deséa salvar los resultados?\n1. SI\n2. NO\n"))
    if resp == 1:
        nombre = input("Nombre del archivo: ")
        extension = input("Extensión: ")
        plt.savefig("{}.{}".format(nombre, extension))
    return
