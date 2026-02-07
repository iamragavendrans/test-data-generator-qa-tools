"""
Test Data Generator - Comprehensive Fixes
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional
import random
import uuid
from datetime import datetime

app = FastAPI(title="Test Data Generator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Countries for phone/address
COUNTRIES = {
    "US": {"name": "United States", "code": "+1"},
    "GB": {"name": "United Kingdom", "code": "+44"},
    "IN": {"name": "India", "code": "+91"},
    "DE": {"name": "Germany", "code": "+49"},
    "FR": {"name": "France", "code": "+33"},
    "CA": {"name": "Canada", "code": "+1"},
    "AU": {"name": "Australia", "code": "+61"},
    "JP": {"name": "Japan", "code": "+81"},
    "BR": {"name": "Brazil", "code": "+55"},
    "IT": {"name": "Italy", "code": "+39"},
    "ES": {"name": "Spain", "code": "+34"},
    "MX": {"name": "Mexico", "code": "+52"},
    "KR": {"name": "South Korea", "code": "+82"},
    "CN": {"name": "China", "code": "+86"},
    "RU": {"name": "Russia", "code": "+7"},
    "NL": {"name": "Netherlands", "code": "+31"},
    "SE": {"name": "Sweden", "code": "+46"},
    "NO": {"name": "Norway", "code": "+47"},
    "DK": {"name": "Denmark", "code": "+45"},
    "FI": {"name": "Finland", "code": "+358"},
    "CH": {"name": "Switzerland", "code": "+41"},
    "AT": {"name": "Austria", "code": "+43"},
    "BE": {"name": "Belgium", "code": "+32"},
    "PT": {"name": "Portugal", "code": "+351"},
    "PL": {"name": "Poland", "code": "+48"},
    "CZ": {"name": "Czech Republic", "code": "+420"},
    "HU": {"name": "Hungary", "code": "+36"},
    "GR": {"name": "Greece", "code": "+30"},
    "TR": {"name": "Turkey", "code": "+90"},
    "ZA": {"name": "South Africa", "code": "+27"},
    "NZ": {"name": "New Zealand", "code": "+64"},
    "SG": {"name": "Singapore", "code": "+65"},
    "HK": {"name": "Hong Kong", "code": "+852"},
    "AE": {"name": "UAE", "code": "+971"},
    "SA": {"name": "Saudi Arabia", "code": "+966"},
    "IL": {"name": "Israel", "code": "+972"},
    "TH": {"name": "Thailand", "code": "+66"},
    "VN": {"name": "Vietnam", "code": "+84"},
    "PH": {"name": "Philippines", "code": "+63"},
    "ID": {"name": "Indonesia", "code": "+62"},
    "MY": {"name": "Malaysia", "code": "+60"},
    "AR": {"name": "Argentina", "code": "+54"},
    "CL": {"name": "Chile", "code": "+56"},
    "CO": {"name": "Colombia", "code": "+57"},
    "PE": {"name": "Peru", "code": "+51"},
    "EG": {"name": "Egypt", "code": "+20"},
    "NG": {"name": "Nigeria", "code": "+234"},
    "KE": {"name": "Kenya", "code": "+254"},
    "MA": {"name": "Morocco", "code": "+212"},
}

# IMEI Brands
IMEI_BRANDS = {
    "Apple": "35",
    "Samsung": "49",
    "Google": "49",
    "Huawei": "86",
    "Xiaomi": "86",
    "OnePlus": "86",
    "Sony": "35",
    "LG": "35",
    "Motorola": "35",
    "Nokia": "35",
}

# Credit Card Types with logos
CREDIT_CARD_TYPES = {
    "Visa": {"prefix": "4", "length": 16, "logo": "💳"},
    "Mastercard": {"prefix": str(random.randint(51, 55)), "length": 16, "logo": "💳"},
    "American Express": {"prefix": "37", "length": 15, "logo": "💳"},
    "Discover": {"prefix": "6011", "length": 16, "logo": "💳"},
    "JCB": {"prefix": "3528", "length": 16, "logo": "💳"},
    "Diners Club": {"prefix": "36", "length": 14, "logo": "💳"},
    "UnionPay": {"prefix": "62", "length": 16, "logo": "💳"},
}

# URL Domains
URL_DOMAINS = ["google", "facebook", "amazon", "apple", "microsoft", "twitter", "linkedin", "github", "stackoverflow", "youtube", "netflix", "instagram", "pinterest", "reddit", "tumblr", "whatsapp", "telegram", "discord", "slack", "zoom"]
URL_TLDS = ["com", "org", "net", "io", "co", "ai", "app", "dev", "tech", "info", "biz"]

# Real-world username patterns
USERNAME_NAMES = ["alex", "sam", "jordan", "taylor", "morgan", "riley", "jamie", "quinn", "casey", "dakota", "avery", "skyler", "dylan", "tanner", "emma", "olivia", "ava", "isabella", "sophia", "mia", "charlotte", "amelia", "harper", "evelyn", "liam", "noah", "oliver", "elijah", "james", "william", "benjamin"]
USERNAME_ADJ = ["cool", "happy", "sunny", "lucky", "smart", "swift", "bright", "wild", "funny", "nice", "epic", "super", "mega", "ultra", "hyper", "active", "chill", "fresh", "big", "small", "fast", "slow", "young", "big", "little", "great", "mega", "prime", "pro", "max", "ace"]
USERNAME_NOUN = ["cat", "dog", "wolf", "shark", "lion", "bear", "fox", "hawk", "eagle", "panda", "koala", "puppy", "kitten", "bunny", "duck", "bird", "fish", "unicorn", "dragon", "ninja", "coder", "geek", "hero", "star", "moon", "sun", "wave", "fire", "ice", "storm", "king", "queen", "prince", "lord", "lady"]

# Job Titles - 50+
JOB_TITLES = [
    "Software Engineer", "Senior Software Engineer", "Staff Engineer", "Principal Engineer",
    "Full Stack Developer", "Frontend Developer", "Backend Developer", "Mobile Developer",
    "DevOps Engineer", "Site Reliability Engineer", "Cloud Engineer", "Platform Engineer",
    "Data Engineer", "Machine Learning Engineer", "AI Engineer", "Deep Learning Engineer",
    "MLOps Engineer", "Data Scientist", "Senior Data Scientist", "Lead Data Scientist",
    "Cloud Architect", "Solutions Architect", "Enterprise Architect", "Technical Architect",
    "Engineering Manager", "Senior Engineering Manager", "Director of Engineering", "VP of Engineering", "CTO",
    "UI Designer", "UX Designer", "Product Designer", "Senior Product Designer",
    "Visual Designer", "Graphic Designer", "Interaction Designer", "Design Systems Lead",
    "Creative Director", "Art Director",
    "Product Manager", "Senior Product Manager", "Director of Product", "VP of Product",
    "Product Owner", "Business Analyst", "Technical Business Analyst",
    "Project Manager", "Senior Project Manager", "Program Manager", "Scrum Master", "Agile Coach",
    "Data Analyst", "Senior Data Analyst", "Analytics Engineer", "BI Developer", "BI Analyst",
    "Data Administrator", "Database Administrator", "DBA", "Data Governance Analyst",
    "System Administrator", "Network Engineer", "Security Engineer", "Security Analyst",
    "Penetration Tester", "Ethical Hacker", "SOC Analyst", "DevSecOps Engineer",
    "QA Engineer", "QA Automation Engineer", "Test Engineer", "SDET",
    "Technical Writer", "Senior Technical Writer", "Documentation Engineer",
    "Customer Success Engineer", "Support Engineer", "Sales Engineer", "Solutions Engineer",
    "Recruiter", "Technical Recruiter", "Talent Acquisition Specialist", "HR Manager",
    "Marketing Manager", "Digital Marketing Manager", "SEO Specialist", "Content Manager",
]

# Company suffixes
COMPANY_SUFFIXES = ["Inc", "Corp", "LLC", "Ltd", "Group", "Solutions", "Systems", "Tech", "Labs", "Ventures", "Holdings", "Enterprises", "Co", "Partners", "Associates"]

# Street names
US_STREETS = ["Main St", "Oak Ave", "Park Blvd", "First St", "Second St", "Elm St", "Maple Dr", "Cedar Ln", "Pine St", "Elmwood Ave", "Washington St", "Lake Dr", "Hill Rd", "River Rd", "Forest Ave", "Broadway", "Market St", "Church St", "School Ave", "Mill Rd"]
UK_STREETS = ["High Street", "Station Road", "London Road", "Victoria Road", "Church Lane", "Manor Road", "Park Road", "Queens Road", "Kings Road", "Church Street", "Main Road", "River Close", "Hill View", "Station Lane", "Park Lane"]
DE_STREETS = ["Hauptstraße", "Bahnhofstraße", "Schulstraße", "Gartenstraße", "Dorfstraße", "Bergstraße", "Waldstraße", "Kirchstraße", "Lindenstraße", "Brunnenstraße", "Schloßstraße", "Friedrichstraße", "Bismarckstraße", "Goethestraße", "Schillerstraße"]
FR_STREETS = ["Rue de la Paix", "Avenue des Champs-Élysées", "Boulevard Saint-Michel", "Place de la République", "Rue Victor Hugo", "Rue du Commerce", "Avenue Jean Jaurès", "Rue de la Gare", "Place du Marché", "Avenue de la Libération"]

# Cities
CITIES = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte", "San Francisco", "Indianapolis", "Seattle", "Denver", "Boston", "London", "Manchester", "Birmingham", "Edinburgh", "Glasgow", "Paris", "Lyon", "Marseille", "Berlin", "Munich", "Hamburg", "Tokyo", "Osaka", "Sydney", "Melbourne", "Toronto", "Vancouver", "Mumbai", "Delhi", "Bangalore", "Shanghai", "Beijing", "Singapore", "Dubai", "Amsterdam", "Barcelona", "Milan", "Rome", "Lisbon", "Vienna", "Prague"]

# Countries list
COUNTRIES_LIST = ["United States", "Canada", "United Kingdom", "Germany", "France", "Australia", "India", "Japan", "Brazil", "Italy", "Spain", "Mexico", "South Korea", "Netherlands", "Sweden", "Norway", "Denmark", "Finland", "Switzerland", "Austria", "Belgium", "Portugal", "Poland", "Czech Republic", "Hungary", "Greece", "Turkey", "Russia", "China", "Singapore", "UAE", "Thailand", "Vietnam", "Philippines", "Indonesia", "Malaysia", "New Zealand", "South Africa", "Egypt", "Nigeria", "Kenya", "Argentina", "Chile", "Colombia", "Peru"]

# Meaningful words for text generator
TEXT_WORDS = ["the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog", "hello", "world", "test", "data", "generator", "sample", "text", "random", "useful", "helpful", "amazing", "awesome", "brilliant", "fantastic", "wonderful", "excellent", "perfect", "beautiful", "lovely", "nice", "good", "great"]

# Data types configuration
DATA_TYPES = [
    {"type": "uuid", "name": "UUID", "icon": "🎲", "supports_prefix_suffix": True, "options": [
        {"key": "prefix", "label": "Prefix", "type": "text", "placeholder": "e.g., ID_"},
        {"key": "suffix", "label": "Suffix", "type": "text", "placeholder": "e.g., _test"}
    ]},
    {"type": "phone", "name": "Phone", "icon": "📞", "supports_prefix_suffix": False, "options": [
        {"key": "country", "label": "Country", "type": "select_search", "values": [[k, f"{v['code']} - {v['name']}"] for k, v in COUNTRIES.items()], "default": "US"}
    ]},
    {"type": "email", "name": "Email", "icon": "📧", "supports_prefix_suffix": False, "options": [
        {"key": "domain", "label": "Domain", "type": "text", "placeholder": "e.g., gmail.com or company.com"},
        {"key": "extension", "label": "Extension", "type": "text", "placeholder": "e.g., com, org, net"}
    ]},
    {"type": "address", "name": "Address", "icon": "🏠", "supports_prefix_suffix": False, "options": [
        {"key": "country", "label": "Country", "type": "select_search", "values": [[k, v['name']] for k, v in COUNTRIES.items()], "default": "US"}
    ]},
    {"type": "name", "name": "Name", "icon": "👤", "supports_prefix_suffix": False, "options": [
        {"key": "starts_with", "label": "Starts With", "type": "text", "placeholder": "Letter or word"}
    ]},
    {"type": "imei", "name": "IMEI", "icon": "📱", "supports_prefix_suffix": False, "options": [
        {"key": "brand", "label": "Brand", "type": "select", "values": [("Apple", "🍎 Apple"), ("Samsung", "📱 Samsung"), ("Google", "🔵 Google"), ("Huawei", "🏭 Huawei"), ("Xiaomi", "📱 Xiaomi"), ("OnePlus", "1️⃣ OnePlus"), ("Sony", "🎮 Sony"), ("LG", "📺 LG"), ("Random", "🎲 Random")], "default": "Random"}
    ]},
    {"type": "credit_card", "name": "Credit Card", "icon": "💳", "supports_prefix_suffix": False, "options": [
        {"key": "card_type", "label": "Card Type", "type": "select", "values": [("Visa", "💳 Visa"), ("Mastercard", "💳 Mastercard"), ("American Express", "💳 Amex"), ("Discover", "💳 Discover"), ("Random", "🎲 Random")], "default": "Random"}
    ]},
    {"type": "ssn", "name": "SSN", "icon": "🔢", "supports_prefix_suffix": False, "options": []},
    {"type": "ip", "name": "IP Address", "icon": "🌐", "supports_prefix_suffix": True, "options": [
        {"key": "version", "label": "IP Version", "type": "radio", "values": [("ipv4", "IPv4"), ("ipv6", "IPv6")], "default": "ipv4"}
    ]},
    {"type": "datetime", "name": "DateTime", "icon": "🕐", "supports_prefix_suffix": False, "options": [
        {"key": "include_date", "label": "Include Date", "type": "checkbox", "default": True},
        {"key": "include_time", "label": "Include Time", "type": "checkbox", "default": True},
        {"key": "include_seconds", "label": "Include Seconds", "type": "checkbox", "default": False},
        {"key": "include_timezone", "label": "Include Timezone (Z)", "type": "checkbox", "default": False}
    ]},
    {"type": "username", "name": "Username", "icon": "🎮", "supports_prefix_suffix": False, "options": [
        {"key": "prefix", "label": "Prefix", "type": "text", "placeholder": "e.g., user_"},
        {"key": "style", "label": "Style", "type": "select", "values": [("name_year", "name + year"), ("adj_noun", "adjective + noun"), ("name_random", "name + random"), ("mrx", "mrx + name")], "default": "name_year"}
    ]},
    {"type": "password", "name": "Password", "icon": "🔐", "supports_prefix_suffix": False, "options": [
        {"key": "uppercase", "label": "Uppercase (A-Z)", "type": "checkbox", "default": True},
        {"key": "lowercase", "label": "Lowercase (a-z)", "type": "checkbox", "default": True},
        {"key": "numbers", "label": "Numbers (0-9)", "type": "checkbox", "default": True},
        {"key": "special", "label": "Special (!@#$)", "type": "checkbox", "default": False},
        {"key": "length", "label": "Length", "type": "number", "default": 16, "min": 4, "max": 128}
    ]},
    {"type": "company", "name": "Company", "icon": "🏢", "supports_prefix_suffix": False, "options": [
        {"key": "starts_with", "label": "Starts With", "type": "text", "placeholder": "e.g., Tech"}
    ]},
    {"type": "job", "name": "Job Title", "icon": "💼", "supports_prefix_suffix": False, "options": []},
    {"type": "country", "name": "Country", "icon": "🌍", "supports_prefix_suffix": False, "options": [
        {"key": "starts_with", "label": "Starts With", "type": "text", "placeholder": "e.g., U"}
    ]},
    {"type": "city", "name": "City", "icon": "🏙️", "supports_prefix_suffix": False, "options": [
        {"key": "starts_with", "label": "Starts With", "type": "text", "placeholder": "e.g., N"}
    ]},
    {"type": "street", "name": "Street", "icon": "🛣️", "supports_prefix_suffix": False, "options": []},
    {"type": "zipcode", "name": "ZIP Code", "icon": "📮", "supports_prefix_suffix": False, "options": [
        {"key": "min_length", "label": "Min Length", "type": "number", "default": 5, "min": 3, "max": 10},
        {"key": "max_length", "label": "Max Length", "type": "number", "default": 5, "min": 3, "max": 10}
    ]},
    {"type": "text", "name": "Text", "icon": "📝", "supports_prefix_suffix": False, "options": [
        {"key": "length", "label": "Word Count", "type": "number", "default": 5, "min": 1, "max": 50}
    ]},
    {"type": "sentence", "name": "Sentence", "icon": "📚", "supports_prefix_suffix": False, "options": []},
    {"type": "paragraph", "name": "Paragraph", "icon": "📖", "supports_prefix_suffix": False, "options": []},
    {"type": "hex_color", "name": "Hex Color", "icon": "🎨", "supports_prefix_suffix": False, "options": []},
    {"type": "rgb_color", "name": "RGB Color", "icon": "🌈", "supports_prefix_suffix": False, "options": []},
    {"type": "url", "name": "URL", "icon": "🔗", "supports_prefix_suffix": False, "options": [
        {"key": "domain", "label": "Domain", "type": "text", "placeholder": "e.g., google"},
        {"key": "tld", "label": "TLD", "type": "text", "placeholder": "e.g., com"}
    ]},
    {"type": "mac_address", "name": "MAC Address", "icon": "🔌", "supports_prefix_suffix": True, "options": []},
    {"type": "isbn", "name": "ISBN", "icon": "📚", "supports_prefix_suffix": True, "options": []},
    {"type": "barcode", "name": "Barcode", "icon": "📊", "supports_prefix_suffix": True, "options": []},
]

FUN_MESSAGES = [
    "✨ Poof! All done!", "🎉 Boom! Data incoming!", "🚀 Ready for liftoff!",
    "🎯 Bullseye!", "🪄 Magic happens here!", "⚡ ZAP! Done!",
    "🔥 Hot fresh data!", "🌟 Shining bright!", "💥 Pow!", "🎊 Party time!"
]

# Generator functions
def generate_uuid():
    return str(uuid.uuid4())

def generate_phone(country="US"):
    c = COUNTRIES.get(country, COUNTRIES["US"])
    code = c["code"]
    if country in ["US", "CA"]:
        return f"{code} ({random.randint(200, 999)}) {random.randint(200, 999)}-{random.randint(1000, 9999)}"
    elif country == "IN":
        return f"{code} {random.randint(7000000000, 9999999999)}"
    elif country == "UK":
        return f"{code} {random.randint(20, 99)} {random.randint(1000, 9999)} {random.randint(100, 999)}"
    elif country == "DE":
        return f"{code} {random.randint(10, 99)} {random.randint(100000, 999999)}"
    elif country == "FR":
        return f"{code} {random.randint(6, 7)}{random.randint(10000000, 99999999)}"
    else:
        return f"{code} {random.randint(100000000, 999999999)}"

def generate_email(domain=None, extension=None):
    names = ["alex", "sam", "jordan", "taylor", "morgan", "riley", "jamie", "quinn", "casey", "dakota", "avery", "skyler", "dylan", "tanner"]
    
    if domain and extension:
        # Both provided: user@domain.extension
        user = random.choice(names).lower() + str(random.randint(1, 999))
        return f"{user}@{domain}.{extension}"
    elif domain:
        # Only domain: user@domain (domain includes TLD if needed)
        user = random.choice(names).lower() + str(random.randint(1, 999))
        return f"{user}@{domain}"
    elif extension:
        # Only extension: user@randomdomain.extension
        user = random.choice(names).lower() + str(random.randint(1, 999))
        dom = random.choice(["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"])
        return f"{user}@{dom}"
    else:
        # Neither: random
        user = random.choice(names).lower() + str(random.randint(1, 999))
        dom = random.choice(["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"])
        return f"{user}@{dom}"

def generate_address(country="US"):
    if country == "US":
        return f"{random.randint(100, 9999)} {random.choice(US_STREETS)}, {random.choice(CITIES[:20])}, {random.choice(['CA', 'NY', 'TX', 'FL', 'IL', 'PA', 'OH', 'GA', 'NC', 'MI'])} {random.randint(10000, 99999)}"
    elif country == "UK":
        return f"{random.randint(1, 200)} {random.choice(UK_STREETS)}\n{random.choice(['London', 'Manchester', 'Birmingham', 'Edinburgh', 'Glasgow'])}\n{random.choice(['SW1A', 'EC1A', 'W1A', 'NW1', 'SE1'])} {random.randint(1, 9)}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}"
    elif country == "IN":
        return f"{random.randint(1, 500)}, {random.choice(['Main Road', 'Sector', 'Colony', 'Nagar'])}\n{random.choice(['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata', 'Hyderabad', 'Pune'])} - {random.randint(100000, 699999)}"
    elif country == "DE":
        return f"{random.randint(1, 200)} {random.choice(DE_STREETS)}\n{random.randint(10000, 99999)} {random.choice(['Berlin', 'Hamburg', 'Munich', 'Cologne', 'Frankfurt'])}"
    elif country == "FR":
        return f"{random.randint(1, 200)} {random.choice(FR_STREETS)}\n{random.randint(75000, 75020)} {random.choice(['Paris', 'Lyon', 'Marseille'])}"
    else:
        return f"{random.randint(100, 9999)} {random.choice(US_STREETS)}, {random.choice(CITIES[:10])} {random.randint(10000, 99999)}"

def generate_name(starts_with=None):
    first_names = ["James", "Mary", "Robert", "Patricia", "John", "Jennifer", "Michael", "Linda", "David", "Elizabeth", "William", "Barbara", "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah", "Charles", "Karen", "Emma", "Olivia", "Ava", "Isabella", "Sophia", "Mia", "Charlotte", "Amelia", "Harper", "Evelyn", "Liam", "Noah", "Oliver", "Elijah", "James", "William", "Benjamin"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson"]
    
    if starts_with:
        starts_with = starts_with.strip().upper()
        candidates = []
        for f in first_names:
            if f.upper().startswith(starts_with):
                candidates.append((f, random.choice(last_names)))
        for l in last_names:
            if l.upper().startswith(starts_with):
                candidates.append((random.choice(first_names), l))
        if candidates:
            first, last = random.choice(candidates)
            return f"{first} {last}"
    
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_imei(brand="Random"):
    if brand == "Random":
        brand = random.choice(list(IMEI_BRANDS.keys()))
    
    tac = IMEI_BRANDS.get(brand, IMEI_BRANDS["Apple"])
    imei = tac + "".join([str(random.randint(0, 9)) for _ in range(12)])
    
    # Luhn checksum
    total = 0
    doubled = False
    for digit in imei[::-1]:
        d = int(digit) * (2 if doubled else 1)
        total += d if d < 10 else d - 9
        doubled = not doubled
    check = (10 - (total % 10)) % 10
    return imei + str(check)

def generate_credit_card(card_type="Random"):
    if card_type == "Random":
        card_type = random.choice(list(CREDIT_CARD_TYPES.keys()))
    
    config = CREDIT_CARD_TYPES.get(card_type, CREDIT_CARD_TYPES["Visa"])
    prefix = config["prefix"]
    length = config["length"]
    
    cc = prefix
    while len(cc) < length - 1:
        cc += str(random.randint(0, 9))
    
    # Luhn
    total = 0
    doubled = True
    for digit in cc[::-1]:
        d = int(digit) * (2 if doubled else 1)
        if d > 9: d -= 9
        total += d
        doubled = not doubled
    check = (10 - (total % 10)) % 10
    cc += str(check)
    
    # Format
    if card_type == "American Express":
        return f"{cc[:4]}-{cc[4:10]}-{cc[10:]} {config['logo']}"
    else:
        return "-".join([cc[i:i+4] for i in range(0, len(cc), 4)]) + f" {config['logo']}"

def generate_ssn():
    return f"{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(1000, 9999)}"

def generate_ip(version="ipv4"):
    if version == "ipv6":
        return ":".join([f"{random.randint(0, 65535):x}" for _ in range(8)])
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

def generate_datetime(include_date=True, include_time=True, include_seconds=False, include_timezone=False):
    year = random.randint(2020, 2025)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59) if include_seconds else 0
    
    parts = []
    if include_date:
        parts.append(f"{year}-{month:02d}-{day:02d}")
    if include_time:
        if include_seconds:
            parts.append(f"{hour:02d}:{minute:02d}:{second:02d}")
        else:
            parts.append(f"{hour:02d}:{minute:02d}")
    if include_timezone:
        parts.append("Z")
    
    return " ".join(parts)

def generate_username(prefix=None, style="name_year"):
    year = str(random.randint(1980, 2024))
    num = str(random.randint(10, 999))
    random_num = str(random.randint(1000, 9999))
    
    name = random.choice(USERNAME_NAMES)
    adj = random.choice(USERNAME_ADJ)
    noun = random.choice(USERNAME_NOUN)
    
    if style == "name_year":
        username = f"{name}{year}"
    elif style == "adj_noun":
        username = f"{adj}{noun}{num}"
    elif style == "name_random":
        username = f"{name}{random_num}"
    elif style == "mrx":
        username = f"mrx{name}"
    else:
        username = f"{name}{num}"
    
    if prefix:
        username = prefix + username
    
    return username

def generate_password(uppercase=True, lowercase=True, numbers=True, special=False, length=16):
    chars = ""
    if uppercase:
        chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if lowercase:
        chars += "abcdefghijklmnopqrstuvwxyz"
    if numbers:
        chars += "0123456789"
    if special:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    if not chars:
        chars = "abcdefghijklmnopqrstuvwxyz"
    
    return "".join([random.choice(chars) for _ in range(length)])

def generate_company(starts_with=None):
    prefixes = ["Tech", "Smart", "Global", "Digital", "Future", "Next", "Prime", "Alpha", "Beta", "Omega", "Ultra", "Mega", "Super", "Hyper", "Quantum", "Cloud", "Data", "Net", "Web", "App"]
    
    if starts_with:
        starts_with = starts_with.strip()
        return f"{starts_with} {random.choice(COMPANY_SUFFIXES)}"
    
    return f"{random.choice(prefixes)} {random.choice(COMPANY_SUFFIXES)}"

def generate_job():
    return random.choice(JOB_TITLES)

def generate_country(starts_with=None):
    if starts_with:
        starts_with = starts_with.strip().upper()
        filtered = list(dict.fromkeys([c for c in COUNTRIES_LIST if c.upper().startswith(starts_with)]))
        if filtered:
            return random.choice(filtered)
    return random.choice(COUNTRIES_LIST)

def generate_city(starts_with=None):
    if starts_with:
        starts_with = starts_with.strip().upper()
        filtered = list(dict.fromkeys([c for c in CITIES if c.upper().startswith(starts_with)]))
        if filtered:
            return random.choice(filtered)
    return random.choice(CITIES)

def generate_street():
    return f"{random.randint(100, 9999)} {random.choice(US_STREETS)}"

def generate_zipcode(min_length=5, max_length=5):
    length = random.randint(min(min_length, max_length), max(min_length, max_length))
    return "".join([str(random.randint(0, 9)) for _ in range(length)])

def generate_text(length=5):
    words = random.choices(TEXT_WORDS, k=length)
    return " ".join(words)

def generate_sentence():
    words = random.choices(TEXT_WORDS, k=random.randint(5, 10))
    return " ".join(words).capitalize() + "."

def generate_paragraph(sentences=3):
    return " ".join([generate_sentence() for _ in range(sentences)])

def generate_hex_color():
    return f"#{random.randint(0, 16777215):06x}"

def generate_rgb_color():
    return f"rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})"

def generate_url(domain=None, tld=None):
    if domain:
        dom = domain
    else:
        dom = random.choice(URL_DOMAINS)
    if tld:
        ext = tld
    else:
        ext = random.choice(URL_TLDS)
    path = random.choice(["about", "products", "services", "blog", "contact", "pricing", "docs", "help", "support", "news", "careers"])
    return f"https://{dom}.{ext}/{path}"

def generate_mac_address():
    return ":".join([f"{random.randint(0, 255):02x}" for _ in range(6)])

def generate_isbn():
    return f"978-{random.randint(0, 9999999):7d}-{random.randint(0, 9)}"

def generate_barcode():
    return "".join([str(random.randint(0, 9)) for _ in range(13)])

GENERATORS = {
    "uuid": generate_uuid,
    "phone": generate_phone,
    "email": generate_email,
    "address": generate_address,
    "name": generate_name,
    "imei": generate_imei,
    "credit_card": generate_credit_card,
    "ssn": generate_ssn,
    "ip": generate_ip,
    "datetime": generate_datetime,
    "username": generate_username,
    "password": generate_password,
    "company": generate_company,
    "job": generate_job,
    "country": generate_country,
    "city": generate_city,
    "street": generate_street,
    "zipcode": generate_zipcode,
    "text": generate_text,
    "sentence": generate_sentence,
    "paragraph": generate_paragraph,
    "hex_color": generate_hex_color,
    "rgb_color": generate_rgb_color,
    "url": generate_url,
    "mac_address": generate_mac_address,
    "isbn": generate_isbn,
    "barcode": generate_barcode,
}

def apply_prefix_suffix(data, prefix, suffix):
    if not prefix and not suffix:
        return data
    prefix_len = len(prefix) if prefix else 0
    suffix_len = len(suffix) if suffix else 0
    total_extra = prefix_len + suffix_len
    original_len = len(data)
    
    if total_extra >= original_len:
        return (prefix or "")[:original_len - suffix_len] + (suffix or "")[-suffix_len:] if suffix_len > 0 else (prefix or "")[:original_len]
    
    truncated = data[:original_len - total_extra]
    return (prefix or "") + truncated + (suffix or "")

# Request model
class GenerateRequest(BaseModel):
    type: str
    count: int = 1
    # Type-specific options
    prefix: Optional[str] = None
    suffix: Optional[str] = None
    country: Optional[str] = None
    domain: Optional[str] = None
    extension: Optional[str] = None
    starts_with: Optional[str] = None
    brand: Optional[str] = None
    card_type: Optional[str] = None
    version: Optional[str] = None
    include_date: Optional[bool] = None
    include_time: Optional[bool] = None
    include_seconds: Optional[bool] = None
    include_timezone: Optional[bool] = None
    style: Optional[str] = None
    uppercase: Optional[bool] = None
    lowercase: Optional[bool] = None
    numbers: Optional[bool] = None
    special: Optional[bool] = None
    length: Optional[int] = None
    min_length: Optional[int] = None
    max_length: Optional[int] = None

@app.get("/")
async def root():
    return FileResponse("index.html")

@app.get("/api/types")
async def get_types():
    return {"types": DATA_TYPES}

@app.post("/api/generate")
async def generate(req: GenerateRequest):
    if req.type not in GENERATORS:
        raise HTTPException(status_code=400, detail=f"Unknown type: {req.type}")
    
    if req.count < 1 or req.count > 1000:
        raise HTTPException(status_code=400, detail="Count must be 1-1000")
    
    generator = GENERATORS[req.type]
    results = []
    
    for _ in range(req.count):
        type_info = next((t for t in DATA_TYPES if t["type"] == req.type), None)
        
        if req.type == "phone":
            data = generator(country=req.country or "US")
        elif req.type == "email":
            data = generator(domain=req.domain, extension=req.extension)
        elif req.type == "address":
            data = generator(country=req.country or "US")
        elif req.type == "name":
            data = generator(starts_with=req.starts_with)
        elif req.type == "imei":
            data = generator(brand=req.brand or "Random")
        elif req.type == "credit_card":
            data = generator(card_type=req.card_type or "Random")
        elif req.type == "ip":
            data = generator(version=req.version or "ipv4")
        elif req.type == "datetime":
            data = generator(
                include_date=req.include_date if req.include_date is not None else True,
                include_time=req.include_time if req.include_time is not None else True,
                include_seconds=req.include_seconds if req.include_seconds is not None else False,
                include_timezone=req.include_timezone if req.include_timezone is not None else False
            )
        elif req.type == "username":
            data = generator(prefix=req.prefix, style=req.style or "name_year")
        elif req.type == "password":
            data = generator(
                uppercase=req.uppercase if req.uppercase is not None else True,
                lowercase=req.lowercase if req.lowercase is not None else True,
                numbers=req.numbers if req.numbers is not None else True,
                special=req.special if req.special is not None else False,
                length=req.length or 16
            )
        elif req.type == "company":
            data = generator(starts_with=req.starts_with)
        elif req.type == "country":
            data = generator(starts_with=req.starts_with)
        elif req.type == "city":
            data = generator(starts_with=req.starts_with)
        elif req.type == "zipcode":
            data = generator(min_length=req.min_length or 5, max_length=req.max_length or 5)
        elif req.type == "text":
            data = generator(length=req.length or 5)
        elif req.type == "url":
            data = generator(domain=req.domain, tld=req.extension)
        elif type_info and type_info.get("supports_prefix_suffix"):
            data = generator()
            data = apply_prefix_suffix(data, req.prefix, req.suffix)
        else:
            data = generator()
        
        results.append(data)
    
    return {
        "success": True,
        "message": random.choice(FUN_MESSAGES),
        "data": results
    }

@app.get("/health")
async def health():
    return {"status": "healthy", "message": "Test Data Generator is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
