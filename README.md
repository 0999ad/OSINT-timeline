Here's the full `README.md` with the virtual environment setup steps included.

---

# OSINT Timeline Tool

The OSINT Timeline Tool is a Python-based application designed to help you create, manage, and visualize timelines for Open Source Intelligence (OSINT) investigations. The tool allows users to document events, link related entities, and visualize interactions over time through an intuitive web interface. You can also export the timelines and query results in various formats, including CSV, Excel, and PDF.

## Features
- **Web Interface**: Manage your timeline through a user-friendly web interface.
- **Timeline Management**: Create, load, and save timelines.
- **Entry Documentation**: Add detailed entries with date, time, location, involved entities, descriptions, and more.
- **File Uploads**: Add image and video files as part of your timeline entries.
- **Relational Visualization**: Generate interactive visualizations showing connections between entities and events.
- **Querying with Pagination**: Search and filter timeline entries with pagination for large datasets.
- **Export**: Export timelines or query results to CSV, Excel, and PDF formats.
- **Input Validation**: Validates URLs and uploaded files to ensure data integrity.

## Setup and Installation (Ubuntu)

### Prerequisites
- Python 3.7 or later
- `pip` (Python package installer)

### Virtual Environment Setup

To run the OSINT Timeline Tool in an isolated Python environment using `venv`, follow these steps:

1. **Install `venv` if Necessary**:
   If `venv` isn't installed on your system, install it with:

   ```bash
   sudo apt update
   sudo apt install python3-venv
   ```

2. **Create a Virtual Environment**:
   Navigate to the project directory and create a virtual environment. Replace `env` with your preferred environment name:

   ```bash
   cd osint-timeline-tool  # Navigate to the project folder
   python3 -m venv env     # Create a virtual environment named 'env'
   ```

3. **Activate the Virtual Environment**:
   After creating the virtual environment, activate it:

   ```bash
   source env/bin/activate
   ```

   You should see the virtual environment name (e.g., `(env)`) in your terminal prompt.

4. **Install Required Dependencies**:
   Use the `requirements.txt` file to install dependencies in the virtual environment:

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**:
   Once the dependencies are installed, start the Flask application:

   ```bash
   python osint_timeline_tool.py
   ```

6. **Access the Web Interface**:
   Open your web browser and go to `http://127.0.0.1:5000` to use the OSINT Timeline Tool.

### Deactivating and Reactivating the Virtual Environment

- **Deactivate the Virtual Environment**:
   When finished, deactivate the virtual environment by running:

   ```bash
   deactivate
   ```

- **Reactivate the Virtual Environment Later**:
   To work on the project again later, navigate back to the project folder and reactivate the environment:

   ```bash
   cd osint-timeline-tool
   source env/bin/activate
   ```

### Usage

- **Add New Entries**: Use the web form to add new events to your timeline. You can include images and videos by uploading supported file types.
- **Query Timeline**: Use the query form to filter timeline events based on date, time, entities, etc. The query results are paginated for better performance with large datasets.
- **Visualize Timeline**: Generate static and relational visualizations of your timeline data.
- **Export Data**: Export timeline data or query results in CSV, Excel, or PDF formats for reporting and sharing.

### Supported File Types

- **Images**: PNG, JPG, JPEG, GIF
- **Videos**: MP4, AVI, MOV

### Input Validation
- **URL Validation**: Ensures that only valid URLs are accepted in the "Source Link" field.
- **File Validation**: Only supported image and video file types can be uploaded.

## API Instructions (Coming Soon)

Future versions will include API support. Planned features:
- **POST** `/api/timeline`: Add new entries to the timeline via API.
- **GET** `/api/timeline`: Retrieve timeline data via API.
- **GET** `/api/query`: Query the timeline based on specific parameters via API.

## Screenshots

_Add screenshots to demonstrate the web interface. Replace these with your own screenshots._

![Add New Entry](screenshots/add_entry.png)
![Query Timeline](screenshots/query_timeline.png)

## Contributing
Contributions are welcome! Please open an issue or submit a pull request with any improvements or new features you'd like to see in the OSINT Timeline Tool.

## License
[Include your license information here.]

---

This updated `README.md` includes full instructions for setting up and running the OSINT Timeline Tool in a virtual environment. Let me know if you need any further updates or assistance!
