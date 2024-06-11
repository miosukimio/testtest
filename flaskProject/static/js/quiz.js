let currentAnswer = '';
let currentSelection = null;

function generateQuestion() {
    const questions = [
        {
            question: "听音频并选择正确的发音对应的假名:",
            audio: "sounds/a.mp3",
            correctAnswer: "あ",
            options: ["あ", "い", "う", "え", "お"]
        },
        {
            question: "听音频并选择正确的发音对应的假名:",
            audio: "sounds/ka.mp3",
            correctAnswer: "か",
            options: ["か", "き", "く", "け", "こ"]
        },
         {
            question: "选择正确的罗马音对应「か」:",
            correctAnswer: "ka",
            options: ["ka", "ki", "ku", "ke", "ko"]
        },
        {
            question: "选择与「ア」对应的罗马音:",
            correctAnswer: "a",
            options: ["i", "u", "e", "o", "a"]
        },
         {
        question: "选择正确的罗马音对应「し」:",
        correctAnswer: "shi",
        options: ["sa", "shi", "su", "se", "so"]
    },
    {
        question: "选择与「オ」对应的罗马音:",
        correctAnswer: "o",
        options: ["a", "i", "u", "e", "o"]
    },
    {
        question: "选择正确的罗马音对应「つ」:",
        correctAnswer: "tsu",
        options: ["ta", "chi", "tsu", "te", "to"]
    },
    {
        question: "选择与「ネ」对应的罗马音:",
        correctAnswer: "ne",
        options: ["na", "ni", "nu", "ne", "no"]
    },
    {
        question: "选择正确的罗马音对应「は」:",
        correctAnswer: "ha",
        options: ["ha", "hi", "fu", "he", "ho"]
    },
    {
        question: "选择与「キ」对应的罗马音:",
        correctAnswer: "ki",
        options: ["ka", "ki", "ku", "ke", "ko"]
    },
    {
        question: "选择正确的罗马音对应「む」:",
        correctAnswer: "mu",
        options: ["ma", "mi", "mu", "me", "mo"]
    },
    {
        question: "选择与「ラ」对应的罗马音:",
        correctAnswer: "ra",
        options: ["ra", "ri", "ru", "re", "ro"]
    },
        // 添加更多含音频的问题...
    ];

    const q = questions[Math.floor(Math.random() * questions.length)];
    document.getElementById('question').innerHTML = q.question;
    const audioControl = document.getElementById('audioControl');
    if (q.audio) {
        audioControl.src = q.audio;
        audioControl.hidden = false;
    } else {
        audioControl.hidden = true; // 隐藏音频控件如果没有音频
    }

    const optionsContainer = document.getElementById('options');
    optionsContainer.innerHTML = '';
    q.options.forEach(option => {
        let button = document.createElement('button');
        button.innerHTML = option;
        button.onclick = function() { selectOption(option); };
        optionsContainer.appendChild(button);
    });

    document.getElementById('result').innerHTML = '';
    currentAnswer = q.correctAnswer;
    currentSelection = null;
}
document.getElementById('audioControl').onclick = function() {
    if (this.paused) {
        this.play();
    } else {
        this.pause();
    }
};

function selectOption(selected) {
    currentSelection = selected;
    const optionsContainer = document.getElementById('options');
    Array.from(optionsContainer.children).forEach(button => {
        button.style.backgroundColor = '';
        button.disabled = false;
    });
    event.target.style.backgroundColor = '#add8e6';
    event.target.disabled = true;
}

function checkAnswer() {
    if (currentSelection) {
        const result = document.getElementById('result');
        if (currentSelection === currentAnswer) {
            result.innerHTML = "正确！";
            result.style.color = "green";
        } else {
            result.innerHTML = "错误，正确答案是: " + currentAnswer;
            result.style.color = "red";
        }
    } else {
        document.getElementById('result').innerHTML = "请选择一个选项。";
        document.getElementById('result').style.color = "red";
    }
}
