var http = require('http');
var fs = require('fs');
var os = require('os');
var ip = require('ip');

http.createServer(function(req, res){
    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8",function(err,body){
            res.writeHead(200, {"Content-Type":"text/html"});
            res.end(body);
        });
    }
    else if (req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        uptime = function(){
            var up_time_secs = os.uptime()
            var up_days = Math.floor(up_time_secs / 86400)
            up_time_secs = up_time_secs - (up_days * 86400)
            var up_hours = Math.floor(up_time_secs / 3600)
            up_time_secs = up_time_secs - (up_hours * 3600)
            var up_mins = Math.floor(up_time_secs / 60)
            up_time_secs = up_time_secs - (up_mins * 60)
            var up_secs = up_time_secs
            return `Days: ${up_days}, Hours: ${up_hours}, Minutes: ${up_mins}, Seconds: ${up_secs}`
        }
        totalmem = function(){
            return (os.totalmem() / (10**6))
        }
        freemem = function(){
            return (os.freemem() / (10**6))
        }
        cpu_num = function(){
            return os.cpus().length
        }
        html=`
            <!DOCTYPE html>
            <html>
                <head>
                    <title>Node JS Response</title>
                </head>
                <body>
                    <p>Hostname: ${myHostName}</p>
                    <p>IP: ${ip.address()}</p>
                    <p>Server Uptime: ${uptime()}</p>
                    <p>Total Memory: ${totalmem()}</p>
                    <p>Free Memory: ${freemem()}</p>
                    <p>Number of CPUs: ${cpu_num()}</p>
                </body>
            </html>`
        res.writeHead(200, {"Content-Type":"text/html"});
        res.end(html)
    }
    else{
        res.writeHead(404, {"Content-Type":"text/plain"});
        res.end("404 File Not Found");
    }
}).listen(3000)
console.log("Server listening on port 3000")
