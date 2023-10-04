document.addEventListener("DOMContentLoaded", function() {
    const captureBtn = document.getElementById("captureBtn");
    captureBtn.addEventListener("click", function() {
        chrome.runtime.sendMessage({ action: "captureScreenshot" });
    });
});
