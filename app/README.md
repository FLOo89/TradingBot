# TradingBot Application

Le robot de trading est mis à diposition à plusieurs niveaux. 

Dans un premier temps voici l'aborescence du projet :


- app 
  |
  - ui.R
  - server.R
  - global.R
  - src
    | 
    - data
    - py
    - R
    - TradinBot.py
  - env
    | 
    - virtual environnement python
  - rsconnect 
    |
    - exportation shinyapps.io
    

## Application Shiny

Les fichiers et dossiers qui concernent la mise en place de l'application Web, shiny sont

- ui.R, server.R, global.R
- env et rsconnect


Comme sont nom l'indique, ui est le fichier pour le Frontend, server pour le Backend et global une bonne pratique pour initialiser les composants nécessaires.

### ShinyApp en local

Si vous voulez lancer l'application en local, rien de plus simple. 

- Avec RStudio :
  Ouvrir le fichier ui.R et de cliquer en haut à droite (dans la fenêtre de l'éditeur de texte) sur `RunApp`
- Via cmd:
  `path\\R.exe -e "shiny::runApp('path\\ui.R')"`

### shinyapps.io


<div style="border: 2px solid red; padding: 5px; align-items: 'center'">
  <p>
  ATTENTION le projet utilise le module tensorflow ce qui implique un poids supérieur à 1Go !
  Pour la version gratuite de shinyapp.io, le poids ds applications ne peuvent pas excéder 1Go.
  
  Il vous faut minimum l'abonnment **Starter Plan** pour pouvoir le mettre en ligne sur cette API.
  </p>
</div>


Afin d'intégrer la solution en python dans une application shiny en ligne, il vous faudra installer un environnement virtuel python.

```batch
cd yourpath\app\src

pip install virtualenv

virtualenv env

.\env\Scripts\activate.bat

# installer les libraries avec pip install 
```

Une fois l'environnement virtuel créé, il faut ajouter la ligne ci-dessous au fichier global.R (c'est pour indiquer à reticulate, le bridge de python vers R, où se trouve le virtual environnment)

```r
use_virtualenv("env", required = F)
```

Pour mettre l'application en ligne, ouvrez le fichier ui.R puis appuyer sur le symbole en bleu (ça ressemble à une sorte de Pokéball) en haut à droite.

Sélectionner tous les fichiers et cliquer sur publish. 
