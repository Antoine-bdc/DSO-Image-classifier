const { cp } = require('fs');
const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  const content = await page.content();
  for (let i = 0; i <= 4; i++) {
    await page.goto('https://simbad.u-strasbg.fr/simbad/sim-id?Ident=m' + i.toString() + '&submit=submit+id');
    let clip = await new Object();
    clip.x = await 1300;
    clip.y = await 300;
    clip.width = await 260;
    clip.height = await 250;
    if (i > 0) {
      const hrefElement = await page.$('canvas.aladin-reticleCanvas');
      const box = await hrefElement.boundingBox()
      await console.log(box)
      clip.x = await parseInt(box.x);
      clip.y = await parseInt(box.y);
    }
    await page.setViewport({
      width: 1920,
      height: 1080,
    });
    await page.screenshot({
        path: 'image-data/dss/m' + i.toString() + '.png',
        clip,
    });
    
  };
  await browser.close();
})();
