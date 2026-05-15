import requests

def get_data():

    url = "https://api.autopi.io/?format=openapi&_gl=1*cxvtk6*_ga*MjM1Mzg3NjMuMTc3ODEzNzMwNw..*_ga_DB2BZPKYN9*czE3Nzg2OTc2MDEkbzIkZzEkdDE3Nzg2OTg3MzUkajYwJGwwJGgw"

    autopi_api_data = None

    try:
        with requests.Session() as session:
            # 1. Attempt the request
            response = session.get(url, timeout=5)
            print("OK | Data - Attempt the request")

            # Get latecy in seconds or milliseconds
            latency_seconds = response.elapsed.total_seconds()
            print(f"OK | Data - HTTP Latency: {latency_seconds * 1000: .2f} ms")


            # 2. Raise an exception for 4xx or 5xx HTTP status code
            response.raise_for_status()
            print("OK | Data - Raise an exception for 4xx or 5xx HTTP status code")



            # 3. Process the JSON if successful
            content_type = response.headers.get("Content-Type", "")

            if "json" in content_type:
                autopi_api_data = response.json()
                print("OK | Data - Process the JSON if successful")
            else:
                raise ValueError("Error | Data: The server returned a non-JSON response.")
            

    except requests.exceptions.HTTPError as http_err:
        # Catches 404, 500, etc.
        print(f"Data | HTTP error occurred: {http_err}")

    except requests.exceptions.ConnectionError:
        # Catches network issues or wrong URLs
        print("Data | Could not connect to the server.")

    except requests.exceptions.Timeout:
        # Catches requests that take too Long
        print("Data | Error: The request timed out.")

    except requests.exceptions.RequestException as err:
        # Generic catch-all for any other requests-related issues
        print(f"Data | An unexpected error occured: {err}")

    except ValueError:
        # If the API returns malformed JSON, response.json() will raise a ValueError.
        print("Data | Failed to parse JSON response.")


    finally:
        # Always runs, regardless of success of failure
        print("OK | Data - API request attempt finished.")

        # Process data outside the error handling
        if autopi_api_data:
            print(f"\nSuccessfully retrieved {len(autopi_api_data)} data.\n")

    return autopi_api_data