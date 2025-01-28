import cv2
from pyzbar.pyzbar import decode
import requests

def get_content_type(url):
    try:
        response = requests.head(url, allow_redirects=True)
        return response.headers.get('Content-Type', '')
    except:
        return None

def classify_content(content):
    if content.startswith(('http://', 'https://')):
        content_type = get_content_type(content)
        if 'image' in content_type:
            return "Photo"
        elif 'video' in content_type:
            return "Video"
        elif 'text/html' in content_type:
            return "Website"
        return "Other URL" if content_type else "Invalid URL"
    return "Text"

def main():
    cap = cv2.VideoCapture(0)
    print("Scanning for QR code...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        for obj in decode(frame):
            qr_data = obj.data.decode('utf-8')
            print(f"QR Code Data: {qr_data}")
            print(f"Content Type: {classify_content(qr_data)}")
            break

        cv2.imshow("QR Code Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()