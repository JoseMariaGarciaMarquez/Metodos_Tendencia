def polis(t,s):
    i = 1;
    tendencia = np.poly1d(np.polyfit(t, s,  i))
    exactitud = r2_score(s, tendencia(t))*100
    exacto = float(input("¿Qué tanta exactitud quieres en tu modelo?: "))


    while exactitud < exacto:
        tendencia = np.poly1d(np.polyfit(t, s, i))
        exactitud = r2_score(s, tendencia(t))*100
        i +=1

    print("El polinomio de grado {} tiene una exactitud de {}%"
          .format(i,round(exactitud,3)))
    fig = plt.figure(figsize = (10,6), dpi = 300)
    plt.plot(t, s, c = "k")
    plt.plot(t, tendencia(t), "--", c = "darkred", linewidth = 2, 
             label = "Tendencia")
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
