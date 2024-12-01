const axios = require('axios');

module.exports = async (req, res) => {
  const { url } = req.body;

  try {
    const response = await axios.get(`${url}/api/`);
    res.json({ api: response.data });
  } catch (error) {
    res.status(500).json({ error: 'Error analyzing API.' });
  }
};
