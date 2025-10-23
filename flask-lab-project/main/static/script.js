// Flask Lab Project - Frontend JavaScript

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('dataForm');
    const responseDiv = document.getElementById('response');

    form.addEventListener('submit', async function(e) {
        e.preventDefault();

        const name = document.getElementById('nameInput').value;
        const message = document.getElementById('messageInput').value;

        const data = {
            name: name,
            message: message,
            timestamp: new Date().toISOString()
        };

        try {
            const response = await fetch('/data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();

            if (response.ok) {
                showResponse('success', `✅ Success! Data received: ${JSON.stringify(result.received_data, null, 2)}`);
                form.reset();
            } else {
                showResponse('error', `❌ Error: ${result.message}`);
            }
        } catch (error) {
            showResponse('error', `❌ Network Error: ${error.message}`);
        }
    });

    function showResponse(type, message) {
        responseDiv.className = `response ${type}`;
        responseDiv.textContent = message;
        
        // Auto-hide after 5 seconds
        setTimeout(() => {
            responseDiv.style.display = 'none';
        }, 5000);
    }
});
