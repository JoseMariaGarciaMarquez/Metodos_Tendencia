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
    fig = plt.figure(figsize = (20,10), dpi = 300)
    plt.plot(t, s, c = "c")
    plt.plot(t, tendencia(t), "--", c = "y", linewidth = 3, 
             label = "Tendencia")
    titulo = input("Título de la gráfica: ")
    plt.title("{}".format(titulo), fontsize = 40)
    xlab = input("Eje x: ")
    ylab = input("Eje y: ")
    plt.xlabel("{}".format(xlab), fontsize = 20)
    plt.ylabel("{}".format(ylab), fontsize = 20)
    plt.legend()
    plt.grid()
    return