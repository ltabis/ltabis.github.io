import path from 'path';
import url  from 'url'
// import fs   from 'fs';
import util from 'util';

export const handleRequest = async (req: any, res: any): Promise<void> => {

  const parsed = url.parse(req.url, true);

  console.log(parsed);

  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.write('Response:')
  res.write(util.inspect(parsed.query));
  res.end('End of message');
  // res.end(await fs.promises.readFile(path.join(__dirname, '../index.html'), 'utf8'));
}