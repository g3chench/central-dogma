# central-dogma

[The Central Dogma of Molecular Biology](http://en.wikipedia.org/wiki/Central_dogma_of_molecular_biology)

A RESTful API that converts a given DNA sequence into its corresponding RNA and amino acid sequences and stores the information in a Mongo database for later retrieval. Built using the [MEAN](http://mean.io/) stack:

- [MongoDB](https://www.mongodb.org/)
- [Express](http://expressjs.com/)
- [AngularJS](https://angularjs.org/)
- [NodeJS](https://nodejs.org/)

### Dependencies

- [NodeJS](https://nodejs.org/)
- [MongoDB](https://www.mongodb.org/)
- [Python 3](https://www.python.org/)

Install Node modules:

    npm install express
    npm install mongojs
    npm install body-parser

### Development

To set up the app:

- Make sure MongoDB is up by `cd`-ing to its directory and executing
`mongod`

- Run the server with
`node server`

The app runs at
`http://localhost:9000/`
