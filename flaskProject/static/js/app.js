let mediaRecorder;
let audioChunks = [];
let audioBlob;
let audioUrl;
let audio = new Audio();

document.getElementById('startRecording').addEventListener('click', startRecording);
document.getElementById('stopRecording').addEventListener('click', stopRecording);
document.getElementById('playRecording').addEventListener('click', playRecording);
function generateRandomSentence() {
    // 伪代码：生成随机句子并显示在输入框中
    const sentences = ["こんにちは、元気ですか？", "今日はいい天気ですね。", "私の趣味は読書です。","おはようございます"];
    const randomIndex = Math.floor(Math.random() * sentences.length);
    document.getElementById('customSentence').value = sentences[randomIndex];
}


function startRecording() {
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ audio: true })
            .then(stream => {
                mediaRecorder = new MediaRecorder(stream);
                mediaRecorder.start();
                audioChunks = [];

                mediaRecorder.addEventListener("dataavailable", event => {
                    audioChunks.push(event.data);
                });

                mediaRecorder.addEventListener("stop", () => {
                    audioBlob = new Blob(audioChunks);
                    audioUrl = URL.createObjectURL(audioBlob);
                    audio.src = audioUrl;
                });

                document.getElementById('stopRecording').disabled = false;
                document.getElementById('startRecording').disabled = true;
                document.getElementById('playRecording').disabled = true;
            })
            .catch(error => {
                console.error("Error accessing media devices.", error);
            });
    } else {
        alert("Your browser does not support audio recording.");
    }
}

function stopRecording() {
    if (mediaRecorder) {
        mediaRecorder.stop();
        document.getElementById('stopRecording').disabled = true;
        document.getElementById('startRecording').disabled = false;
        document.getElementById('playRecording').disabled = false;
    }
}

function playRecording() {
    if (audioUrl) {
        audio.play();
    } else {
        alert("No recording available to play.");
    }
}
