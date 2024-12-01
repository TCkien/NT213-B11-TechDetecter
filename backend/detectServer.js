const axios = require('axios');

module.exports = async (req, res) => {
  const { url } = req.body;

  try {
    const response = await axios.head(url);
    const server = response.headers['server'] || 'Unknown';

    res.json({ server });
  } catch (error) {
    res.status(500).json({ error: 'Error detecting server.' });
  }
};
