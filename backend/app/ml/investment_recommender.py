def get_investment_recommendation(user_id):
    # This is a simplified rule-based recommender.
    # You can replace this with a more sophisticated model based on risk profiling.

    # Example: Based on user's risk profile
    # risk_profile = get_user_risk_profile(user_id)

    # if risk_profile == 'low':
    #     return [{"asset": "Bonds", "reason": "Low risk"}]
    # elif risk_profile == 'medium':
    #     return [{"asset": "Index Funds", "reason": "Moderate risk and diversification"}]
    # else:
    #     return [{"asset": "Stocks", "reason": "High growth potential"}]

    return [{"stock": "AAPL", "reason": "Strong fundamentals"}, {"stock": "GOOGL", "reason": "Market leader"}]
