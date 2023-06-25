$(document).on("submit", "#message", function (e) {
    e.preventDefault();
    $.ajax({
        type: "POST",
        url: "",
        data: {
            body: $("#msg").val(),
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
        },
    });
    $(".chat-container").load(
        window.location.href + " .chat-container",
        function () {
            var msgPage = $(".msg-page");
            msgPage.scrollTop(msgPage.prop("scrollHeight"));
        }
    );
});
  

// suggested and working
function scrollToBottom() {
  var msgPage = $(".msg-page");
  var scrollHeight = msgPage.prop("scrollHeight");
  msgPage.scrollTop(scrollHeight);
}

function refreshMessages() {
  $.ajax({
    url: window.location.href,
    type: "GET",
    dataType: "html",
    success: function(response) {
      var newContent = $(response).find(".msg-page");
      $(".msg-page").replaceWith(newContent);
      // scroll to bottom
    },
    error: function(xhr, status, error) {
      console.log("Error: " + error);
    }
  });
}

$(document).ready(function() {
  refreshMessages();
  setInterval(refreshMessages, 5000);
});

// $(document).ready(function() {

//   $("#message").submit(function(event) {
//     refreshMessages();
//     scrollToBottom();
//   })
// });
