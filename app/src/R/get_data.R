library(jsonlite)

list_market_name <- as.list(read.csv("app/src/data/ListMarketName.csv")['x'])

get_data <- function(market = list_market_name, nb_data = 100, time_step = 5, toSave = T){
  if(!match.arg(market, list_market_name)){
    return("Marché inconnue")
  }
  
  marketURL <- paste0("https://api.bittrex.com/api/v1.1/public/getmarketsummary?market=",market)
  
  for(i in 1:nb_data){
    current_data <- fromJSON(marketURL)$result
    Sys.sleep(time_step)
    current_data <- rbind(current_data, temp_data)
  }
  
  # Remake data frame for python script
  
  current_data <- data.frame(
    "ask"              = current_data$Ask,
    "base_volume"      = current_data$BaseVolume,
    "bid"              = current_data$Bid,
    "date"             = current_data$TimeStamp,
    "high"             = current_data$High,
    "last"             = current_data$Last,
    "low"              = current_data$Low,
    "marketName"       = current_data$MarketName,
    "moy_prev_dev"     = current_data$PrevDay,
    "open_buy_orders"  = current_data$OpenBuyOrders,
    "open_sell_orders" = current_data$OpenSellOrders,
    "volume"           = current_data$Volume,
    stringsAsFactors = F
  )
  
  if(toSave){
    csv_name <- paste(market, nb_data, sep = '_')
    write.csv(current_data, paste0("src/data/", csv_name, ".csv"))
  }
  current_data <<- current_data
}


# transform_data <- read.csv("app/src/data/BTC_NEO_100.csv")
# 
# transform_data <- data.frame(
#   "ask"              = transform_data$Ask,
#   "base_volume"      = transform_data$BaseVolume,
#   "bid"              = transform_data$Bid,
#   "date"             = transform_data$TimeStamp,
#   "high"             = transform_data$High,
#   "last"             = transform_data$Last,
#   "low"              = transform_data$Low,
#   "marketName"       = transform_data$MarketName,
#   "moy_prev_dev"     = transform_data$PrevDay,
#   "open_buy_orders"  = transform_data$OpenBuyOrders,
#   "open_sell_orders" = transform_data$OpenSellOrders,
#   "volume"           = transform_data$Volume,
#   stringsAsFactors = F
# )
# 
# write.csv(transform_data, "app/src/data/BTC_NEO_100.csv")
