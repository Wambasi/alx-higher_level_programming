t size = parseInt(process.argv[2]);
if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';// appends character x
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
