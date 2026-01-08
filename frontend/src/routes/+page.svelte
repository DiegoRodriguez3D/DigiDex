<script lang="ts">
    import DigiGrid from "$lib/components/DigiGrid.svelte";
    import PaginationControls from "$lib/components/PaginationControls.svelte";

    interface Props {
        data: {
            digimon: import("$lib/types").DigimonListItem[];
            pagination: import("$lib/types").Pagination | null;
            searchQuery: string | null;
            error: string | null;
        };
    }

    let { data }: Props = $props();
</script>

<svelte:head>
    <title>Digital Gate | DigiDex - Explore the Digital World</title>
</svelte:head>

<div class="container mx-auto px-4 py-8">
    <div class="mb-8">
        {#if data.searchQuery}
            <div class="flex items-center gap-4 mb-4">
                <h2 class="font-display text-xl text-white">
                    Search Results for "<span class="text-neon-blue"
                        >{data.searchQuery}</span
                    >"
                </h2>
                <a
                    href="/"
                    class="text-sm font-mono text-gray-400 hover:text-neon-blue transition-colors"
                >
                    ← Clear Search
                </a>
            </div>
            <p class="font-mono text-sm text-gray-500">
                Found {data.digimon.length} Digimon
            </p>
        {:else}
            <h2 class="font-display text-xl text-white mb-2 section-header">
                <span>The Grid</span>
            </h2>
            <p class="font-mono text-sm text-gray-500">
                {#if data.pagination}
                    Displaying {data.digimon.length} of {data.pagination
                        .total_elements} Digimon
                {:else}
                    Loading...
                {/if}
            </p>
        {/if}
    </div>

    {#if data.error}
        <div class="glass-card border border-red-500/30 p-6 text-center mb-8">
            <div class="text-4xl mb-4">⚠️</div>
            <h3 class="font-display text-lg text-red-400 mb-2">
                Connection Error
            </h3>
            <p class="font-mono text-sm text-gray-400">{data.error}</p>
        </div>
    {/if}

    <DigiGrid digimon={data.digimon} />

    {#if data.pagination && !data.searchQuery}
        <PaginationControls
            currentPage={data.pagination.current_page}
            totalPages={data.pagination.total_pages}
            hasNext={data.pagination.has_next}
            hasPrevious={data.pagination.has_previous}
        />
    {/if}
</div>
