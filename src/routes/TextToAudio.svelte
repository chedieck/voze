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
<div class="mainInput">
	<textarea class="text-area" bind:value={text}></textarea>
	<select class="language-select" bind:value={lang}>
	{#each languages as language}
		<option value={language.code}>{language.name} ({language.code})</option>
	{/each}
	</select>
	<button class="mp3-button" on:click={() => getMP3()} aria-label="Get mp3">
		MP3
	</button>
</div>

<style>
	.mainInput {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: space-around;
		margin: 1rem 0;
		padding: 1rem;
		width: 40em;
	}

	.language-select {
		width: 50%;
		height: 2.5rem;
		font-size: 1rem;
		margin-bottom: 1rem;
		border: 1px solid #ccc;
	}

	.text-area {
		width: 100%;
		height: 5rem;
		resize: none;
		border: 1px solid #ccc;
		margin-bottom: 1rem;
	}

	.mp3-button {
		width: 50%;
		height: 2.5rem;
		font-size: 1.2rem;
		cursor: pointer;
		background-color: #000;
		color: #fff;
		border: none;
	}

	@media only screen and (max-width: 600px) {
		.mainInput {
			width: 90%;
		}
	}

	.mainInput-viewport {
		width: 8em;
		height: 4em;
		overflow: hidden;
		text-align: center;
		position: relative;
	}

	.mainInput-viewport strong {
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

	.mainInput-digits {
		position: absolute;
		width: 100%;
		height: 100%;
	}

	.hidden {
		top: -100%;
		user-select: none;
	}
</style>
