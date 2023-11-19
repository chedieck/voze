import { exec as execCb } from 'child_process'
import { promisify } from 'util'
import * as  fs from 'fs'

const exec = promisify(execCb);
const writeFile = promisify(fs.writeFile);

export async function runScript(text, lang) {
  try {
    // Create temp file
    const { stdout: stdoutTmp } = await exec('mktemp');
    const textfile = stdoutTmp.trim();

    // Write to temp file
    await writeFile(textfile, text);

    // Run shell script
    const { stdout } = await exec(`./src/scripts/script.sh ${textfile} ${lang}`);

    console.log('Script output:', stdout);
    return stdout;

  } catch (error) {
    console.error('Error:', error);
    return null;
  }
}
