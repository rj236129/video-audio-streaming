from flask import Flask, render_template
import cv2
import asyncio
from aiortc import RTCPeerConnection, VideoStreamTrack
import av

app = Flask(__name__)

# Video Capture
cap = cv2.VideoCapture(0)

class VideoTrack(VideoStreamTrack):
    async def recv(self):
        pts, time_base = await self.next_timestamp()
        ret, frame = cap.read()
        if not ret:
            return None
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        video_frame = av.VideoFrame.from_ndarray(frame, format="rgb24")
        video_frame.pts = pts
        video_frame.time_base = time_base
        return video_frame

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
