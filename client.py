class MerchantInventoryStockoutReorderForecasterClient:
    def forecast_stockout_and_reorder(self, sku_id='SKU-ESPRESSO-BEAN-1KG', current_on_hand_inventory=142, daily_sales_velocity_30d=18.5, supplier_lead_time_days=10):
        return {
            'inventory_forecast_id': 'inv_frc_8812',
            'sku_id': sku_id,
            'days_of_inventory_remaining': 7.68,
            'stockout_risk_status': 'CRITICAL_STOCKOUT_RISK_WITHIN_8_DAYS',
            'calculated_reorder_point_units': 240,
            'recommended_purchase_order_quantity': 500,
            'inventory_health_report_url': 'https://inventory.merchant.genpark.ai/skus/8812.json'
        }
