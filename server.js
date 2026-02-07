// Test Data Generator - Bun Server
// Pure HTML, CSS, JS frontend with Bun backend

const GENERATORS = {
    uuid: () => crypto.randomUUID(),
    phone: () => {
        const area = Math.floor(Math.random() * 900) + 100;
        const exchange = Math.floor(Math.random() * 900) + 100;
        const line = Math.floor(Math.random() * 9000) + 1000;
        return `+1-${area}-${exchange}-${line}`;
    },
    email: () => {
        const domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com', 'example.com'];
        const names = ['john', 'jane', 'smith', 'doe', 'test', 'demo', 'user'];
        return `${names[Math.floor(Math.random() * names.length)]}${Math.floor(Math.random() * 999)}@${domains[Math.floor(Math.random() * domains.length)]}`;
    },
    address: () => {
        const streets = ['Main St', 'Oak Ave', 'Park Blvd', 'First St', 'Second St'];
        const cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'];
        return `${Math.floor(Math.random() * 9999)} ${streets[Math.floor(Math.random() * streets.length)]}, ${cities[Math.floor(Math.random() * cities.length)]}`;
    },
    name: () => {
        const first = ['John', 'Jane', 'Michael', 'Emily', 'David', 'Sarah', 'Chris', 'Emma'];
        const last = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis'];
        return `${first[Math.floor(Math.random() * first.length)]} ${last[Math.floor(Math.random() * last.length)]}`;
    },
    imei: () => {
        let imei = '';
        for (let i = 0; i < 14; i++) {
            imei += Math.floor(Math.random() * 10);
        }
        // Calculate Luhn checksum
        let sum = 0;
        for (let i = imei.length - 1; i >= 0; i--) {
            let digit = parseInt(imei[i]);
            if ((imei.length - i) % 2 === 0) {
                digit *= 2;
                if (digit > 9) digit -= 9;
            }
            sum += digit;
        }
        const checkDigit = (10 - (sum % 10)) % 10;
        return imei + checkDigit;
    },
    credit_card: () => {
        const prefixes = ['4', '5', '37', '6011'];
        const prefix = prefixes[Math.floor(Math.random() * prefixes.length)];
        let cc = prefix;
        while (cc.length < 16 - 1) {
            cc += Math.floor(Math.random() * 10);
        }
        // Calculate Luhn
        let sum = 0;
        let doubled = true;
        for (let i = cc.length - 1; i >= 0; i--) {
            let digit = parseInt(cc[i]);
            if (doubled) {
                digit *= 2;
                if (digit > 9) digit -= 9;
            }
            sum += digit;
            doubled = !doubled;
        }
        const checkDigit = (10 - (sum % 10)) % 10;
        return cc + checkDigit;
    },
    ssn: () => {
        return `${Math.floor(Math.random() * 900) + 100}-${Math.floor(Math.random() * 90) + 10}-${Math.floor(Math.random() * 9000) + 1000}`;
    },
    ip: () => {
        return `${Math.floor(Math.random() * 255)}.${Math.floor(Math.random() * 255)}.${Math.floor(Math.random() * 255)}.${Math.floor(Math.random() * 255)}`;
    },
    date: () => {
        const year = 2020 + Math.floor(Math.random() * 5);
        const month = String(Math.floor(Math.random() * 12) + 1).padStart(2, '0');
        const day = String(Math.floor(Math.random() * 28) + 1).padStart(2, '0');
        return `${year}-${month}-${day}`;
    },
    username: () => {
        const chars = 'abcdefghijklmnopqrstuvwxyz0123456789';
        let username = '';
        for (let i = 0; i < 8 + Math.floor(Math.random() * 8); i++) {
            username += chars[Math.floor(Math.random() * chars.length)];
        }
        return username;
    },
    password: () => {
        const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*';
        let password = '';
        for (let i = 0; i < 16; i++) {
            password += chars[Math.floor(Math.random() * chars.length)];
        }
        return password;
    },
    company: () => {
        const companies = ['Acme Corp', 'TechStart', 'Global Inc', 'Smart Solutions', 'Digital Labs'];
        return companies[Math.floor(Math.random() * companies.length)];
    },
    job: () => {
        const jobs = ['Engineer', 'Designer', 'Manager', 'Developer', 'Analyst', 'Consultant'];
        return jobs[Math.floor(Math.random() * jobs.length)];
    },
    country: () => {
        const countries = ['United States', 'Canada', 'United Kingdom', 'Germany', 'France', 'Japan', 'Australia'];
        return countries[Math.floor(Math.random() * countries.length)];
    },
    city: () => {
        const cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'London', 'Paris'];
        return cities[Math.floor(Math.random() * cities.length)];
    },
    zipcode: () => {
        return String(Math.floor(Math.random() * 90000) + 10000);
    },
    hex_color: () => {
        return '#' + Math.floor(Math.random() * 16777215).toString(16).padStart(6, '0');
    },
    url: () => {
        return `https://example${Math.floor(Math.random() * 999)}.com`;
    }
};

