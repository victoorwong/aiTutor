// JavaScript to handle interactions with the backend

document.getElementById('uploadForm').onsubmit = function(event) {
    event.preventDefault();

    var formData = new FormData();
    formData.append("file", document.getElementById('fileInput').files[0]);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            let quizContent = document.getElementById('quizContent');
            quizContent.innerHTML = JSON.stringify(data.quiz, null, 2);
        })
        .catch(error => console.error('Error:', error));
};
