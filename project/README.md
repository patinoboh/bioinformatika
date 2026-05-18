# Analýza placenty fajčiarok a nefajčiarok

**Autors:** Patrik Broček, Rastislav Nowak

## Dáta

- _72_ fajčiarok
    - _35_ placebo vitamin C
    - _37_ vitamin C
    - tieto dáta boli nedostupné
- _37_ nefajčiarok
- _714666_ záznamov TODO Maťka
- TODO Maťka - povedať o datasete
- [Link na dataset](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE169598)

## Skúmané otázky

- Dá sa z dát placenty zistiť či bola jej matka fajčiarka?
- Dajú sa nájsť hlavné TODO Maťka (gény alebo čo), ktoré sú najviac ovplyvnené fajčením?
- Dá sa učením bez učiteľa doplniť nedostupné dáta o kontrolných skupinách?

## Feature selection

1. Stĺpce s najmenším rozptylom : _714666_ -> _20000_
2. 
    - Sequential feature selection s logistickou regresiou
    - KBest feature selector TODO čo robil? : _20000_ -> _100_


## Ukážka dát

### TODO ukazat hodnoty tych 100 variabli

- Nejak ukazat distribucie tych variabli

### PCA

- ![PCA fajčiari vs nefajčiari](images/pca_smokers.png)
- ![PCA sex](images/pca_sex.png)
- ![PCA sex](images/pca_age.png)

## Klasifikátory

### __Logistická regresia__

- ![confusion matrix logisticka regresia](images/cm_logistic.png)

### __KNN__

- ![confusion matrix knn](images/cm_knn.png)
- ![knn pca](images/knn_pca.png)


### __SVM__

- ![confusion matrix svm](images/cm_svm.png)
- ![svm pca](images/svm_pca.png)

### __Random forests__

- ![foresty roc](images/forests_roc.png)
- ![foresty pca](images/forests_pca.png)

## __Killer features__

Pre získanie TODO génov ktoré sú najviac ovplyvnené fajčením sme použili opačný postup a hľadali sme TODO gény ktoré sú najsmerodatenejšie pri predikcií či bola matka fajčiarka alebo nie.

- Random forests extraction
    - ![naj features](images/top_features.png)
- Sequential feature selector
    - _['cg12268888', 'cg04474990', 'cg08913726', 'cg06369090', 'cg04004205','cg13141983', 'cg01096688', 'cg11739758', '__cg27402634__', 'cg24714864']_

## Unsupervised learning

Nedostupné dáta o rozdelení fajčiarok medzi tie ktoré užívali alebo neužívali vitamín C sme skúsili nájsť pomocou učenia bez učiteľa.

- KMeans
    - Algoritmus našiel rozdelenie do dvoch skupín o veľkosti _36_ a _36_
    - Originálne kontrolné skupiny mali veľkosti _35_ a _37_
    - ![kmeans](images/kmeans_pca.png)

