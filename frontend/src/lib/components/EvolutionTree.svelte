<!-- EvolutionTree.svelte - Horizontal scrollable evolution list -->
<script lang="ts">
    import type { Evolution } from "$lib/types";

    interface Props {
        title: string;
        evolutions: Evolution[];
        emptyMessage?: string;
    }

    let {
        title,
        evolutions,
        emptyMessage = "No evolutions discovered",
    }: Props = $props();
</script>

<div class="space-y-4">
    <h3
        class="font-display text-sm text-neon-blue uppercase tracking-wider section-header"
    >
        <span>{title}</span>
    </h3>

    {#if evolutions.length === 0}
        <div class="text-center py-8 text-gray-500 font-mono text-sm">
            {emptyMessage}
        </div>
    {:else}
        <div class="scroll-x pb-4">
            <div class="flex gap-4" style="min-width: max-content;">
                {#each evolutions as evo (evo.id)}
                    <a
                        href="/digimon/{evo.id}"
                        class="group flex-shrink-0 w-36 glass-card border border-white/10 p-3 hover:border-neon-blue/50 hover:glow-data transition-all duration-300"
                    >
                        <!-- Evolution Image -->
                        <div
                            class="aspect-square flex items-center justify-center mb-2 overflow-hidden"
                        >
                            <img
                                src={evo.image}
                                alt={evo.name}
                                class="max-w-full max-h-full object-contain group-hover:scale-110 transition-transform duration-300"
                                loading="lazy"
                            />
                        </div>

                        <!-- Evolution Name -->
                        <div class="text-center">
                            <p class="font-mono text-xs text-white truncate">
                                {evo.name}
                            </p>
                            {#if evo.condition}
                                <p
                                    class="font-mono text-[10px] text-gray-500 truncate mt-1"
                                    title={evo.condition}
                                >
                                    {evo.condition}
                                </p>
                            {/if}
                        </div>

                        <!-- Connection Line Decoration -->
                        <div
                            class="absolute -right-4 top-1/2 w-4 h-px bg-gradient-to-r from-neon-blue/50 to-transparent
                        opacity-0 group-last:hidden"
                        ></div>
                    </a>
                {/each}
            </div>
        </div>
    {/if}
</div>
