# RUSA ACP Brevet Control Time Calculator

## Overview
This web application serves as a specialized tool for calculating and storing control times in accordance with RUSA (Randonneurs USA) and ACP (Audax Club Parisien) brevet guidelines. It replicates the functionality of the official RUSA ACP control time calculator, enabling users to enter distances and promptly receive both opening and closing times for controls in long-distance cycling events. Implemented using Flask, Ajax, MongoDB, and REST, this application is a testament to modern, efficient web development practices.

## Author Information
- **Name:** Deem Alowairdhi
- **QU ID:** 411214706
- **Email:** [411214706@qu.edu.sa](mailto:411214706@qu.edu.sa)

## Architecture

### Docker Compose
The project employs Docker Compose to facilitate the streamlined deployment of its multi-container Docker applications. The `docker-compose.yml` file meticulously outlines the configuration of service components, notably using the following ports:
1. Control Time Calculator - Port 5000
2. API Service - Port 5001
3. Website Service - Port 5002

### 'api' Folder
The 'api' folder is the backbone of the application, containing Python scripts and Flask routes. It is responsible for the handling of API requests and database interactions, ensuring efficient data processing and storage.

### 'web' Folder
The 'web' folder is the face of the application, comprising front-end components like HTML templates and CSS files. It fetches data through requests to the API service, presenting a seamless user experience.

## Features
- **Control Time Calculation:** This core feature allows for the input of distances in kilometers or miles, subsequently calculating the corresponding opening and closing times as per ACP regulations.
- **Data Storage:** Utilizing MongoDB, the application adeptly manages control data, including location, distance, and start time.
- **Versatile API Formats:** The application offers data display in both JSON and CSV formats, catering to diverse user needs.
- **User Interface:** The application boasts an intuitive and responsive interface, simplifying the process of data input and visualization.

## Technology Stack
- **Frontend:** Crafted with HTML, JavaScript (including jQuery), and Bootstrap.
- **Backend:** Powered by Python and the Flask framework.
- **Database:** Leveraging MongoDB for robust data management.

## Frontend-Backend Communication
- The application utilizes Ajax for seamless asynchronous data exchange between the frontend and the Flask backend.
- Flask adeptly manages control time calculation requests and MongoDB interactions, ensuring data integrity and responsiveness.
- RESTful endpoints facilitate efficient communication between the API and web services, ensuring a cohesive and functional application.

## Building the Project
1. **Project Directory:**
   Navigate to the project directory using:
   ```bash
   cd path/to/project-6-brevets-db/brevets
   ```
2. **Environment Variables:**
   These are configured within `Dockerfile` and `docker-compose.yml`, establishing the necessary settings for the application:
   - `docker-compose.yml`: Defines services, ports, volumes, and pertinent environment variables.
   - `Dockerfile`: Sets up the Python environment and oversees the installation of dependencies.

3. **Build Docker Images:**
   Initiate the building of Docker images with:
   ```bash
   docker-compose up --build
   ```

4. **Access the Application:**
   Upon successful building and starting of the application, the RUSA ACP control time calculator and its API are accessible via several endpoints, each offering distinct functionalities and data formats.

   ### RUSA ACP Control Time Calculator
   - **Web Interface:** `http://localhost:5000`
     - Access the main user interface for inputting distances and calculating control times.

   ### API Endpoints
   The API offers multiple endpoints to retrieve control times in both JSON and CSV formats. These endpoints provide flexibility in accessing data for open, close, or all control times.

   - **All Control Times:**
     - JSON Format: `http://localhost:5001/listAll` or `http://localhost:5001/listAll/json`
     - CSV Format: `http://localhost:5001/listAll/csv`

   - **Open Control Times Only:**
     - JSON Format: `http://localhost:5001/listOpenOnly` or `http://localhost:5001/listOpenOnly/json`
     - CSV Format: `http://localhost:5001/listOpenOnly/csv`
     - Query Parameter: Add `?top=k` (where `k` is the number of top records desired) to retrieve a specific number of top open control times, e.g., `http://localhost:5001/listOpenOnly/csv?top=2`.

   - **Close Control Times Only:**
     - JSON Format: `http://localhost:5001/listCloseOnly` or `http://localhost:5001/listCloseOnly/json`
     - CSV Format: `http://localhost:5001/listCloseOnly/csv`
     - Query Parameter: Add `?top=k` (where `k` is the number of top records desired) to retrieve a specific number of top close control times, e.g., `http://localhost:5001/listCloseOnly/csv?top=2`.

5. **Manage the Application:**
   - To stop the application, use `docker-compose down`.
   - For diagnostics, `docker-compose logs` provides valuable insights.

6. **Updates and Changes:**
   To implement updates or changes, rebuild the Docker images and restart the containers to reflect the modifications.


## Testing
[![Video Thumbnail](https://img.youtube.com/vi/I8kQC1xZZ6U/maxresdefault.jpg)](https://youtu.be/I8kQC1xZZ6U)

