#!/usr/bin/node

const request = require('request');


// Gets the movie ID from the command line arguments[argv2]

const movie_Id = process.argv[2];

const api_Url = `https://swapi-api.hbtn.io/api/films/${movie_Id}/`;



// Makes a request to the Star Wars API for the movie details

request(api_Url, (error, response, body) => {

  if (error) {

    console.error(error);

    return;

  }



  // Parses the API response

  const film = JSON.parse(body);

  const characters = film.characters;



  // For every character URL, make a request to get the character's name

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
