#!/usr/bin/node

import request from 'request';

/**
 * Fetches data from a given URL using the request module and returns a promise.
 *
 * @param {string} url - The URL to fetch data from.
 * @returns {Promise<Object>} - A promise that resolves with the parsed JSON data.
 */
function get (url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

/**
 * Fetches and prints the names of characters in a Star Wars movie specified by movieID.
 *
 * @param {string} movieID - The ID of the movie to fetch characters from.
 */
async function printCharacters (movieID) {
  try {
    const apiFilmLink = 'https://swapi-api.alx-tools.com/api/films/';
    const filmData = await get(apiFilmLink + movieID);
    const characters = filmData.characters;

    for (const characterUrl of characters) {
      const characterData = await get(characterUrl);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error occurred:', error);
    process.exit(1);
  }
}

// Ensure correct usage
if (process.argv.length !== 3) {
  console.log(`Usage: ${process.argv[1]} movieID`);
  process.exit(1);
}

// Extract movieID from command-line arguments
const movieID = process.argv[2];

// Execute the main function
printCharacters(movieID);
