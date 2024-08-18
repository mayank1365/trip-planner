# 7-Day Itinerary Planner

This tool helps you prepare a personalized 7-day itinerary by asking for your starting location, destination, date range (either a month or specific dates), and interests. It leverages GPT-4 to generate detailed itineraries and runs in the background.

## Features
- **Interactive Input:** The tool asks for your starting location, destination, and date range (either a month or a specific date).
- **Interest-Based Itinerary:** It gathers your interests to tailor the itinerary to your preferences.
- **Background Processing:** The tool runs in the background, leveraging GPT-4 for itinerary creation.

## Prerequisites
- **Python 3.10+**
- **Poetry Package Manager**
- **Access to Serper API Key**
- **Access to GPT-4:** Ensure you have access to GPT-4 as the tool uses it by default. Note that using GPT-4 may incur costs.

## Setup and Installation

1. **Configure Environment Variables:**
   - Copy the `.env.example` file and rename it to `.env`.
   - Set up the environment variables for Browseless, Serper, and OpenAI in the `.env` file.

2. **Install Dependencies:**
   ```bash
   poetry install --no-root ```

3. **Running the Script**
   ```bash
   python main.py
   ```
   or
   ``` bash 
   python run 
   ```
## **Key Components**
   - ```./main.py```: The main script file responsible for user interaction and initiating the itinerary creation process.
   - ```./tasks.py```: Contains the tasks and prompts used for gathering information and generating the itinerary.
   - ```./agents.py```: Manages the creation and orchestration of agents that handle different aspects of the itinerary planning.
   - ```./tools```: Contains various tool classes utilized by the agents to enhance functionality.


## Sample Output
#### Input given while using OpenAIGPT4 (GPT 4)
  - Travel from - Bangalore, India
  - Travel to - Thailand
  - Travel date - October
  - Interests and hobbies - sightseeing, hiking, eating, culture
```
Day 1: Arrival in Bangkok. Visit the Grand Palace, Wat Pho, and Wat Arun to experience the local culture. Dine at a local restaurant.

Day 2: Explore the Chatuchak Weekend Market for shopping and street food experience. Try out the nightlife at Khao San Road.

Day 3: Travel to Ayutthaya and explore the Ayutthaya Historical Park.

Day 4: Travel to Chiang Mai. Visit the Old City and local temples. Enjoy a traditional Khantoke Dinner and cultural show.

Day 5: Spend the day in the mountains, hike to Doi Inthanon National Park.

Day 6: Visit the Elephant Nature Park. In the evening, explore the Night Bazaar.

Day 7: Departure.

Budget Breakdown for 7 days:
- Average total travel cost: $700
- Accommodation: $224
- Food: $126
- Activities: $133
- Total: $1183

Packing Suggestions:
- Quick-drying clothes and waterproof jackets for rain showers
- Sturdy waterproof footwear
- A good travel backpack
- Quality flip flops
- A day bag
- A reusable water bottle
- Mini LED flashlight
- Waterproof phone pack

Safety Measures:
- Follow local customs and etiquette
- Keep your belongings secure
- Have copies of your important documents
- Stay hydrated and protect yourself from the sun.

Please note these are average costs and actual costs may vary. Prices for restaurants, activities, and accommodations can fluctuate.
```
