function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

async function SendUserRoundChoice(event) {
    event.preventDefault();

    var selectPlayerName = document.getElementById("select_player_name");
    var selectPlayerChoice = document.getElementById("select_player_choice");

    const response = await fetch(
        SEND_USER_ROUND_CHOICE_URL,
        {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body: JSON.stringify({
                player_name: selectPlayerName.value,
                choice: selectPlayerChoice.value,
            }),
        }
    );
    removeUserFromSelect(selectPlayerName);
}

function removeUserFromSelect(select) {
    for (var i = 0; i < select.length; i++) {
        if (select.options[i].value == select.value) {
            select.remove(i);
        }
    }
    checkSelectState(select);
}

function checkSelectState(select) {
    if (select.options.length === 0) {
        window.location = GAME_URL;
    }
}