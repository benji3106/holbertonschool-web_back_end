const express = require('express');
const fs = require('fs');

const app = express();
const database = process.argv[2];

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data
        .split('\n')
        .filter((line) => line.trim() !== '');

      const students = lines.slice(1);
      const fields = {};

      students.forEach((student) => {
        const parts = student.split(',');
        const firstname = parts[0];
        const field = parts[3];

        if (!fields[field]) {
          fields[field] = [];
        }

        fields[field].push(firstname);
      });

      const output = [`Number of students: ${students.length}`];

      Object.keys(fields).forEach((field) => {
        const list = fields[field];
        const names = list.join(', ');

        output.push(
          `Number of students in ${field}: ${list.length}. List: ${names}`,
        );
      });

      resolve(output.join('\n'));
    });
  });
}

app.get('/', (request, response) => {
  response.send('Hello Holberton School!');
});

app.get('/students', (request, response) => {
  countStudents(database)
    .then((students) => {
      response.send(`This is the list of our students\n${students}`);
    })
    .catch((error) => {
      response.send(`This is the list of our students\n${error.message}`);
    });
});

app.listen(1245);

module.exports = app;
