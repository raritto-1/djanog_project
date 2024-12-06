document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('message-form');
    const messageInput = document.getElementById('message-input');
    const messageList = document.getElementById('message-list');

    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        
        const message = messageInput.value.trim();
        if (!message) return;

        // Send message to the backend (update with actual WebSocket or AJAX logic)
        messageInput.value = ''; // Clear input
        const listItem = document.createElement('li');
        listItem.textContent = `You: ${message}`;
        messageList.querySelector('ul').appendChild(listItem);
    });
});
