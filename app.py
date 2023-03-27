from flask import Flask, render_template, request
import openai

# Set up OpenAI API key
openai.api_key = "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"

# Initialize Flask app
app = Flask(__name__)

# Define routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    # Get user input from form
    code = request.form.get("code")

    # Use OpenAI API to generate code explanation
    prompt = "Explain this code:\n" + code
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    explanation = response.choices[0].text

    # Render result page with generated explanation
    return render_template("result.html", code=code, explanation=explanation)

# Run app
if __name__ == "__main__":
    app.run(debug=True)
