# Next Read [![Visits Badge](https://badges.pufler.dev/visits/bumbot-hub/Next-Read)](https://badges.pufler.dev)

## Summary

This project personalizes book recommendations by using Goodreads and user data to create feature vectors, including ratings and genres. These vectors feed into a KNN model that generates a list of the 30 most compatible books for each user based on their preferences .

## Background
Many readers struggle to discover new books that truly match their interests, despite the vast catalogs available online. While platforms like Goodreads offer rich user preference data, current personalized recommendations often fall short. For instance, recommendations are frequently limited to selected genres, and even within those, the quality and relevance can be inconsistent.

This AI idea resonated deeply with me, as I am an avid reader and, ironically, a regular Goodreads user myself. My personal experiences with the platform's limitations directly inspired me to choose this topic for my AI project, aiming to develop a more effective recommendation system.

This project addresses:

- Difficulty in finding relevant book suggestions tailored to personal taste,
- Under utilization of publicly available user rating and review data.

## Getting Started

This guide will walk you through setting up and running the project on your local machine.
### How It Works

Users provide their Goodreads data export (a .csv file containing ratings, reviews, etc.). The system processes this data to generate a list of personalized book recommendations.
### Prerequisites

To run this project, you will need:
- Python 3.10 or higher.
- Git to clone the repository.

### Installation & Setup

1. Clone the repository:
    Open your terminal and run the following command to clone the project:
    ```
    git clone https://github.com/bumbot-hub/Next-Read.git
    ```
2. Navigate to the Project Directory.
    ```
    cd Next-Read
    ```
3. Install Required Dependencies.  
Install all the necessary libraries listed in the requirements.txt file:
    ```
    pip install -r requriements.txt
    ```
4. **Add your Goodreads data.**  
This is a crucial step for personalized recommendations:
    - Log in to your [Goodreads](https://www.goodreads.com/) account,
    - Go to the [Export site](https://www.goodreads.com/review/import) page,
    - Click the **Export library** button,
    - After the export is complete, a link like "Your export from..." will appear. Click it to download your library as a ``.csv`` file,
    - Important: Move the downloaded file (e.g., goodreads_library_export.csv) into the data/ directory within the project. The final path should look like: Goodreads_Book_Recomendation/data/your_file_name.csv.

5. Run the app.
    Once the setup is complete, you can run the application with the following command in your terminal:
    ```
    python main.py
    ```
The application will then generate your personalized book list. Enjoy discovering your next favorite book

## Data Sources and AI Methods

- User data exported from Goodreads profiles (ratings, reviews, shelves)
- Public Goodreads datasets from platforms like Kaggle containing millions of user ratings and reviews
- AI methods: kNN model used for recommendation system, feature engineering to create book and users feature vectors.

## Challenges

- **Cold start problem**: New users or books without sufficient data face difficulties in making accurate recommendations.
- **Balancing diversity and relevance**: Avoiding echo chambers while ensuring recommendations remain relevant.
- **Bias in recommendations**: Ensuring recommendations don’t reinforce biases in user preferences or popular books only.

## What’s next?

Future improvements could include:

- Incorporating sentiment analysis of reviews to better understand user preferences
- Adding social network data (friends’ recommendations) to enhance collaborative filtering
- Building a user-friendly interface for easy data upload and personalized results
- Exploring multimodal data (book covers, author interviews) for richer content-based filtering
