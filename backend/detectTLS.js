const tls = require('tls');

module.exports = (req, res) => {
  const { url } = req.body;

  const options = {
    host: url.replace(/https?:\/\//, ''),
    port: 443,
    servername: url.replace(/https?:\/\//, ''),
  };

  const socket = tls.connect(options, () => {
    const certificate = socket.getPeerCertificate();
    res.json({ tls: certificate });
    socket.end();
  });

  socket.on('error', () => {
    res.status(500).json({ error: 'Error detecting TLS certificate.' });
  });
};
