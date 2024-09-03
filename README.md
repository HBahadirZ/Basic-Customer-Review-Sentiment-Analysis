
# Customer Review Sentiment Analysis

This repository contains a web-based application for sentiment analysis of customer reviews. The application preprocesses review data, applies sentiment analysis, and displays the results on a web page using an interactive table and chart.

## Project Structure

- **app.py**: The main Flask application file that runs the web server and serves the HTML page.
- **preprocessing.py**: Contains functions to preprocess the customer review data, such as cleaning and preparing the text for sentiment analysis.
- **sentiment_analysis.py**: Implements the sentiment analysis logic, calculating sentiment scores and assigning labels (Positive, Negative, Neutral) to each review.
- **index.html**: The HTML file that provides the front-end interface for displaying the sentiment analysis results in a tabular format and visualizing them in a bar chart.
- **Sample_Customer_Reviews.csv**: A CSV file containing raw customer reviews to be analyzed.
- **sentiment_scores.csv**: A CSV file containing the output of sentiment analysis, including sentiment scores and labels for each review.
- **cleaned_file.csv**: A CSV file that contains cleaned data after preprocessing.

## Getting Started

### Prerequisites

To run this project, you need:

- Python 3.x
- Flask
- Pandas
- Scikit-learn
- Chart.js (for frontend visualization)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Install the required Python libraries:
    ```bash
    pip install Flask pandas scikit-learn
    ```

### Running the Application

1. Start the Flask server:
    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000` to view the sentiment analysis results.

## Usage

1. **Preprocessing**: The `preprocessing.py` script cleans and prepares the raw customer reviews in `Sample_Customer_Reviews.csv`.
2. **Sentiment Analysis**: The `sentiment_analysis.py` script computes sentiment scores and labels for the cleaned reviews.
3. **Web Interface**: The results are displayed on the `index.html` page, showing individual review sentiments and an aggregated sentiment distribution chart.

## File Descriptions

- **app.py**: Uses Flask to create a web server and serve `index.html`. Fetches sentiment data and passes it to the frontend.
- **preprocessing.py**: Prepares the data by removing unwanted characters, normalizing text, and other preprocessing steps.
- **sentiment_analysis.py**: Performs sentiment analysis using methods such as Naive Bayes or any other technique to classify the text into Positive, Negative, or Neutral categories.
- **index.html**: Displays the sentiment results in a table and a bar chart using Bootstrap and Chart.js.
- **yedek.py**: Additional functionality or backup script.
- **Sample_Customer_Reviews.csv**: Raw data of customer reviews for sentiment analysis.
- **sentiment_scores.csv**: The output file with computed sentiment scores and labels.
- **cleaned_file.csv**: Cleaned data ready for sentiment analysis.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [Pandas](https://pandas.pydata.org/) and [Scikit-learn](https://scikit-learn.org/stable/) for data processing and analysis.
- [Chart.js](https://www.chartjs.org/) for data visualization.
