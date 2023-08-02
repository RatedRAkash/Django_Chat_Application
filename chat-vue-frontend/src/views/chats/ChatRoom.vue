<template>
  <div>
    <!-- Your chat interface UI here -->
    <button @click="sendMessage">Send Message</button>
  </div>

  <div class="container">
    <h3 class="heading text-center">{{ single_room.name }}</h3>
    <div class="messaging">
        <div class="inbox_msg">
            <div class="mesgs">
                <div class="chat-messages" id="chat-messages">
                    {% for m in messages %}
                        {% if m.user.username == request.user.username %}
                            <div class="outgoing_msg">
                                <div class="sent_msg">
                                    <span>{{ m.user.username }} (Me)</span>
                                    <p> {{ m.content }}</p>
                                    <span class="time_date"> 11:01 AM    |    June 9</span>
                                </div>
                            </div>

                        {% else %}
                            <div class="incoming_msg">
                                <div class="incoming_msg_img"><img
                                        src="https://ptetutorials.com/images/user-profile.png"
                                        alt="sunil"></div>
                                <div class="received_msg">
                                    <div class="received_withd_msg">
                                        <span>{{ m.user.username }}</span>
                                        <p> {{ m.content }}</p>
                                        <span class="time_date"> 11:01 AM    |    June 9</span>

                                    </div>
                                </div>
                            </div>
                        {% endif %}
                    {% endfor %}
                </div>

            </div>
        </div>

    </div>

    <div class="lg:w mt-6 mb-6 mx-4 lg:mx-auto p-4 bg-white rounded-xl">
        <form method="post" action="." class="flex">
            <input type="text" name="content" class="flex-1 mr-3" placeholder="Your message..."
                   id="chat-message-input">

            <button
                    class="px-5 py-3 rounded-xl text-white bg-teal-600 hover:bg-teal-700"
                    id="chat-message-submit">Submit
            </button>
        </form>
    </div>

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
  