# Test Data Generator

A modern, web-based test data generator built with Python (FastAPI) and vanilla JavaScript. Generate realistic test data for development, testing, and seeding databases.

![Test Data Generator](https://img.shields.io/badge/Python-FastAPI-009688?style=for-the-badge&logo=fastapi)
![Test Data Generator](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=for-the-badge&logo=javascript)

## ✨ Features

- **Modern Dark UI** - Beautiful dark theme with smooth animations
- **Real-time Generation** - Generate data instantly as you configure
- **20+ Data Types** - Covers identifiers, contact info, financial data, networks, and more
- **Export Options** - Copy raw data, JSON, or CSV format
- **Cross-Platform** - Works on Windows, macOS, and Linux
- **Self-Hosted** - Run locally or deploy anywhere

## 🚀 Quick Start

### Prerequisites

- Python 3.8+ 
- pip or poetry

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/test-data-generator.git
cd test-data-generator

# Install dependencies
pip install fastapi uvicorn jinja2 python-multipart

# Or use the provided requirements.txt
pip install -r requirements.txt
```

### Running the Application

```bash
# Start the server
python main.py

# Or with uvicorn directly
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

Open your browser and navigate to:
```
http://127.0.0.1:8000
```

## 📋 Supported Data Types

### 🔐 Identifiers
| Type | Description | Options |
|------|-------------|---------|
| UUID | Standard UUID v4 format | Prefix/Suffix support |
| IMEI | Device IMEI numbers | Brand, Valid checksum |
| MAC Address | Network MAC addresses | Uppercase, Separator (:/-/.) |

### 👤 Contact & Identity
| Type | Description | Options |
|------|-------------|---------|
| Name | Person names | Starts/Ends with filter |
| Email | Email addresses | Domain, Extension (.com/.org/.net/.io) |
| Phone | Phone numbers | Country code, Include code |
| Address | Street addresses | Country filter |
| Country | Country names | Starts with filter |
| City | City names | Country filter |
| ZIP Code | Postal codes | Country, Range (From/To) |

### 💳 Financial & Sensitive
| Type | Description | Options |
|------|-------------|---------|
| Credit Card | Valid credit card numbers | Visa/Mastercard/AmEx, Valid/Invalid |
| SSN | Social Security Numbers | US/UK/Random |
| Barcode | EAN-13 barcodes | Numeric only, Length (8-20) |
| ISBN | Book ISBN numbers | ISBN-10 / ISBN-13 format |

### 🌐 Network & Web
| Type | Description | Options |
|------|-------------|---------|
| IP Address | IPv4 or IPv6 | Version selection |
| URL | Website URLs | Domain, Extension, Protocol |

### 📅 Time & Text
| Type | Description | Options |
|------|-------------|---------|
| DateTime | ISO 8601 timestamps | Date, Time, Timezone (Z suffix) |
| Sentence | Random sentences | Grammatically valid |
| Paragraph | Multi-sentence paragraphs | Min/Max sentences |

### 🎨 Colors
| Type | Description | Options |
|------|-------------|---------|
| Hex Color | HEX color codes | Uppercase/Lowercase |
| RGB Color | RGB color values | Min/Max value range |

### 🏢 Work & Organization
| Type | Description | Options |
|------|-------------|---------|
| Company | Company names | Starts with filter |
| Job Title | Professional titles | Seniority level |

## 🖥️ API Reference

### Endpoints

#### Get All Categories
```http
GET /api/categories
```

#### Get Type Configuration
```http
GET /api/types/{type_id}
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

### Example Response
```json
{
    "data": [
        "user_a1b2c3d4-e5f6-7890-abcd-ef1234567890_test",
        "user_f6e5d4c3-b2a1-0987-fedc-ba0987654321_test"
    ],
    "message": "🎉 Boom! Data incoming!"
}
```

## 🛠️ Tech Stack

- **Backend**: Python 3.8+, FastAPI, Uvicorn
- **Frontend**: Vanilla JavaScript (ES6+), HTML5, CSS3
- **Styling**: Custom dark theme with CSS animations
- **Real-time**: Fetch API for async requests

## 📁 Project Structure

```
test-data-generator/
├── main.py           # FastAPI application & data generators
├── index.html        # Single-page application UI
├── server.js        # Alternative Node.js server
├── requirements.txt  # Python dependencies
├── README.md        # This file
└── plans/           # Development planning docs
```

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
