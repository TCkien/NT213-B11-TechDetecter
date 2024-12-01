const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async (req, res) => {
  const { url } = req.body;

  try {
    const response = await axios.get(url);
    const $ = cheerio.load(response.data);

    const scripts = [];
    $('script').each((_, el) => {
      const src = $(el).attr('src');
      if (src) scripts.push(src);
    });

    res.json({ jsLibraries: scripts });
  } catch (error) {
    res.status(500).json({ error: 'Error detecting JavaScript libraries.' });
  }
};
