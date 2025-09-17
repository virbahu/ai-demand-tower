import numpy as np
def forecast_demand_tower(history, horizon=24, alpha=0.35, beta=0.15):
    n = len(history)
    level = history[0]; trend = 0
    fitted = []
    for t in range(n):
        prev_level = level
        level = alpha*history[t] + (1-alpha)*(level+trend)
        trend = beta*(level-prev_level) + (1-beta)*trend
        fitted.append(round(level+trend, 1))
    forecasts = []
    for h in range(1, horizon+1):
        forecasts.append(round(level + trend*h, 1))
    residuals = np.array(history) - np.array(fitted)
    rmse = round(np.sqrt(np.mean(residuals**2)), 2)
    return {{"forecasts": forecasts, "rmse": rmse, "last_level": round(level,1),
            "trend_per_period": round(trend,2), "fitted_last5": fitted[-5:]}}
if __name__=="__main__":
    np.random.seed(42)
    hist = (np.cumsum(np.random.normal(5, 15, 104)) + 5000).tolist()
    r = forecast_demand_tower(hist)
    print(f"RMSE: {{r['rmse']}}, Trend: {{r['trend_per_period']}}")
    print(f"Forecast: {{r['forecasts']}}")
