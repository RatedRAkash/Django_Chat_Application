<template>
    <div>
      <!-- Your chat interface UI here -->
      <button @click="sendMessage">Send Message</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        socket: null,
      };
    },
    created() {
      // Connect to the Django WebSocket URL
      const webSocketUrl = 'ws://localhost:7070/ws/office/';
      this.socket = new WebSocket(webSocketUrl);
  
      // Handle incoming messages from the WebSocket
      this.socket.onmessage = (event) => {
        const message = JSON.parse(event.data);
        // Process the received message here
      };
    },
    methods: {
      sendMessage(message) {
        // Send a message to the Django WebSocket
        const messageData = {
            'message': "Hello",
            'username': "admin",
            'room': "office"
          // Add any other required data
        };
        this.socket.send(JSON.stringify(messageData));
        console.log(messageData)
      },
    },
  };
  </script>
  