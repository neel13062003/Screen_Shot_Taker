// chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
//     if (request.action === "captureScreenshot") {
//         chrome.tabs.captureVisibleTab({ format: "png" }, function(dataUrl) {
//             chrome.downloads.download({
//                 url: dataUrl,
//                 filename: "ScreenShot.png",
//                 saveAs: false
//             });
//         });
//     }
// });
// Initialize a counter for screenshot index
let screenshotIndex = 1;

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === "captureScreenshot") {
        const { width, height, left, top } = request;

        chrome.tabs.captureVisibleTab({ format: "png" }, function(dataUrl) {
            const now = new Date();
            const timestamp = now.toISOString().replace(/[:.]/g, "-");
            const filename = `screenshot_${timestamp}_index${screenshotIndex}.png`;
            screenshotIndex++;

            const downloadOptions = {
                url: dataUrl,
                filename: filename,
                saveAs: false
            };

            if (width !== undefined && height !== undefined && left !== undefined && top !== undefined) {
                downloadOptions.clip = {
                    x: left,
                    y: top,
                    width: width,
                    height: height
                };
            }

            chrome.downloads.download(downloadOptions);
        });
    }
});
