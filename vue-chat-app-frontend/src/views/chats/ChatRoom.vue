<template>
  <div>
    <!-- Your chat interface UI here -->
    <div class="container">
      <h3 class="heading text-center">{{room_slug}}</h3>
      <div class="messaging">
        <div class="inbox_msg">
          <div class="mesgs">

            <div class="chat-messages" id="chat-messages"
            v-for="single_message in messages_list"
            v-bind:key="single_message.id">

              <!-- if-->
              <div v-if="userInfo.user.id===single_message.user.id" class="outgoing_msg">
                <div class="sent_msg">
                  <span>{{single_message.user.username}}(Me)</span>
                  <p>{{single_message.content}}</p>
                  <span class="time_date">{{single_message.created_at}}</span>
                </div>
              </div>

              <!-- else-->
              <div v-else class="incoming_msg">
                <div class="incoming_msg_img"><img src="https://ptetutorials.com/images/user-profile.png" alt="sunil">
                </div>
                <div class="received_msg">
                  <div class="received_withd_msg">
                    <span>{{single_message.user.username}}</span>
                    <p>{{single_message.content}}</p>
                    <span class="time_date">{{single_message.created_at}}</span>
                  </div>
                </div>
              </div>

            </div>

          </div>
        </div>
      </div>

      <div class="lg:w mt-6 mb-6 mx-4 lg:mx-auto p-4 bg-white rounded-xl">
        <form @submit.prevent="sendMessage" class="flex">
          <input v-model="new_submit_message" type="text" name="content" class="flex-1 mr-3" placeholder="Your message..." id="chat-message-input">

          <button class="px-5 py-3 rounded-xl text-white bg-teal-600 hover:bg-teal-700" id="chat-message-submit">Submit
          </button>
        </form>
      </div>

    </div>

  </div>
</template>
  
<script>
import axios from "axios";
export default {
  data() {
    return {
      socket: null,
      room_slug: null,
      messages_list: [],
      userInfo: null,
      new_submit_message: ''
    };
  },
  mounted() {
    this.getAllMessages()
  },
  created() {
    const storedUserInfo = localStorage.getItem('user-info');
    // Parse the JSON string back to an object
    this.userInfo = JSON.parse(storedUserInfo);

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
        'message': this.new_submit_message,
        'username': this.userInfo.user.username,
        'room': this.room_slug
        // Add any other required data
      };
      this.socket.send(JSON.stringify(messageData));
      console.log(messageData)
      this.getAllMessages()
      this.new_submit_message = ''
    },

    async getAllMessages() {
      this.$store.commit('setIsLoading', true)

      this.room_slug = this.$route.params.room_slug

      await axios
          .get(`api/room/${this.room_slug}/messages`)
          .then(responseObj =>{
            this.messages_list = responseObj.data
            console.log(responseObj.data)
            document.title =  room_slug + ' | DjangoChat'
          })
          .catch(errorObj =>{
            console.log(errorObj)
          })

      this.$store.commit('setIsLoading', false)
    },
  },
};
</script>

<style>

body {
  font-family: sans-serif !important;
}

.bg-funky {
  background: #17b2ff;
}

.heading {
  color: #fff;
  margin: 30px;
  font-weight: 600;
}

img {
  max-width: 100%;
}

.inbox_msg {
  border: 1px solid #c4c4c4;
  clear: both;
  overflow: hidden;
}

.top_spac {
  margin: 20px 0 0;
}

.recent_heading {
  float: left;
  width: 40%;
}

.headind_srch {
  padding: 10px 29px 10px 20px;
  overflow: hidden;
  border-bottom: 1px solid #c4c4c4;
}

.recent_heading h4 {
  color: #05728f;
  font-size: 21px;
  margin: auto;
}

.chat_ib h5 {
  font-size: 15px;
  color: #464646;
  margin: 0 0 8px 0;
}

.chat_ib h5 span {
  font-size: 13px;
  float: right;
}

.chat_ib p {
  font-size: 14px;
  color: #989898;
  margin: auto
}

.chat_img {
  float: left;
  width: 11%;
}

.chat_ib {
  float: left;
  padding: 0 0 0 15px;
  width: 88%;
}

.chat_people {
  overflow: hidden;
  clear: both;
}

.chat_list {
  border-bottom: 1px solid #c4c4c4;
  margin: 0;
  padding: 18px 16px 10px;
}

.inbox_chat {
  height: 550px;
  overflow-y: scroll;
}

.active_chat {
  background: #ebebeb;
}

.incoming_msg_img {
  display: inline-block;
  width: 6%;
}

.received_msg {
  display: inline-block;
  padding: 0 0 0 10px;
  vertical-align: top;
  width: 92%;
}

.received_withd_msg p {
  background: #e4e8fb none repeat scroll 0 0;
  border-radius: 3px;
  color: #646464;
  font-size: 14px;
  margin: 0;
  padding: 5px 10px 5px 12px;
  width: 100%;
}

.time_date {
  color: #747474;
  display: block;
  font-size: 10px;
  margin: 3px 0 0;
}

.received_withd_msg {
  width: 100%;
}

.mesgs {
  border: 1px solid #c4c4c4;
  clear: both;
  overflow: hidden;
  padding: 40px;
}

.sent_msg p {
  background: #3F51B5 none repeat scroll 0 0;
  border-radius: 3px;
  font-size: 14px;
  margin: 0;
  color: #fff;
  padding: 5px 10px 5px 12px;
  width: 100%;
}

.outgoing_msg {
  overflow: hidden;
  margin: 26px 0 26px;
}

.sent_msg {
  float: right;
  width: 70%;
  text-align: right;
}

.input_msg_write input {
  background: rgba(0, 0, 0, 0) none repeat scroll 0 0;
  border: medium none;
  color: #4c4c4c;
  font-size: 15px;
  min-height: 48px;
  width: 100%;
}

.type_msg {
  border-top: 1px solid #c4c4c4;
  position: relative;
}

.msg_send_btn {
  background: #05728f none repeat scroll 0 0;
  border: medium none;
  border-radius: 50%;
  color: #fff;
  cursor: pointer;
  font-size: 17px;
  height: 33px;
  position: absolute;
  right: 0;
  top: 11px;
  width: 33px;
}

.messaging {
  background: #fff;
}

.msg_history {
  max-height: 516px;
  overflow-y: auto;
}

.credit {
  margin-bottom: 20px;
  margin-top: 20px;
}

.credit a {
  color: #fff;
  font-weight: 300;
  letter-spacing: 2px;
  border-bottom: dotted 1px;
}
</style>
  