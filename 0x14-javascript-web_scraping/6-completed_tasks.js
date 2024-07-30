#!/usr/bin/node
/*
 script that computes the number of tasks completed by user id.
 first argument is the API URL: https://jsonplaceholder.typicode.com/todos
 print users with completed task
 use the module request
 */
const url = process.argv.slice(2)[0];
const request = require('request');
const completed = [];
const tasks = {};
let i, j;

request(url, { json: true }, (error, response, body) => {
  if (!error) {
    for (i = 0; body[i]; i++) {
      if (body[i].completed) {
        completed.push(body[i].userId);
      }
    }
    for (j = 0; completed[j]; j++) {
      if (tasks[completed[j]] === undefined) {
        tasks[completed[j]] = 1;
      } else {
        tasks[completed[j]] += 1;
      }
    }
  }
  console.log(tasks);
});
