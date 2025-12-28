# Invisible Friction Index

**We don’t predict failing students — we measure failing academic design.**

---

## Overview

Capable students often struggle or burn out not because of lack of effort or ability, but because academic systems silently overload them.

The **Invisible Friction Index (IFI)** reframes student failure as a **system-level design problem**, not an individual weakness. It quantifies hidden workload pressure created by dense schedules, rigid timing, and clustered demands — long before burnout or failure becomes visible.

Instead of asking *“Which student is at risk?”*, this project asks:  
**“Which academic designs are unsafe?”**

---

## The Problem

Academic systems create **invisible friction** through design choices such as:

- Back-to-back classes with no recovery buffers  
- Compressed daily schedules  
- Clustered deadlines and assessments  
- Rigid early and late class timings  

This friction:
- Is **not graded**
- Is **not tracked**
- Is **not measured**

Yet it steadily drains cognitive and physical energy, reduces learning quality, and increases failure risk. Most interventions occur **after** collapse, while the underlying design remains unchanged.

---

## What This Project Does

The Invisible Friction Index is a **system-level analytics tool** that:

- Engineers timetable-like design features from student performance data  
- Computes a composite **Invisible Friction Index**  
- Categorizes conditions into **Survivable**, **Warning**, and **Unsafe** bands  
- Aggregates risk at the **system level**, not the individual level  
- Suggests **concrete design fixes**, not student interventions  

The goal is **prevention through better design**, not monitoring or labeling students.

---

## How It Works

### 1. Data
We use a public Kaggle / UCI student performance dataset as a proxy environment.

### 2. Friction Feature Engineering
We construct timetable-inspired design signals such as:
- Schedule density  
- Back-to-back intensity  
- Deadline clustering  
- Temporal rigidity  

These features represent **system-imposed workload pressure**, not student behavior.

### 3. Invisible Friction Index
The engineered features are normalized and combined into a single index representing how difficult an academic design is to sustain over time.

### 4. Validation (Ablation Study)
We compare:
- A baseline model using standard student covariates  
- The same model augmented with the friction index  

The model including friction consistently performs better, demonstrating that **design-level friction adds independent predictive signal** beyond individual attributes.

### 5. Interactive Dashboard
A Streamlit app visualizes:
- System-level friction distribution  
- Risk bands (Survivable / Warning / Unsafe)  
- Automatic, rule-based design fix suggestions  
- A clear model card explaining scope and limits  

---

## Key Insight

> **Burnout is often an emergent property of academic design, not a personal failure.**

Even with data not explicitly designed for scheduling analysis, design-level friction emerges as a measurable and actionable risk signal.

---

## Ethics & Responsibility

**What this model does:**
- Measures system-imposed academic design friction  
- Identifies unsafe scheduling patterns  

**What this model does NOT do:**
- No mental health diagnosis  
- No behavioral surveillance  
- No student labeling or grading decisions  

**Intended users:**
- Timetable designers  
- Academic planners  
- Institutional policy teams  

The project is explicitly designed to avoid surveillance and blame, focusing instead on **structural accountability**.

---

## Tech Stack

- Python  
- Pandas, NumPy — data processing  
- Scikit-learn — modeling and ablation  
- Streamlit — interactive dashboard  

---

## Running the Demo

```bash
streamlit run app/app.py
