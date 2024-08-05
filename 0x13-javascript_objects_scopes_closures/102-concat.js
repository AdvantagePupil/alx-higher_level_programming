#!/usr/bin/env node

const fs = require('fs').promises; // Using the promise-based API for async operations
const { argv } = require('process'); // Accessing command line arguments

// Function to read the content of a file asynchronously
async function readFile(filePath) {
  try {
    const content = await fs.readFile(filePath, 'utf8');
    return content;
  } catch (error) {
    console.error(`Failed to read file ${filePath}: ${error.message}`);
    process.exit(1);
  }
}

// Main function to execute the concatenation
async function concatFiles() {
  if (argv.length < 4) {
    console.error("Usage: node script.js <sourceFile1> <sourceFile2> <destination>");
    process.exit(1);
  }

  try {
    const file1Content = await readFile(argv[2]);
    const file2Content = await readFile(argv[3]);
    const combinedContent = `${file1Content}\n${file2Content}`;

    await fs.writeFile(argv[4], combinedContent, 'utf8');
    console.log("Files concatenated successfully.");
  } catch (error) {
    console.error(`An error occurred: ${error.message}`);
    process.exit(1);
  }
}

concatFiles();
