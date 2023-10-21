import { exec } from 'child_process'
import * as  fs from 'fs'

export function runScript(text, lang) {
  let tempfile
  exec('mktemp', (error, stdout, stderr) => {
    if (error) {
      console.error(`Error making temp: ${error}`);
      return;
    }
    const textfile = stdout.trim()
    fs.writeFile(textfile, text, (err) => { if (err) throw err })
    exec(`./src/scripts/script.sh ${textfile} ${lang}`, (error, stdout, stderr) => {
      if (error) {
        console.error(`Error running script: ${error}`);
        return;
      }
      console.log(`SCRIPT stdout: ${stdout}`);
      console.log(`SCRIPT stderr: ${stderr}`);
    });

    console.log(`tmpout: ${stdout}`);
    console.log(`stderr: ${stderr}`);
  })
}
