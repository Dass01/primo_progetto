from django.shortcuts import render

def view_a(request):
    materie = ["Matematica","Italiano","Inglese","Storia","Geografia"]
    context={"materie":materie}

    return render(request, "listaMaterie.html",context)


def view_b(request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    context={"voti":voti}
    
    return render(request, "listaVoti.html",context)

def view_c (request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}    
    medie=[]
    tot=0

    for studenti,materie in voti.items():
        for materia in materie:
            tot+=materia[1]
        medie.append([studenti,tot/5])
        tot=0
    context={"medie":medie}
    return render(request,"media_studenti.html",context)

def view_d (request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    max=-1
    min=11
    maxMat=[]
    minMat=[]
    maxStud=[]
    minStud=[]

    for studenti,materie in voti.items():
        for materia in materie:
            if(materia[1]>max):
                max=materia[1]
                maxMat.clear()
                maxMat.append(materia[0])
                maxStud.clear()
                maxStud.append(studenti)

            elif(materia[1]==max):
                maxMat.append(materia[0])
                maxStud.append(studenti)

            if(materia[1]<min):
                min=materia[1]
                minMat.clear()
                minMat.append(materia[0])
                minStud.clear()
                minStud.append(studenti)

            elif(materia[1]==min):
                minMat.append(materia[0])
                minStud.append(studenti)

    context={"max":max,"min":min,"maxMat":maxMat,"minMat":minMat,"maxStud":maxStud,"minStud":minStud}
    return render(request,"max_min.html",context)