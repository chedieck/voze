import { runScript } from '../../../scripts/script.js'


/** @type {import('./$types').RequestHandler} */
export function GET({ url }) {
  console.log('uai')
  runScript()
  const random = 10 + Math.random() * 2;
  return new Response(String(random));
}
