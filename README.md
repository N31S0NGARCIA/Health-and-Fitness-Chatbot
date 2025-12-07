# **Health & Fitness Coach Chatbot**

A simple and interactive Python-based chatbot designed to help users improve their fitness lifestyle.
It provides **workout recommendations**, **dietary suggestions**, **motivational quotes**, and **water-intake calculations** based on user input.

---

## Features

### Workout Recommendations

Users can request exercise suggestions for major muscle groups:

* Chest
* Back
* Shoulders
* Biceps
* Triceps
* Legs
* Core
* Forearms

Each selection displays a curated list of recommended exercises.

---

### Dietary Recommendations

The chatbot offers food recommendations across multiple categories:

* Fruits
* Vegetables
* Grains
* Protein
* Dairy

This helps users build balanced and healthy meals.

---

### Daily Water Intake Calculator

Users can enter their weight and receive a recommended amount of daily water intake in:

* Ounces
* 8-oz cups

Designed to encourage smart hydration habits.

---

### Motivational Fitness Quotes

The chatbot includes 10 randomized motivational quotes from athletes and iconic figures to keep users motivated.

---

## How It Works

1. When the program starts, the chatbot greets the user and asks for their name.
2. The **Main Menu** provides five options:

   * `"Workout"`
   * `"Diet"`
   * `"Quotes"`
   * `"Water"`
   * `"End"` to exit the chatbot
3. Each option leads to a specialized function that handles user interaction.
4. Users can type `"exit"` within menus to return to the main menu.

---

## Program Structure

The project is organized into modular functions:

| Function                | Purpose                                          |
| ----------------------- | ------------------------------------------------ |
| `main_menu()`           | Core navigation menu                             |
| `exercises()`           | Gives workout recommendations                    |
| `dietary()`             | Gives food recommendations                       |
| `water_intake()`        | Calculates water needs based on weight           |
| `motivational_quotes()` | Prints a random motivational quote               |
| `print_header()`        | Creates formatted visual headers for readability |

Two internal dictionaries store data:

* `recommendations` → exercise lists
* `food_options` → dietary lists

---

## How to Run the Chatbot

Ensure you have **Python 3** installed.
Run the program from your terminal:

```bash
python ngarcia_chatbot.py
```

Follow the prompts and enjoy your personalized fitness guidance!

---

## Dependencies

* Python Standard Library

  * `random`


