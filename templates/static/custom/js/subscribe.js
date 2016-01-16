var csrf_token = getCsrfToken();
var subscribe_email = $("#subscribe_email");
var subscribe_group = $("#subscribe_group");
var subscribe_status_icon = $("#subscribeStatusIcon");
var subscribe_button = $("#subscribeButton");
var subscribe_text = $("#subscribeText");
var subscribe_nav_bar = $("#subscribeNavBar");

function subscribe() {
  if (!validateEmail(subscribe_email.val())) {
    setErrorClass(subscribe_group);
    setErrorIcon(subscribe_status_icon);
    subscribe_text.text("Please enter Valid Email.");
    return;
  }

  $.ajax({
    url: '/authentication/subscribe',
    type: 'POST',
    data: {
      'email': subscribe_email.val()
    },
    success: function (data) {
      if (data == "done") {
        setSuccessClass(subscribe_group);
        setSuccessIcon(subscribe_status_icon);
        subscribe_email.prop('disabled', true);
        subscribe_button.hide();
        subscribe_text.text("Subscribed");
        setTimeout(function () {
          subscribe_nav_bar.fadeOut();
        }, 2000);
      } else {
        setErrorClass(subscribe_group);
        setErrorIcon(subscribe_status_icon);
      }
    },
    beforeSend: function (xhr, settings) {
      xhr.setRequestHeader("X-CSRFToken", csrf_token);
    },
    error: function (jqXHR, textStatus, errorThrown) {

    }
  });
}
