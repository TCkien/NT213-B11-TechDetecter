const axios = require('axios');

module.exports = async (req, res) => {
  const { url } = req.body;

  try {
    const response = await axios.head(url);
    const headers = response.headers;

    if (headers['x-powered-by']) {
      res.json({ framework: `Framework detected: ${headers['x-powered-by']}` });
    } else {
      res.json({ framework: 'No framework detected' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Error detecting framework.' });
  }
};
