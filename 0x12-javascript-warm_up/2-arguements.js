#!/usr/bin/node

const elements = process.argv;

if (elements.length === 2) {
	console.log('No arguement');
}
else if (elements.length === 3) {
	console.log('Arguement found');
}
else {
	console.log('Arguements found')
}
