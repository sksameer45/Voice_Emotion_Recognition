let recorder;
let audioChunks = [];

async function startRecording() {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    recorder = new MediaRecorder(stream);

    recorder.ondataavailable = e => audioChunks.push(e.data);
    recorder.start();
}

async function stopRecording() {
    recorder.stop();

    recorder.onstop = async () => {
        const blob = new Blob(audioChunks, { type: "audio/wav" });
        audioChunks = [];

        const formData = new FormData();
        formData.append("audio", blob);

        const res = await fetch("http://127.0.0.1:5000/analyze", {
            method: "POST",
            body: formData
        });

        const data = await res.json();
        document.getElementById("result").innerText = "Emotion: " + data.emotion;
    };
}
