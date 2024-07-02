# academic_chatbot_GGS
Whatsapp Chatbot for Educational Institute

Project Description : 

The Whatsapp Chatbot for Educational Institute is designed to provide automated responses to queries related to the college. The chatbot can answer questions about the college, courses, faculty, schedules, and more. It integrates with the UltraMsg API for Whatsapp communication and uses ChatterBot for natural language processing to generate responses.

Features :

- Automated responses to common queries about the college
- Integration with UltraMsg API for Whatsapp
- Natural Language Processing using ChatterBot
- Easy deployment using ngrok

Project Structure :

```
academic_chatbot_GGS/
│
├── app.py
├── Bot_whatsapp4.py
├── clg.json
├── clgg.json
├── college.json
├── college_data.json
├── hello.py
├── intentions.py
├── requirements.txt
├── textsim2.py
│
├── ngrok/
│   └── ngrok
│
└── README.md
```


Working and Installation Steps :

1. Go to the ngrok folder:
   - Open Command Prompt and navigate to the ngrok folder.
   - Run the following command:
     ```bash
     ngrok.exe http 5000
     ```
   - This will provide some public URLs. Copy the HTTP link.

2. Create an UltraMsg Account:
   - Sign up for an account on UltraMsg.
   - Create a new instance.
   - Log in to your Whatsapp account by scanning the QR code.
   - After logging in, copy the instance ID and paste it into your Python script.
   - Scroll down on the instance page, paste the ngrok HTTP link, and start the webhook.

3. Run the Chatbot:
   - Run the `app.py` file:
     ```bash
     python app.py
     ```

4. Interact with the Chatbot:
   - Send a message to the number associated with the UltraMsg API.
   - Start your query with the chat key `#123`. For example, send `#123` followed by your query.


Required Python Libraries :

Ensure you have the following Python libraries installed for the setup:

- Flask
- ChatterBot
- Requests
- JSON

To install the required libraries, run:
```bash
pip install -r requirements.txt
```

Usage :

1. Start the chatbot by running `app.py`.
2. Use ngrok to expose your local server to the internet.
3. Connect your Whatsapp account to the UltraMsg API.
4. Send a message to the chatbot on Whatsapp and receive automated responses.


Acknowledgements

- [ChatterBot](https://github.com/gunthercox/ChatterBot)
- [Flask](https://flask.palletsprojects.com/)
- [UltraMsg](https://www.ultramsg.com/)

---

