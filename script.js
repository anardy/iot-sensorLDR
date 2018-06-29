var py = require('python-shell');
var express = require('express');
var bodyParser = require('body-parser');
var path = require('path');
var mqtt = require('mqtt');

var app = express();
var port = process.env.PORT || 8080;

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

var client = mqtt.connect('mqtt://localhost');

var historico = [];

client.on('connect', function() {
    client.subscribe('sensor-ldr');
});

client.on('message', function(topic, message) {
    var msg = message.toString();
    var obj = JSON.parse(msg);
    console.log(obj)
    historico.push(obj);
});

app.get('/', function(req, res) {
    res.render('index', { data: historico });
});

app.listen(port, function() {
    console.log('servidor rodando');
});