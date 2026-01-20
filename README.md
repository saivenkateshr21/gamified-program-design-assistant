# 🎓 Gamified Program Design Assistant

**Streamlining Program Design for NGOs**

The **Gamified Program Design Assistant** is a lightweight, frontend-driven web application aimed at helping NGOs design structured, scalable, and effective education programs. It guides teams through a step-by-step process—from problem definition to success metrics—turning a complex task into an engaging, gamified workflow.

## 🚀 Key Features

-   **Step-by-Step Guidance**: Breaks program design into clear stages (Problem, Outcomes, Stakeholders, Activities, Metrics).
-   **Gamified Experience**: Progress bars, completion badges, and "Coach" tips keep users engaged.
-   **Smart Readiness Score**: A specialized algorithm evaluates your design for coverage (completeness) and depth (detail), providing a "Readiness Score" (0-100).
-   **Review & Gap Analysis**: Automatically highlights missing sections or weak responses with constructive feedback.
-   **Downloadable Framework**: Export your final design as a professional **PDF** or **Text/Doc** file.
-   **No Backend Required**: Built entirely with Python and Streamlit, running locally or on any cloud platform with minimal setup.

## 🛠️ Technology Stack

-   **Frontend/Logic**: [Streamlit](https://streamlit.io/) (Python)
-   **PDF Generation**: [FPDF](https://pyfpdf.readthedocs.io/en/latest/)
-   **Data Handling**: JSON (In-memory session state)

## 📦 How to Run Locally

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/saivenkateshr21/gamified-program-design-assistant.git
    cd gamified-program-design-assistant
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the App**
    ```bash
    streamlit run app.py
    ```

4.  **Access the App**
    Open your browser and navigate to `http://localhost:8501`.

## 📂 Project Structure

```
├── src/
│   ├── data/
│   │   └── templates.py    # Questions and structure for each stage
│   ├── logic/
│   │   └── framework.py    # Scoring, progress tracking, and export logic
│   └── ui/
│       ├── generic_stage.py # Dynamic renderer for input stages
│       ├── review.py       # Final review page with score and download
│       └── welcome.py      # Landing page
├── app.py                  # Main application entry point
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## 🤝 Contribution

This project was built for the **Shikshalokam – Innovation for Education Equity Hackathon**.
Suggestions and improvements are welcome!

---
*Built with ❤️ for Education Equity.*
