<!-- SearchBar.svelte -->
<script lang="ts">
    import { goto } from "$app/navigation";

    let searchQuery = $state("");
    let isLoading = $state(false);

    async function handleSearch(event: Event) {
        event.preventDefault();
        const query = searchQuery.trim();
        if (!query) return;

        isLoading = true;
        try {
            // Navigate to search results or directly to Digimon if exact match
            goto(`/?search=${encodeURIComponent(query)}`);
        } finally {
            isLoading = false;
        }
    }
</script>

<form onsubmit={handleSearch} class="relative">
    <div class="relative">
        <!-- Search Icon -->
        <div
            class="absolute left-3 top-1/2 -translate-y-1/2 text-neon-blue/50 pointer-events-none"
        >
            <svg
                class="w-5 h-5"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
            >
                <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                />
            </svg>
        </div>

        <!-- Input -->
        <input
            type="text"
            bind:value={searchQuery}
            placeholder="Search Digimon..."
            class="w-full pl-10 pr-4 py-2.5 bg-cyber-dark-700 border border-white/10 rounded-lg
             font-mono text-sm text-white placeholder-gray-500
             focus:outline-none focus:border-neon-blue focus:ring-1 focus:ring-neon-blue/50
             transition-all duration-200"
        />

        <!-- Loading Spinner -->
        {#if isLoading}
            <div class="absolute right-3 top-1/2 -translate-y-1/2">
                <div
                    class="w-4 h-4 border-2 border-neon-blue/30 border-t-neon-blue rounded-full animate-spin"
                ></div>
            </div>
        {/if}
    </div>

    <!-- Search Hint -->
    <div
        class="absolute right-3 top-1/2 -translate-y-1/2 text-xs text-gray-600 font-mono hidden sm:block"
    >
        {#if !isLoading && !searchQuery}
            Press Enter
        {/if}
    </div>
</form>
