import requests

# URL of the movie
url = "https://api.marts.ws/embed/movie/52006?season=3&episode=5"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Open a file in binary write mode
    with open("movie.mp4", "wb") as file:
        # Write the content to the file
        file.write(response.content)
    print("Movie downloaded successfully.")
else:
    print(f"Failed to download movie. Status code: {response.status_code}")
