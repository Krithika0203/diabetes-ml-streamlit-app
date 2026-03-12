# 🧠 Prompt Templates – Diabetes Prediction ML App

This document contains reusable **prompt engineering templates** used in the **Diabetes Prediction Streamlit Application**.

These prompts help generate **clear explanations, health guidance, and educational responses** based on the machine learning prediction results.

---

# 📌 Purpose of Prompt Templates

Prompt engineering helps improve the quality of AI-generated responses by structuring the input given to the AI model.

In this project, prompts are designed to:

* Explain ML model predictions
* Provide health awareness guidance
* Help users understand medical terms
* Generate personalized recommendations
* Improve user experience in the application

---

# 🧩 Prompt Structure Used

Each prompt follows a structured format to ensure better AI responses.

**Role**
Defines what the AI should act as.

**Task**
Defines what the AI should do.

**Context**
Provides additional information for better responses.

**Format**
Specifies how the output should be structured.

---

# 📊 1. Diabetes Prediction Explanation Prompt

### Purpose

Explain the machine learning prediction result in a simple and understandable way.

### Prompt Template

Role: You are a healthcare AI assistant.

Task: Explain the diabetes prediction result to the user.

Context:
Prediction Result: {prediction}

Health Metrics:

* Pregnancies: {pregnancies}
* Glucose Level: {glucose}
* Blood Pressure: {blood_pressure}
* Skin Thickness: {skin_thickness}
* Insulin Level: {insulin}
* BMI: {bmi}
* Diabetes Pedigree Function: {dpf}
* Age: {age}

Format:

1. Simple explanation of the result
2. Possible risk factors
3. General health suggestions

### Example Prompt

Explain why the model predicted **High Diabetes Risk** for a patient with:

Glucose: 165
BMI: 34
Age: 47

---

# 🥗 2. Health Recommendation Prompt

### Purpose

Provide lifestyle advice based on the prediction result.

### Prompt Template

Role: You are a certified health advisor.

Task: Provide lifestyle suggestions for diabetes prevention or management.

Context:
Prediction Result: {prediction}

Format:

* Diet recommendations
* Exercise suggestions
* Lifestyle improvements
* When to consult a doctor

### Example Prompt

Provide healthy lifestyle suggestions for a person predicted to have a **high risk of diabetes**.

---

# 📘 3. Medical Term Explanation Prompt

### Purpose

Help users understand medical terms used in the diabetes prediction system.

### Prompt Template

Role: You are a medical educator.

Task: Explain a medical term in simple language.

Context:
Medical Term: {term}

Format:

1. Simple definition
2. Why it matters for diabetes
3. Example

### Example Prompt

Explain **Blood Glucose Level** in simple terms for a beginner.

---

# ⚠️ 4. Input Validation Prompt

### Purpose

Explain invalid or unrealistic input values entered by users.

### Prompt Template

Role: You are an assistant in a health prediction system.

Task: Explain why a user input is invalid.

Context:
Invalid Input: {input_value}
Feature: {feature_name}

Format:

* Why the input is incorrect
* Valid range for the feature
* Example of correct value

### Example Prompt

Explain why **BMI value -5** is invalid and provide the correct range.

---

# 📚 5. Diabetes Awareness Prompt

### Purpose

Educate users about diabetes and its prevention.

### Prompt Template

Role: You are a diabetes awareness educator.

Task: Explain diabetes in simple language.

Context:
Audience: general public

Format:

1. What is diabetes
2. Common symptoms
3. Causes
4. Prevention tips

### Example Prompt

Explain diabetes in simple terms for someone who has never studied medicine.

---

# 🧾 6. Risk Factor Explanation Prompt

### Purpose

Explain which health metrics increase diabetes risk.

### Prompt Template

Role: You are a medical AI assistant.

Task: Identify and explain risk factors.

Context:
User Health Metrics:

* Glucose: {glucose}
* BMI: {bmi}
* Age: {age}

Format:

* Identify major risk factors
* Explain why they matter
* Suggest improvements

---

# 🧪 7. Prediction Confidence Explanation Prompt

### Purpose

Help users understand how confident the ML model is.

### Prompt Template

Role: You are an AI system explaining machine learning predictions.

Task: Explain prediction confidence.

Context:
Prediction: {prediction}
Model Accuracy: {accuracy}

Format:

* Explain confidence level
* What it means for the user
* Reminder that ML predictions are not medical diagnoses

---

# 📈 8. Preventive Health Tips Prompt

### Purpose

Provide actionable tips for preventing diabetes.

### Prompt Template

Role: You are a preventive healthcare specialist.

Task: Provide practical tips for diabetes prevention.

Format:

* Daily habits
* Diet improvements
* Exercise recommendations
* Health monitoring suggestions

---

# 🧩 Example Combined Prompt

Role: Healthcare AI assistant
Task: Explain the prediction and provide suggestions

Context:
Prediction Result: High Diabetes Risk
Glucose Level: 170
BMI: 35
Age: 50

Format:

* Explanation of prediction
* Risk factors
* Lifestyle advice

---

# 🚀 Future Improvements

Future versions of this project may include:

* Integration with **LLM APIs**
* AI-generated **personalized health guidance**
* Chatbot for **diabetes awareness**
* AI-powered **medical explanation system**

---
