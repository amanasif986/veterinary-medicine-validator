# Veterinary Medicine Concentration & Safety Validator

A Python OOP application that validates safe drug concentrations and detects dangerous compound combinations for veterinary use across 5 animal types.

---

## About the Project

This project was built as part of my Object-Oriented Programming coursework at COMSATS University Islamabad. The goal was to simulate a real-world veterinary pharmacy system where a user can select an animal, choose a medicine, and mix compounds — while the system validates that concentrations are safe and that no dangerous drug combinations are being used.

---

## Features

- Select from 5 animal types: Dog, Cat, Rabbit, Parrot, Hamster
- Choose from species within each animal type
- Select weight class (Small, Medium, Large) for dosage adjustment
- Weight-based concentration recommendation system
- Dangerous drug combination detection with safe alternative suggestions
- Input validation to ensure all concentrations stay within medically safe ranges

---

## OOP Concepts Used

| Concept | How it's used |
|---|---|
| Inheritance | All pet classes inherit from a base class `PetBase` |
| Polymorphism | Each subclass overrides `medicines` and `compounds` with its own data |
| Encapsulation | Medicine rules and compound ranges are contained within each class |
| Static Methods | `adjust_concentration()` is a static method used by all subclasses |
| Abstraction | User interacts through simple menus; complexity is hidden inside the classes |

---

## How It Works

1. User selects a **pet type** (Dog, Cat, Rabbit, Parrot, Hamster)
2. User selects a **species** within that pet type
3. User selects a **weight class** — Small, Medium, or Large
4. System recommends a safe concentration range based on weight
5. User selects a **medicine** and then chooses **2 compounds** to mix
6. System **validates** the mixture:
   - Checks if the correct compounds are used for the selected medicine
   - Checks if the combination is **dangerous**
   - If dangerous, suggests **safe alternatives**
   - Checks if concentrations are within the **safe range**
   - If all checks pass, confirms the mixture is **SAFE**

---

## Technologies Used

- Python 3
- OOP (Classes, Inheritance, Polymorphism, Static Methods)
- Command-line interface (CLI)

---

## Author

**Aman Asif**
BS Business Data Analytics — COMSATS University Islamabad
[LinkedIn](https://www.linkedin.com/in/aman-asif-7aa496257) | [Email](mailto:amanasif986@gmail.com)
