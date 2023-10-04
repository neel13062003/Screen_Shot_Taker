document.addEventListener('DOMContentLoaded', function() {
    const captureButton = document.getElementById('captureButton');
    const status = document.getElementById('status');

    captureButton.addEventListener('click', function() {
        chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
            chrome.scripting.executeScript({
                target: { tabId: tabs[0].id },
                function: captureScreenshot
            });
        });
    });

    function captureScreenshot() {
        chrome.runtime.sendMessage({ action: 'capture_screenshot' }, function(response) {
            if (response && response.success) {
                status.textContent = 'Screenshot captured and saved.';
            } else {
                status.textContent = 'Error capturing screenshot.';
            }
        });
    }
});
