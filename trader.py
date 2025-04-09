from datamodel import OrderDepth, UserId, TradingState, Order
from typing import List
import string

class Trader:

    product_max = 50

    def calcBidQuantity(self, state:TradingState):
        return 1

    def calcAskQuantity(self, state:TradingState):
        return 1


    
    def run(self, state: TradingState):
        product = "RAINFOREST_RESIN"
        orderDepth = state.order_depths[product]
        result = {}
        orders = []
        if len(orderDepth) > 0:
            highBid = orderDepth.buy_orders.keys()[0]
            lowAsk = orderDepth.sell_orders.keys()[0]
            if state.position.get(product) < self.product_max:
                orders.append(Order(product, highBid, self.calcBidQuantity(state)))
            if state.position.get(product) > 0:
                orders.append(Order(product, lowAsk, self.calcAskQuantity(state)))
        else:
            #bid for one lower than its value
            if state.position.get(product) < self.product_max:
                orders.append(Order(product, 9999, 5)) 
            #sell for one higher than its value
            if state.position.get(product) > 0:
                orders.append(Order(product, 10001, 5)) 
            
        result[product] = orders
        result["KELP"] = []
        result["SQUID_INK"] = []
        traderData = "SAMPLE" # String value holding Trader state data required. It will be delivered as TradingState.traderData on next execution.
        
        conversions = 1
        return(result, conversions, traderData)

        



        # Only method required. It takes all buy and sell orders for all symbols as an input, and outputs a list of orders to be sent
        # print("traderData: " + state.traderData)
        # print("Observations: " + str(state.observations))
        # result = {}
        # for product in state.order_depths:
        #     order_depth: OrderDepth = state.order_depths[product]
        #     orders: List[Order] = []
        #     acceptable_price = 10;  # Participant should calculate this value
        #     print("Acceptable price : " + str(acceptable_price))
        #     print("Buy Order depth : " + str(len(order_depth.buy_orders)) + ", Sell order depth : " + str(len(order_depth.sell_orders)))
    
        #     if len(order_depth.sell_orders) != 0:
        #         best_ask, best_ask_amount = list(order_depth.sell_orders.items())[0]
        #         if int(best_ask) < acceptable_price:
        #             print("BUY", str(-best_ask_amount) + "x", best_ask)
        #             orders.append(Order(product, best_ask, -best_ask_amount))
    
        #     if len(order_depth.buy_orders) != 0:
        #         best_bid, best_bid_amount = list(order_depth.buy_orders.items())[0]
        #         if int(best_bid) > acceptable_price:
        #             print("SELL", str(best_bid_amount) + "x", best_bid)
        #             orders.append(Order(product, best_bid, -best_bid_amount))
            
        #     result[product] = orders
    
    
        # traderData = "SAMPLE" # String value holding Trader state data required. It will be delivered as TradingState.traderData on next execution.
        
        # conversions = 1
        # return result, conversions, traderData
