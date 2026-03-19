import requests

# WhatsApp API endpoint
whatsapp_api_url = 'https://api.whatsapp.com/send'

def respond_to_message(message):
    if message == "T F":
        response = "ok"
        send_response(response)

def send_response(response):
    # Here you would implement your logic to send the response using the WhatsApp API
    # requests.post(whatsapp_api_url, data={'message': response})
    print(response)  # For demo purposes, we'll just print the response

# Example usage
respond_to_message("T F")  # This would output 'ok'