const message_ele = document.getElementById("message_container");
const over_stock = document.getElementsByClassName("itemOverOrder");

if (message_ele) {
  setTimeout(function () {
    message_ele.classList.add("message-exit");
  }, 3000);
}

if (over_stock.length > 0) {
  var checkout_button = document.getElementById("checkoutButton");
  checkout_button.disabled = true;
  checkout_button.classList.add("disabled");
}
