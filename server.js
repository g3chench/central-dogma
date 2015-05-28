var express = require('express');
var app = express();
var mongojs = require('mongojs');
var db = mongojs('centraldogma', ['centraldogma']);
var bodyParser = require('body-parser');
var childProcess = require('child_process');

app.use(express.static(__dirname + "/public"));
app.use(bodyParser.json());

app.get('/getdb', function (req, res) {

    db.centraldogma.find(function (err, docs) {
		res.send(entries);
	});
});

app.post('/convertAA', function (req, res) {

	var script = childProcess.spawn(
     	'python3', ["./sequence.py", req.body.dna]
	);
	var output = ""
	script.stdout.on('data', function (stdout) {
		output = stdout.toString();
	});
	script.on('close', function (code) {
		console.log(output);
       	res.send(output);
    });
});

app.listen(9000);
console.log("Server running on port 9000");
