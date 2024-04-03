// script.js

$(document).ready(function() {
    // Add your JavaScript/jQuery code here
    $('.image-container img').click(function() {
        var imageUrl = $(this).attr('src');
        var textFileName = imageUrl.replace('.jpg', '.txt');

        // AJAX request to fetch text content
        $.ajax({
            url: '/read_text',
            type: 'GET',
            data: { filename: textFileName },
            success: function(response) {
                // Speak out the text
                speakText(response);
            },
            error: function(xhr, status, error) {
                console.error('Error fetching text:', error);
            }
        });
    });

    // Function to speak out text
    function speakText(text) {
        var msg = new SpeechSynthesisUtterance();
        msg.text = text;
        window.speechSynthesis.speak(msg);
    }
});

