let isPaused = false;
const youtubePlayer = document.getElementById('youtubeVideo');
const generatedText = document.getElementById('generatedText');

// Function to regenerate text
function regenerateText() {
    generatedText.textContent = "This is the regenerated text at " + new Date().toLocaleTimeString();
    // Reset YouTube video to start
    const player = new YT.Player('youtubeVideo', {
        events: {
            'onReady': function(event) {
                event.target.seekTo(0);
                event.target.playVideo();
            }
        }
    });
}

// Function to pause/resume video and audio
function togglePause() {
    const player = new YT.Player('youtubeVideo', {
        events: {
            'onReady': function(event) {
                if (isPaused) {
                    event.target.playVideo();
                    // Resume text-to-speech if applicable
                    // textToSpeech.resume(); // Uncomment if you have a text-to-speech implementation
                } else {
                    event.target.pauseVideo();
                    // Pause text-to-speech if applicable
                    // textToSpeech.pause(); // Uncomment if you have a text-to-speech implementation
                }
            }
        }
    });
    isPaused = !isPaused;
}

// Load YouTube API
function onYouTubeIframeAPIReady() {
    const player = new YT.Player('youtubeVideo', {
        events: {
            'onReady': function(event) {
                // You can add any additional setup here
            }
        }
    });
}

// Event listeners
document.getElementById('regenerateButton').addEventListener('click', regenerateText);
document.getElementById('pauseButton').addEventListener('click', togglePause);

// Load YouTube IFrame API
const tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
const firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);