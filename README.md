# Project Title: Stores Sales Prediction
Project Description: 
The main objective is to find the sales per product for each store and evaluate meaningful insights. 
Using this model, BigMart will try to understand different attributes of the product and apply them to
increase their overall sales. The project workflow initiated with data exporting from My SQL DB, Analyzing 
the dataset, and coming up with more insights to predict the Sales figure for the test dataset Approach. 
By applying Exploratory Data Analysis identified the relationship between different attributes and evaluate meaningful information. 
Applying different supervised machine learning algorithms predicts the sales for the test dataset.

Deployment link :
https://salespredictionkk.herokuapp.com

Problem Statement:
Nowadays, shopping malls and Big Marts keep track of individual item sales data in order to forecast
future client demand and adjust inventory management. In a data warehouse, these data stores hold a 
significant amount of consumer information and particular item details. By mining the data store from the
data warehouse, more anomalies and common patterns can be discovered.

Aim of the Project
The main objective is to find the sales per product for each store and evaluate meaningful insights. Using this model,
BigMart will try to understand different attributes of the product and apply them to increase their overall sales.

Workflow stages
The solution workflow goes through seven stages as described 

1.Question or problem definition.
2.Acquire training and testing data.
3.Wrangle, prepare, cleanse the data.
4.Analyze, identify patterns, and explore the data.
5.Model, predict and solve the problem.
6.Visualize, report, and present the problem solving steps and final solution.
7.Supply or submit the results.

The workflow indicates general sequence of how each stage may follow the other. 
However there are use cases with exceptions.

1.combine mulitple workflow stages to visualizing data.
2.Perform a stage earlier than indicated. to analyze data before and after wrangling.
3.Perform a stage multiple times in our workflow. Visualize stage may be used multiple times.
4.Drop a stage altogether,may not need supply stage to productize or service enable our dataset.

#Introduction
The features of BigMarts Sales dataset

Item_Identifier: Product ID
Item_Weight: Weight of Product
Item_Fat_Content: Fat content of Product- Low/Regular
Item_Visibility: Parameter to know the visiblity/reach of product
Item_Type: Category of Product
Item_MRP: Maximum Retail Price of the Product
Outlet_Identifier: Store ID
Outlet_Establishment_Year: The Year in which store is established
Outlet_Size: Areawise distribution of Stores- Low/Medium/High
Outlet_Location_Type: Type of city in which outlet is located
Outlet_Type: Type of outlet - Grocery store or supermarket
Item_Outlet_Sales: Sale price of product - The dependant variable to be predicted

#The Hypothesis

Locality: Outlet in populated locality should generate more revenue

Spending Capacity: Tier 1 should have more spending capacity than tier 2 and tier 3

Product Selection: Tier 1 should prefer low fat content food as they tend to be more aware of their health

Item Visiblity: More visible Item should have more revenue generating power

Area: Stores which have early establishment could have higher outlet size

MRP: Consumers prefer reasonable product or Branded products
