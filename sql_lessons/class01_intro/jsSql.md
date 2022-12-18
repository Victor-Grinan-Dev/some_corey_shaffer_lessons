# JS and database

## Install

```
npm install mysql
```

## js 
```javascript
const mysql = require('mysql');

const mysql = require('mysql');

const con = mysql.createConnection({
  host: "localhost",
  user: "yourusername",
  password: "yourpassword"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
});
```

### Save the code above in a file called "demo_db_connection.js" and run the file in terminal:
```
node demo_db_connection.js
```
Which will give you this result:

```
Connected!
```
