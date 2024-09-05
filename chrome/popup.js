document.addEventListener('DOMContentLoaded', function() {
    const sendButton = document.getElementById('send'); // Access the button after DOM is loaded

    if (sendButton) { // Check if the button exists
        sendButton.addEventListener('click', function() {
            const fileInput = document.getElementById('fileInput');
            const question = document.getElementById('question').value;
            const file = fileInput.files[0];

            if (file) {
                const formData = new FormData();
                formData.append('file', file);
                formData.append('question', question);

                fetch('http://localhost:8000/analyze', { // Replace with your server URL
                    method: 'POST',
                    body: formData
                })
                .then(response => response.json())
                .then(data => {
                    document.getElementById('response').innerText = data.result || data.error;
                })
                .catch(error => {
                    console.error('Error:', error);
                    document.getElementById('response').innerText = 'An error occurred. Please try again.';
                });
            } else {
                alert('Please select a file.');
            }
        });
    } else {
        console.error('Send button not found in the DOM.');
    }
});