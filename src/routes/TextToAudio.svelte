<script lang="ts">
	let text = '';
	let lang = 'en';
	let error = '';

	const languages = [
		{ name: "English", code: "en" },
		{ name: "Português", code: "pt-br" },
		{ name: "Русcкий", code: "ru" }
	];

	async function startDownload(path: string) {
		// Create an anchor element
		const a = document.createElement('a');

		// Set attributes to the anchor element
		a.href = path;
		a.download = path.split('/').pop() || ''; // Extract file name from path

		// Append the anchor to the DOM (not visible)
		document.body.appendChild(a);

		// Simulate a click to start download
		a.click();

		// Remove the anchor from the DOM
		document.body.removeChild(a);
	}

	async function getMP3() {
		if (text.length > 5000) {
			error = 'At most 5000 chars.'
		}
		let res = await fetch('/api/tomp3', {
			method: 'POST',
			headers: {
				"Content-type": "application/json"
			},
			body: JSON.stringify({
				text,
				lang
			})
		})
		const path = await res.text()
		console.log('peguei no comp', path)
		startDownload(path)
	}
</script>

<div class="counter">
		<select bind:value={lang}>
  {#each languages as language}
    <option value={language.code}>{language.name} ({language.code})</option>
  {/each}
</select>
	<textarea bind:value={text}/>
	<button on:click={() => getMP3()} aria-label="Get mp3">
		MP3
	</button>

</div>

<style>
	.counter {
		display: flex;
		border-top: 1px solid rgba(0, 0, 0, 0.1);
		border-bottom: 1px solid rgba(0, 0, 0, 0.1);
		margin: 1rem 0;
	}

	.counter button {
		width: 2em;
		padding: 0;
		display: flex;
		align-items: center;
		justify-content: center;
		border: 0;
		background-color: transparent;
		touch-action: manipulation;
		font-size: 2rem;
	}

	.counter button:hover {
		background-color: var(--color-bg-1);
	}

	svg {
		width: 25%;
		height: 25%;
	}

	path {
		vector-effect: non-scaling-stroke;
		stroke-width: 2px;
		stroke: #444;
	}

	.counter-viewport {
		width: 8em;
		height: 4em;
		overflow: hidden;
		text-align: center;
		position: relative;
	}

	.counter-viewport strong {
		position: absolute;
		display: flex;
		width: 100%;
		height: 100%;
		font-weight: 400;
		color: var(--color-theme-1);
		font-size: 4rem;
		align-items: center;
		justify-content: center;
	}

	.counter-digits {
		position: absolute;
		width: 100%;
		height: 100%;
	}

	.hidden {
		top: -100%;
		user-select: none;
	}
</style>
