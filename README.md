# 🏠 House Price Prediction API

This project deploys a **Machine Learning model** to predict house prices using **FastAPI**, **Docker**, and **AWS ECS Fargate**.

## 🚀 Features

- FastAPI-based REST API
- Predicts house price from structured input data
- Dockerized for easy deployment
- Deployed on AWS ECS using GitHub Actions (CI/CD)
- CloudWatch logging enabled for monitoring

## 📦 Tech Stack

- Python, FastAPI
- Docker
- GitHub Actions
- AWS ECS (Fargate)
- CloudWatch Logs

## 🔧 API Endpoints

| Method | Endpoint     | Description                  |
|--------|--------------|------------------------------|
| GET    | `/`          | Welcome route                |
| GET    | `/health`    | Health check route           |
| POST   | `/predict`   | Send features to get price   |

## 🧪 Example Request

```json
POST /predict
{
  "area": 1200,
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
📤 Deployment
Handled using GitHub Actions which:

Builds Docker image

Pushes it to Docker Hub

Deploys to AWS ECS Fargate

Feel free to contribute or fork! ⭐
