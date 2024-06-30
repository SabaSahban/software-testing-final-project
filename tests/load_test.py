import subprocess


def run_bombardier(url, concurrency=10, total_requests=1000, duration='30s'):
    command = f"bombardier -c {concurrency} -n {total_requests} -d {duration} {url}"
    print(f"Running command: {command}")

    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        print("\n--- Command output ---")
        print(result.stdout)
        print("\n--- Command error (if any) ---")
        print(result.stderr)
    except Exception as e:
        print(f"Error running bombardier command: {str(e)}")


if __name__ == "__main__":
    url = "https://portal.aut.ac.ir/aportal/"  # Replace with your actual URL
    concurrency = 10
    total_requests = 5000
    duration = '1s'

    run_bombardier(url, concurrency, total_requests, duration)
