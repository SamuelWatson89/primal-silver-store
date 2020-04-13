const message_ele = document.getElementById("message_container");
if (message_ele) {
  setTimeout(function () {
    message_ele.classList.add("message-exit");
  }, 3000);
}

const over_stock = document.getElementsByClassName("itemOverOrder");
if (over_stock.length > 0) {
  var checkout_button = document.getElementById("checkoutButton");
  checkout_button.disabled = true;
  checkout_button.classList.add("disabled");
}

var product_banner_image = document.getElementById("products-banner-image");
var url = window.location.href.split("/");
var last_item = url[url.length - 2];
if (product_banner_image) {
  product_banner_image.src =
    product_banner_image.src + `banners/${last_item}-banner.jpg`;
} else {
  product_banner_image.src =
    product_banner_image.src + "banners/generic-banner.jpg";
}
