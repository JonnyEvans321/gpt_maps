# gpt_responses.py
import openai
import os
import json

# Replace 'your_api_key' with your actual OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_first_response(prompt):

    messages = [
            {"role": "system", "content": "You are a helpful tour guide. Do not respond to the user directly, just give the response."},
            {"role": "user", "content": "Make me a simple 1 day itinerary for a road trip from Cardiff to London emphasising small towns and nature"},
            {"role": "assistant", "content": """Here's a 1-day itinerary for a road trip from Cardiff to London that takes you through small towns and nature:

1. Start your day early and head out from Cardiff towards Brecon Beacons National Park, one of the most stunning natural areas in Wales. Take a scenic drive through the park, and take a short walk to see some of the famous waterfalls in the area.

2. From there, head towards the small town of Hay-on-Wye, famous for its numerous independent bookshops and as a haven for bibliophiles. Spend some time browsing the shops and exploring the town.

3. Continue your journey towards Ludlow, a beautiful market town in Shropshire. The town has a number of historic timber-framed buildings, as well as a castle and a medieval church. Stop here for lunch and perhaps explore the town a little before hitting the road again.

4. Finally, make your way to the lovely university town of Oxford, famous for its stunning architecture and rich history. Take a stroll through the cobbled streets of the city centre and maybe explore one of the many museums or historic sites in the town. Or, if you're feeling adventurous, head out to the outskirts of town for a short walk in the beautiful countryside.

And that's it! You should reach London late in the evening. I hope this itinerary helps!"""},
            {"role": "user", "content": "Make me a simple 2 day itinerary for a road trip from Athens to Venice emphasising small towns and nature"},
            {"role": "assistant", "content": """Great choice! Here's a 2-day itinerary for a road trip from Athens to Venice that takes you through small towns and nature:

Day 1:

1. Start your journey early in the morning and head towards Meteora, a complex of Eastern Orthodox monasteries situated on top of natural sandstone pillars. Take a guided tour of the monasteries and marvel at the incredible views.

2. Next, drive towards the town of Ioannina, famous for its beautiful lake and historic castle. Take a boat ride on the lake or stroll through the town and explore its many shops and cafes.

3. After lunch, continue on to the village of Zagorochoria, a cluster of 46 picturesque villages nestled in the Pindus Mountains. Take a scenic hike on one of the many trails, or simply drive through the villages and admire the traditional architecture.

4. Spend the night in one of the charming guesthouses in the area.

Day 2:

1. Start your day early and make your way towards the stunning Plitvice Lakes National Park, located in Croatia. Take a walk through the park's series of cascading lakes and waterfalls, and perhaps even take a boat ride or hike to explore more of the area.

2. Finally, drive towards the historic town of Trieste, located on the border of Italy and Slovenia. Take a walk through the narrow streets of the old town and marvel at the stunning architecture, or take a scenic drive along the coast.

And that's it! You can now head towards Venice, which will take you 1-2 hours depending on the traffic."""},
            {"role": "user", "content": prompt}
        ]
    
    first_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    print('first response', first_response['choices'][0]['message']['content'])
    return first_response['choices'][0]['message']['content']

def get_coordinates(first_response):


    # messages.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
    messages = [{"role": "system", "content": "You are a data analyst that must output only what is asked of you in a structured JSON format. Do not output anything other than valid JSON" }]
    messages.append({"role": "user", "content": """Study the following text, then output all the latitude and longitude coordinates of it in JSON array format. Do not output anything other than valid JSON. You must always output valid latitude and longitude values for each placemarker, never null. The format must be an array of objects, each with keys "label", "latitude" and "longitude". The output should be in the same format as this example: [{"label": "Eiffel Tower", "latitude": 48.8582, "longitude": 2.2945}, {"label": "Louvre Museum", "latitude": 48.8606, "longitude": 2.3376}, {"label": "Montmartre", "latitude": 48.8867, "longitude": 2.3431}, {"label": "Sacré-Cœur Basilica", "latitude": 48.8842, "longitude": 2.3488}, {"label": "Notre-Dame Cathedral", "latitude": 48.8529, "longitude": 2.3499}, {"label": "Seine River", "latitude": 48.8606, "longitude": 2.3231}, {"label": "The Marais", "latitude": 48.8588, "longitude": 2.358}] \n """ + first_response})
    
    second_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    
    print('second response', second_response['choices'][0]['message']['content'])
    
    final_dict = json.loads(second_response['choices'][0]['message']['content'])
    print(final_dict)
    
    return final_dict
