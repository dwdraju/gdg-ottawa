
const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

const jokes = [
  "Why did the Ottawa Senators cross the road? To get to the other rink!",
  "What's the difference between a Sens fan and a baby? The baby will stop whining eventually.",
  "I asked my GPS for the fastest way to get to Ottawa. It told me to take the 417, but to be prepared for a long nap.",
  "Why don't they have a professional basketball team in Ottawa? Because no one wants to be a politician and a player at the same time!",
  "What do you call a snowstorm in Ottawa in May? A long weekend."
];

app.get('/', (req, res) => {
  const randomJoke = jokes[Math.floor(Math.random() * jokes.length)];
  const html = `
    <!DOCTYPE html>
    <html>
      <head>
        <title>Ottawa Jokes</title>
        <style>
          body {
            font-family: sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
          }
          .joke-container {
            background-color: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            text-align: center;
          }
        </style>
      </head>
      <body>
        <div class="joke-container">
          <h1>Here's a joke about Ottawa:</h1>
          <p>${randomJoke}</p>
        </div>
      </body>
    </html>
  `;
  res.send(html);
});

app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`);
});