const DATA_TYPES = [
    { type: 'uuid', name: 'UUID', icon: '🎲' },
    { type: 'phone', name: 'Phone', icon: '📞' },
    { type: 'email', name: 'Email', icon: '📧' },
    { type: 'address', name: 'Address', icon: '🏠' },
    { type: 'name', name: 'Name', icon: '👤' },
    { type: 'imei', name: 'IMEI', icon: '📱' },
    { type: 'credit_card', name: 'Credit Card', icon: '💳' },
    { type: 'ssn', name: 'SSN', icon: '🔢' },
    { type: 'ip', name: 'IP Address', icon: '🌐' },
    { type: 'date', name: 'Date', icon: '📅' },
    { type: 'username', name: 'Username', icon: '🎮' },
    { type: 'password', name: 'Password', icon: '🔐' },
    { type: 'company', name: 'Company', icon: '🏢' },
    { type: 'job', name: 'Job Title', icon: '💼' },
    { type: 'country', name: 'Country', icon: '🌍' },
    { type: 'city', name: 'City', icon: '🏙️' },
    { type: 'zipcode', name: 'ZIP Code', icon: '📮' },
    { type: 'hex_color', name: 'Hex Color', icon: '🎨' },
    { type: 'url', name: 'URL', icon: '🔗' }
];

const FUN_MESSAGES = [
    '✨ Poof! All done!',
    '🎉 Boom! Data incoming!',
    '🚀 Ready for liftoff!',
    '🎯 Bullseye!',
    '🪄 Magic happens here!',
    '⚡ ZAP! Done!',
    '🔥 Hot fresh data!',
    '🌟 Shining bright!',
    '💥 Pow! Right there!',
    '🎊 Party time!'
];

function applyPrefixSuffix(data, prefix, suffix) {
    let prefixLen = prefix ? prefix.length : 0;
    let suffixLen = suffix ? suffix.length : 0;
    let totalExtra = prefixLen + suffixLen;
    let originalLen = data.length;
    
    if (totalExtra === 0) return data;
    
    let targetDataLen = originalLen - totalExtra;
    
    if (targetDataLen <= 0) {
        let result = (prefix || '') + (suffix || '');
        return result.slice(0, originalLen);
    }
    
    let truncated = data.slice(0, targetDataLen);
    return (prefix || '') + truncated + (suffix || '');
}

function generateData(type, prefix, suffix, count) {
    let results = [];
    for (let i = 0; i < count; i++) {
        let data = GENERATORS[type]();
        results.push(applyPrefixSuffix(data, prefix, suffix));
    }
    return results;
}

