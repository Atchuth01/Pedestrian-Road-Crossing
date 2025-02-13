# Pedestrian-Road-Crossing
Alerts the pedestrians when to cross road using AI openCV 

🏢 Smart Pedestrian Crossing System

📌 Project Overview

The Smart Pedestrian Crossing System is an AI-powered real-time detection system that helps pedestrians decide whether it is safe to cross the road. It uses YOLOv5 for vehicle detection and Norfair for object tracking to monitor traffic and provide crossing recommendations.

🔍 How It Works

🚗 Detects Vehicles: The system identifies vehicles using the YOLOv5 object detection model.

📏 Assigns Lanes: Each detected vehicle is assigned to a specific lane based on its position.

📊 Analyzes Traffic Density: The system tracks vehicle movement and estimates traffic density.

✅ Gives a Decision:

If the traffic is low, the system displays "CROSS ✅" in green.

If the traffic is high, the system displays "DO NOT CROSS ❌" in red.

🎯 Features

✔️ AI-Based Traffic Analysis – Uses deep learning for vehicle detection and tracking.✔️ Lane-Based Traffic Monitoring – Assigns vehicles to specific lanes and counts them.✔️ Real-Time Decision Making – Predicts whether it is safe for pedestrians to cross.✔️ Optimized Performance – Runs on CPU or GPU (CUDA-enabled) for faster processing.✔️ Simple & Lightweight – Uses YOLOv5 and Norfair, ensuring a fast and efficient implementation.


🔧 Installation

Clone the Repository

git clone https://github.com/Atchuth01/Pedestrian Road Crossing.git
cd Smart-Pedestrian-Crossing

Install Dependencies

Install the modules in the file
pip install module_name

Run the System

python pedestrian_crossing.py

👨‍🎓 License

This project is licensed under the MIT License.

##Author

Atchuth V

GitHub: [github.com/Atchuth01]

