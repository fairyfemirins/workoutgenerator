#!/usr/bin/env python3
"""
Workout Generator - A web-based tool for generating personalized workouts.
"""

import os
import sqlite3
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Mock data for offline testing
MOCK_WORKOUTS = {
    "strength": {
        "dumbbells": [
            {"exercise": "Goblet Squat", "sets": 3, "reps": 10},
            {"exercise": "Dumbbell Bench Press", "sets": 3, "reps": 10},
            {"exercise": "Bent-Over Row", "sets": 3, "reps": 10}
        ],
        "bodyweight": [
            {"exercise": "Push-Ups", "sets": 3, "reps": 15},
            {"exercise": "Bodyweight Squats", "sets": 3, "reps": 20},
            {"exercise": "Plank", "sets": 3, "duration": "30s"}
        ]
    },
    "endurance": {
        "dumbbells": [
            {"exercise": "Dumbbell Thrusters", "sets": 3, "reps": 12},
            {"exercise": "Dumbbell Swings", "sets": 3, "reps": 15},
            {"exercise": "Jump Rope", "sets": 3, "duration": "1m"}
        ],
        "bodyweight": [
            {"exercise": "Burpees", "sets": 3, "reps": 10},
            {"exercise": "Mountain Climbers", "sets": 3, "duration": "30s"},
            {"exercise": "Jumping Jacks", "sets": 3, "reps": 30}
        ]
    },
    "flexibility": {
        "dumbbells": [
            {"exercise": "Dumbbell Stretch", "sets": 3, "duration": "20s"},
            {"exercise": "Seated Forward Fold", "sets": 3, "duration": "30s"}
        ],
        "bodyweight": [
            {"exercise": "Cat-Cow Stretch", "sets": 3, "duration": "20s"},
            {"exercise": "Downward Dog", "sets": 3, "duration": "30s"},
            {"exercise": "Child's Pose", "sets": 3, "duration": "30s"}
        ]
    }
}

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('workouts.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            goal TEXT NOT NULL,
            equipment TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_workout', methods=['POST'])
def generate_workout():
    data = request.json
    goal = data.get('goal', 'strength')
    equipment = data.get('equipment', 'bodyweight')
    
    # Fetch workout from mock data
    workout = MOCK_WORKOUTS.get(goal, {}).get(equipment, [])
    
    return jsonify({
        "workout": workout,
        "goal": goal,
        "equipment": equipment
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=True)