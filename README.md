# IR-Cs-429_project_sunkari.Bhavana

PROJECT REPORT
on
TextQuest





Illinois Institute of Technology
CS 429 – Information Retrieval
Professor: Jawahar Panchal





                               SUBMITTED BY 
                              Sunkari Bhavana
                                A20543227         
	Abstract:
Development Summary:
TextQuest is a web-based application designed to optimize text data retrieval across large datasets using natural language processing (NLP). Developed with Flask and Vue.js, the application integrates TF-IDF and cosine similarity to enhance search accuracy and relevance.

Objectives:
The primary goal of TextQuest is to provide a fast, secure, and intuitive search platform for users needing to access and analyze large volumes of text efficiently. It aims to improve research efficiency in academic, corporate, and research settings.

Next Steps:
Moving forward, the project will focus on:
- Enhancing the AI algorithms for better accuracy and speed.
- Implementing additional security measures and compliance checks.
- Expanding the system’s scalability to support larger datasets and more concurrent users.
- Conducting extensive user testing to refine the interface and user experience.

TextQuest is poised to become an essential tool for data-driven insights, offering powerful search capabilities and user-friendly features tailored to the needs of diverse users.
 
	Overview:
Solution Outline:
TextQuest leverages advanced natural language processing (NLP) to enhance information retrieval from large text datasets, catering to academic, corporate, and research sectors.

Relevant Literature:
The system utilizes TF-IDF for indexing and cosine similarity for query processing, established techniques documented in core texts like "Introduction to Information Retrieval" by Manning et al.

Proposed System:
TextQuest combines the Flask web framework and Vue.js to deliver a secure, responsive, and user-friendly interface. It uses Flask-Talisman for HTTPS enforcement, ensuring secure data transfers.

System Features:
User-Friendly Interface: Simplifies query input and displays real-time search results.
Secure and Scalable: Supports HTTPS and scales effectively to handle multiple simultaneous user requests.
Efficient Search: Employs TF-IDF and cosine similarity for quick and relevant results.

 
Deployment Strategy:
Designed for easy integration, TextQuest is ideal for settings requiring fast access to extensive text data, such as universities, research facilities, and businesses needing efficient search capabilities.

	Design: 
System Capabilities:
TextQuest is engineered to efficiently handle extensive text searches with high accuracy and speed. Its core capabilities are rooted in utilizing advanced NLP techniques such as TF-IDF for text indexing and cosine similarity for determining the relevance of search results. The system is designed to be robust, supporting multiple simultaneous user requests without performance degradation.

Interactions:
The application features a clean, intuitive user interface developed with Vue.js, which facilitates easy submission of search queries and real-time display of search results. Users interact with the system through a simple web interface that provides quick access to document retrieval functionalities.

Integration:
TextQuest integrates seamlessly with existing data management systems and infrastructures. It is designed to operate over secure HTTP (HTTPS), ensuring data integrity and security in all communications. This integration capability makes it suitable for deployment in a variety of environments, including cloud-based platforms and local servers, allowing for flexibility in how and where it is deployed.
In summary, TextQuest combines sophisticated search technology with user-centered design to provide a seamless and efficient experience for accessing large volumes of text data.

	Architecture:
Software Components:
TextQuest consists of
1. Backend: Powered by Flask, it manages query processing and implements NLP features like TF-IDF and cosine similarity for document indexing and relevance scoring.
2. Frontend: Developed with Vue.js, it provides a dynamic user interface for real-time search operations and result display.
3. Security: Flask-Talisman enforces HTTPS, securing data transmissions and protecting against web vulnerabilities.

Interfaces:
The system features a RESTful API, facilitating backend to frontend communication via JSON-formatted data, supporting straightforward integration with external systems.

Implementation:
- Backend: Utilizes Python and Scikit-learn for NLP algorithm implementation.
 
- Frontend: Vue.js ensures a responsive, AJAX-driven interface.
 
- Security: Configured in Flask, Talisman adds critical HTTP security headers.
This streamlined architecture ensures that TextQuest is secure, responsive, and efficient, capable of integrating smoothly into various operational environments.           

	Operation:
Software Commands:
- Start the Server: Launch the Flask application using the command:
  ```bash
  python3 search_api.py
  ```
 This starts the Flask server, typically listening on `http://localhost:5000`, ready to handle incoming search queries.

