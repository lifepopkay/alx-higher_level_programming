#!/usr/bin/node
// Writes a string to a file
// call the filestream library
const fs = require('fs');

// Read the content of the first
// argument
const content = process.argv[3];
const filepath = process.argv[2];

fs.writeFile(filepath, content, 'utf8', (err) => {
	if (err) {
		console.error(err);
		return;
	}
});
