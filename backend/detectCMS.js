const axios = require('axios');

module.exports = async (req, res) => {
  const { url } = req.body;
  const cmsPatterns = ['/wp-admin', '/admin.php'];

  try {
    for (const path of cmsPatterns) {
      const response = await axios.get(`${url}${path}`);
      if (response.status === 200) {
        return res.json({ cms: `Detected CMS with pattern: ${path}` });
      }
    }
    res.json({ cms: 'No CMS detected' });
  } catch (error) {
    res.status(500).json({ error: 'Error detecting CMS.' });
  }
};
