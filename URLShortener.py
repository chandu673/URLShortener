import hashlib
class URLShortener :
    def __init__(self):
        self.url_map = {}    
    def generate_short_code(self, url):
        hash_object = hashlib.md5(url.encode())
        short_code = hash_object.hexdigest()[:8]  # Using first 8 characters of MD5 hash
        return short_code   
    def shorten_url(self, url):
        short_code = self.generate_short_code(url)
        self.url_map[short_code] = url
        return f"short.ly/{short_code}"  # Replace with your desired domain   
    def get_original_url(self, short_code):
        return self.url_map.get(short_code, "URL not found")
# Example usage
url_shortener = URLShortener()
long_url = "https://www.example.com/this-is-a-very-long-url-that-needs-to-be-shortened"
short_url = url_shortener.shorten_url(long_url)
print(f"Shortened URL: {short_url}")
original_url = url_shortener.get_original_url(short_url.split("/")[-1])
print(f"Original URL: {original_url}")
