# Knowledge-based Video Recommendation App

This Flask application recommends YouTube videos based on the user's knowledge level. It utilizes the YouTube API to fetch relevant content based on predefined categories.

## Prerequisites
The website runs locally, and needs:
- Python 3.x
- Flask
- Google API Client Library (for YouTube API)
- YouTube Data API Key

## Setup

### 1. Setting up Flask

#### Install Flask

If Flask is not installed, you can install it using pip:

```bash
pip install flask
```

#### Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/DarioTortorici/youtube_recommendation.git
```

#### Set up Virtual Environment (optional but recommended)

A virtual environment isolates dependencies for your project, preventing conflicts with other projects. Follow these steps to create and activate a virtual environment named `YTSuggestions`.

##### Using Python's `venv`:

1. **Create a virtual environment:**

   ```bash
   python -m venv YTSuggestions
   ```

   This command creates a new virtual environment named `YTSuggestions`.

2. **Activate the virtual environment:**

   - On Windows (using Command Prompt):
     ```bash
     YTSuggestions\Scripts\activate
     ```

   - On Windows (using PowerShell):
     ```bash
     .\YTSuggestions\Scripts\Activate.ps1
     ```

   - On macOS/Linux:
     ```bash
     source YTSuggestions/bin/activate
     ```

   This command activates the virtual environment. You should see `(YTSuggestions)` in your command prompt.

##### Using Conda (Windows/macOS/Linux):

1. **Create a virtual environment:**

   ```bash
   conda create --name YTSuggestions python=3.x
   ```

   Replace `3.x` with your preferred Python version (e.g., `3.8`, `3.9`, etc.).

2. **Activate the virtual environment:**

   - On Windows:
     ```bash
     conda activate YTSuggestions
     ```

   - On macOS/Linux:
     ```bash
     source activate YTSuggestions
     ```

   This command activates the Conda virtual environment `YTSuggestions`. You should see `(YTSuggestions)` in your command prompt.

#### Install Dependencies:

Once the virtual environment is activated, you can install the required dependencies:

```bash
pip install -r requirements.txt
```

Replace `requirements.txt` with the actual file containing your dependencies.

#### Deactivate the Virtual Environment:

When you're done working on your project, deactivate the virtual environment:

```bash
deactivate
```

This command will return you to your system's default Python environment.


### 2. Obtain a YouTube API Key

To use the YouTube Data API, you need an API key:

#### Steps to Obtain API Key:

1. **Create a Google Cloud Project**:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project (if you haven't already).

2. **Enable the YouTube Data API**:
   - Navigate to the API & Services → Library section.
   - Search for "YouTube Data API v3" and enable it.

3. **Create Credentials**:
   - Go to API & Services → Credentials.
   - Click on "Create Credentials" and select "API key".
   - Copy the generated API key.

4. **Store API Key Securely**:
   - Save the API key securely. Do not expose it in your code repository or to the public.

### 3. Configure the Application

#### Update Configuration

In your Flask application, update the configuration to include your YouTube API key:

```python
# Inside run.py
api_key = 'YOUR_API_KEY'
```

### 4. Run the Application

Now you're ready to run the Flask application:

```bash
python run.py
```

Visit `http://localhost:5000` in your web browser to see the application in action.

## Usage

- The application will prompt users to input their topic and knowledge level.
- Based on the input, it will fetch and display recommended YouTube videos.
- Users can click on the video thumbnails to watch the recommended videos.

## Contributing

Contributions are welcome! If you have any improvements or feature suggestions, please submit a pull request.

## License

This project is licensed under the MIT License
