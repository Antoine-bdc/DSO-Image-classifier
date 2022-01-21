const fs = require('fs');
const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  for (let i = 1; i <= 5387; i++) {
    await page.goto('https://simbad.u-strasbg.fr/simbad/sim-id?Ident=ngc' + i.toString() + '&submit=submit+id');
    const pageData = (await page.content());
    // const NGCContent = (await page.content()).match("NGC " + i.toString());
    // await console.log(NGCContent);s
    // await console.log(typeof(NGCContent));
    // await console.log(typeof(pageData));
    let distance = "  ";
    if (i < 1000) {
      distance = await distance + " ";
    };
    if (i < 100) {
      distance = await distance + " ";
    };
    if (i < 10) {
      distance = await distance + " ";
    };
    const labelIndex = await pageData.indexOf("NGC" + distance + i.toString());
    // await console.log(labelIndex);
    const grossData = pageData.substring(labelIndex, labelIndex + 70);
    const beginningIndex = grossData.indexOf(" --") + 3;
    const finishingIndex = grossData.indexOf("\n       </font>");
    const objectData = grossData.substring(beginningIndex, finishingIndex);
    console.log(objectData, '(' + i.toString() + ')');

    if (i == 1) {
      fs.writeFile('imageData/labels/ngcLabels.txt', objectData + "; NGC " + i.toString(), (err) => {
        if (err) {
            throw err;
        }
      });
    }
    if (i > 1 && objectData != "NG") {
      fs.appendFile('imageData/labels/ngcLabels.txt', objectData + " ; NGC " + i.toString(), (err) => {
        if (err) {
            throw err;
        }
      });

    }
  };
  await browser.close();
})();
