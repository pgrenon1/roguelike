console.log('server is starting...');

// var data = require('data/entities.json');
var express = require('express');

var app = express();
var server = app.listen(process.env.PORT || 3000, listening);

function listening() {
    console.log('listening...');
}

app.use(express.static('public'));

// function tweeted(err, data, response) {
//     console.log(data);
// }

app.get("/publish/:json", publish);

function publish(request, response) {
    console.log(request)
    // var data = request.params.json
    // console.log(data);
    // T.post('statuses/update', tweet, tweeted);
}