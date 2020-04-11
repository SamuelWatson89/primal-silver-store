var message_ele = document.getElementById("message_container");

if (message_ele) {
  setTimeout(function () {
    message_ele.classList.add("message-exit");
  }, 3000);
}
