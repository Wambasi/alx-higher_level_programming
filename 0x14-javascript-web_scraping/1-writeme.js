t fs = require('fs');
// get file path
const filePath = process.argv[2];
// get string to write
const stringToWrite = process.argv[3];
// write to the file
fs.writeFile(filePath, stringToWrite, 'utf-8', (err, data) => {
  if (err) { // if error print error
    console.log(err);
  }
});
