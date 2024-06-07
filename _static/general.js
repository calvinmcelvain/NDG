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


// Quiz answer validations
  function checkAnswers() {
    var answers = {
      Q1: document.querySelector('input[name="Q1"]').value.trim(),
      Q2: document.querySelector('input[name="Q2"]').value.trim(),
      Q3: document.querySelector('select[name="Q3"]').value.trim(),
      Q4: document.querySelector('select[name="Q4"]').value.trim(),
    };

    var correctAnswers = {
      Q1: 'True',
      Q2: 'True',
      Q3: 'False',
      Q4: 'True',
    };

    var correct = true;

    // Clear previous error messages
    var errorSpans = document.querySelectorAll('[id^="errorQ"]');
    errorSpans.forEach(function (errorSpan) {
      errorSpan.textContent = '';
      errorSpan.style.display = 'none';
    });

    // Check if all answers are correct
    for (var key in answers) {
      if (answers[key] !== correctAnswers[key]) {
        showErrorMessage(key);
        correct = false;
      }
    }

    if (correct) {
      // Submit the form
      document.forms[0].submit();
    }
  }


  function showErrorMessage(question) {
    var errorSpan = document.getElementById('error' + question);
    errorSpan.textContent = 'Incorrect';
    errorSpan.style.display = 'inline';
  }
