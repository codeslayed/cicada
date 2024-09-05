<h1>Cicada Ai: Cryptographic Algorithm Detector</h1>

<p>Cicada Ai is a project that aims to detect and analyze cryptographic algorithms in various file formats. It includes three main components:</p>

<ol>
    <li><strong>Streamlit App</strong>: A web application built with Streamlit that allows users to upload files and ask questions about them.</li>
    <li><strong>Flask API</strong>: A RESTful API built with Flask that provides file analysis functionality.</li>
    <li><strong>Telegram Bot</strong>: A Telegram bot that enables users to upload files and ask questions via chat.</li>
</ol>

<h2>Features</h2>
<ul>
    <li>Supports image (JPG, PNG) and text (TXT, CSV) file formats</li>
    <li>Detects and analyzes cryptographic algorithms in uploaded files</li>
    <li>Provides detailed explanations of the detected algorithms</li>
    <li>Allows users to ask questions about the uploaded files</li>
    <li>Utilizes Google Generative AI for content generation</li>
</ul>

<h2>Upcoming YouTube Video</h2>
<p>Stay tuned for our upcoming YouTube video where we will demonstrate how to use the Cicada Ai project, including step-by-step instructions for each component. Subscribe to our channel for updates!</p>

<h2>Components</h2>

<h3>1. Streamlit App</h3>
<p>The Streamlit app allows users to upload files and ask questions about them. It displays the uploaded image and generates a response based on the user's question and the file content.</p>
<details>
    <summary>Click to expand the Streamlit app code</summary>
    <pre><code># Streamlit app code goes here</code></pre>
</details>

<h3>2. Flask API</h3>
<p>The Flask API provides a RESTful interface for file analysis. Users can upload files and receive a response containing the analysis results.</p>
<details>
    <summary>Click to expand the Flask API code</summary>
    <pre><code># Flask API code goes here</code></pre>
</details>

<h3>3. Telegram Bot</h3>
<p>The Telegram bot enables users to interact with the file analysis functionality via chat. Users can send documents to the bot and ask questions, and the bot will respond with the analysis results.</p>
<details>
    <summary>Click to expand the Telegram bot code</summary>
    <pre><code># Telegram bot code goes here</code></pre>
</details>

<h2>Dependencies</h2>
<p>The project relies on the following dependencies, which are listed in the <a href="requirements.txt">requirements.txt</a> file:</p>
<ul>
    <li><strong>Streamlit</strong>: A Python library for building interactive web applications</li>
    <li><strong>Flask</strong>: A micro web framework for Python</li>
    <li><strong>telebot</strong>: A Python library for creating Telegram bots</li>
    <li><strong>google.generativeai</strong>: A library for interacting with Google's Generative AI API</li>
    <li><strong>google.ai.generativelanguage</strong>: A library for generative language processing</li>
</ul>

<h2>Configuration</h2>
<p>Before running any of the components, make sure to set the appropriate API keys in the respective files:</p>
<ul>
    <li><strong>Streamlit App</strong>: Set the Google API key in the <code>API_KEY</code> variable</li>
    <li><strong>Flask API</strong>: Set the Google API key in the <code>API_KEY</code> variable</li>
    <li><strong>Telegram Bot</strong>: Set the Telegram API token in the <code>TELEGRAM_API_TOKEN</code> variable and the Google API key in the <code>API_KEY</code> variable</li>
</ul>

<h2>Running the Components</h2>
<p>To run each component, navigate to the corresponding directory and execute the following commands:</p>

<h3>Streamlit App</h3>
<pre><code>streamlit run cicada.py</code></pre>

<h3>Flask API</h3>
<pre><code>python server.py</code></pre>

<h3>Telegram Bot</h3>
<pre><code>python cryptidtele.py</code></pre>

<p>Make sure to have the necessary dependencies installed before running each component.</p>

<h2>Contributing</h2>
<p>Contributions to the Cicada Ai project are welcome. If you find any issues or have suggestions for improvements, please feel free to submit a pull request or create an issue on the project's repository.</p>

<h2>License</h2>
<p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>
