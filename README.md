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


## Key Findings
Highlight any interesting trends such as popular categories, user engagement patterns, or correlations found.


## Tableau Dashboard
Link to the Tableau dashboard: [Dashboard Link Here]


## Conclusions
Summarize insights gained, potential business implications, and strategies for improvement.


## Future Work
Discuss additional analyses or features that could be added in future iterations.
