const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);
      const fields = {};

      students.forEach((line) => {
        const student = line.split(',');
        const firstname = student[0];
        const field = student[3];

        if (!fields[field]) {
          fields[field] = [];
        }

        fields[field].push(firstname);
      });

      console.log(`Number of students: ${students.length}`);

      Object.keys(fields).forEach((field) => {
        const list = fields[field];
        const names = list.join(', ');

        console.log(`Number of students in ${field}: ${list.length}. List: ${names}`);
      });

      resolve();
    });
  });
}

module.exports = countStudents;
