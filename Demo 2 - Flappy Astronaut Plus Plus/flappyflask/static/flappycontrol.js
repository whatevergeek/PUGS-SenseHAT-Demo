var game_started = false;
var direction_up = false;

function startgame() {
    if(!game_started)
    {
        game_started = true;
        var url = "http://<place your flappy server here>:5000/flappycmd?cmd=startgame";
        $.get(url, function(response){});
    }
}

function flapup() {
    if(!direction_up)
    {
        direction_up = true;
        var url = "http://<place your flappy server here>:5000/flappycmd?cmd=flapup";
        $.get(url, function(response){});
    }
}

function flapdown() {
    if(direction_up)
    {
        direction_up = false;
        var url = "http://<place your flappy server here>:5000/flappycmd?cmd=flapdown";
        $.get(url, function(response){});
    }
}

function stopgame() {
    if(game_started)
    {
        game_started = false;
        var url = "http://<place your flappy server here>:5000/flappycmd?cmd=stopgame";
        $.get(url, function(response){});
    }
}

$(function() {
    // http://www.cambiaresearch.com/articles/15/javascript-char-codes-key-codes
    $(document).on("keydown", function(e){
        if (e.keyCode === 38)  flapup();// up
        if (e.keyCode === 40)  flapdown(); // down
        if (e.keyCode === 32)  flapup(); // space
        if (e.keyCode === 83)  startgame(); // s 
        if (e.keyCode === 88)  stopgame(); // x
    });

    $(document).on("keyup", function(e){
        if (e.keyCode === 32) flapdown(); // space
    });
})