#Flat list array
run_list = [
    #Lateral Force I tests
    {"run_name": "Run 3", "tire": "Goodyear 20x7-13", "tire_id": "Tire 19", "test_type": "Lateral Force I"},
    {"run_name": "Run 4", "tire": "Hoosier 20x6-13", "tire_id": "Tire 7", "test_type": "Lateral Force I"},
    {"run_name": "Run 5", "tire": "Hoosier 20x7-13", "tire_id": "Tire 13", "test_type": "Lateral Force I"},
    {"run_name": "Run 6", "tire": "Goodyear 20x6.5-13", "tire_id": "Tire 25", "test_type": "Lateral Force I"},
    {"run_name": "Run 13", "tire": "Hoosier 20x6-10", "tire_id": "Tire 4", "test_type": "Lateral Force I"},
    
    #Lateral Force II tests
    {"run_name": "Run 7", "tire": "Goodyear 20x7-13", "tire_id": "Tire 20", "test_type": "Lateral Force II"},
    {"run_name": "Run 8", "tire": "Hoosier 20x6-13", "tire_id": "Tire 8", "test_type": "Lateral Force II"},
    {"run_name": "Run 9", "tire": "Hoosier 20x7-13", "tire_id": "Tire 14", "test_type": "Lateral Force II"},
    {"run_name": "Run 10", "tire": "Goodyear 20x6.5-13", "tire_id": "Tire 26", "test_type": "Lateral Force II"},
    {"run_name": "Run 12", "tire": "Hoosier 20x6-10", "tire_id": "Tire 3", "test_type": "Lateral Force II"},
    
    #Longitudinal Force tests (12 psi)
    {"run_name": "Run 14", "tire": "Goodyear 20x6.5-13", "tire_id": "Tire 27", "test_type": "Longitudinal Force", "psi": 12},
    {"run_name": "Run 16", "tire": "Hoosier 20x6-13", "tire_id": "Tire 9", "test_type": "Longitudinal Force", "psi": 12},
    {"run_name": "Run 18", "tire": "Hoosier 20x7-13", "tire_id": "Tire 15", "test_type": "Longitudinal Force", "psi": 12},
    {"run_name": "Run 20", "tire": "Goodyear 20x7-13", "tire_id": "Tire 21", "test_type": "Longitudinal Force", "psi": 12},
    
    #Longitudinal Force tests (8 psi)
    {"run_name": "Run 15", "tire": "Goodyear 20x6.5-13", "tire_id": "Tire 27", "test_type": "Longitudinal Force", "psi": 8},
    {"run_name": "Run 17", "tire": "Hoosier 20x6-13", "tire_id": "Tire 9", "test_type": "Longitudinal Force", "psi": 8},
    {"run_name": "Run 19", "tire": "Hoosier 20x7-13", "tire_id": "Tire 15", "test_type": "Longitudinal Force", "psi": 8},
    {"run_name": "Run 21", "tire": "Goodyear 20x7-13", "tire_id": "Tire 21", "test_type": "Longitudinal Force", "psi": 8}
]

#Grouped dictionaries
test_data = {
    "Lateral Force I": [
        {"run_name": "Run 3", "tire": "Goodyear 20x7-13", "tire_id": "Tire 19"},
        {"run_name": "Run 4", "tire": "Hoosier 20x6-13", "tire_id": "Tire 7"},
        {"run_name": "Run 5", "tire": "Hoosier 20x7-13", "tire_id": "Tire 13"},
        {"run_name": "Run 6", "tire": "Goodyear 20x6.5-13", "tire_id": "Tire 25"},
        {"run_name": "Run 13", "tire": "Hoosier 20x6-10", "tire_id": "Tire 4"}
    ],
    "Lateral Force II": [
        {"run_name": "Run 7", "tire": "Goodyear 20x7-13", "tire_id": "Tire 20"},
        {"run_name": "Run 8", "tire": "Hoosier 20x6-13", "tire_id": "Tire 8"},
        {"run_name": "Run 9", "tire": "Hoosier 20x7-13", "tire_id": "Tire 14"},
        {"run_name": "Run 10", "tire": "Goodyear 20x6.5-13", "tire_id": "Tire 26"},
        {"run_name": "Run 12", "tire": "Hoosier 20x6-10", "tire_id": "Tire 3"}
    ],
    "Longitudinal Force": {
        "12 psi": [
            {"run_name": "Run 14", "tire": "Goodyear 20x6.5-13", "tire_id": "Tire 27"},
            {"run_name": "Run 16", "tire": "Hoosier 20x6-13", "tire_id": "Tire 9"},
            {"run_name": "Run 18", "tire": "Hoosier 20x7-13", "tire_id": "Tire 15"},
            {"run_name": "Run 20", "tire": "Goodyear 20x7-13", "tire_id": "Tire 21"}
        ],
        "8 psi": [
            {"run_name": "Run 15", "tire": "Goodyear 20x6.5-13", "tire_id": "Tire 27"},
            {"run_name": "Run 17", "tire": "Hoosier 20x6-13", "tire_id": "Tire 9"},
            {"run_name": "Run 19", "tire": "Hoosier 20x7-13", "tire_id": "Tire 15"},
            {"run_name": "Run 21", "tire": "Goodyear 20x7-13", "tire_id": "Tire 21"}
        ]
    }
}