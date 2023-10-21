<script lang="ts">
	let text = '';
	let lang = 'en';
	let error = '';
	let creating: boolean = false;
	let buttonDisabled = false;

	import config from '../config.json'

	const languages = [
		{ name: "English", code: "en" },
		{ name: "Português", code: "pt-br" },
		{ name: "Русcкий", code: "ru" }
	];

	const maxLength = config.maxLength

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
		if (text.length > maxLength) {
			error = `${maxLength} chars limit exceeded.`
			return
		}
		if (text.length === 0) {
			error = 'Input should not be empty.'
			return
		}
		error = ''
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

	$: {
		if (text.length > maxLength) {
			error = `${text.length}/${maxLength} chars limit exceeded.`
			buttonDisabled = true
		} else {
			error = "";
			buttonDisabled = false
		}
	}
	$: creating, buttonDisabled = creating

</script>
<div class="mainInput">
	<textarea autofocus class="text-area" bind:value={text}></textarea>
	<select class="language-select" bind:value={lang}>
	{#each languages as language}
		<option value={language.code}>{language.name} ({language.code})</option>
	{/each}
	</select>
	<button disabled={buttonDisabled} class="mp3-button {creating ? 'center-spinner' : ''}" on:click={() => getMP3()} aria-label="Get mp3">
		{#if creating}
			<div class="spinner"></div>
		{:else}
			MP3
		{/if}
	</button>
	{#if creating}
		<p class="creating-text">Your mp3 is being created and will be downloaded automatically.</p>
	{/if}
	{#if error}
		<p class="error-text">{error}</p>
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
		width: 40%;
		height: 2.5rem;
		font-size: 1.5rem;
		margin-bottom: 3rem;
		background-color: rgba(0,0,0,0.3);
		color: white;
		border: none;
		text-align: center; /* Center-aligns the text */
		border-radius: 2px;
	}

	.text-area {
		width: 100%;
		height: 15rem;
		font-size: 1.2rem;
		resize: none;
		margin-bottom: 3rem;
		background-color: rgba(0,0,0,0.3);
		padding: 4px;
		color: #fff;
		border-radius: 4px;
	}

	.text-area[focus] {
		border: 4px solid var(--color-bg-2);
	}

	.mp3-button {
		width: 60%;
		height: 4rem;
		font-size: 1.2rem;
		cursor: pointer;
		background-color: #000;
		color: #fff;
		background-color: var(--color-bg-4);
		border: none;
		border-radius: 2px;
		transition: transform 0.1s ease-in-out; /* Add transition effect */
	}

	.mp3-button:hover {
		transform: scale(1.1); /* Scale up the button when hovered */
	}

	.mp3-button:active {
		transform: scale(1); /* Scale back when clicked */
	}

	.mp3-button[disabled] {
		background-color: #ccc;
		cursor: not-allowed;
	}

	.error-text {
		font-size: 0.9rem;
		color: var(--color-bg-4);
		margin-top: 0.5rem;
		text-align: center;
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
