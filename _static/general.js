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
        Q1: document.querySelector('select[name="Q1"]').value.trim(),
        Q2: document.querySelector('select[name="Q2"]').value.trim(),
        Q3: document.querySelector('input[name="Q3"]').value.trim(),
        Q4: document.querySelector('input[name="Q4"]').value.trim()
    };

    var correctAnswers = {
        Q1: 'True',
        Q2: 'True',
        Q3: '0',
        Q4: '300'
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
    if (errorSpan) {
        errorSpan.textContent = 'Incorrect';
        errorSpan.style.display = 'inline';
    }
  }


// Decision button highlighting for player 1
  function highlightRow(element) {
    // Remove highlight from all cells
    var cells = document.querySelectorAll('td.highlight-g');
    for (var i = 0; i < cells.length; i++) {
        cells[i].classList.remove('highlight-g');
    }

    // Highlight the corresponding row cells to the right
    var row = element.parentNode.parentNode;
    var cellsToHighlight = row.querySelectorAll('td:nth-child(n+' + (element.parentNode.cellIndex + 2) + ')');
    for (var j = 0; j < cellsToHighlight.length; j++) {
        cellsToHighlight[j].classList.add('highlight-g');
    }

    // Change the button color to red
    var confirmButton = document.getElementById('confirmButton');
    confirmButton.style.backgroundColor = 'red';
  }


// Decision button highlighting for player 2
  function highlightCol(element) {
    // Remove highlight from all cells
    var cells = document.querySelectorAll('td.highlight-g');
    for (var i = 0; i < cells.length; i++) {
        cells[i].classList.remove('highlight-g');
    }

    // Highlight the rows below the clicked radio button in the same column
    var cell = element.parentNode;
    var column = cell.cellIndex;
    var table = cell.closest('table');
    var rows = table.querySelectorAll('tr');
    for (var j = cell.parentNode.rowIndex + 1; j < rows.length; j++) {
        var cellsToHighlight = rows[j].querySelectorAll('td:nth-child(' + (column + 1) + ')');
        for (var k = 0; k < cellsToHighlight.length; k++) {
            cellsToHighlight[k].classList.add('highlight-g');
        }
    }

    // Change the button color to red
    var confirmButton = document.getElementById('confirmButton');
    confirmButton.style.backgroundColor = 'red';
  }


// Decision confirmation pop-up
/// Decision Button
  function confirmDecision(event) {
    event.preventDefault(); // Prevents the form from submitting by default
    const decision = document.getElementById("decision");

    const decisionChecked = document.querySelector('input[name="pa_low_advice"]:checked');

    if (!decisionChecked) {
        lowError.textContent = "Field must be selected";
        lowError.style.display = "block";
    } else {
        lowError.style.display = "none";
    }

    // Check if all three are checked before submitting the form
    if (decisionChecked) {
        var confirmationModal = new bootstrap.Modal(document.getElementById('confirmationModal'));
        confirmationModal.show();

        // Handle confirm button click inside the modal
        document.getElementById("confirmButton").onclick = function () {
            confirmationModal.hide();
            document.forms[0].submit();
        };
    }
  }
