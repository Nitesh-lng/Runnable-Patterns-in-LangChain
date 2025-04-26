# 🛠️ Runnables with LangChain & Groq

This project demonstrates how to use **LangChain**'s `Runnable` interfaces with **Groq LLMs** for building modular, composable, and flexible AI pipelines.  
Each runnable script explores different patterns like **sequence**, **parallel**, **branching**, **passthrough**, and **lambda** operations.

---

## 📂 Project Structure

```bash
runnables/
├── branch_runnable.py         # Branching based on input conditions
├── lambda_runnable.py         # Using lambda runnable for custom logic
├── parelle_runnable.py        # Parallel execution of multiple tasks
├── passthrough_runnable.py    # Passthrough and explanation chain
├── sequence_runnable.py       # Sequential chaining of prompts
├── requirements.txt           # Python dependencies
```

---

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

### 3. Install the Required Packages

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root with the following content:

```env
GROQ_API_KEY=your_groq_api_key_here
```

(Replace `your_groq_api_key_here` with your actual Groq API Key.)

### 5. Run the Scripts

You can execute any runnable script individually:

```bash
python branch_runnable.py
python lambda_runnable.py
python parelle_runnable.py
python passthrough_runnable.py
python sequence_runnable.py
```

---

## 🛠️ Explanation of Each Runnable

| File | Description |
| :--- | :--- |
| `branch_runnable.py` | Uses `RunnableBranch` to dynamically choose the next step based on the word length of input text. |
| `lambda_runnable.py` | Integrates a custom Python function with `RunnableLambda` inside the AI pipeline. |
| `parelle_runnable.py` | Demonstrates parallel execution: generates a tweet and a LinkedIn post simultaneously. |
| `passthrough_runnable.py` | Generates a joke, then passes it through to generate an explanation using a second model call. |
| `sequence_runnable.py` | Chains prompts and LLM responses sequentially to first generate a joke and then explain it. |

---

## 🛆 Requirements

- Python 3.8 or above
- [LangChain](https://python.langchain.com/)
- [Groq](https://groq.com/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

All dependencies are listed in `requirements.txt`.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## ❤️ Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain)
- [Groq LLMs](https://groq.com/)

---

# ✨ Quick Demo

Each script prints its final output directly to the console after execution.

