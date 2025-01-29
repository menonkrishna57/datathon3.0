let isPaused = false;
const youtubePlayer = document.getElementById('youtubeVideo');
const generatedText = document.getElementById('generatedText');
function regenerateText() {
    generatedText.textContent = "This is the regenerated text at " + new Date().toLocaleTimeString();
    const player = new YT.Player('youtubeVideo', {
        events: {
            'onReady': function(event) {
                event.target.seekTo(0);
                event.target.playVideo();
            }
        }
    });
}
function togglePause() {
    const player = new YT.Player('youtubeVideo', {
        events: {
            'onReady': function(event) {
                if (isPaused) {
                    event.target.playVideo();
                } else {
                    event.target.pauseVideo();
                }
            }
        }
    });
    isPaused = !isPaused;
}
function onYouTubeIframeAPIReady() {
    const player = new YT.Player('youtubeVideo', {
        events: {
            'onReady': function(event) {
                
            }
        }
    });
}
document.getElementById('regenerateButton').addEventListener('click', regenerateText);
document.getElementById('pauseButton').addEventListener('click', togglePause);
const tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
const firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
