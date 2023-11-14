#!/usr/bin/node

const fs = require('fs');

function concatFiles(file1Path, file2Path, destinationPath) {
  try {
    const content1 = fs.readFileSync(file1Path, 'utf-8');
    const content2 = fs.readFileSync(file2Path, 'utf-8');

    fs.writeFileSync(destinationPath, content1 + content2);

    console.log(`Files ${file1Path} and ${file2Path} successfully concatenated to ${destinationPath}`);
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
}

if (require.main === module) {
  if (process.argv.length !== 5) {
    console.log('Usage: ./script.js <file1Path> <file2Path> <destinationPath>');
    process.exit(1);
  }

  const file1Path = process.argv[2];
  const file2Path = process.argv[3];
  const destinationPath = process.argv[4];

  concatFiles(file1Path, file2Path, destinationPath);
}

module.exports = concatFiles;

