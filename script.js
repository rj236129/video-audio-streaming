// Browser side WebRTC code
const pc = new RTCPeerConnection();
const videoElement = document.getElementById("video");

pc.ontrack = function(event) {
    videoElement.srcObject = event.streams[0];
};

async function start() {
    const offer = await pc.createOffer();
    await pc.setLocalDescription(offer);

    // Send offer to server (Flask + signaling)
    // TODO: signaling server implementation
}

start();
