<script>
	import TextToAudio from './TextToAudio.svelte';
	import banner from '$lib/images/banner.png';
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Text-to-voice simple app" />
</svelte:head>

<section>
	<div>
		<span class="logo">
			<picture>
				<img src={banner} alt="banner" />
			</picture>
		</span>
	</div>

	<TextToAudio/>
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	h1 {
		width: 100%;
	}

	.logo {
		justify-content: center;
		align-items: center;
		display: block;
		width: 100%;
		height: 0;
		padding: 0 0 calc(100% * 495 / 2048) 0;
		margin-bottom: 10rem;
	}

	.logo img {
		display: block;
	}
</style>
