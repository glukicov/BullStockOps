# 🐂 📈 🔁 BullStockOps
![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge)
![uv Badge](https://img.shields.io/badge/uv-DE5FE9?logo=uv&logoColor=fff&style=for-the-badge)
![Docker Badge](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff&style=for-the-badge)
![React Badge](https://img.shields.io/badge/React-61DAFB?logo=react&logoColor=000&style=for-the-badge)
![TypeScript Badge](https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=fff&style=for-the-badge)
![Google Cloud Badge](https://img.shields.io/badge/Google%20Cloud-4285F4?logo=googlecloud&logoColor=fff&style=for-the-badge)
![Google Gemini Badge](https://img.shields.io/badge/Google%20Gemini-8E75B2?logo=googlegemini&logoColor=fff&style=for-the-badge)

Welcome to **BullStockOps**, a personal open-source project combining cutting-edge AI, financial analytics, and scalable software operations to revolutionize day trading.
<p align="center">
<img src="docs/bsops.png" width=500>
</p>

## Project Overview

**BullStockOps** is designed to empower traders with AI-driven insights and seamless trading operations. From stock price predictions to AI-assisted trade execution, this project provides a robust platform for experimentation and learning.

## MVP1 Goals
- ➡️ Display real-time stock prices in a web and iOS app.

### Features backlog
- 📊 Stock Market Data Integration: Access real-time and historical data through APIs (e.g., Alpha Vantage).
- 📈 Predictive Analytics: Build LSTM-based models to forecast stock prices.
- 🤖 AI-Assisted Trading: Develop AI agents for automated trading decisions.
- 📱 iOS App Development: Leverage Apple Core ML and MLX for offline and online ML features.

## Tech Stack
- Backend:	Python 3.13, FastAPI, Pydantic
- Frontend:	React & TypeScript (future)
- Mobile: Apple Core ML, MLX
- AI Models	GPT-4, Claude, Gemini

## Setup
1. Update or install [uv](https://docs.astral.sh/uv/) using
```shell
brew install uv
```
2. Install this project's dependencies and activate project's venv in your shell
```shell
uv sync
source .venv/bin/activate
```