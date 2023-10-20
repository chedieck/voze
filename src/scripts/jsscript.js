import { exec } from 'child_process'

export function runScript() {
  exec('./src/scripts/script.sh', (error, stdout, stderr) => {
    if (error) {
      console.error(`Error running script: ${error}`);
      return;
    }
    console.log(`stdout: ${stdout}`);
    console.log(`stderr: ${stderr}`);
  });
}
