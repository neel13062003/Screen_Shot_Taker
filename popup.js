const captureButton = document.getElementById("captureBtn");
captureButton.addEventListener('click', function() {
    chrome.runtime.sendMessage({ action: "captureScreenshot" });
});
