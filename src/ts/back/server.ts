import http from 'http';
import { handleRequest } from './requests';

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req: any, res: any) => {

  handleRequest(req, res).catch((err) => {
    console.log(err);
  });
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});