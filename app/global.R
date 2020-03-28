#-------------------------------------#
# Libraries pour la partie graphique  #
#-------------------------------------#

library(shiny)
library(shinydashboard)
library(shinydashboardPlus)
library(DT)

#-------------------------------------#
# Pour les plot dynamiques            #
#-------------------------------------#

library(plotly)

#-------------------------------------#
# Bridge de Python vers R             #
#-------------------------------------#

library(reticulate)

print(py_config())

# A ajouter quand le modele compilera
#print(paste0(getwd(),"/env/Scripts/python.exe"))
#use_python(paste0(getwd(),"/env/Scripts/python.exe"), required = T)
#use_virtualenv("env", required = F)

#source_python('src/get_data.py')
