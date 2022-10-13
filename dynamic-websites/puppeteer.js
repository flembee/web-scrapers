const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://airbnb.com/experiences/272085');
  await page.waitForSelector("h1");
  await page.content();
  await browser.close();
})();