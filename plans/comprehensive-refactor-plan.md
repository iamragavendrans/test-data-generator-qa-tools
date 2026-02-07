# Test Data Generator - Comprehensive Refactor Plan

## Overview
Major redesign based on user feedback. Replace prefix/suffix with type-specific options.

---

## 1. Remove Prefix/Suffix from These Types

| Type | Reason |
|------|--------|
| address | Full addresses don't need prefix/suffix |
| ssn | Numeric format, can't truncate |
| street | Part of address |
| job title | Full job titles |
| hex_color | Numeric color code |
| rgb_color | Numeric format |
| text | Fixed-length text |
| sentence | Fixed sentence |
| paragraph | Fixed paragraph |

**New supported types for prefix/suffix:**
- uuid (keep)
- email (keep)
- username (change - real-world style)
- company (change - use "starts with")
- name (change - use "starts with")
- country (change - use "starts with")
- city (change - use "starts with")
- url (change - use custom domain)
- ip (keep)
- ipv4 (keep)
- ipv6 (keep)
- mac_address (keep)
- isbn (keep)
- barcode (keep)

---

## 2. "Starts With" Option for Name-Based Types

### Name
- Input: "starts_with" field (optional)
- If provided: generate names starting with that letter
- Example: starts_with="J" → "James Wilson", "Jane Smith"

### Company
- Input: "starts_with" field (optional)
- Example: starts_with="Tech" → "TechCorp", "TechStart Inc"

### Country
- Input: "starts_with" field (optional)
- Example: starts_with="U" → "United States", "United Kingdom"

### City
- Input: "starts_with" field (optional)
- Example: starts_with="N" → "New York", "Nashville", "New Delhi"

---

## 3. Fix Text Generators

### Current (Broken)
```python
def generate_text():
    return "".join([...])  # Not implemented properly
```

### New Implementations

#### Text (fixed-length random string)
```python
def generate_text(length=20):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join(random.choice(chars) for _ in range(length))
```

#### Sentence (random words ending with period)
```python
def generate_sentence():
    words = ["The", "quick", "brown", "fox", "jumps", "over", "lazy", "dog", "This", "is", "sample", "text"]
    sentence = " ".join(random.sample(words, random.randint(5, 10)))
    return sentence + "."
```

#### Paragraph (multiple sentences)
```python
def generate_paragraph(sentences=3):
    return " ".join([generate_sentence() for _ in range(sentences)])
```

---

## 4. URL Generator Improvement

### Current
```python
def generate_url():
    return f"https://example{random.randint(1, 999)}.com"
```

### New
```python
def generate_url(domain=None, tld=None):
    words = ["google", "facebook", "amazon", "apple", "microsoft", "twitter", "linkedin", "github", "stackoverflow", "youtube", "netflix", "instagram"]
    domains = domain or random.choice(words)
    tlds = tld or random.choice(["com", "org", "net", "io", "co", "ai", "app"])
    path = random.choice(["about", "products", "services", "blog", "contact", "pricing", "docs"])
    return f"https://{domains}.{tlds}/{path}"
```

**Options:**
- `domain`: specific domain name
- `tld`: top-level domain
- `path`: URL path

---

## 5. Date/Datetime Consolidation

### Single Type: "DateTime"

**Checkbox Options:**
- [x] Include Date (default: checked)
- [x] Include Time (default: checked)
- [x] Include Seconds (default: unchecked)
- [x] Include Timezone (default: unchecked)

**Examples:**
- Date only: "2024-03-15"
- Date + Time: "2024-03-15 14:30"
- Full: "2024-03-15 14:30:45 +05:30"

**Remove:** Separate "date" and "datetime" types - consolidate to one.

---

## 6. IP Address Consolidation

### Current Types
- ip (generic)
- ipv4 (IPv4 format)
- ipv6 (IPv6 format)

### New: Single "IP Address" Type

**Dropdown Options:**
- IPv4 (default)
- IPv6

**Rationale:** Most users just need IPv4. IPv6 is for advanced users.

---

## 7. Password Generator with Checkboxes

