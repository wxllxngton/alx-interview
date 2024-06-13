#!/usr/bin/node

const request = require('request');

/**
 * Recursively prints character names from an array of URLs.
 *
 * @param {string[]} urls - Array of character URLs.
 * @param {number} index - Current index in the array.
 */
const printCharacterNames = (urls, index) => {
  if (index === urls.length) return;
  request(urls[index], (err, response, body) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(JSON.parse(body).name);
    printCharacterNames(urls, index + 1);
  });
};

// Retrieve the Movie ID from the command line arguments
const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide a Movie ID');
  process.exit(1);
}

// Construct the API URL for the specified movie
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

/**
 * Sends a request to the Star Wars API to get the characters of the specified movie.
 *
 * @param {string} apiUrl - URL to the Star Wars API film endpoint.
 */
request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const characters = JSON.parse(body).characters;
  printCharacterNames(characters, 0);
});
