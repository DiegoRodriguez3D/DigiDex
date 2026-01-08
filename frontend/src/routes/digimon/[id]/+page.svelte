<script lang="ts">
    import { fade, fly } from "svelte/transition";
    import DigiProfile from "$lib/components/DigiProfile.svelte";
    import EvolutionTree from "$lib/components/EvolutionTree.svelte";

    interface Props {
        data: {
            digimon: import("$lib/types").DigimonDetail | null;
            error: string | null;
        };
    }

    let { data }: Props = $props();
</script>

<svelte:head>
    {#if data.digimon}
        <title>{data.digimon.name} | DigiDex - Digital Gate</title>
        <meta
            name="description"
            content="Analyze {data.digimon
                .name} - {data.digimon.description?.slice(0, 150) ||
                'View stats, skills, and evolutions.'}"
        />
    {:else}
        <title>Digimon Not Found | DigiDex</title>
    {/if}
</svelte:head>

<div class="container mx-auto px-4 py-8" in:fade={{ duration: 200 }}>
    <a
        href="/"
        class="inline-flex items-center gap-2 font-mono text-sm text-gray-400 hover:text-neon-blue transition-colors mb-6"
    >
        <svg
            class="w-4 h-4"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
        >
            <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M15 19l-7-7 7-7"
            />
        </svg>
        Back to Grid
    </a>

    <div class="mb-6">
        <h2
            class="font-display text-sm text-neon-blue uppercase tracking-widest mb-1"
        >
            Digi-Analyzer
        </h2>
        <div
            class="h-px bg-gradient-to-r from-neon-blue via-neon-purple to-transparent"
        ></div>
    </div>

    {#if data.error}
        <div
            class="glass-card border border-red-500/30 p-8 text-center"
            in:fly={{ y: 20, duration: 300 }}
        >
            <div class="text-6xl mb-4">❌</div>
            <h3 class="font-display text-xl text-red-400 mb-2">
                Analysis Failed
            </h3>
            <p class="font-mono text-sm text-gray-400 mb-6">{data.error}</p>
            <a href="/" class="cyber-btn">Return to Grid</a>
        </div>
    {:else if data.digimon}
        <div class="space-y-8" in:fly={{ y: 20, duration: 300, delay: 100 }}>
            <DigiProfile digimon={data.digimon} />

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                <div class="glass-card border border-white/10 p-6">
                    <EvolutionTree
                        title="Prior Evolutions"
                        evolutions={data.digimon.prior_evolutions}
                        emptyMessage="This is a base form"
                    />
                </div>

                <div class="glass-card border border-white/10 p-6">
                    <EvolutionTree
                        title="Next Evolutions"
                        evolutions={data.digimon.next_evolutions}
                        emptyMessage="No evolutions discovered"
                    />
                </div>
            </div>
        </div>
    {/if}
</div>
