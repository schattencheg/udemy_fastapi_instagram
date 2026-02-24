import requests
import subprocess
import time
import sys

BASE_URL = "http://127.0.0.1:8000"


def test_health_endpoint():
    """Test if the FastAPI app is running and healthy."""
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=5)
        if response.status_code == 200:
            print("SELFTESTING: OK - Health check passed")
            print(f"  Response: {response.json()}")
            return True
        else:
            print(f"SELFTESTING: FAIL - Unexpected status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("SELFTESTING: FAIL - Cannot connect to server. Is it running?")
        return False
    except requests.exceptions.Timeout:
        print("SELFTESTING: FAIL - Request timed out")
        return False
    except Exception as e:
        print(f"SELFTESTING: FAIL - Error: {e}")
        return False


def run_with_server():
    """Start the server, run tests, then stop it."""
    print("SELFTESTING: Starting FastAPI server...")
    
    # Start the server
    process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # Wait for server to start
    time.sleep(3)
    
    try:
        result = test_health_endpoint()
        return result
    finally:
        print("SELFTESTING: Stopping server...")
        process.terminate()
        process.wait()


if __name__ == "__main__":
    # Check if server is already running or start it for testing
    print("SELFTESTING: Running FastAPI self-test...\n")
    
    # Try testing first (in case server is already running)
    if not test_health_endpoint():
        print("\nSELFTESTING: Server not running, starting it for test...\n")
        success = run_with_server()
        sys.exit(0 if success else 1)
    
    sys.exit(0)
