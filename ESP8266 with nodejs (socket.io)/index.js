var express = require('express');
var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var light = { state: false };

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');
});

app.use(express.static(__dirname + '/public'));

io.on('connection', function(socket) {
    console.log('User connected: ' + socket.id);
    socket.emit('light', light);
    socket.on('disconnect', function() {
        console.log('User disconnected: ' + socket.id);
    });
    socket.on('toggle', function(state) {
        console.log("hit toggle");
        light.state = !light.state;
        console.log('id: ' + socket.id + ' light: ' + light.state);
        io.sockets.emit('light', light);
    });
});

http.listen(8089, '192.168.137.240', function() {
    console.log('listening on *:8089');
});