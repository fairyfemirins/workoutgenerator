# Workout Generator - Reproducible Setup Guide

## Prerequisites
- Python 3.8+
- pip
- A modern web browser (Chrome, Firefox, Edge)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/fairyfemirins/workoutgenerator.git
cd workoutgenerator
```

### 2. Install Dependencies
```bash
pip install flask python-dotenv --break-system-packages
```

### 3. Run the Server
```bash
python3 app.py
```

### 4. Access the App
Open your browser and navigate to:
```
http://localhost:5011
```

## Usage

### 1. Generate a Workout
- Select a **goal** (Strength, Endurance, Flexibility).
- Select your **equipment** (Bodyweight, Dumbbells, Resistance Bands).
- Click **"Generate Workout"** to view your personalized workout.

## Troubleshooting

### 1. Port Already in Use
If port `5011` is already in use, change the port in `app.py`:
```python
app.run(host='0.0.0.0', port=5012, debug=True)
```

### 2. Frontend Not Loading
- Ensure the server is running (`python3 app.py`).
- Check the browser console for errors.

### 3. No Workout Generated
- Ensure you have selected a **goal and equipment**.

## License
MIT