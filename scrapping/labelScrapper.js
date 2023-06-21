const fs = require('fs');
const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setDefaultNavigationTimeout(0); 
  var NALabelString = await fs.readFileSync("../data/rawData/nonConformingData.txt").toString().split('\n');
  var NALabelInt = [];
  for (value in NALabelString) {
    await NALabelInt.push(parseInt(NALabelString[value]));
  };
  await NALabelInt.pop();
  
  for (let i = 1; i <=  5387; i++) {
    await page.goto('https://simbad.u-strasbg.fr/simbad/sim-id?Ident=ngc' + i.toString() + '&submit=submit+id');
    const pageData = (await page.content());
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
    const grossData = pageData.substring(labelIndex, labelIndex + 120);
    const beginningIndex = grossData.indexOf(" --") + 3;
    const finishingIndex = grossData.indexOf("\n        </font>");
    const objectData = grossData.substring(beginningIndex, finishingIndex);
    
    if (i == 1) {
      console.log(objectData, '(' + i.toString() + ')');
      fs.writeFile('../data/rawData/labels/ngcLabels.txt', objectData + "; NGC " + i.toString(), (err) => {
        if (err) {
          throw err;
        }
      });
    }
    if ((i > 1) && !(NALabelInt.includes(i)) && (objectData != '<!') && (objectData != 'NG')) {
      console.log(objectData, '(' + i.toString() + ')');
      fs.appendFile('../data/rawData/labels/ngcLabels.txt', objectData + " ; NGC " + i.toString(), (err) => {
        if (err) {
            throw err;
        }
      });

    }
  };
  await browser.close();
})();