Inputs:
- Search Queries: Users input their search queries through the web interface. These queries are sent to the backend via AJAX calls from the frontend.
- API Requests: The RESTful API accepts POST requests at the `/search` endpoint, where the payload includes the `query` string and an optional `top_k` parameter to specify the number of top results returned.

Installation:
1. Environment Setup:
- Ensure Python 3 is installed on your system.
- Set up a virtual environment:
```bash
     python3 -m venv venv
     source venv/bin/activate  # On Unix/Linux
     venv\Scripts\activate  # On Windows
     ```

2. Dependency Installation:
- Install required Python packages:
```bash
pip install flask numpy scikit-learn flask-talisman gunicorn
```

3. Application Setup:
   - Place the application files in your project directory.
   - Ensure the `search_api.py` file is at the root of your directory structure for easy access.
   - Prepare your `tfidf_model.pkl` and data files (`output.json`) in the designated data directory.

4. Running the Application:
   - Navigate to the application directory.
   - Run the Flask application using:
     ```bash
     python3 search_api.py
     ```
 
5. Accessing the Application:
   - Open a web browser.
   - Visit `http://localhost:5000` to interact with the application through the provided web interface.

This operational guide outlines how to start, interact with, and manage the TextQuest application, providing a seamless user experience from installation to daily usage.     

	Conclusion: 
Success/Failure Results:
TextQuest effectively enhances text data retrieval, praised for its responsiveness and user-friendly interface. Its use of advanced NLP techniques has markedly improved search precision.

Outputs:
Outputs include dynamically displayed search results, ranked by relevance, with features allowing detailed text reviews directly in the user interface.
 
Caveats/Cautions:
Data Sensitivity: Ensuring compliance with data protection regulations is crucial due to the sensitivity of processed data.
Performance and Scalability: Performance may vary with very large datasets or high user traffic, requiring scalability enhancements.
HTTPS Configuration: Proper certificate management is essential; incorrect setup can disrupt service.                      
Data Sources: TextQuest

Access Information:
- Links: TextQuest accesses data primarily through internal databases configured at installation. External data integrations are facilitated via RESTful API endpoints.
- Downloads: Users can access and download search results directly through the web interface, provided in commonly used formats such as PDF or plain text.
- Access Permissions: Access is controlled through user authentication to ensure data security and integrity, with different access levels depending on user roles and privileges.

This streamlined setup ensures secure and efficient data management and retrieval, catering to both casual users and data professionals.
Source Code: TextQuest

Listings and Documentation:
- The complete source code for TextQuest is hosted on a public GitHub repository, enabling collaboration and transparency.
- Comprehensive documentation covers installation, configuration, and usage guidelines, along with detailed API documentation for developers.
Dependencies (Open-Source):
- Flask: A lightweight WSGI web application framework used as the core for creating the web server.
- Vue.js: Handles the dynamic user interface on the client side.
- NumPy and Scikit-learn: Utilized for handling data processing and implementing machine learning algorithms like TF-IDF and cosine similarity.
- Flask-Talisman: Ensures security best practices by enforcing HTTPS.
- Gunicorn: Serves as the WSGI HTTP server for Unix-based systems, enhancing production deployment.

These tools and libraries are open-source, ensuring that TextQuest remains adaptable and up-to-date with the latest developments in technology and security standards.

	Bibliography:

1.	Flask. "Welcome to Flask — Flask Documentation (2.0.x)." Accessed April 22, 2024. https://flask.palletsprojects.com/en/2.0.x/.
2.	Vue.js. "Introduction — Vue.js." Accessed April 22, 2024. https://vuejs.org/v2/guide/.
3.	NumPy. "NumPy v1.21 Manual." Accessed April 22, 2024. https://numpy.org/doc/stable/.
4.	Scikit-learn. "scikit-learn: Machine Learning in Python — scikit-learn 0.24.2 documentation." Accessed April 22, 2024. https://scikit-learn.org/stable/.
5.	Flask-Talisman. "Flask-Talisman 0.8.1 documentation." Accessed April 22, 2024. https://pypi.org/project/Flask-Talisman/.
6.	Gunicorn. "Gunicorn - Python WSGI HTTP Server for UNIX." Accessed April 22, 2024. https://gunicorn.org/.        
