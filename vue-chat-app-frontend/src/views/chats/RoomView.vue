<template>
  <div class="p-10 lg:p-20 text-center">
    <h1 class="text-3xl lg:text-6xl text-white">Rooms</h1>
  </div>

  <div class="w-full flex flex-wrap items-center"
       v-for="single_room in room_list"
       v-bind:key="single_room.id">

    <div class="w-full lg:w-1/4 px-3 py-3">
      <div class="p-4 bg-white shadow rounded-xl text-center">
        <h2 class="mb-5 text-2xl font-semibold">{{ single_room.name }}</h2>
        <!--  (``) eita use kore CUSTOM Variable er agge $ use kore amra v-bind:to=""  er moddhe dite pari-->
        <router-link v-bind:to=" `room/${single_room.slug}` " class="px-5 py-3 block rounded-xl text-white bg-teal-600 hover:bg-teal-700">View Details</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ProductBoxComponent from "@/components/ProductBoxComponent.vue";
export default {
  components: {ProductBoxComponent},
  data() {
    return {
      socket: null,
      room_list: [],
    };
  },
  mounted() {
    this.getAllRooms()
  },

  methods: {
    async getAllRooms() {
      this.$store.commit('setIsLoading', true)

      await axios
          .get(`api/rooms`)
          .then(responseObj =>{
            this.room_list = responseObj.data
            console.log(responseObj.data)
            document.title =  'Rooms | DjangoChat'
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
