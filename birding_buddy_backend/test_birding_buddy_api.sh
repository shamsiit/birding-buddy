#!/bin/bash

BASE_URL="http://127.0.0.1:8000"

USERNAME="testuser"
EMAIL="testuser@example.com"
PASSWORD="Testpass123"

echo "1️⃣ Registering new user..."
curl -X POST "$BASE_URL/api/users/register/" \
    -H "Content-Type: application/json" \
    -d "{\"username\": \"$USERNAME\", \"email\": \"$EMAIL\", \"password\": \"$PASSWORD\"}"
echo -e "\n"

echo "2️⃣ Logging in to obtain JWT tokens..."
TOKENS=$(curl -s -X POST "$BASE_URL/api/auth/token/" \
    -H "Content-Type: application/json" \
    -d "{\"username\": \"$USERNAME\", \"password\": \"$PASSWORD\"}")
ACCESS_TOKEN=$(echo "$TOKENS" | python3 -c "import sys, json; print(json.load(sys.stdin)['access'])")
echo "Access token: $ACCESS_TOKEN"
echo -e "\n"

echo "3️⃣ Creating a bird sighting..."
curl -X POST "$BASE_URL/api/sightings/" \
    -H "Authorization: Bearer $ACCESS_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
        "species_name": "House Sparrow",
        "count": 5,
        "behavior_notes": "Feeding at window",
        "location_lat": 23.8103,
        "location_long": 90.4125
    }'
echo -e "\n"

echo "4️⃣ Listing all sightings..."
curl -X GET "$BASE_URL/api/sightings/" \
    -H "Authorization: Bearer $ACCESS_TOKEN"
echo -e "\n"

echo "5️⃣ Creating a hotspot..."
curl -X POST "$BASE_URL/api/hotspots/" \
    -H "Content-Type: application/json" \
    -d '{
        "name": "Lalbagh Fort",
        "description": "Common birds near old ruins",
        "location_lat": 23.7188,
        "location_long": 90.3881
    }'
echo -e "\n"

echo "6️⃣ Listing all hotspots..."
curl -X GET "$BASE_URL/api/hotspots/"
echo -e "\n"

echo "7️⃣ Fetching user profile..."
# Get user ID from profile (example assumes ID is 1 — you may update if needed)
curl -X GET "$BASE_URL/api/users/1/" \
    -H "Authorization: Bearer $ACCESS_TOKEN"
echo -e "\n"
