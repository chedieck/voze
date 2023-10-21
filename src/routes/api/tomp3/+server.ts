import { runScript } from '../../../scripts/script.js'


/** @type {import('./$types').RequestHandler} */
export async function POST({ request }: any) {
  const body = JSON.parse(await request.text())
  const text = body.text
  const lang =  body.lang
  const x = await runScript(text, lang)
  const random = 10 + Math.random() * 2;
  return new Response(String(random));
}
