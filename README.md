# FUTURE_DS_03
#  Marketing Funnel & Conversion Performance Dashboard
Project Overview
This project analyzes user behavior across a marketing funnel to understand how customers move from **product views - cart -purchase**.

The goal is to identify:
- Drop-off points in the funnel
- High-performing product categories
- Revenue drivers
- Opportunities to improve conversion rates

 Objectives
- Analyze funnel performance (View → Cart → Purchase)
- Calculate conversion rates at each stage
- Identify key drop-off points
- Evaluate category-level performance
- Provide actionable business insights
  
 Tools & Technologies
- Python (Pandas, NumPy, Matplotlib)
- Power BI (Dashboard & Visualization)

 Data Preparation
- Cleaned raw dataset (handled missing values)
- Converted timestamps to datetime format
- Reduced dataset size for performance
- Created additional fields (date, purchase flag)

 Key Metrics
- View-to-Cart Conversion Rate
- Cart-to-Purchase Conversion Rate
- Overall Conversion Rate
- Total Revenue
- Average Order Value (AOV)

 Dashboard Features
- Funnel visualization
- Conversion rate analysis
- Category performance comparison
- Revenue insights
- Time-based user activity trends
- Interactive filters (category, date, event type)

 Key Insights
- Significant drop-off occurs at the **view - cart stage (~95%)**
- Strong conversion from **cart - purchase (~60%)**
- Electronics categories generate the highest revenue
- Some categories show high traffic but low conversion (optimization opportunity)

 Recommendations
- Improve product pages to increase add-to-cart rate
- Enhance product descriptions and reviews
- Focus marketing efforts on high-converting categories
- Optimize low-performing categories

 Project Structure
- `funnelAnalysis.py` → Data cleaning & analysis
- `clean_funnel_data.csv` → Processed dataset
- `PowerBI Dashboard.pbix` → Final dashboard
