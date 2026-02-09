# Test Data Generator

A modern, web-based test data generator built with Python FastAPI. Generate realistic test data for development, testing, and seeding databases.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Usage](#usage)
- [Data Types](#data-types)
- [API Reference](#api-reference)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Contributing](#contributing)
- [License](#license)

## About

Test Data Generator is a user-friendly tool designed to help developers, QA engineers, and testers generate realistic mock data quickly. It features a modern dark UI, real-time generation, and support for various data types commonly needed in software development.

## ✨ Features

- 🎨 **Modern Dark UI** - Beautiful dark theme with smooth animations and transitions
- ⚡ **Real-time Generation** - Generate data instantly as you configure options
- 📦 **20+ Data Types** - Covers identifiers, contact info, financial data, networks, and more
- 📋 **Export Options** - Copy raw data, JSON, or CSV format
- 🔧 **Configurable** - Fine-tune each data type with specific options
- 🌐 **Cross-Platform** - Works on Windows, macOS, and Linux
- 🚀 **Self-Hosted** - Run locally or deploy to your own server

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have:

- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** - Python package manager (comes with Python)

### Installation

Follow these steps to set up the project:

#### Step 1: Clone the Repository

```bash
# Open your terminal/command prompt
git clone https://github.com/iamragavendrans/test-data-generator.git
cd test-data-generator
```

#### Step 2: Create a Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

#### Step 3: Install Dependencies

```bash
# Install required packages
pip install fastapi uvicorn jinja2 python-multipart
```

#### Step 4: Start the Server

```bash
# Run the application
python main.py
```

You should see output similar to:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

#### Step 5: Open the Application

Open your web browser and navigate to:

```
http://127.0.0.1:8000
```

You should see the Test Data Generator UI.

## 💡 Usage

### Using the Web Interface

1. **Select a Category** - Click on a tab (Identifiers, Contact & Identity, Financial & Sensitive, etc.)
2. **Choose a Data Type** - Select from the left panel
3. **Configure Options** - Adjust settings in the right panel
4. **Generate** - Data is generated automatically or click the Generate button
5. **Export** - Click Copy Raw, JSON, or CSV to export

### Using the API

Generate data programmatically using the REST API:

```bash
# Generate 5 UUIDs
curl -X POST http://127.0.0.1:8000/api/generate \
  -H "Content-Type: application/json" \
  -d '{"type": "uuid", "count": 5}'
```

## 📦 Data Types

### 🔐 Identifiers

| Type | Description | Options |
|------|-------------|---------|
| UUID | Standard UUID v4 format | Prefix/Suffix support |
| IMEI | Device IMEI numbers | Brand (Apple/Samsung/Generic), Valid checksum |
| MAC Address | Network MAC addresses | Uppercase (True/False), Separator (:/-/./None) |

### 👤 Contact & Identity

| Type | Description | Options |
|------|-------------|---------|
| Name | Person names | Starts with (filter), Ends with (filter) |
| Email | Email addresses | Domain (custom), Extension (.com/.org/.net/.io/.test/.co) |
| Phone | Phone numbers | Country (40+ countries), Include country code |
| Address | Street addresses | Country filter (40+ countries) |
| Country | Country names | Starts with (filter) |
| City | City names | Country filter |
| ZIP Code | Postal codes | Country, Range (From/To numbers) |

### 💳 Financial & Sensitive

| Type | Description | Options |
|------|-------------|---------|
| Credit Card | Valid credit card numbers | Card Type (Visa/Mastercard/AmEx/Random), Valid/Invalid |
| SSN | Social Security Numbers | Country (US/UK/Random) |
| Barcode | EAN-13 barcodes | Numeric only (True/False), Length (8-20) |
| ISBN | Book ISBN numbers | Format (ISBN-10 / ISBN-13) |

### 🌐 Network & Web

| Type | Description | Options |
|------|-------------|---------|
| IP Address | IPv4 or IPv6 addresses | Version (IPv4/IPv6) |
| URL | Website URLs | Domain (custom), Extension, Protocol (https/http) |

### 📅 Time & Text

| Type | Description | Options |
|------|-------------|---------|
| DateTime | ISO 8601 timestamps | Date (True/False), Time (True/False), Timezone Z (True/False) |
| Sentence | Random sentences | Grammatically valid |
| Paragraph | Multi-sentence paragraphs | Min sentences (1-10), Max sentences (1-20) |

### 🎨 Colors

| Type | Description | Options |
|------|-------------|---------|
| Hex Color | HEX color codes | Uppercase (True/False) |
| RGB Color | RGB color values | Min value (0-255), Max value (0-255) |

### 🏢 Work & Organization

| Type | Description | Options |
|------|-------------|---------|
| Company | Company names | Starts with (filter) |
| Job Title | Professional titles | Seniority (Any/Junior/Senior/Lead) |

## 🔌 API Reference

### Endpoints

#### Get All Categories

```http
GET /api/categories
```

**Response:**

```json
[
  {
    "id": "identifiers",
    "name": "Identifiers",
    "icon": "🔐",
    "types": [...]
  }
]
```

#### Get Type Configuration

```http
GET /api/types/{type_id}
```

**Example:**

```http
GET /api/types/uuid
```

**Response:**

```json
{
  "type": "uuid",
  "name": "UUID",
  "icon": "🔑",
  "category": "identifiers",
  "supports_prefix_suffix": true,
  "options": [...]
}
```

#### Generate Data

```http
POST /api/generate
Content-Type: application/json

{
  "type": "uuid",
  "count": 10,
  "prefix": "user_",
  "suffix": "_test"
}
```

**Response:**

```json
{
  "data": [
    "user_a1b2c3d4-e5f6-7890-abcd-ef1234567890_test",
    "user_f6e5d4c3-b2a1-0987-fedc-ba0987654321_test"
  ],
  "message": "🎉 Boom! Data incoming!"
}
```

## 📁 Project Structure

```
test-data-generator/
├── main.py              # FastAPI application & data generators
├── index.html           # Single-page application UI
├── server.js            # Alternative Node.js server
├── requirements.txt     # Python dependencies
├── README.md            # This file
└── plans/               # Development planning documents
```

## 🛠️ Tech Stack

- **Backend**: Python 3.8+, FastAPI, Uvicorn
- **Frontend**: Vanilla JavaScript (ES6+), HTML5, CSS3
- **Styling**: Custom CSS with animations, dark theme
- **Real-time**: Fetch API for async requests

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the amazing web framework
- [Uvicorn](https://www.uvicorn.org/) for the ASGI server
- All contributors who have helped improve this project

---

⭐ If this project helped you, please consider giving it a star!
