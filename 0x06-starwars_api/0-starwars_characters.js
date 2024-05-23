#!/usr/bin/node

const https = require('https');

function fetchUrl(url) {
  return new Promise((resolve, reject) => {
    https.get(url, (res) => {
      let data = '';

      res.on('data', (chunk) => {
        data += chunk;
      });

      res.on('end', () => {
        resolve(JSON.parse(data));
      });
    }).on('error', (err) => {
      reject(err);
    });
  });
}

async function getMovieCharacters(movieId) {
  const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
  const movieUrl = `${baseUrl}${movieId}/`;

  try {
    const movieData = await fetchUrl(movieUrl);
    const characters = movieData.characters;

    for (const characterUrl of characters) {
      try {
        const characterData = await fetchUrl(characterUrl);
        console.log(characterData.name);
      } catch (error) {
        console.error(`Failed to fetch character data: ${error.message}`);
      }
    }
  } catch (error) {
    console.error(`Failed to fetch data for movie ID ${movieId}: ${error.message}`);
  }
}

const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: node script.js <movie_id>');
  process.exit(1);
}

getMovieCharacters(movieId);
