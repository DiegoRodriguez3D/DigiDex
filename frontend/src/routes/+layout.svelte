<script lang="ts">
	import "../app.css";
	import Header from "$lib/components/Header.svelte";

	interface Props {
		children: import("svelte").Snippet;
	}

	let { children }: Props = $props();
</script>

<svelte:head>
	<link rel="preconnect" href="https://fonts.googleapis.com" />
	<link
		rel="preconnect"
		href="https://fonts.gstatic.com"
		crossorigin="anonymous"
	/>
	<link
		href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Orbitron:wght@500;600;700;800;900&display=swap"
		rel="stylesheet"
	/>
	<meta
		name="description"
		content="DigiDex - Your digital gateway to the Digimon world. Explore, analyze, and discover all Digimon."
	/>
	<meta name="theme-color" content="#050505" />
</svelte:head>

<div class="min-h-screen flex flex-col bg-cyber-dark">
	<Header />

	<main class="flex-1">
		{@render children()}
	</main>

	<footer class="border-t border-white/10 py-6 mt-auto">
		<div class="container mx-auto px-4 text-center">
			<p class="font-mono text-xs text-gray-500">
				Data provided by <a
					href="https://digi-api.com"
					target="_blank"
					rel="noopener"
					class="text-neon-blue hover:underline">Digi-API</a
				>
				<span class="mx-2">•</span>
				Digital Gate v1.0
			</p>
		</div>
	</footer>
</div>
