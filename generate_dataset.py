import os
import json

hotels_100 = [
    # Top Luxury & 5-Star Hotels
    {"rank": 1, "name": "ITC Narmada, A Luxury Collection Hotel", "locality": "Vastrapur", "category": "5-star hotel"},
    {"rank": 2, "name": "Taj Skyline Ahmedabad", "locality": "Sindhu Bhavan Road / Bodakdev", "category": "5-star hotel"},
    {"rank": 3, "name": "Hyatt Regency Ahmedabad", "locality": "Ashram Road, Usmanpura", "category": "5-star hotel"},
    {"rank": 4, "name": "Hyatt Ahmedabad", "locality": "Vastrapur", "category": "5-star hotel"},
    {"rank": 5, "name": "Crowne Plaza Ahmedabad City Centre", "locality": "S.G. Highway", "category": "5-star hotel"},
    {"rank": 6, "name": "Radisson Blu Hotel Ahmedabad", "locality": "Panchavati, City Centre", "category": "5-star hotel"},
    {"rank": 7, "name": "Novotel Ahmedabad", "locality": "S.G. Highway", "category": "5-star hotel"},
    {"rank": 8, "name": "Vivanta Ahmedabad SG Highway", "locality": "S.G. Highway", "category": "5-star hotel"},
    {"rank": 9, "name": "DoubleTree by Hilton Ahmedabad", "locality": "Ambli / S.G. Highway", "category": "5-star hotel"},
    {"rank": 10, "name": "Courtyard by Marriott Ahmedabad", "locality": "Satellite / Ramdev Nagar", "category": "5-star hotel"},
    {"rank": 11, "name": "Courtyard by Marriott Ahmedabad Sindhu Bhavan Road", "locality": "Sindhu Bhavan Road", "category": "5-star hotel"},
    {"rank": 12, "name": "The Fern An Ecotel Hotel", "locality": "S.G. Highway", "category": "5-star hotel"},
    {"rank": 13, "name": "The Ummed Ahmedabad Airport", "locality": "Airport Circle, Hansol", "category": "5-star hotel"},
    {"rank": 14, "name": "Pride Plaza Hotel Ahmedabad", "locality": "Judges Bungalow Road", "category": "5-star hotel"},
    {"rank": 15, "name": "Welcomhotel by ITC Hotels", "locality": "Ashram Road", "category": "5-star hotel"},
    {"rank": 16, "name": "Renaissance Ahmedabad Hotel", "locality": "S.G. Highway", "category": "5-star hotel"},
    {"rank": 17, "name": "The House of MG (Heritage Hotel)", "locality": "Lal Darwaja", "category": "Heritage Hotel"},
    
    # 4-Star & Premium Business Hotels
    {"rank": 18, "name": "Four Points by Sheraton Ahmedabad", "locality": "Ellisbridge", "category": "4-star hotel"},
    {"rank": 19, "name": "Fairfield by Marriott Ahmedabad", "locality": "Usmanpura", "category": "4-star hotel"},
    {"rank": 20, "name": "Lemon Tree Premier, The Atrium", "locality": "Khanpur / Riverfront", "category": "4-star hotel"},
    {"rank": 21, "name": "Regenta Central Antarim Hotel", "locality": "Navrangpura", "category": "4-star hotel"},
    {"rank": 22, "name": "Fortune Landmark Ahmedabad", "locality": "Usmanpura", "category": "4-star hotel"},
    {"rank": 23, "name": "The Cama - A Sabarmati Riverfront Hotel", "locality": "Khanpur", "category": "4-star hotel"},
    {"rank": 24, "name": "Holiday Inn Express Ahmedabad Prahlad Nagar", "locality": "Prahlad Nagar", "category": "4-star hotel"},
    {"rank": 25, "name": "Lemon Tree Hotel, Ahmedabad", "locality": "Navrangpura", "category": "4-star hotel"},
    {"rank": 26, "name": "Ramada by Wyndham Ahmedabad", "locality": "Prahlad Nagar", "category": "4-star hotel"},
    {"rank": 27, "name": "Ramada Plaza by Wyndham Ahmedabad SG Highway", "locality": "S.G. Highway", "category": "4-star hotel"},
    {"rank": 28, "name": "BloomSuites l Ahmedabad", "locality": "Satellite", "category": "4-star hotel"},
    {"rank": 29, "name": "Sarovar Portico Ahmedabad", "locality": "Khanpur", "category": "4-star hotel"},
    {"rank": 30, "name": "Fortune Select SG Highway", "locality": "S.G. Highway", "category": "4-star hotel"},
    {"rank": 31, "name": "Hotel Metropole Ahmedabad", "locality": "Subhash Bridge", "category": "4-star hotel"},
    {"rank": 32, "name": "Goldfinch Hotel Ahmedabad", "locality": "C.G. Road", "category": "4-star hotel"},
    {"rank": 33, "name": "Silver Cloud Hotel & Banquets", "locality": "Ashram Road", "category": "4-star hotel"},
    {"rank": 34, "name": "Ginger Ahmedabad (Drive In Road)", "locality": "Drive In Road", "category": "3-star hotel"},
    {"rank": 35, "name": "Ginger Ahmedabad (Changodar)", "locality": "Changodar", "category": "3-star hotel"},
    {"rank": 36, "name": "Ginger Ahmedabad (Satellite)", "locality": "Satellite", "category": "3-star hotel"},
    {"rank": 37, "name": "Treebo Trend Trend Hotel Pinnacle", "locality": "Ellisbridge", "category": "3-star hotel"},
    {"rank": 38, "name": "Hotel Platinum Residency", "locality": "Prahlad Nagar", "category": "3-star hotel"},
    {"rank": 39, "name": "The Grand Bhagwati (TGB)", "locality": "S.G. Highway", "category": "3-star hotel"},
    {"rank": 40, "name": "Clubhouse Nami Residency Sabarmati Riverfront", "locality": "Sabarmati Riverfront", "category": "3-star hotel"},
    {"rank": 41, "name": "Hotel Pleasant Lake", "locality": "Kankaria Lake", "category": "3-star hotel"},
    {"rank": 42, "name": "Radhe Upavan Resort", "locality": "Hathijan", "category": "3-star resort"},
    {"rank": 43, "name": "Rudra Royale Hotel", "locality": "Ellisbridge", "category": "3-star hotel"},
    {"rank": 44, "name": "Hotel Le Grande Residency", "locality": "Ellisbridge", "category": "3-star hotel"},
    {"rank": 45, "name": "Hotel Elysian Residency", "locality": "Bodakdev", "category": "3-star hotel"},
    {"rank": 46, "name": "Hotel German Palace", "locality": "Airport Circle", "category": "3-star hotel"},
    {"rank": 47, "name": "Hotel Nalanda", "locality": "Mithakhali", "category": "3-star hotel"},
    {"rank": 48, "name": "Hotel Classic Inn", "locality": "Navrangpura", "category": "3-star hotel"},
    {"rank": 49, "name": "Toran Gujarat Tourism Hotel", "locality": "Subhash Bridge", "category": "3-star hotel"},
    {"rank": 50, "name": "Hotel SG Residency", "locality": "S.G. Highway", "category": "3-star hotel"},
    {"rank": 51, "name": "Hotel Comfort Inn Sunset", "locality": "Airport Circle", "category": "3-star hotel"},
    {"rank": 52, "name": "Hotel Suba Star", "locality": "Vasna", "category": "3-star hotel"},
    {"rank": 53, "name": "Hotel Kausalya", "locality": "Paldi", "category": "3-star hotel"},
    {"rank": 54, "name": "Express Towers Hotel", "locality": "Ellisbridge", "category": "3-star hotel"},
    {"rank": 55, "name": "Hotel Summit", "locality": "Navrangpura", "category": "3-star hotel"},
    {"rank": 56, "name": "Hotel Royal Highness", "locality": "Lal Darwaja", "category": "3-star hotel"},
    {"rank": 57, "name": "Hotel Classic Gold", "locality": "Navrangpura", "category": "3-star hotel"},
    {"rank": 58, "name": "Hotel Comfort Inn President", "locality": "C.G. Road", "category": "3-star hotel"},
    {"rank": 59, "name": "Zone by The Park Ahmedabad", "locality": "Maninagar", "category": "3-star hotel"},
    {"rank": 60, "name": "Hotel City Inn", "locality": "Kalupur / Railway Station", "category": "3-star hotel"},
    {"rank": 61, "name": "Hotel Chicago", "locality": "Relief Road", "category": "3-star hotel"},
    {"rank": 62, "name": "Hotel Tulip Inn Ahmedabad", "locality": "S.G. Highway", "category": "3-star hotel"},
    {"rank": 63, "name": "FabHotel Corporate Inn", "locality": "Navrangpura", "category": "3-star hotel"},
    {"rank": 64, "name": "FabHotel Prime C.G. Inn", "locality": "C.G. Road", "category": "3-star hotel"},
    {"rank": 65, "name": "FabHotel Kadam", "locality": "Ashram Road", "category": "3-star hotel"},
    {"rank": 66, "name": "Treebo Trend Ambassador", "locality": "Khanpur", "category": "3-star hotel"},
    {"rank": 67, "name": "Treebo Trend Signature", "locality": "S.G. Highway", "category": "3-star hotel"},
    {"rank": 68, "name": "Hotel Riverfront", "locality": "Ashram Road", "category": "3-star hotel"},
    {"rank": 69, "name": "Hotel Grand Sahara", "locality": "Ellisbridge", "category": "3-star hotel"},
    {"rank": 70, "name": "Hotel Pragati The Grand", "locality": "S.G. Highway", "category": "3-star hotel"},
    {"rank": 71, "name": "Hotel Maruti", "locality": "Maninagar", "category": "3-star hotel"},
    {"rank": 72, "name": "Hotel Kuber", "locality": "Kalupur", "category": "3-star hotel"},
    {"rank": 73, "name": "Hotel Ashray", "locality": "Navrangpura", "category": "3-star hotel"},
    {"rank": 74, "name": "Hotel Aakash", "locality": "Lal Darwaja", "category": "3-star hotel"},
    {"rank": 75, "name": "Hotel Neelam", "locality": "Paldi", "category": "3-star hotel"},
    {"rank": 76, "name": "Hotel Swagath", "locality": "Relief Road", "category": "3-star hotel"},
    {"rank": 77, "name": "Hotel Royal", "locality": "Usmanpura", "category": "3-star hotel"},
    {"rank": 78, "name": "Hotel Silver Palace", "locality": "Kalupur", "category": "3-star hotel"},
    {"rank": 79, "name": "Hotel Relax Inn", "locality": "S.G. Highway", "category": "3-star hotel"},
    {"rank": 80, "name": "Hotel Dipak", "locality": "Gita Mandir", "category": "3-star hotel"},
    {"rank": 81, "name": "Hotel Sunrise", "locality": "Satellite", "category": "3-star hotel"},
    {"rank": 82, "name": "Hotel Heritage", "locality": "Prahlad Nagar", "category": "3-star hotel"},
    {"rank": 83, "name": "Hotel Green Orchid", "locality": "Bodakdev", "category": "3-star hotel"},
    {"rank": 84, "name": "Hotel Landmark", "locality": "Usmanpura", "category": "3-star hotel"},
    {"rank": 85, "name": "Hotel Crossway", "locality": "Ashram Road", "category": "3-star hotel"},
    {"rank": 86, "name": "Hotel Park Plaza", "locality": "S.G. Highway", "category": "3-star hotel"},
    {"rank": 87, "name": "Hotel Sahil", "locality": "Lal Darwaja", "category": "3-star hotel"},
    {"rank": 88, "name": "Hotel Crown", "locality": "Khanpur", "category": "3-star hotel"},
    {"rank": 89, "name": "Hotel Shivam", "locality": "Paldi", "category": "3-star hotel"},
    {"rank": 90, "name": "Hotel Imperial", "locality": "Ellisbridge", "category": "3-star hotel"},
    {"rank": 91, "name": "Hotel Crystal", "locality": "Navrangpura", "category": "3-star hotel"},
    {"rank": 92, "name": "Hotel City Palace", "locality": "Kalupur", "category": "3-star hotel"},
    {"rank": 93, "name": "Hotel Golden Plaza", "locality": "Ellisbridge", "category": "3-star hotel"},
    {"rank": 94, "name": "Hotel Prime", "locality": "Ashram Road", "category": "3-star hotel"},
    {"rank": 95, "name": "Hotel Metro", "locality": "C.G. Road", "category": "3-star hotel"},
    {"rank": 96, "name": "Hotel Regency", "locality": "Paldi", "category": "3-star hotel"},
    {"rank": 97, "name": "Hotel Grand Residency", "locality": "Navrangpura", "category": "3-star hotel"},
    {"rank": 98, "name": "Hotel Sunstep", "locality": "C.G. Road", "category": "3-star hotel"},
    {"rank": 99, "name": "Hotel Pinnacle", "locality": "Ellisbridge", "category": "3-star hotel"},
    {"rank": 100, "name": "Hotel Ambassador", "locality": "Khanpur", "category": "3-star hotel"}
]

# Destination folders and files
targets = [
    # 1. dataset/hotels and resturants/
    "dataset/hotels and resturants/ahmedabad_100_hotels.json",
    "dataset/hotels and resturants/hotels and resturants.json",
    # 2. dataset/
    "dataset/ahmedabad_100_hotels.json",
    "dataset/hotels and resturants.json",
    # 3. hotels and resturants/
    "hotels and resturants/ahmedabad_100_hotels.json",
    "hotels and resturants/hotels and resturants.json",
    # 4. Root level
    "ahmedabad_100_hotels.json",
    "hotels and resturants.json"
]

for target in targets:
    os.makedirs(os.path.dirname(target) if os.path.dirname(target) else ".", exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        json.dump(hotels_100, f, indent=2)
    print(f"Created {target}")

print(f"Successfully generated datasets with {len(hotels_100)} hotels.")
