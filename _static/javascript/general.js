// Websocket for conditional continue buttons
  function validating() {
    document.getElementById('validation').disabled = true;
    document.querySelectorAll('input[type=radio]').forEach(function (radioButton) {
      radioButton.disabled = true
    });
    sessionStorage.setItem('IsClicked', 'true');
    liveSend('send');
  }


  window.onload = function () {
    const IsClicked = sessionStorage.getItem('IsClicked');
      if (IsClicked === 'true') {
          document.getElementById('validation').disabled = true;
      }
  }


  function liveRecv(data) {
    if (data === 'all_ready') {
        sessionStorage.setItem('IsClicked', 'false')
        document.forms[0].submit();
    }
  }


