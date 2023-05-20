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
  

// Scroll to bottom
// $('.msg-page').scrollTop($('.msg-page')[0].scrollHeight);

// // currently working
// $(document).ready(function () {
//     setInterval(function () {
//         $(".msg-page").load(window.location.href + " .msg-page", function() {
//             $('.msg-page').scrollTop($('.msg-page')[1].scrollHeight);
//         });
//     }, 1000);
// });


// suggested and working
$(document).ready(function() {
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
          scrollToBottom();
        },
        error: function(xhr, status, error) {
          console.log("Error: " + error);
        }
      });
    }
  
    refreshMessages();
    setInterval(refreshMessages, 5000);
  });
  
  

