import subprocess


def stop_uvicorn():
    """Stop all running uvicorn processes on Windows."""
    try:
        result = subprocess.run(
            ["taskkill", "/F", "/IM", "uvicorn.exe"],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print("✓ Stopped all uvicorn processes")
        else:
            print("No uvicorn processes running")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    stop_uvicorn()
