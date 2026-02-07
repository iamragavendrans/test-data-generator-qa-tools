# Test Data Generator - Improvement Plan

## Overview
Based on your feedback, here are the 5 improvements to implement:

---

## 1. Horizontal Single-View Layout

### Current
- 2-column layout (left sidebar with types, right panel with options)
- Types in a 2-column grid

### New Design
```
┌─────────────────────────────────────────────────────────────────────┐
│  UUID  Phone  Email  Address  Name  IMEI  Credit Card  SSN  ...     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Selected: [Icon] UUID                                               │
│  ┌─────────────┬─────────────┬─────────────┐                       │
│  │   Prefix    │   Suffix    │    Count    │                       │
│  └─────────────┴─────────────┴─────────────┘                       │
│                       [ GENERATE ]                                   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ 🎊 Party time!                            [Copy All][JSON]  │   │
│  ├─────────────────────────────────────────────────────────────┤   │
│  │ #1  550e8400-e29b-41d4-a716-446655440000      [Click to copy]│   │
│  │ #2  a1b2c3d4-e5f6-7890-abcd-ef1234567890      [Click to copy]│   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

### Changes
- Top horizontal bar with all 20 types as tabs/buttons
- Click type to select, shows current selection
- Single unified config row below
- All types visible without scrolling

---

## 2. Conditional Prefix/Suffix

### Types WITH prefix/suffix support
- uuid, email, username, name, company, job, country, city, street, text, sentence, paragraph, url, isbn, barcode

### Types WITHOUT prefix/suffix (numeric/formatted)
- phone, imei, credit_card, ssn, ip, date, datetime, zipcode, hex_color, rgb_color, ipv4, ipv6, mac_address

### UI Behavior
- Prefix/Suffix inputs only appear for supported types
- Or show them disabled with hint for unsupported types

---

## 3. Hex Color Preview

### Current
```
#1  #ff6b6b        [Click to copy]
```

### New
```
#1  [■ #ff6b6b]    #ff6b6b        [Click to copy]
```

### Implementation
- Add color swatch div with background-color
- Show both color swatch and hex value
- Click copies the hex value (not the swatch)

---

## 4. Country/Area Code Options

### Phone
- Dropdown: US (+1), UK (+44), India (+91), Germany (+49), etc.
- Default: US (+1)

### ZIP Code
- Dropdown: US (5-digit), UK (postcode), India (6-digit), etc.

### Address
- Dropdown: US, UK, India, Germany, France, etc.
- Generates country-specific address format

### Backend API Changes
```python
class GenerateRequest(BaseModel):
    type: str
    prefix: Optional[str] = None
    suffix: Optional[str] = None
    count: int = 1
    locale: Optional[str] = None  # For country-specific data
```

---

## 5. More Job Titles (50+)

### Current (5)
```
["Engineer", "Designer", "Manager", "Developer", "Analyst"]
```

### New (50+)
```
[
    # Tech
    "Software Engineer", "Senior Software Engineer", "Full Stack Developer",
    "Frontend Developer", "Backend Developer", "DevOps Engineer",
    "Data Engineer", "Machine Learning Engineer", "AI Engineer",
    "Cloud Architect", "Solutions Architect", "Technical Lead",
    "Engineering Manager", "VP of Engineering", "CTO",
    
    # Design
    "UI Designer", "UX Designer", "Product Designer",
    "Graphic Designer", "Visual Designer", "Interaction Designer",
    
    # Business
    "Product Manager", "Project Manager", "Scrum Master",
    "Business Analyst", "Data Analyst", "Financial Analyst",
    "Marketing Manager", "Sales Manager", "Account Manager",
    "HR Manager", "Recruiter", "Talent Acquisition Specialist",
    
    # Data
    "Data Scientist", "Data Analyst", "Data Administrator",
    "Database Administrator", "BI Analyst", "Analytics Manager",
    
    # Other
    "System Administrator", "Network Engineer", "Security Analyst",
    "QA Engineer", "Test Automation Engineer", "Technical Writer",
    "Customer Success Manager", "Support Engineer", "Sales Engineer"
]
```

---

## Implementation Order

### Step 1: Backend Changes
1. Update `DATA_TYPES` with `supports_prefix_suffix` flag
2. Add `locale` support to generators
3. Expand job titles to 50+
4. Add country-specific phone/zip/address generators
5. Update API schema

### Step 2: Frontend Changes
1. Redesign to horizontal layout
2. Add type-specific options dynamically
3. Implement hex color preview
4. Hide/show prefix/suffix based on type
5. Add country/area dropdowns

### Step 3: Testing
1. Test all data types work correctly
2. Test prefix/suffix with/without locale
3. Test color preview
4. Verify job titles are unique

---

## File Changes Summary

| File | Changes |
|------|---------|
| `main.py` | - Add `supports_prefix_suffix` to DATA_TYPES<br>- Add locale parameter<br>- Expand job titles<br>- Add country-specific generators<br>- Update API schema |
| `index.html` | - Horizontal layout<br>- Dynamic options per type<br>- Color preview styling<br>- Country dropdowns |

---

## Questions to Confirm

1. **Job titles**: Should we categorize them (Tech, Design, Business) or keep flat?
2. **Countries**: Which countries do you need phone/zip/address support for?
3. **RGB color**: Should it also show color preview like hex?
