from datetime import date
from twilio.rest import Client

# Twilio account credentials
account_sid = 'Twilio Account SID'
auth_token = 'Twilio Account Token'
twilio_phone_number = 'Your Twilio Phone Number'  # This should be the Twilio phone number you purchased

# Your friend's phone number in international format (e.g., '+1234567890')
friend_phone_number = 'Your Friends Phone Number'

# Function to send a text message using Twilio
def send_text_message(to_phone_number, message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=to_phone_number
    )
    return message

# Function to check if it's your friend's birthday (January 29th)
def is_friend_birthday_today():
    today = date.today()
    return today.month == 7 and today.day == 24

# Main function to send the birthday message if it's your friend's birthday
def send_birthday_message():
    if is_friend_birthday_today():
        message = "Happy Birthday! 🎉🎂 Wishing you a fantastic day!"
        try:
            send_text_message(friend_phone_number, message)
            print("Birthday message sent successfully!")
        except Exception as e:
            print(f"Error sending the birthday message: {str(e)}")
    else:
        print("It's not your friend's birthday today.")

# Run the main function
if __name__ == "__main__":
    send_birthday_message()