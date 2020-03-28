############
# FRONTEND #
############
options(rsconnect.max.bundle.size  = 3145728000,
        rsconnect.max.bundle.files = 20000 )

source('global.R', encoding = "UTF-8")

ui <- dashboardPage(
  header  = dashboardHeaderPlus(
    title = "Bot de Trading"
  ),
  sidebar = dashboardSidebar(
    collapsed = T,
    width = "300px",
    sidebarMenu(
      menuItem("Données", tabName = "df", icon = icon("fab fa-database")),
      menuItem("Analyse", tabName = "an", icon = icon("random")),
      menuItem("Script", tabName = "scpy", newtab = F, icon = icon("book-open"))
    )
  ),
  body    = dashboardBody(
    tabItems(
      tabItem(
        tabName = "df",
        fluidPage(
          width = 12,
          height = 'auto',
          box(
            title = "Data frame des données récupérées",
            width = 12,
            dataTableOutput("contents")
          )
        )
      )
    )
  )
)