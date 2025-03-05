AIC COLLECTION VISUALIZATION
=======================

Description
-----------
This project provides interactive visualizations of the Art Institute of Chicago's collection using data downloaded from the AIC API. It features two main visualizations:

1. Hierarchical Treemap:
   - An interactive treemap that categorizes artworks by:
       * Region: US vs. non-US
       * Art Period: Pre-modern, Modern, Contemporary
       * Media Type (e.g., print, painting, etc.)
   - Hovering over each segment displays the number of artworks.
   - This visualization allows users to compare collection counts across different levels.

2. Line Chart:
   - Focused on the Contemporary Art period (1975-2025).
   - Allows users to select different media types.
   - The x-axis represents the artwork's completion year, and the y-axis shows the number of artworks.
   - This chart displays annual trends in artwork counts for the selected media.

Installation
------------
This project requires the following Python packages:
    pandas>=1.0
    streamlit>=1.0
    plotly>=4.0

To install these dependencies, run the following commands in your terminal:
    pip install pandas>=1.0
    pip install streamlit>=1.0
    pip install plotly>=4.0

Usage
-----
You have two options to view and interact with this application:

1. **Online Deployment:**  
   Visit the deployed Streamlit application at:
       https://sunnyziyi15-aic-collection-data-visualization-final-aytjzy.streamlit.app/

2. **Local Run:**  
   Clone the repository and run the application locally with:
       streamlit run final.py

Data Source
-----------
The data used in this project is sourced from the Art Institute of Chicago API:
    https://api.artic.edu/
Hosted by Streamlit.
