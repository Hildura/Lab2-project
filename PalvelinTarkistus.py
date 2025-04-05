def handle_request(request):
    if request is None:
        return "Error: Invalid request"
    return f"Handling request: {request}"

# Simuloitu virheellinen pyyntö, joka ennen olisi kaatanut palvelimen
print(handle_request(None))  # Tulostaa: Error: Invalid request


