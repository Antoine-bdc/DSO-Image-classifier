const fs = require('fs');
const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  twoMassDx = await 71;
  twoMassDy = await 260;
  dssDx = await 119;
  dssDy = await 260;

  // Preload the page for screenshot:
  await page.goto('https://simbad.u-strasbg.fr/simbad/sim-id?Ident=ngc1');
  // await console.log(i)
  let clip = await new Object();
  clip.x = await 1300;
  clip.y = await 300;
  clip.width = await 259;
  clip.height = await 249;

  await page.setViewport({
    width: 1920,
    height: 1080,
  });
  await page.mouse.click(10 + dssDx, 10 + dssDy)
  await new Promise(r => setTimeout(r, 300)); // needed to confirm the page loads
  await page.screenshot({
    path: '../data/imageData/other/preload_1.png',
    clip,
  });
  await page.mouse.click(10 + twoMassDx, 10 + twoMassDy)
  await new Promise(r => setTimeout(r, 300)); // needed to confirm the page loads
  await page.screenshot({
      path: '../data/imageData/other/preload_2.png',
      clip,
  });

  for (let i = 1; i <= 5387; i++) {  // max NGC 5387
    await page.goto('https://simbad.u-strasbg.fr/simbad/sim-id?Ident=ngc' + i.toString());  //  + '&submit=submit+id'
    // await console.log(i)
    let clip = await new Object();
    clip.x = await 1300;
    clip.y = await 300;
    clip.width = await 259;
    clip.height = await 249;
    if (i > 0) {
      try {
        const boxElement = await page.$('canvas.aladin-reticleCanvas');
        
        const box = await boxElement.boundingBox()
        clip.x = await parseInt(box.x) + 1;
        clip.y = await parseInt(box.y) + 1;
        await page.setViewport({
          width: 1920,
          height: 1080,
        });
        await page.mouse.click(clip.x + dssDx, clip.y + dssDy)
        await new Promise(r => setTimeout(r, 300)); // needed to confirm the page loads
        await page.screenshot({
          path: '../data/imageData/dss/ngc' + i.toString() + '.png',
          clip,
        });
        await page.mouse.click(clip.x + twoMassDx, clip.y + twoMassDy)
        await new Promise(r => setTimeout(r, 300)); // needed to confirm the page loads
        await page.screenshot({
            path: '../data/imageData/2mass/ngc' + i.toString() + '.png',
            clip,
        });
      }
      catch (error) {
        console.log(i);
        fs.appendFile('../data/imageData/nonConformingData.txt', i.toString() + '\n', (err) => {
          if (err) {
              throw err;
          }
        });
      };
    }
    
  };
  await browser.close();
})();
