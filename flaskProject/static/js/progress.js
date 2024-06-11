// progress.js
document.getElementById('refresh').addEventListener('click', loadProgress);

function loadProgress() {
    // 示例数据，实际应通过AJAX从服务器获取
    const progressData = [
        { lessonTitle: '基础发音教程', status: '完成', score: 95, lastAccessed: '2024-04-12' },
        { lessonTitle: '日常用语速成', status: '进行中', score: 80, lastAccessed: '2024-04-10' }
    ];

    const progressBody = document.getElementById('progress-body');
    progressBody.innerHTML = ''; // 清空现有内容

    progressData.forEach(data => {
        const row = `<tr>
                        <td>${data.lessonTitle}</td>
                        <td>${data.status}</td>
                        <td>${data.score}</td>
                        <td>${data.lastAccessed}</td>
                     </tr>`;
        progressBody.innerHTML += row;
    });
}

// 初始加载
window.onload = loadProgress;
