chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
    if (message.action === 'capture_screenshot') {
        fetch('http://localhost:8080/capture')
            .then(response => response.text())
            .then(data => {
                // Handle the response as needed
                console.log(data);
            })
            .catch(error => {
                console.error('Error capturing screenshot:', error);
            });
    }
});
