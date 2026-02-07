"""🎲 Test Data Generator - Unit Tests"""

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestAPIEndpoints:
    """Test API endpoints"""
    
    def test_health_check(self):
        """Test health check endpoint"""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "🎲" in data["message"]
    
    def test_get_data_types(self):
        """Test getting all data types"""
        response = client.get("/api/types")
        assert response.status_code == 200
        data = response.json()
        assert "types" in data
        assert len(data["types"]) > 0
        
        # Check that common types exist
        types = [t["type"] for t in data["types"]]
        assert "uuid" in types
        assert "email" in types
        assert "phone" in types
        assert "name" in types
    
    def test_random_message(self):
        """Test random message endpoint"""
        response = client.get("/api/random-message")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert len(data["message"]) > 0


class TestGenerators:
    """Test data generation"""
    
    def test_generate_uuid(self):
        """Test UUID generation"""
        response = client.post("/api/generate", json={
            "type": "uuid",
            "count": 1
        })
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert len(data["data"]) == 1
        assert len(data["data"][0]) == 36  # UUID length
        
    def test_generate_uuid_with_prefix(self):
        """Test UUID with prefix"""
        response = client.post("/api/generate", json={
            "type": "uuid",
            "prefix": "test_",
            "count": 1
        })
        assert response.status_code == 200
        data = response.json()
        assert data["data"][0].startswith("test_")
        
    def test_generate_uuid_with_suffix(self):
        """Test UUID with suffix"""
        response = client.post("/api/generate", json={
            "type": "uuid",
            "suffix": "_2024",
            "count": 1
        })
        assert response.status_code == 200
        data = response.json()
        assert data["data"][0].endswith("_2024")
        
    def test_generate_uuid_with_prefix_and_suffix(self):
        """Test UUID with both prefix and suffix"""
        response = client.post("/api/generate", json={
            "type": "uuid",
            "prefix": "pre_",
            "suffix": "_suf",
            "count": 1
        })
        assert response.status_code == 200
        data = response.json()
        result = data["data"][0]
        assert result.startswith("pre_")
        assert result.endswith("_suf")
        
    def test_generate_batch(self):
        """Test batch generation"""
        count = 10
        response = client.post("/api/generate", json={
            "type": "name",
            "count": count
        })
        assert response.status_code == 200
        data = response.json()
        assert len(data["data"]) == count
        
    def test_generate_email(self):
        """Test email generation"""
        response = client.post("/api/generate", json={
            "type": "email",
            "count": 3
        })
        assert response.status_code == 200
        data = response.json()
        assert len(data["data"]) == 3
        assert "@" in data["data"][0]
        
    def test_generate_phone(self):
        """Test phone generation"""
        response = client.post("/api/generate", json={
            "type": "phone",
            "count": 5
        })
        assert response.status_code == 200
        data = response.json()
        assert len(data["data"]) == 5
        
    def test_generate_address(self):
        """Test address generation"""
        response = client.post("/api/generate", json={
            "type": "address",
            "count": 2
        })
        assert response.status_code == 200
        data = response.json()
        assert len(data["data"]) == 2
        assert len(data["data"][0]) > 0
        
    def test_generate_imei(self):
        """Test IMEI generation"""
        response = client.post("/api/generate", json={
            "type": "imei",
            "count": 1
        })
        assert response.status_code == 200
        data = response.json()
        imei = data["data"][0]
        assert len(imei) == 15
        assert imei.isdigit()
        
    def test_generate_credit_card(self):
        """Test credit card generation"""
        response = client.post("/api/generate", json={
            "type": "credit_card",
            "count": 1
        })
        assert response.status_code == 200
        data = response.json()
        cc = data["data"][0]
        # Should be formatted with dashes (16-19 chars total)
        assert len(cc) >= 16
        assert "-" in cc
        
    def test_generate_ssn(self):
        """Test SSN generation"""
        response = client.post("/api/generate", json={
            "type": "ssn",
            "count": 1
        })
        assert response.status_code == 200
        data = response.json()
        ssn = data["data"][0]
        # SSN format: XXX-XX-XXXX
        assert len(ssn) == 11
        assert "-" in ssn
        
    def test_generate_ip(self):
        """Test IP address generation"""
        response = client.post("/api/generate", json={
            "type": "ip",
            "count": 1
        })
        assert response.status_code == 200
        data = response.json()
        ip = data["data"][0]
        # Should contain dots or colons
        assert "." in ip or ":" in ip
        
    def test_generate_url(self):
        """Test URL generation"""
        response = client.post("/api/generate", json={
            "type": "url",
            "count": 1
        })
        assert response.status_code == 200
        data = response.json()
        url = data["data"][0]
        assert url.startswith("https://")
        
    def test_generate_hex_color(self):
        """Test hex color generation"""
        response = client.post("/api/generate", json={
            "type": "hex_color",
            "count": 1
        })
        assert response.status_code == 200
        data = response.json()
        color = data["data"][0]
        assert color.startswith("#")
        assert len(color) == 7
        assert all(c in "0123456789abcdefABCDEF" for c in color[1:])
        
    def test_generate_username(self):
        """Test username generation"""
        response = client.post("/api/generate", json={
            "type": "username",
            "count": 3
        })
        assert response.status_code == 200
        data = response.json()
        assert len(data["data"]) == 3
        assert " " not in data["data"][0]  # No spaces in username
        
    def test_generate_password(self):
        """Test password generation"""
        response = client.post("/api/generate", json={
            "type": "password",
            "count": 1
        })
        assert response.status_code == 200
        data = response.json()
        password = data["data"][0]
        assert len(password) == 16


