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

$(document).ready(function() {
    var msgPage = $(".msg-page");
  
    // Set scroll position to bottom
    msgPage.scrollTop(msgPage.prop("scrollHeight"));
  
    setInterval(function() {
      $.ajax({
        url: window.location.href,
        type: "GET",
        dataType: "html",
        success: function(response) {
          var updatedMsgPage = $(response).find(".msg-page");
  
          // Replace the existing .msg-page element
          msgPage.replaceWith(updatedMsgPage);
  
          // Update the reference to the new .msg-page element
          msgPage = updatedMsgPage;
  
          // Set scroll position to bottom if there are new messages
          if (msgPage.prop("scrollHeight") > msgPage.innerHeight()) {
            msgPage.scrollTop(msgPage.prop("scrollHeight"));
          }
        },
        error: function(error) {
          console.log("Error: " + error);
        }
      });
    }, 5000);
  });
  

// This is working
$('.msg-page').scrollTop($('.msg-page')[0].scrollHeight);

  