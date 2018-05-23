console.log("Hello, World")
var hello = "Hello from Node JS Variable!"
console.log(hello)
console.log(`Printing variable hello: ${hello}`);
console.log("directory name: " + __dirname);
console.log("directory and file name: " + __filename);
var path = require("path");
console.log(`Hello from file ${path.basename(__filename)}`);
console.log(`Process args: ${process.argv}`)

if (process.argv.length <= 2){
  console.log("USAGE: " + __filename + "IPADDR")
  process.exit(-1)
}
var ip = process.argv[2]
console.log(`Checking IP: ${ip}`)
var dns = require('dns');
function reverseLookup(ip){
    dns.reverse(ip, function(err, domains){
      if(err!=null){
        console.log("Something is wrong with that IP");
      }
      else{
        domains.forEach(function(domain){
          dns.lookup(domain, function(err, address, family){
            console.log(domain,'[',address,']');
          });
        });
      }
    });
}

if (process.argvlength <= 2){
  console.log("USAGE: " + __filename + " IPADDR")
  process.exit(-1)
}

var ip = process.argv[2]
console.log(`Checking IP: ${ip}`)
reverseLookup(ip)