### Options (checkboxes):
- [x] Uppercase (A-Z) - default: checked
- [x] Lowercase (a-z) - default: checked
- [x] Numbers (0-9) - default: checked
- [x] Special (!@#$...) - default: unchecked
- [x] Underscore (_) - default: unchecked
- [x] Hyphen (-) - default: unchecked

### Length Slider
- Default: 16
- Range: 4-128

**Example:**
- If only uppercase + numbers: "A1B2C3D4E5F6G7H8"

---

## 8. Email Generator with Custom Fields

### Options:
- `username`: custom username part (optional)
- `domain`: specific domain (optional)
- `extension`: after the dot (e.g., "com", "org")

### Behavior:
1. If username provided → use it
2. If domain provided → use it
3. If extension provided → override default

**Examples:**
- No options: "john.doe@gmail.com"
- username="john": "john@random.com"
- domain="company": "random.name@company.com"
- domain="google", extension="co.in": "random@google.co.in"

---

## 9. Username Generator (Real-World Style)

### Current
```python
# Random alphanumeric: "a8xk9m2n4"
```

### New Patterns
| Pattern | Example |
|---------|---------|
| name + numbers | "badbunny2003", "sarah1990" |
| name + random | "mrxfromarizona", "sunny_ca" |
| adjective + noun | "coolcat42", "happyshark" |
| name_underscore_number | "john_smith_123" |

### Options:
- `prefix`: add text at start
- `style`: dropdown (name_number, name_random, adjective_noun, name_underscore_number)
- `max_length`: 10-50 (default: 20)

### Examples:
- Default: "badbunny2003"
- prefix="user_": "user_badbunny2003"
- style="adjective_noun": "happyshark99"

---

## 10. IMEI with Mobile Brand Selection

### Options (radio/searchable dropdown):
- Apple
- Samsung
- Google
- Huawei
- Xiaomi
- OnePlus
- Sony
- LG
- Motorola
- Nokia
- Random (default)

### Behavior:
- Each brand uses appropriate TAC (Type Allocation Code)
- Format: `35 + brand + model + serial`

### Example:
- Apple: "358099001234567"
- Samsung: "358099012345678"
- Random: picks random brand

---

## 11. Credit Card with Type Selection

### Options (radio/searchable dropdown):
- Visa
- Mastercard
- American Express
- Discover
- JCB
- Diners Club
- UnionPay
- Random (default)

### Behavior:
- Each type uses correct prefix/format
- Visa: starts with 4, 16 digits
- Amex: starts with 37, 15 digits
- Mastercard: starts with 51-55, 16 digits

### Examples:
- Visa: "4532-1234-5678-9012"
- Amex: "3782-8224-6310-005"
- Mastercard: "5425-2341-6789-0123"

---

## 12. Phone with Searchable Country List

### Current
Fixed dropdown: US, UK, India, Germany, France, Canada, Australia

### New
- Searchable dropdown with 200+ countries
- Each shows: Flag + Country Name + Country Code
- Recent/常用 (frequently used) section at top

### Implementation
```python
COUNTRIES = {
    "US": {"name": "United States", "code": "+1", "format": "(XXX) XXX-XXXX"},
    "GB": {"name": "United Kingdom", "code": "+44", "format": "XXXX XXXXXX"},
    "IN": {"name": "India", code: "+91", "format": "XXXXX XXXXX"},
    # ... 200+ countries
}
```

### Features:
- Search by country name OR country code
- Keyboard navigation
- Most recently used at top

---

## Summary of Changes

### Types Removed
- "datetime" (merged into DateTime with options)
- "ip" (merged into IP Address with IPv4/IPv6 toggle)
- "ipv4" (merged)
- "ipv6" (merged)

### Types Renamed
- "ip" → "IP Address"

### New Types/Features
- Password with checkboxes
- Email with custom fields
- Username with real-world patterns
- IMEI with brand selection
- Credit Card with type selection
- Phone with searchable 200+ countries
- DateTime with checkbox options

### Options per Type

| Type | Options |
|------|---------|
| UUID | prefix, suffix |
| Phone | searchable country list |
| Email | username, domain, extension |
| Address | locale (country) |
| Name | starts_with |
| IMEI | brand dropdown |
| Credit Card | type dropdown |
| SSN | locale (country) |
| IP Address | IPv4/IPv6 toggle |
| DateTime | date, time, seconds, timezone checkboxes |
| Username | prefix, style, max_length |
| Password | upper, lower, numbers, special, _, -, length |
| Company | starts_with |
| Job Title | none |
| Country | starts_with |
| City | starts_with |
| Street | none |
| ZIP Code | locale (country) |
| Hex Color | none |
| RGB Color | none |
| URL | domain, tld, path |
| IPv4 | none |
| IPv6 | none |
| MAC Address | none |
| ISBN | none |
| Barcode | none |
| Text | length |
| Sentence | none |
| Paragraph | sentences |

---

## File Changes

### main.py
- Refactor all generators
- Add new options to DATA_TYPES
- Add 200+ countries list
- Fix text/sentence/paragraph generators
- Consolidate date/datetime → DateTime
- Consolidate ip/ipv4/ipv6 → IP Address

### index.html
- New searchable dropdown for countries (using datalist or custom)
- Checkbox groups for password options
- Radio buttons for IMEI brand, Credit Card type
- Toggle for IPv4/IPv6
- Checkboxes for DateTime format
- Style dropdown for username generation
