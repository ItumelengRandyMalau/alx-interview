#!/usr/bin/node



const request = require('request');



// Get the movie ID from the command line arguments

const movieId = process.argv[2];

const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;



// Make a request to the Star Wars API for the movie details

request(apiUrl, (error, response, body) => {

  if (error) {

    console.error(error);

    return;

  }



  // Parse the API response

  const film = JSON.parse(body);

  const characters = film.characters;



  // For each character URL, make a request to get the character's name

  characters.forEach((characterUrl) => {

    request(characterUrl, (error, response, body) => {

      if (error) {

        console.error(error);

        return;

      }



      // Parse the character response and print the name

      const character = JSON.parse(body);

      console.log(character.name);

    });

  });

});

