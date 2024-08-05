#!/usr/bin/node
const fs = require('fs').promises; // Use promises API for async operations
const { argv } = require('process');

async function getContent(file) {
  try {
    const content = await fs.readFile(file, 'utf8');
    return content;
  } catch (error) {
    console.error(`Failed to read file ${file}: ${error.message}`);
    process.exit(1);
  }
}

(async () => {
  if (argv.length < 5) {
    console.error("Usage: node script.js inputFile1 inputFile2 outputFile");
    process.exit(1);
  }

  try {
    const file1Content = await getContent(argv[2]);
    const file2Content = await getContent(argv[3]);
    const concated = file1Content + file2Content;

    await fs.writeFile(argv[4], concated, 'utf8');
    console.log("Files concatenated successfully.");
  } catch (error) {
    console.error(`An error occurred: ${error.message}`);
    process.exit(1);
  }
})();