// Bun HTTP Server
export default {
    port: 3000,
    fetch(request) {
        const url = new URL(request.url);
        const path = url.pathname;
        
        if (path === '/' || path === '/index.html') {
            return new Response(HTML, {
                headers: { 'Content-Type': 'text/html' }
            });
        }
        
        if (path === '/api/types') {
            return new Response(JSON.stringify({ types: DATA_TYPES }), {
                headers: { 'Content-Type': 'application/json' }
            });
        }
        
        if (path === '/api/generate' && request.method === 'POST') {
            try {
                const body = await request.json();
                const { type, prefix, suffix, count = 1 } = body;
                
                if (!GENERATORS[type]) {
                    return new Response(JSON.stringify({ 
                        success: false, 
                        message: 'Unknown type: ' + type 
                    }), {
                        status: 400,
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                const results = generateData(type, prefix, suffix, count);
                const message = FUN_MESSAGES[Math.floor(Math.random() * FUN_MESSAGES.length)];
                
                return new Response(JSON.stringify({
                    success: true,
                    message,
                    data: results
                }), {
                    headers: { 'Content-Type': 'application/json' }
                });
            } catch (e) {
                return new Response(JSON.stringify({ 
                    success: false, 
                    message: 'Invalid request' 
                }), {
                    status: 400,
                    headers: { 'Content-Type': 'application/json' }
                });
            }
        }
        
        if (path === '/health') {
            return new Response(JSON.stringify({ 
                status: 'healthy', 
                message: 'Test Data Generator is running!' 
            }), {
                headers: { 'Content-Type': 'application/json' }
            });
        }
        
        return new Response('Not Found', { status: 404 });
    }
};

const HTML = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Data Generator</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #e4e8ec 100%);
            min-height: 100vh;
            color: #333;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px;
        }
        header {
            text-align: center;
            margin-bottom: 40px;
        }
        header h1 {
            font-size: 2.5rem;
            color: #1a1a2e;
            margin-bottom: 8px;
        }
        header p {
            color: #666;
        }
        .main-grid {
            display: grid;
            grid-template-columns: 280px 1fr;
            gap: 30px;
        }
        .types-panel {
            background: white;
            border-radius: 16px;
            padding: 24px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.08);
            height: fit-content;
            position: sticky;
            top: 20px;
        }
        .types-panel h2 {
            font-size: 1.1rem;
            color: #444;
            margin-bottom: 16px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .types-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 8px;
        }
        .type-card {
            padding: 12px;
            border-radius: 10px;
            background: #f8f9fa;
            cursor: pointer;
            transition: all 0.2s;
            border: 2px solid transparent;
            position: relative;
        }
        .type-card:hover {
            background: #e9ecef;
            transform: translateY(-2px);
        }
        .type-card.selected {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .type-card .icon {
            font-size: 1.5rem;
            display: block;
            margin-bottom: 4px;
        }
        .type-card .name {
            font-size: 0.75rem;
            font-weight: 500;
        }
        .type-card .gear {
            position: absolute;
            top: 8px;
            right: 8px;
            width: 24px;
            height: 24px;
            border-radius: 6px;
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            transition: opacity 0.2s;
            background: rgba(255,255,255,0.2);
            cursor: pointer;
        }
        .type-card:hover .gear {
            opacity: 1;
        }
        .type-card.selected .gear {
            background: rgba(255,255,255,0.3);
        }
        .gear svg {
            width: 14px;
            height: 14px;
        }
        .options-popup {
            position: absolute;
            right: 0;
            top: 100%;
            margin-top: 8px;
            background: white;
            border-radius: 12px;
            padding: 16px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.15);
            z-index: 100;
            width: 220px;
            display: none;
        }
        .options-popup.show {
            display: block;
        }
        .options-popup label {
            display: block;
            font-size: 0.7rem;
            color: #888;
            margin-bottom: 4px;
            text-transform: uppercase;
        }
        .options-popup input {
            width: 100%;
            padding: 8px 12px;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            margin-bottom: 12px;
            font-size: 0.85rem;
        }
        .options-popup input:focus {
            outline: none;
            border-color: #667eea;
        }
        .generator-panel {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        .config-card {
            background: white;
            border-radius: 16px;
            padding: 24px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.08);
        }
        .selected-info {
            display: flex;
            align-items: center;
            gap: 16px;
            padding: 16px;
            background: #f8f9fa;
            border-radius: 12px;
            margin-bottom: 20px;
        }
        .selected-info .icon {
            font-size: 2.5rem;
        }
        .selected-info h3 {
            font-size: 1.2rem;
            color: #333;
        }
        .selected-info p {
            color: #888;
            font-size: 0.85rem;
        }
        .config-row {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 16px;
        }
        .config-item label {
            display: block;
            font-size: 0.8rem;
            color: #666;
            margin-bottom: 6px;
        }
        .config-item input {
            width: 100%;
            padding: 10px 14px;
            border: 1px solid #e0e0e0;
            border-radius: 10px;
            font-size: 0.9rem;
        }
        .config-item input:focus {
            outline: none;
            border-color: #667eea;
        }
        .generate-btn {
            width: 100%;
            padding: 16px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 12px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            margin-top: 20px;
        }
        .generate-btn:hover:not(:disabled) {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
        }
        .generate-btn:disabled {
            opacity: 0.6;
            cursor: not-allowed;
        }
        .results-card {
            background: white;
            border-radius: 16px;
            padding: 24px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.08);
        }
        .results-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
        }
        .results-header h3 {
            font-size: 1rem;
            color: #333;
        }
        .export-btns {
            display: flex;
            gap: 8px;
        }
        .export-btn {
            padding: 8px 16px;
            background: #f0f0f0;
            border: none;
            border-radius: 8px;
            font-size: 0.8rem;
            cursor: pointer;
            transition: background 0.2s;
        }
        .export-btn:hover {
            background: #e0e0e0;
        }
        .results-list {
            max-height: 400px;
            overflow-y: auto;
        }
        .result-item {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 12px;
            background: #f8f9fa;
            border-radius: 10px;
            margin-bottom: 8px;
            cursor: pointer;
            transition: background 0.2s;
        }
        .result-item:hover {
            background: #e9ecef;
        }
        .result-item .num {
            color: #aaa;
            font-size: 0.85rem;
            width: 24px;
        }
        .result-item .value {
            flex: 1;
            font-family: 'SF Mono', Monaco, monospace;
            font-size: 0.9rem;
            word-break: break-all;
        }
        .result-item .copy-hint {
            color: #aaa;
            font-size: 0.75rem;
        }
        .empty-state {
            text-align: center;
            padding: 60px 20px;
            color: #888;
        }
        .empty-state .icon {
            font-size: 4rem;
            margin-bottom: 16px;
        }
        .empty-state h3 {
            font-size: 1.2rem;
            color: #555;
            margin-bottom: 8px;
        }
        @media (max-width: 768px) {
            .main-grid {
                grid-template-columns: 1fr;
            }
            .config-row {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Test Data Generator</h1>
            <p>Select a type, customize options, and generate</p>
        </header>
        
        <div class="main-grid">
            <div class="types-panel">
                <h2>Data Types <span id="typeCount"></span></h2>
                <div class="types-grid" id="typesGrid"></div>
            </div>
            
            <div class="generator-panel">
                <div class="config-card">
                    <div class="selected-info" id="selectedInfo">
                        <span class="icon">🎲</span>
                        <div>
                            <h3 id="selectedName">UUID</h3>
                            <p id="selectedType">uuid</p>
                        </div>
                    </div>
                    
                    <div class="config-row">
                        <div class="config-item">
                            <label>Prefix</label>
                            <input type="text" id="prefix" placeholder="e.g., test_">
                        </div>
                        <div class="config-item">
                            <label>Suffix</label>
                            <input type="text" id="suffix" placeholder="e.g., _2024">
                        </div>
                        <div class="config-item">
                            <label>Count</label>
                            <input type="number" id="count" value="5" min="1" max="1000">
                        </div>
                    </div>
                    
                    <button class="generate-btn" id="generateBtn">Generate</button>
                </div>
                
                <div class="results-card" id="resultsCard" style="display: none;">
                    <div class="results-header">
                        <h3 id="resultMessage">✨ Poof! All done!</h3>
                        <div class="export-btns">
                            <button class="export-btn" id="copyAllBtn">Copy All</button>
                            <button class="export-btn" id="jsonBtn">JSON</button>
                            <button class="export-btn" id="csvBtn">CSV</button>
                        </div>
                    </div>
                    <div class="results-list" id="resultsList"></div>
                </div>
                
                <div class="config-card empty-state" id="emptyState">
                    <div class="icon">📦</div>
                    <h3>Ready to Generate!</h3>
                    <p>Select a data type and click generate</p>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        let dataTypes = [];
        let selectedType = 'uuid';
        let results = [];
        let configs = {};
        let openPopup = null;
        
        async function init() {
            try {
                const res = await fetch('/api/types');
                dataTypes = await res.json();
                document.getElementById('typeCount').textContent = dataTypes.length;
                
                dataTypes.forEach(t => {
                    configs[t.type] = { prefix: '', suffix: '', count: 5 };
                });
                
                renderTypes();
                updateSelectedInfo();
            } catch (e) {
                console.error('Failed to load types:', e);
            }
        }
        
        function renderTypes() {
            const grid = document.getElementById('typesGrid');
            grid.innerHTML = dataTypes.map(t => \`
                <div class="type-card \${t.type === selectedType ? 'selected' : ''}" data-type="\${t.type}">
                    <span class="icon">\${t.icon}</span>
                    <span class="name">\${t.name}</span>
                    <div class="gear" onclick="event.stopPropagation(); togglePopup('\${t.type}')">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <circle cx="12" cy="12" r="3"/>
                            <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/>
                        </svg>
                    </div>
                    <div class="options-popup" id="popup-\${t.type}">
                        <label>Prefix</label>
                        <input type="text" value="\${configs[t.type].prefix}" 
                            oninput="updateConfig('\${t.type}', 'prefix', this.value)">
                        <label>Suffix</label>
                        <input type="text" value="\${configs[t.type].suffix}"
                            oninput="updateConfig('\${t.type}', 'suffix', this.value)">
                        <label>Count</label>
                        <input type="number" value="\${configs[t.type].count}" min="1" max="1000"
                            oninput="updateConfig('\${t.type}', 'count', parseInt(this.value))">
                    </div>
                </div>
            \`).join('');
            
            grid.querySelectorAll('.type-card').forEach(card => {
                card.addEventListener('click', () => {
                    selectedType = card.dataset.type;
                    renderTypes();
                    updateSelectedInfo();
                    closePopup();
                });
            });
        }
        
        function updateConfig(type, field, value) {
            configs[type][field] = value;
        }
        
        function togglePopup(type) {
            if (openPopup === type) {
                closePopup();
            } else {
                closePopup();
                openPopup = type;
                renderTypes();
                document.getElementById('popup-' + type).classList.add('show');
            }
        }
        
        function closePopup() {
            openPopup = null;
            renderTypes();
        }
        
        function updateSelectedInfo() {
            const t = dataTypes.find(d => d.type === selectedType);
            document.getElementById('selectedName').textContent = t.name;
            document.getElementById('selectedType').textContent = selectedType;
            document.getElementById('selectedInfo').querySelector('.icon').textContent = t.icon;
            
            const config = configs[selectedType];
            document.getElementById('prefix').value = config.prefix;
            document.getElementById('suffix').value = config.suffix;
            document.getElementById('count').value = config.count;
        }
        
        document.getElementById('prefix').addEventListener('input', e => {
            configs[selectedType].prefix = e.target.value;
        });
        document.getElementById('suffix').addEventListener('input', e => {
            configs[selectedType].suffix = e.target.value;
        });
        document.getElementById('count').addEventListener('input', e => {
            configs[selectedType].count = parseInt(e.target.value) || 1;
        });
        
        document.getElementById('generateBtn').addEventListener('click', async () => {
            const btn = document.getElementById('generateBtn');
            btn.disabled = true;
            btn.textContent = 'Generating...';
            
            try {
                const config = configs[selectedType];
                const res = await fetch('/api/generate', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        type: selectedType,
                        prefix: config.prefix || null,
                        suffix: config.suffix || null,
                        count: config.count
                    })
                });
                
                const data = await res.json();
                results = data.data;
                
                document.getElementById('resultMessage').textContent = data.message;
                document.getElementById('resultsList').innerHTML = results.map((r, i) => \`
                    <div class="result-item" onclick="copyToClipboard('\${r}')">
                        <span class="num">\${i + 1}</span>
                        <span class="value">\${r}</span>
                        <span class="copy-hint">Click to copy</span>
                    </div>
                \`).join('');
                
                document.getElementById('emptyState').style.display = 'none';
                document.getElementById('resultsCard').style.display = 'block';
                
                // Confetti
                confetti({
                    particleCount: 80,
                    spread: 60,
                    origin: { y: 0.6 },
                    colors: ['#667eea', '#764ba2', '#f093fb']
                });
            } catch (e) {
                console.error('Generation failed:', e);
            } finally {
                btn.disabled = false;
                btn.textContent = 'Generate';
            }
        });
        
        async function copyToClipboard(text) {
            await navigator.clipboard.writeText(text);
            const items = document.querySelectorAll('.result-item .value');
            items.forEach(item => {
                if (item.textContent === text) {
                    item.nextElementSibling.textContent = 'Copied!';
                    setTimeout(() => item.nextElementSibling.textContent = 'Click to copy', 1500);
                }
            });
        }
        
        document.getElementById('copyAllBtn').addEventListener('click', async () => {
            await navigator.clipboard.writeText(results.join('\\n'));
        });
        
        document.getElementById('jsonBtn').addEventListener('click', () => {
            const config = configs[selectedType];
            const data = {
                type: selectedType,
                prefix: config.prefix || null,
                suffix: config.suffix || null,
                count: results.length,
                generated_at: new Date().toISOString(),
                data: results
            };
            download(JSON.stringify(data, null, 2), 'test-data.json', 'application/json');
        });
        
        document.getElementById('csvBtn').addEventListener('click', () => {
            download(results.join('\\n'), 'test-data.csv', 'text/csv');
        });
        
        function download(content, filename, type) {
            const blob = new Blob([content], { type });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            a.click();
            URL.revokeObjectURL(url);
        }
        
        document.addEventListener('click', (e) => {
            if (!e.target.closest('.gear') && !e.target.closest('.options-popup')) {
                closePopup();
            }
        });
        
        init();
    </script>
</body>
</html>`;
