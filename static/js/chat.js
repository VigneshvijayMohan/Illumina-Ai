// static/js/chat.js

document.addEventListener('DOMContentLoaded', () => {
    const messageForm = document.getElementById('messageForm');
    const messageInput = document.getElementById('messageInput');
    const chatBox = document.getElementById('chatBox');
    const contactList = document.getElementById('contactList');

    let currentContact = null;

    messageForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const message = messageInput.value.trim();
        if (!message || !currentContact) return;

        // Send message via API
        await sendMessage(currentContact, message);

        addMessage('you', message);
        messageInput.value = '';
    });

    async function sendMessage(toUser, message) {
        // Replace with your API endpoint
        await fetch('/api/send/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ to: toUser, message })
        });
    }

    function addMessage(sender, message) {
        const msg = document.createElement('div');
        msg.className = `message ${sender}`;
        msg.innerText = message;
        chatBox.appendChild(msg);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    async function loadContacts() {
        // Replace with your API endpoint
        const res = await fetch('/api/contacts/');
        const users = await res.json();

        users.forEach(user => {
            const li = document.createElement('li');
            li.className = 'list-group-item list-group-item-action';
            li.innerText = user.username;
            li.addEventListener('click', () => {
                currentContact = user.username;
                document.getElementById('chatTitle').innerText = `Chat with ${user.username}`;
                loadMessages(user.username);
            });
            contactList.appendChild(li);
        });
    }

    async function loadMessages(user) {
        chatBox.innerHTML = '';

        // Replace with your API endpoint
        const res = await fetch(`/api/messages/${user}/`);
        const messages = await res.json();

        messages.forEach(msg => {
            addMessage(msg.sender === 'you' ? 'you' : 'other', msg.text);
        });
    }

    loadContacts();
});
