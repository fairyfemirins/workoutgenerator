# Workout Generator - Design Decisions & Rationale

## Problem Statement
Fitness enthusiasts and beginners struggle to **find personalized workouts** that match their goals and available equipment. This project provides a **free, open-source tool** to generate tailored workouts without the need for expensive apps or trainers.

## Design Decisions

### 1. Backend: Flask
- **Why Flask?** Lightweight, easy to set up, and ideal for small-scale web apps.
- **Why Mock Data?** Ensures the app works **offline or without external dependencies**.

### 2. Frontend: HTML/CSS/JS + Bootstrap
- **Why Bootstrap?** Ensures a **responsive, mobile-friendly UI** with minimal effort.
- **Why Vanilla JS?** Simplifies deployment and avoids heavy frameworks like React.

### 3. Workout Generation Logic
- **Goal-Based Workouts:** Users can select **Strength, Endurance, or Flexibility** goals.
- **Equipment Adaptation:** Workouts adapt to **Bodyweight, Dumbbells, or Resistance Bands**.
- **Mock Data:** Predefined workouts for each goal/equipment combination.

### 4. Database: SQLite
- **Why SQLite?** Lightweight, file-based, and ideal for small-scale persistence.
- **Future Extensions:** Can be extended to store **user profiles and workout history**.

## Challenges & Solutions

### 1. Offline Support
- **Challenge:** Users may not have internet access.
- **Solution:** **Mock data** ensures the app works offline.

### 2. Scalability
- **Challenge:** In-memory storage does not scale for large numbers of users.
- **Solution:** Future work includes **user authentication** and **persistent storage**.

### 3. Personalization
- **Challenge:** AI-driven personalization requires training data and infrastructure.
- **Solution:** **Mock logic** provides a starting point for future enhancements.

## Future Work
- **User Authentication:** Add login via Google/GitHub to save preferences.
- **Video Demonstrations:** Add video links for each exercise.
- **Apple Health/Google Fit Integration:** Sync workouts automatically.
- **Gamification:** Add achievements and progress tracking.

## License
MIT