# Project Title: Analyzing User Behavior in eCommerce

## Introduction
This project utilizes the User-Behavior eCommerce dataset sourced from Kaggle, which captures user interactions on an online retail platform. The dataset includes various attributes, such as user IDs, product categories, timestamps, and actions taken, providing insights into customer purchasing behavior. This analysis aims to uncover patterns in user engagement and product performance, ultimately helping to inform strategies for improving sales and user experience.


## Objectives
- Identify trends in user purchases over time.
- Analyze the most popular product categories.
- Explore the relationship between user behavior and sales performance.


## Tools and Techniques
For this project, I employed:

- Excel for an initial overview and validation of the data.
- Python (using libraries such as Pandas, Seaborn, and Matplotlib) for exploratory data analysis, creating bar plots, scatter plots, and generating insights.
- Tableau for developing an interactive dashboard to visualize trends and findings effectively.


## Data Overview
The dataset used in this project consists of user interactions on an eCommerce platform and includes 546,599 records with the following attributes:

- event_time: The timestamp of each user interaction.
- event_type: The type of user action (e.g., view, purchase).
- product_id: A unique identifier for each product.
- category: Product category and subcategory information.
- price: The price of each product.
- user_id: A unique identifier for each user.
- is_purchased: A binary indicator of whether the product was purchased.

This data allowed for analyzing trends in purchasing behavior, user engagement with different product categories, and the relationship between price and purchase frequency.


## Exploratory Data Analysis (EDA)

![Purchasing Behavior by Price Range (1)](https://github.com/user-attachments/assets/a5646087-3812-4861-9484-be3a7773da4f)

Purchasing Behavior by Price Range The histogram visualizes user purchasing patterns segmented by price range. The majority of purchases are concentrated in the lower price ranges, particularly under $100, with a notable spike at around $150. This suggests that users are more inclined to make purchases in the affordable category. Purchases become less frequent as prices increase, indicating lower demand for higher-priced items.


![Highest Selling Brands (1)](https://github.com/user-attachments/assets/bd5a15b2-26a2-4592-9ce4-c0b074f62640)

Highest Selling Brands The bubble chart showcases the top-selling brands based on transaction volume. Samsung and Apple dominate as the leading brands, represented by the largest bubbles. Other significant contributors include Xiaomi and Huawei. This visualization highlights the strong market presence of these key players and reflects their popularity among consumers. The various smaller bubbles represent a diverse range of brands that contribute to overall sales but hold a smaller market share.

![Sales by Day](https://github.com/user-attachments/assets/96a5b9dd-1929-45a0-bad1-2bc3a4eadb88)

The line graph titled "Sales by Day" illustrates the distribution of daily purchases throughout the week. Monday registers the lowest sales at 12.70% of total weekly sales, while Friday sees the highest with 15.31%. Tuesday follows closely with 15.02%. The graph also includes an average sales line, which helps in visualizing deviations from the mean. This data suggests that consumer purchasing behavior peaks towards the end of the week, indicating potential trends for targeted marketing strategies and resource allocation during high-demand days.

![Sales by Hour](https://github.com/user-attachments/assets/f802f4bd-fcbb-4057-952f-e23e079ac8f9)

The heat map titled "Sales by Hour" shows the distribution of purchases throughout the week at different times of the day. The highest number of purchases occurs at 8 a.m., marked by the darkest region on the map. The time range from 6 a.m. to 10 a.m. is particularly dense, indicating a significant volume of sales. After this peak period, the purchasing activity gradually decreases throughout the day in each direction. This trend highlights early morning as the most active purchasing window across the week.

## Key Findings
- Purchasing Behavior by Price Range: High consumer interest in budget (<$100) and mid-tier ($300-$400, $900-$1000) price ranges.
- Top-Selling Brands: Dominance by Samsung and Apple, with significant shares by Xiaomi and Huawei.
- Sales by Day: Friday is the peak sales day (15.31%); Monday has the lowest (12.70%).
- Sales by Hour: Highest purchasing activity at 8 a.m.; strong demand between 6 a.m. and 10 a.m.



## Tableau Dashboard
![User-Behavior eCommerce Sales](https://github.com/user-attachments/assets/d7db909e-a2a8-418d-bcc8-e2e75c716deb)

Link to the Tableau dashboard: [User Behavior eCommerce](https://public.tableau.com/app/profile/tyler.ross7761/viz/User-BehavioreCommerce/Dashboard1#1)


## Conclusions
This eCommerce purchasing behavior analysis highlights key trends and insights that can inform strategic decisions. The most frequent purchases are within the lower price range, especially under $100, indicating a preference for affordable items. Samsung and Apple are the most prominent brands, demonstrating significant market share. Sales activity peaks on Fridays and during morning hours, with 8 a.m. showing the highest transaction rate. Understanding these patterns can help businesses tailor their marketing strategies, optimize stock management, and schedule promotions to maximize sales and customer engagement.


## Future Work
To expand on this eCommerce analysis, future work could include integrating customer demographics to better understand purchasing preferences across age and gender. Adding a time-series analysis to capture seasonal trends and incorporating sentiment analysis of customer reviews could enhance understanding of product appeal. Further segmentation by customer location would offer insights into regional purchasing habits. Additionally, applying predictive modeling could forecast future sales and identify potential product recommendations, boosting targeted marketing and inventory management.
