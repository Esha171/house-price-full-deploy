# 🏠 House Price Prediction - Full Stack ML Deployment

A complete end-to-end machine learning deployment project that predicts house prices using a trained ML model. The project features a **FastAPI backend**, **Streamlit frontend**, **Docker containerization**, and **AWS ECS Fargate deployment** with automated CI/CD.

[![Deploy to Amazon ECS](https://github.com/Esha171/house-price-full-deploy/actions/workflows/docker-deploy.yml/badge.svg)](https://github.com/Esha171/house-price-full-deploy/actions/workflows/docker-deploy.yml)

## 📋 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Local Development Setup](#-local-development-setup)
- [API Documentation](#-api-documentation)
- [Streamlit Frontend](#-streamlit-frontend)
- [Docker Deployment](#-docker-deployment)
- [AWS ECS Deployment](#-aws-ecs-deployment)
- [CI/CD Pipeline](#-cicd-pipeline)
- [Model Information](#-model-information)
- [Contributing](#-contributing)
- [License](#-license)

## 🚀 Features

- **FastAPI Backend**: High-performance REST API for house price predictions
- **Streamlit Frontend**: Interactive web interface for easy predictions
- **ML Model**: Pre-trained scikit-learn model with MLflow tracking
- **Dockerized**: Fully containerized application for consistent deployment
- **AWS ECS Fargate**: Serverless container deployment on AWS
- **CI/CD**: Automated deployment pipeline using GitHub Actions
- **CloudWatch Logging**: Comprehensive logging and monitoring
- **Health Checks**: Built-in health check endpoints
- **Input Validation**: Pydantic models for request validation

## 🏗 Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         GitHub Actions                       │
│                     (CI/CD Pipeline)                         │
└───────────────────┬─────────────────────────────────────────┘
                    │
                    ├─► Build Docker Image
                    ├─► Push to Docker Hub
                    └─► Deploy to AWS ECS
                           │
        ┌──────────────────┴──────────────────┐
        │       AWS ECS Fargate Cluster       │
        │                                      │
        │  ┌────────────────────────────────┐ │
        │  │   ML API Container (Port 8000) │ │
        │  │   - FastAPI                    │ │
        │  │   - best_model.pkl             │ │
        │  └────────────────────────────────┘ │
        │                                      │
        │  ┌────────────────────────────────┐ │
        │  │ Streamlit Frontend (Port 8501) │ │
        │  │   - Interactive UI             │ │
        │  └────────────────────────────────┘ │
        │                                      │
        └──────────────────────────────────────┘
                    │
                    ▼
        ┌──────────────────────┐
        │  CloudWatch Logs     │
        └──────────────────────┘
```

## 📦 Tech Stack

### Backend
- **Python 3.9**: Core programming language
- **FastAPI**: Modern web framework for building APIs
- **Uvicorn**: ASGI server for FastAPI
- **Pydantic**: Data validation using Python type annotations
- **scikit-learn 1.5.2**: Machine learning model
- **MLflow**: Model tracking and management
- **CloudPickle**: Model serialization

### Frontend
- **Streamlit**: Interactive web application framework
- **streamlit-lottie**: Animations for enhanced UI

### DevOps & Deployment
- **Docker**: Containerization platform
- **Docker Hub**: Container registry
- **AWS ECS Fargate**: Serverless container orchestration
- **GitHub Actions**: CI/CD automation
- **CloudWatch Logs**: Application monitoring and logging

## 📁 Project Structure

```
house-price-full-deploy/
│
├── ml_api_deploy/              # Backend API service
│   ├── main.py                 # FastAPI application
│   ├── best_model.pkl          # Trained ML model
│   ├── Dockerfile              # Backend container configuration
│   └── requirements.txt        # Backend dependencies
│
├── streamlit-frontend/         # Frontend web interface
│   ├── streamlit_app.py        # Streamlit application
│   ├── Dockerfile              # Frontend container configuration
│   └── requirements.txt        # Frontend dependencies
│
├── .github/
│   └── workflows/
│       └── docker-deploy.yml   # CI/CD pipeline configuration
│
├── ecs-task-def.json           # ECS task definition
├── Dockerfile                  # Root Dockerfile
├── requirements.txt            # Root dependencies
└── README.md                   # Project documentation
```

## 🔧 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.9+**: [Download Python](https://www.python.org/downloads/)
- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Git**: [Install Git](https://git-scm.com/downloads)
- **AWS Account**: (Optional, for deployment)
- **Docker Hub Account**: (Optional, for deployment)

## 💻 Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Esha171/house-price-full-deploy.git
cd house-price-full-deploy
```

### 2. Set Up Backend API

```bash
# Navigate to backend directory
cd ml_api_deploy

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the API
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at `http://localhost:8000`

### 3. Set Up Streamlit Frontend

```bash
# Navigate to frontend directory
cd streamlit-frontend

# Create virtual environment (if not already created)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Update API endpoint in streamlit_app.py if running locally
# Change the URL to: http://localhost:8000/predict

# Run Streamlit
streamlit run streamlit_app.py
```

The frontend will be available at `http://localhost:8501`

## 📡 API Documentation

### Base URL
- **Local**: `http://localhost:8000`
- **Production**: `http://13.232.54.117:8000`

### Endpoints

#### 1. Welcome Route
```http
GET /
```

**Response:**
```json
{
  "message": "Welcome to the House Price Prediction API 🏠"
}
```

#### 2. Health Check
```http
GET /health
```

**Response:**
```json
{
  "status": "API is running 🚀"
}
```

#### 3. Predict House Price
```http
POST /predict
Content-Type: application/json
```

**Request Body:**
```json
{
  "area": 5000,
  "bedrooms": 3,
  "bathrooms": 2,
  "stories": 2,
  "mainroad": 1,
  "guestroom": 0,
  "basement": 1,
  "hotwaterheating": 0,
  "airconditioning": 1,
  "parking": 1,
  "prefarea": 0,
  "furnishingstatus": 1
}
```

**Request Parameters:**

| Parameter | Type | Description | Values |
|-----------|------|-------------|--------|
| `area` | int | Area in square feet | > 0 |
| `bedrooms` | int | Number of bedrooms | 1-10 |
| `bathrooms` | int | Number of bathrooms | 1-10 |
| `stories` | int | Number of stories | 1-4 |
| `mainroad` | int | Located on main road | 0 (No), 1 (Yes) |
| `guestroom` | int | Has guest room | 0 (No), 1 (Yes) |
| `basement` | int | Has basement | 0 (No), 1 (Yes) |
| `hotwaterheating` | int | Hot water heating | 0 (No), 1 (Yes) |
| `airconditioning` | int | Air conditioning | 0 (No), 1 (Yes) |
| `parking` | int | Parking spaces | 0-5 |
| `prefarea` | int | Preferred area | 0 (No), 1 (Yes) |
| `furnishingstatus` | int | Furnishing status | 0 (Unfurnished), 1 (Semi-Furnished), 2 (Furnished) |

**Response:**
```json
{
  "predicted_price": 4500000.0
}
```

### cURL Examples

**Health Check:**
```bash
curl http://localhost:8000/health
```

**Prediction:**
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "area": 5000,
    "bedrooms": 3,
    "bathrooms": 2,
    "stories": 2,
    "mainroad": 1,
    "guestroom": 0,
    "basement": 1,
    "hotwaterheating": 0,
    "airconditioning": 1,
    "parking": 1,
    "prefarea": 0,
    "furnishingstatus": 1
  }'
```

### Interactive API Documentation

FastAPI provides automatic interactive documentation:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🎨 Streamlit Frontend

The Streamlit frontend provides an intuitive interface for making predictions without writing code.

### Features

- **Interactive Form**: User-friendly input fields with sliders and radio buttons
- **Real-time Predictions**: Instant results from the backend API
- **Responsive Design**: Clean and modern UI with custom styling
- **Input Validation**: Client-side validation before API calls
- **Error Handling**: Graceful error messages for connection issues

### Usage

1. Open the Streamlit app in your browser (`http://localhost:8501`)
2. Fill in the house details using the form
3. Click "🔍 Predict Price" to get the estimated house price
4. View the predicted price displayed in Indian Rupees (₹)

## 🐳 Docker Deployment

### Build and Run Backend API

```bash
cd ml_api_deploy
docker build -t house-price-api .
docker run -p 8000:8000 house-price-api
```

### Build and Run Streamlit Frontend

```bash
cd streamlit-frontend
docker build -t house-price-frontend .
docker run -p 8501:8501 house-price-frontend
```

### Using Docker Compose (Alternative)

Create a `docker-compose.yml` file:

```yaml
version: '3.8'

services:
  api:
    build: ./ml_api_deploy
    ports:
      - "8000:8000"
    
  frontend:
    build: ./streamlit-frontend
    ports:
      - "8501:8501"
    depends_on:
      - api
```

Run with:
```bash
docker-compose up -d
```

## ☁️ AWS ECS Deployment

### Prerequisites

1. **AWS Account**: Create an account at [AWS](https://aws.amazon.com/)
2. **AWS CLI**: Install and configure AWS CLI
3. **Docker Hub Account**: For storing Docker images

### Setup Steps

#### 1. Configure AWS Credentials

```bash
aws configure
```

Enter your:
- AWS Access Key ID
- AWS Secret Access Key
- Default region (e.g., `ap-south-1`)
- Output format (e.g., `json`)

#### 2. Create ECR Repository or Use Docker Hub

```bash
# Option 1: Create ECR repository
aws ecr create-repository --repository-name house-price-app --region ap-south-1

# Option 2: Use Docker Hub (already configured in this project)
docker login
```

#### 3. Create ECS Cluster

```bash
aws ecs create-cluster --cluster-name house-price-cluster --region ap-south-1
```

#### 4. Create CloudWatch Log Group

```bash
aws logs create-log-group --log-group-name /ecs/house-price-logs --region ap-south-1
```

#### 5. Create ECS Task Definition

The task definition is already configured in `ecs-task-def.json`. Register it:

```bash
aws ecs register-task-definition --cli-input-json file://ecs-task-def.json
```

#### 6. Create ECS Service

```bash
aws ecs create-service \
  --cluster house-price-cluster \
  --service-name house-price-service \
  --task-definition house-price-task \
  --desired-count 1 \
  --launch-type FARGATE \
  --network-configuration "awsvpcConfiguration={subnets=[subnet-xxxxx],securityGroups=[sg-xxxxx],assignPublicIp=ENABLED}" \
  --region ap-south-1
```

#### 7. Configure Security Group

Ensure your security group allows:
- Port 8000 (API)
- Port 8501 (Streamlit)

## 🔄 CI/CD Pipeline

This project uses GitHub Actions for continuous deployment.

### Workflow Overview

The deployment pipeline (`.github/workflows/docker-deploy.yml`) automatically:

1. **Triggers**: On every push to the `main` branch
2. **Checkout**: Retrieves the latest code
3. **Docker Login**: Authenticates with Docker Hub
4. **Build**: Creates Docker image
5. **Push**: Uploads image to Docker Hub
6. **AWS Configure**: Sets up AWS credentials
7. **Deploy**: Updates ECS service with new task definition

### Required Secrets

Configure these secrets in your GitHub repository settings:

| Secret Name | Description |
|-------------|-------------|
| `DOCKER_USERNAME` | Docker Hub username |
| `DOCKER_PASSWORD` | Docker Hub password or access token |
| `AWS_ACCESS_KEY_ID` | AWS access key |
| `AWS_SECRET_ACCESS_KEY` | AWS secret key |
| `ECS_CLUSTER_NAME` | Name of ECS cluster |

### Setting Up Secrets

1. Go to repository Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Add each secret with its corresponding value

## 🤖 Model Information

### Model Details

- **Algorithm**: Scikit-learn based regression model
- **Input Features**: 12 features (area, bedrooms, bathrooms, etc.)
- **Output**: Predicted house price in Indian Rupees
- **Serialization**: CloudPickle for model persistence
- **Tracking**: MLflow for experiment tracking

### Model Features

The model uses the following features for prediction:

1. **area**: Total area of the house in square feet
2. **bedrooms**: Number of bedrooms
3. **bathrooms**: Number of bathrooms
4. **stories**: Number of floors/stories
5. **mainroad**: Whether on main road (binary)
6. **guestroom**: Guest room availability (binary)
7. **basement**: Basement availability (binary)
8. **hotwaterheating**: Hot water heating system (binary)
9. **airconditioning**: Air conditioning availability (binary)
10. **parking**: Number of parking spaces
11. **prefarea**: Located in preferred area (binary)
12. **furnishingstatus**: Furnishing level (0-2)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a new branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Add docstrings to new functions and classes
- Update tests for new features
- Update documentation as needed

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 📧 Contact

For questions or feedback:

- **GitHub**: [@Esha171](https://github.com/Esha171)
- **Repository**: [house-price-full-deploy](https://github.com/Esha171/house-price-full-deploy)

## 🙏 Acknowledgments

- FastAPI for the excellent web framework
- Streamlit for the interactive UI framework
- AWS for cloud infrastructure
- Docker for containerization technology
- GitHub Actions for CI/CD capabilities

---

**Made with ❤️ by Esha171**

⭐ Star this repository if you find it helpful!
