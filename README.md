# Workout Generator

A **web-based tool** for generating personalized workouts based on goals and equipment.

## Features
- **Generate personalized workouts** for strength, endurance, or flexibility.
- **Adapt to available equipment** (bodyweight, dumbbells, resistance bands).
- **Mock data support** for offline testing.

## Technical Architecture
- **Backend:** Python + Flask (for API endpoints).
- **Frontend:** HTML/CSS/JS + Bootstrap (responsive UI).
- **Database:** SQLite (for future user profiles).

## Usage
1. **Select a goal** (Strength, Endurance, Flexibility).
2. **Select your equipment** (Bodyweight, Dumbbells, Resistance Bands).
3. **Click "Generate Workout"** to view your personalized workout.

## Limitations
- **Mock Data:** Uses mock data for workout generation.
- **No Persistence:** User profiles are not saved (extendable with SQLite).

## Future Extensions
- **User Authentication:** Save workout history and preferences.
- **Video Demonstrations:** Add video links for each exercise.
- **Apple Health/Google Fit Integration:** Sync workouts automatically.
- **Gamification:** Add achievements and progress tracking.

## License
MIT