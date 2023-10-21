<script lang="ts">
	let text = '';
	let lang = 'en';
	let error = '';
	let creating = false;

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
		creating = false
	}

	async function getMP3() {
		if (text.length > 5000) {
			error = 'At most 5000 chars.'
		}
		creating = true
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
	<button disabled={creating} class="mp3-button {creating ? 'center-spinner' : ''}" on:click={() => getMP3()} aria-label="Get mp3">
		{#if creating}
			<div class="spinner"></div>
		{:else}
			MP3
		{/if}
	</button>
	{#if creating}
		<p class="creating-text">Your mp3 is being created and will be downloaded automatically.</p>
	{/if}
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
		height: 15rem;
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

	.mp3-button[disabled] {
		background-color: #ccc;
		cursor: not-allowed;
	}

	.creating-text {
		font-size: 0.9rem;
		color: #666;
		margin-top: 0.5rem;
		text-align: center;
	}

	@media only screen and (max-width: 600px) {
		.mainInput {
			width: 90%;
		}
	}

	.spinner {
		border: 3px solid rgba(255, 255, 255, 0.3);
		border-radius: 50%;
		border-top: 3px solid #fff;
		width: 20px;
		height: 20px;
		animation: spin 1s linear infinite;
		margin-left: 8px;
	}

	.center-spinner {
		display: flex;
		justify-content: center;
		align-items: center;
	}

	@keyframes spin {
		0% { transform: rotate(0deg); }
		100% { transform: rotate(360deg); }
	}
</style>
