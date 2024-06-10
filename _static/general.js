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

    // Get the column index of the clicked radio button
    var cell = element.parentNode;
    var column = cell.cellIndex;

    // Get the table and all its rows
    var table = cell.closest('table');
    var rows = table.querySelectorAll('tr');
    
    // Adjust column index for rows affected by rowspan
    for (var j = cell.parentNode.rowIndex + 1; j < rows.length; j++) {
        var cellsToHighlight = rows[j].querySelectorAll('td, th');
        var offset = 0;

        // Adjust offset if first cell has rowspan
        if (rows[j].querySelector('th[rowspan]') && rows[j].querySelector('th[rowspan]').rowSpan > 1) {
            offset = 1;
        }

        var cellToHighlight = cellsToHighlight[column + offset];
        if (cellToHighlight) {
            cellToHighlight.classList.add('highlight-g');
        }
    }

    // Change the button color to red
    var confirmButton = document.getElementById('cont-btn');
    confirmButton.style.backgroundColor = 'red';
  }


// Decision confirmation pop-up
  function confirmDecision(event) {
    event.preventDefault(); // Prevents the form from submitting by default
    const decision = document.getElementById("decision-choice");

    const decisionChecked = document.querySelector('input[name="decision"]:checked');

    if (!decisionChecked) {
        decision.classList.add('decision-red');
    } else {
      var confirmationModal = new bootstrap.Modal(document.getElementById('confirmationModal'));
      confirmationModal.show();
    }
    // Handle confirm button click inside the modal
    document.getElementById("confirmButton").onclick = function () {
        confirmationModal.hide();
        document.forms[0].submit();
    };
  }