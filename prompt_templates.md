# Prompt Templates – Diabetes ML Streamlit App

This file contains prompt templates used for generating explanations, medical guidance, and user-friendly responses in the Diabetes Prediction Streamlit application.

---

## 1. Prediction Explanation Prompt

Purpose: Explain the ML model prediction to the user.

Template:

Role: You are a healthcare AI assistant.

Task: Explain the diabetes prediction result.

Context:
Prediction Result: {prediction}
User Health Metrics:
- Glucose: {glucose}
- BMI: {bmi}
- Age: {age}

Format:
- Simple explanation
- Possible risk factors
- Lifestyle suggestions

Example Prompt:

Explain why the model predicted "High Diabetes Risk" based on glucose level 160, BMI 32, and age 45.

---

## 2. Health Recommendation Prompt

Purpose: Provide lifestyle suggestions after prediction.

Template:

Role: You are a health advisor.

Task: Provide lifestyle recommendations.

Context:
Prediction: {prediction}

Format:
- Diet advice
- Exercise suggestions
- Medical consultation advice

Example Prompt:

Provide healthy lifestyle suggestions for someone predicted to have a high risk of diabetes.

---

## 3. Medical Concept Explanation Prompt

Purpose: Help users understand health terms.

Template:

Role: You are a medical educator.

Task: Explain a medical term simply.

Context:
Term: {medical_term}

Format:
- Simple definition
- Why it matters for diabetes
- Example

Example Prompt:

Explain what "Blood Glucose Level" means in simple terms.

---

## 4. Input Validation Prompt

Purpose: Explain invalid user inputs.

Template:

Role: You are an assistant in a health prediction system.

Task: Explain input errors politely.

Context:
Invalid Input: {input}

Format:
- Error explanation
- Correct input range
- Example value

Example Prompt:

Explain why BMI value -5 is invalid and provide the correct range.

---

## 5. Educational Prompt

Purpose: Educate users about diabetes.

Template:

Role: You are a diabetes awareness educator.

Task: Explain diabetes.

Context:
Audience: general public

Format:
- What is diabetes
- Common symptoms
- Prevention tips

Example Prompt:

Explain diabetes in simple terms for someone with no medical background.
