# ATP MATCH PREDICTOR

This project uses **machine learning** to predict the outcomes of **ATP** (Association of Tennis Professionals) matches. The goal is to predict the winner of head-to-head matches between two players based on their individual statistics. We use supervised learning algorithms implemented with the **scikit-learn** library.

---

## Data Used

The data used in this project includes information such as:

- **Players**: Information like name, country, height, preferred hand, and more.
- **Matches**: Match results, including date, tournament, surface, and winners.
- **Rankings**: Historical player rankings over time.
- **Other**: Detailed statistics such as first serve percentage, break point conversion, and more.

---

## Project Objective

The goal of this project is to predict the **outcome** of matches between ATP players based on their historical statistics. The model predicts the winner of a match by considering variables such as:

- Historical wins and losses
- ATP ranking
- Performance on different playing surfaces (clay, grass, hard court)
- Match statistics from previous games

The model is trained and evaluated using a historical dataset with results from past matches.

---

## Project Structure

The project is organized as follows:

```
├── data
│ ├── processed/
│ ├── raw/
├── models/
├── notebooks/
├── src/
├── requirements.txt
└── README.md
```

---

## Requirements

This project was developed and tested with the following dependencies:

- Python 3.8 or higher
- Key libraries:
  - **pandas**: For data manipulation
  - **numpy**: For numerical operations
  - **scikit-learn**: For building and evaluating ML models
  - **matplotlib** and **seaborn**: For data visualization

### Installation

To install all necessary dependencies, use the following command:

```bash
pip install -r requirements.txt
```
---

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

We would like to thank **Jeff Sackmann** for the historical ATP match data, which is the foundation of this project. The dataset can be found in the [tennis_atp repository](https://github.com/JeffSackmann/tennis_atp).

---