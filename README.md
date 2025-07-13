# Student Performance Analysis & Prediction

Predicting student success isn’t just a data problem—it’s a challenge that blends curiosity, creativity, and code. This repo is where I set out to crack that challenge: taking raw, messy data and turning it into real, actionable insights with machine learning. From wrangling the data to building modular pipelines and picking the best model, every step here is about pushing the boundaries of what’s possible with Python and ML.

## Why This Project?

I wanted more than just another notebook experiment. My goal: build a project that’s clean, modular, and ready for anything—whether that’s new data, new models, or new questions. It’s about making data science work that’s actually reusable, not just a one-off.

## My Approach

1. **Exploratory Data Analysis (EDA):**
   - Deep dive into the data (see `data/EDA.ipynb`), asking: What features matter? What’s missing? What’s interesting?

2. **Data Preparation:**
   - Wrote scripts to clean, encode, and scale the data—no shortcuts, just solid prep for real modeling.

3. **Model Building:**
   - Threw a bunch of regression models at the problem, compared their performance, and learned what works (and what doesn’t). All the code’s in the notebooks and `src/components/`.

4. **Pipelines & Modularity:**
   - No more “notebook soup.” Everything’s broken into components so I can rerun, swap, or extend any part of the process.

5. **Logging & Error Handling:**
   - Custom logging and exception handling—because real projects need real debugging tools.

## Project Structure

```
DS-ML/
├── artifacts/           # Where data splits, models, and preprocessors are saved
├── data/                # Notebooks for EDA and manual experiments
├── src/                 # All the core Python code
│   ├── components/      # Data ingestion, transformation, and model training
│   ├── pipeline/        # (To be expanded) Scripts for running the full process
│   ├── utils.py         # Helper functions
│   ├── logger.py        # Logging setup
│   └── exceptions.py    # Custom error handling
├── requirements.txt     # Everything you need to install
├── setup.py             # For installing as a package
└── README.md            # This file
```

## How to Use

1. **Clone the repo and install dependencies:**
   ```bash
   git clone https://github.com/yourusername/DS-ML.git
   cd DS-ML
   pip install -r requirements.txt
   ```
2. **(Optional) Install as a package:**
   ```bash
   pip install .
   ```
3. **Run the process step by step:**
   - Data ingestion:
     ```python
     from src.components.data_ingestion import DataIngestion
     di = DataIngestion()
     train_path, test_path, raw_path = di.initiate_data_ingestion()
     ```
   - Data transformation:
     ```python
     from src.components.data_transform import DataTransformation
     dt = DataTransformation()
     train_arr, test_arr, preprocessor_path = dt.initiate_data_transformation(train_path, test_path)
     ```
   - Model training:
     ```python
     from src.components.model_trainer import ModelTrainer
     mt = ModelTrainer()
     r2 = mt.initiate_model_trainer(train_arr, test_arr)
     print(f'Best model R2 score: {r2}')
     ```

## What I Learned
- Clean, modular code is a game-changer (especially when things break)
- Not all models are created equal—real data exposes the difference
- Good logging and error handling save hours of pain
- A well-structured project pays off every time you revisit it

## Next Steps
- Automate the full pipeline (see `src/pipeline/`—work in progress!)
- Experiment with more advanced feature engineering
- Try deploying the model as an API

---

Questions, ideas, or want to collaborate? Hit me up!

*Ratnam Ojha (<ratnamojha71@gmail.com>)*
