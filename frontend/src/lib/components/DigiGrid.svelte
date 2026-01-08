<!-- DigiGrid.svelte -->
<script lang="ts">
    import type { DigimonListItem } from "$lib/types";
    import DigiCard from "./DigiCard.svelte";

    interface Props {
        digimon: DigimonListItem[];
        loading?: boolean;
    }

    let { digimon, loading = false }: Props = $props();
</script>

{#if loading}
    <!-- Loading Skeleton Grid -->
    <div
        class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-4"
    >
        {#each Array(20) as _, i}
            <div class="glass-card border border-white/10 p-4 animate-pulse">
                <div
                    class="aspect-square bg-cyber-dark-600 rounded-lg mb-3"
                ></div>
                <div
                    class="h-4 bg-cyber-dark-600 rounded w-3/4 mx-auto mb-2"
                ></div>
                <div class="h-3 bg-cyber-dark-600 rounded w-1/2 mx-auto"></div>
            </div>
        {/each}
    </div>
{:else if digimon.length === 0}
    <!-- Empty State -->
    <div class="flex flex-col items-center justify-center py-20 text-center">
        <div class="text-6xl mb-4 opacity-30">🔍</div>
        <h3 class="font-display text-xl text-gray-400 mb-2">
            No Digimon Found
        </h3>
        <p class="text-gray-500 font-mono text-sm">
            Try adjusting your search criteria
        </p>
    </div>
{:else}
    <!-- Digimon Grid -->
    <div
        class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-4"
    >
        {#each digimon as mon (mon.id)}
            <DigiCard digimon={mon} />
        {/each}
    </div>
{/if}
