function openTrack(site) {
    const data = {
        url: window.location.href,
        referrer: document.referrer,
        title: document.title,
        lang: navigator.language,
        screenWidth: window.screen.width,
        screenHeight: window.screen.height,
        userAgent: navigator.userAgent,
        isTouch: ("ontouchstart" in window) || (navigator.msMaxTouchPoints > 0) || (navigator.maxTouchPoints),
    };

    fetch(`http://127.0.0.1:8000/tracks/${site}`, {
        method: "POST",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    })
        .catch((error) => {
            console.error("Error:", error);
        });
}
