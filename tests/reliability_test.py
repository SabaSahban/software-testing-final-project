import requests
import time
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(filename='reliability_testing.log', level=logging.INFO, format='%(asctime)s - %(message)s')


# Function to perform a request and measure response time
def perform_request(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()
        response_time = end_time - start_time
        if response.status_code == 200:
            logging.info(f"Request to {url} successful. Response time: {response_time:.2f} seconds")
        else:
            logging.warning(f"Request to {url} failed with status code: {response.status_code}")
    except requests.RequestException as e:
        logging.error(f"Request to {url} failed: {str(e)}")


if __name__ == "__main__":
    url = "https://portal.aut.ac.ir/aportal/"
    test_duration_hours = 5/60  # Adjust as per your testing duration

    start_time = datetime.now()
    end_time = start_time + timedelta(hours=test_duration_hours)

    logging.info(f"Starting reliability testing for {test_duration_hours} hours.")

    while datetime.now() < end_time:
        perform_request(url)
        time.sleep(1)  # Adjust interval between requests as needed

    logging.info("Reliability testing completed.")
