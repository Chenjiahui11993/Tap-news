var jayson = require('jayson');

var client = jayson.client.http({
  hostname: 'localhost',
  port: 4040
});

function add(num1, num2, callback) {
   client.request('add', [num1, num2], function(err, response) {
    if (err) throw err;
    console.log(response);
    callback(response.result);
   });
};

module.exports = {
  add : add
}