###########
# BACKEND #
###########


server <- function(input, output, session){
  
  source_python('src/get_data.py')
  
  output$contents <- renderDataTable({
    py$data
  })
  
}