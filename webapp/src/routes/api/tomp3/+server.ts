import { runScript } from '../../../scripts/script.js'


/** @type {import('./$types').RequestHandler} */
export async function POST({ request }: any) {
  const body = JSON.parse(await request.text())
  const text = body.text
  const lang =  body.lang
  const downloadPath = await runScript(text, lang)
  return new Response(downloadPath);
}
