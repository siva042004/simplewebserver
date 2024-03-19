from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
<title>Revenue Table</title>
<caption> REVENUE TABLE</caption>
</head>
<body>
<table border ="2" cellpadding="2" width="400" heigth="400" bgcolor="yellow">

<tr bgcolor="green">


<th>s.no</th>

<th>Company Name</th>
<th>2020 USD</th>
<th>2021 USD</th>
<th>Industry</th>



</tr>

<tr>


<td>1</td>
<td>jio</td>
<td>961.3</td>
<td>998.3</td>
<td>Tech</td>


</tr>
<tr >


<td>2</td>
<td>zoho</td>
<td>946.5</td>
<td>800.8</td>
<td>Tech</td>


</tr>

<tr >


<td>3</td>
<td>Amazon.com</td>
<td>916.1</td>
<td>900.8</td>
<td>Tech</td>


</tr>
<tr >


<td>4</td>
<td>Alphabet</td>
<td>863.2</td>
<td>850.9</td>
<td>Tech</td>


</tr>
<tr >


<td>5</td>
<td>apple</td>
<td>516.4</td>
<td>456.9</td>
<td>Financials</td>


</tr>
<tr >


<td>6</td>
<td>Alibab</td>
<td>480.8</td>
<td>444.9</td>
<td>Tech</td>


</tr>











</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()