# Smartphone CPU List with Search Functionality

This project is a simple web application built with **Flask**, **HTML**, **CSS**, and **JavaScript** to display a list of smartphone processors (CPUs). The CPU data is **scraped** from the [NanoReview CPU Ranking Page](https://nanoreview.net/en/soc-list/rating) using web scraping techniques. The application includes a search functionality to filter CPUs based on their name or other attributes. The data is dynamically rendered using **Jinja2 templates** and Flask.

## Features
- Displays a list of smartphone CPUs in a table.
- Search functionality to filter the list of CPUs in real-time.
- Fully responsive design for mobile and desktop views.
- Dynamic content rendered using **Flask** and **Jinja2 templates**.
- **Web scraping** to fetch CPU data from the NanoReview website.

## Data Source

The CPU data displayed in this application is fetched by performing web scraping from the [NanoReview CPU ranking](https://nanoreview.net/en/soc-list/rating). The website provides detailed rankings and specifications for various smartphone processors, which are extracted and displayed on this web app.

## Prerequisites

- Python 3.x
- Flask
- BeautifulSoup4
- Requests
- Basic knowledge of HTML, CSS, and JavaScript.

