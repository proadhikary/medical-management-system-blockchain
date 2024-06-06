# Medical Management System Blockchain
Complete codebase for a Blockchain-based medical management system is a substantial task. This project is a Blockchain-based medical management system designed to enhance data security, patient privacy, interoperability, and administrative efficiency in the healthcare sector, particularly tailored for the Indian healthcare context. The system leverages Raspberry Pi devices and Linux-based distributions for cost-effective and scalable implementation.

## Features

- Immutable Ledger: Securely records and prevents unauthorized alterations of patient data.
- Enhanced Privacy: Encrypts patient data, ensuring access only to authorized personnel.
- Interoperability: Facilitates seamless data sharing between healthcare providers.
- Transparency and Trust: Provides a transparent and auditable record of all transactions.
- Smart Contracts: Automates processes such as patient consent management and insurance claims processing.
- Patient-Centric Access Control: Empowers patients with control over their medical records.


## Prerequisites

- Raspberry Pi devices with Raspbian OS
- Python 3.8+
- Flask
- Flask-SQLAlchemy
- paho-mqtt
- Adafruit-DHT

## Installation

### 1. **Clone the repository**
   ```bash
   git clone https://github.com/proadhikary/medical-management-system-blockchain.git
   cd medical-management-system-blockchain
  ```

### 2. **Set up the virtual environment**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. **Install the required dependencies**
  ```bash
  pip install -r requirements.txt

  ```

### 4. **Configure environment variables**
Create a `.env` file in the root directory with the following content:
  ```bash
  SECRET_KEY=your_secret_key
  DATABASE_URL=sqlite:///app.db
  ```

### 4. **Initialize the database**
  ```bash
  flask db init
  flask db migrate -m "Initial migration."
  flask db upgrade
  ```

## Running the Application

### 1. **Start the Flask server**
   ```bash
    python run.py
  ```
### 2. **Access the application**
Open your web browser and navigate to http://localhost:5000.


## Project Components
### Blockchain Module
  - blockchain.py: Manages the blockchain, including block creation and validation.
  - block.py: Defines the Block class with methods for hashing and validating transactions.
  - transaction.py: Defines the Transaction class for managing transactions within blocks.
  - smart_contract.py: Implements smart contracts for automating healthcare processes.

### Data Module
  - data_collector.py: Collects real-time data from IoT sensors.
  - data_transmitter.py: Transmits collected data to the central server using MQTT protocol.
  - sensor.py: Interfaces with sensors to read data.

### Models
  - patient.py: Defines the Patient class and methods for managing patient records.
  - doctor.py: Defines the Doctor class and methods for managing patient care.
  - record.py: Defines the MedicalRecord class for handling medical records.
  - user.py: Defines the User class for user authentication and management.
  - healthcare_provider.py: Manages healthcare providers, doctors, and patients.
### Server
  - app.py: Initializes and configures the Flask application.
  - database.py: Sets up and manages the database connections.
  - routes.py: Defines the API routes for interacting with the system.

### Templates and Static Files
  - templates/: Contains HTML templates for the web application.
  - static/: Contains CSS and JavaScript files for the web application.


## Testing
Run the test suite by:
```bash
pytest
```

## Future Work
  - Address scalability issues to handle increasing volumes of healthcare data.
  - Enhance smart contract functionalities for more comprehensive automation.
  - Improve integration with IoT devices for better real-time data collection.
  - Conduct extensive pilot programs to gather feedback and refine the system.
  - Collaborate with government agencies and private healthcare providers to ensure regulatory compliance and foster widespread adoption.


