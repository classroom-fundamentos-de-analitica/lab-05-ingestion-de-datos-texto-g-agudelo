import glob
import pandas as pd
traindic={"phrase":[],"sentiment":[]}
testdic={"phrase":[],"sentiment":[]}
sentiment = ["negative","neutral","positive"]

#Train Negative
archivo = glob.glob("train/"+sentiment[0]+"/*.*")
for ruta in archivo:
    with open(ruta,"r") as linea:
        traindic["phrase"].append(linea.readline())
        traindic["sentiment"].append(sentiment[0])

#Train Neutral
archivo = glob.glob("train/"+sentiment[1]+"/*.*")
for ruta in archivo:
    with open(ruta,"r") as linea:
        traindic["phrase"].append(linea.readline())
        traindic["sentiment"].append(sentiment[1])

#Train Positive
archivo = glob.glob("train/"+sentiment[2]+"/*.*")
for ruta in archivo:
    with open(ruta,"r") as linea:
        traindic["phrase"].append(linea.readline())
        traindic["sentiment"].append(sentiment[2])

#Train Dataframe
traindf= pd.DataFrame(traindic)
traindf.to_csv("train_dataset.csv")

#Test negative
archivo = glob.glob("test/"+sentiment[0]+"/*.*")
for ruta in archivo:
    with open(ruta,"r") as linea:
        testdic["phrase"].append(linea.readline())
        testdic["sentiment"].append(sentiment[0])

#Test neutral
archivo = glob.glob("test/"+sentiment[1]+"/*.*")
for ruta in archivo:
    with open(ruta,"r") as linea:
        testdic["phrase"].append(linea.readline())
        testdic["sentiment"].append(sentiment[1])

#Test Positive
archivo = glob.glob("test/"+sentiment[2]+"/*.*")
for ruta in archivo:
    with open(ruta,"r") as linea:
        testdic["phrase"].append(linea.readline())
        testdic["sentiment"].append(sentiment[2])

#Test Dataframe
testdf= pd.DataFrame(testdic)
testdf.to_csv("test_dataset.csv")

