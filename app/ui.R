############
# FRONTEND #
############

source('R/global.R', encoding = "UTF-8")

ui <- dashboardPage(
  header  = dashboardHeaderPlus(),
  sidebar = dashboardSidebar(),
  body    = dashboardBody()
)