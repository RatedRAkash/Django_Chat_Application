const roomName = JSON.parse(document.getElementById('json-roomname').textContent);
const userName = JSON.parse(document.getElementById('json-username').textContent);

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/'
    + roomName
    + '/'
);

chatSocket.onclose = function (e) {
    console.log('onclose')
}

console.log("Current User:", currentUser);
console.log("Current Email:", currentEmail);

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    if (data.message) {
        currentDate = new Date().toLocaleDateString()

        if (data.username === currentUser) {
            console.log("CurrentUser Message")
            document.querySelector('#chat-messages').innerHTML +=
                `<div class="outgoing_msg">
                <div class="sent_msg">
                  <span>${data.username} (Me)</span>
                  <p>${data.message}</p>
                  <span class="time_date">${currentDate}</span>
                </div>
              </div>`;
        }else{
            console.log("Outside User Message")
            document.querySelector('#chat-messages').innerHTML +=
                `<div class="incoming_msg">
                     <div class="incoming_msg_img"><img src="https://ptetutorials.com/images/user-profile.png" alt="sunil"></div>
                          <div class="received_msg">
                              <div class="received_withd_msg">
                                  <span>${data.username}</span>
                                     <p>${data.message}</p>
                                       <span class="time_date">${currentDate}</span>
                                       </div>
                                    </div>
                </div>`;
        }

    } else {
        alert('The message was empty!')
    }
    scrollToBottom();
};

document.querySelector('#chat-message-input').focus();


// "ENTER" press korle jeno Form Submit hui... eiknae keyCode=13=`ENTER` keyboard
document.querySelector('#chat-message-input').onkeyup = function (e) {
    if (e.keyCode === 13) {
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function (e) {
    // this is to Prevent SUBMIT button Clicks Default Behaviors(CSRF Token Error OFF + Other features OFF which were By Default On)
    // prevent the default behavior of a form submission
    e.preventDefault()

    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;

    console.log({
        'message': message,
        'username': userName,
        'room': roomName
    })

    chatSocket.send(JSON.stringify({
        'message': message,
        'username': userName,
        'room': roomName
    }));

    messageInputDom.value = '';

    return false
};

/**
 * A function for finding the messages element, and scroll to the bottom of it.
 */
function scrollToBottom() {
    let objDiv = document.getElementById("chat-messages");
    objDiv.scrollTop = objDiv.scrollHeight;
}

// Add this below the function to trigger the scroll on load.
scrollToBottom();
