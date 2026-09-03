from client import MerchantInventoryStockoutReorderForecasterClient

def main():
    client = MerchantInventoryStockoutReorderForecasterClient()
    res = client.forecast_stockout_and_reorder('SKU-01', 80, 12.0, 5)
    print('Merchant Stockout Reorder Forecaster: ' + res['inventory_forecast_id'] + ' (' + res['sku_id'] + ')')
    print('Days Remaining: ' + str(res['days_of_inventory_remaining']) + ' days | Risk: ' + res['stockout_risk_status'])
    print('Recommended PO Qty: ' + str(res['recommended_purchase_order_quantity']) + ' units')
    print('Report URL: ' + res['inventory_health_report_url'])

if __name__ == '__main__':
    main()