class TestValidation:
    """Test input validation"""
    
    def test_invalid_type(self):
        """Test invalid data type"""
        response = client.post("/api/generate", json={
            "type": "invalid_type_xyz",
            "count": 1
        })
        assert response.status_code == 400
        data = response.json()
        assert "detail" in data
        assert "Unknown type" in data["detail"]
        
    def test_invalid_count_too_low(self):
        """Test count too low"""
        response = client.post("/api/generate", json={
            "type": "uuid",
            "count": 0
        })
        assert response.status_code == 400
        
    def test_invalid_count_too_high(self):
        """Test count too high"""
        response = client.post("/api/generate", json={
            "type": "uuid",
            "count": 1001
        })
        assert response.status_code == 400


class TestPrefixSuffixLogic:
    """Test prefix/suffix truncation logic"""
    
    def test_prefix_truncates_data(self):
        """Test that prefix causes data truncation"""
        # Generate UUID with prefix - result should maintain UUID length (36)
        response = client.post("/api/generate", json={
            "type": "uuid",
            "prefix": "test_",
            "count": 1
        })
        data = response.json()
        result = data["data"][0]
        # UUID is 36 chars, prefix is 5, so truncated UUID should be 31 chars
        assert len(result) == 36
        assert result.startswith("test_")
        
    def test_suffix_truncates_data(self):
        """Test that suffix causes data truncation"""
        response = client.post("/api/generate", json={
            "type": "uuid",
            "suffix": "_prod",
            "count": 1
        })
        data = response.json()
        result = data["data"][0]
        # UUID is 36 chars, suffix is 5, so truncated UUID should be 31 chars
        assert len(result) == 36
        assert result.endswith("_prod")
        
    def test_both_prefix_and_suffix(self):
        """Test that both prefix and suffix truncate data"""
        response = client.post("/api/generate", json={
            "type": "uuid",
            "prefix": "pre_",
            "suffix": "_suf",
            "count": 1
        })
        data = response.json()
        result = data["data"][0]
        # Total should be ~36 chars
        assert len(result) == 36
        assert result.startswith("pre_")
        assert result.endswith("_suf")
        

class TestAllDataTypes:
    """Test all available data types"""
    
    types_to_test = [
        "uuid", "phone", "email", "address", "name", "imei",
        "credit_card", "ssn", "ip", "date", "datetime", "username",
        "password", "company", "job", "country", "city", "street",
        "zipcode", "text", "sentence", "paragraph", "hex_color",
        "rgb_color", "url", "ipv4", "ipv6", "mac_address", "isbn", "barcode"
    ]
    
    @pytest.mark.parametrize("data_type", types_to_test)
    def test_all_types_generate(self, data_type):
        """Test that all data types can generate"""
        response = client.post("/api/generate", json={
            "type": data_type,
            "count": 1
        })
        assert response.status_code == 200, f"Failed for type: {data_type}"
        data = response.json()
        assert data["success"] is True
        assert len(data["data"]) == 1
        assert len(data["data"][0]) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
