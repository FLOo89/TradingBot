###########
# BACKEND #
###########


server <- function(input, output, session){
  
  source_python('src/py/Bittrex/get_data.py')
  
  output$contents <- renderDataTable({
    py$data
  })
  
}