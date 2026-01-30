import json
import requests


def main():
    base_url = "http://localhost:5000"

    # Test health
    try:
        r = requests.get(f"{base_url}/health", timeout=5)
        print("Health:", r.status_code, r.text)
    except Exception as e:
        print("Erreur lors de l'appel /health:", e)
        return

    # Test predict
    payload = {"message": "URGENT! Gagnez 1000€ maintenant en cliquant ce lien."}
    try:
        r = requests.post(
            f"{base_url}/predict",
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload),
            timeout=5,
        )
        print("Predict:", r.status_code, r.text)
    except Exception as e:
        print("Erreur lors de l'appel /predict:", e)


if __name__ == "__main__":
    main()

