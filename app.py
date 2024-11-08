from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

mango_conditions = {
    "Thailand": {
        "url": "https://bicon.agriculture.gov.au/BiconWeb4.0/ImportConditions/Conditions?EvaluatableElementId=504544",
        "conditions": [
            "Vapor Heat Treatment (VHT) at 47°C for 20 minutes required",
            "Fresh mangoes must be imported under an approved arrangement",
            "Must be from registered orchards and packhouses approved by Thailand Department of Agriculture",
            "Phytosanitary certificate must be issued by Thailand NPPO",
            "Must be free from quarantine pests including fruit flies",
            "Pre-shipment inspection required by Thailand Department of Agriculture",
            "Must be packed in new, clean containers with ventilation holes",
            "Each box must be marked with treatment date, facility ID, and packhouse code",
            "Random inspection upon arrival in Australia",
            "Fruit must be mature but not ripe",
            "All consignments must be free from leaves, stems, and other plant debris",
            "Temperature sensors and monitoring records required during VHT"
        ]
    },
    "India": {
        "url": "https://bicon.agriculture.gov.au/BiconWeb4.0/ImportConditions/Conditions?EvaluatableElementId=504544",
        "conditions": [
            "Hot water treatment at 48°C for 60 minutes required",
            "Only specific mango varieties allowed: Alphonso, Banganpalli, Chausa, Dashehari, Langra, Mallika",
            "Must be from approved production areas and packhouses",
            "Valid phytosanitary certificate from India NPPO required",
            "Pre-clearance program participation mandatory",
            "Proper labeling with treatment details, facility code, and date",
            "Must be free from specific pests including mango weevil and fruit flies",
            "Post-harvest fungicide treatment required",
            "Maximum transit time restrictions apply",
            "Temperature monitoring records during treatment must be maintained",
            "Sealed containers required for transport",
            "Import permit required before shipment",
            "Break bulk shipments not permitted"
        ]
    },
    "Pakistan": {
        "url": "https://bicon.agriculture.gov.au/BiconWeb4.0/ImportConditions/Conditions?EvaluatableElementId=504544",
        "conditions": [
            "Hot water treatment required with specific temperature-time requirements",
            "Registration of orchards with Pakistan NPPO mandatory",
            "Treatment facility must be approved by Department of Agriculture",
            "Pre-export inspection required",
            "Phytosanitary certificate with additional declarations",
            "Freedom from quarantine pests certification",
            "Specific packaging and labeling requirements",
            "Must be shipped in sealed containers",
            "Inspection on arrival in Australia",
            "Treatment records must accompany shipment"
        ]
    },
    "Philippines": {
        "url": "https://bicon.agriculture.gov.au/BiconWeb4.0/ImportConditions/Conditions?EvaluatableElementId=504544",
        "conditions": [
            "Vapor heat treatment with specific temperature-time protocol",
            "Must be from registered orchards in specific regions",
            "Freedom from mango pulp weevil and seed weevil required",
            "Pre-clearance inspection by Australian authorities",
            "NPPO-issued phytosanitary certificate with additional declarations",
            "Specific packaging requirements with ventilation holes",
            "Each package must be labeled with treatment details",
            "Cold chain maintenance requirements",
            "Maximum transit time specifications",
            "Post-treatment security measures required",
            "Regular pest monitoring records needed",
            "Only commercial consignments accepted"
        ]
    },
    "Fiji": {
        "url": "https://bicon.agriculture.gov.au/BiconWeb4.0/ImportConditions/Conditions?EvaluatableElementId=504544",
        "conditions": [
            "High temperature forced air treatment",
            "Phytosanitary certificate from Fiji NPPO",
            "Must be from registered exporters",
            "Freedom from fruit flies certification",
            "Commercial packaging only",
            "Pre-export verification required"
        ]
    },
    "Mexico": {
        "url": "https://bicon.agriculture.gov.au/BiconWeb4.0/ImportConditions/Conditions?EvaluatableElementId=504544",
        "conditions": [
            "Hot water treatment required",
            "Mexican NPPO certification required",
            "Must be from approved production areas",
            "Freedom from Anastrepha fruit flies",
            "Commercial export packhouse requirement",
            "Treatment certification on packaging"
        ]
    },
    "Vietnam": {
        "url": "https://bicon.agriculture.gov.au/BiconWeb4.0/ImportConditions/Conditions?EvaluatableElementId=504544",
        "conditions": [
            "Irradiation treatment at minimum dose of 400Gy",
            "Alternative VHT treatment option available",
            "Must be from registered orchards and packhouses",
            "Vietnam NPPO phytosanitary certificate required",
            "Pre-export quarantine inspection mandatory",
            "Specific packaging materials approved by Department",
            "Treatment certificate must accompany each consignment",
            "Fruit maturity requirements",
            "Freedom from specific quarantine pests",
            "Security seals on containers required",
            "Detailed labeling requirements including treatment date and facility codes",
            "Import permit required prior to shipment",
            "Transportation temperature monitoring"
        ]
    },
    "Taiwan": {
        "url": "https://bicon.agriculture.gov.au/BiconWeb4.0/ImportConditions/Conditions?EvaluatableElementId=504544",
        "conditions": [
            "Vapor heat treatment required",
            "Taiwan NPPO certification needed",
            "Registered orchard requirement",
            "Freedom from Oriental fruit fly",
            "Specific packaging standards",
            "Pre-export inspection required"
        ]
    },
    "Haiti": {
        "url": "https://bicon.agriculture.gov.au/BiconWeb4.0/ImportConditions/Conditions?EvaluatableElementId=504544",
        "conditions": [
            "Hot water treatment required",
            "Haiti NPPO phytosanitary certificate",
            "Commercial production only",
            "Freedom from fruit flies certification",
            "Approved packaging materials",
            "Pre-export inspection required"
        ]
    }
}

@app.route('/')
def home():
    return render_template('index.html', countries=mango_conditions)

if __name__ == '__main__':
    app.run(debug=True)
