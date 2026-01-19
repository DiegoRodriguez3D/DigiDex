<script lang="ts">
    import SearchBar from "./SearchBar.svelte";
    import ThemeToggle from "./ThemeToggle.svelte";

    interface Props {
        portfolioUrl: string;
    }

    let { portfolioUrl }: Props = $props();
</script>

<header
    class="sticky top-0 z-50 backdrop-blur-md border-b transition-colors duration-300 bg-cyber-dark/95 dark:bg-cyber-dark/95 border-white/10 dark:border-white/10 light:bg-white/95 light:border-gray-200"
>
    <div class="container mx-auto px-4 py-4">
        <div
            class="flex flex-col sm:flex-row items-center justify-between gap-4"
        >
            <a href="/" class="flex items-center gap-3 group">
                <div
                    class="relative w-10 h-10 flex items-center justify-center"
                >
                    <div
                        class="absolute inset-0 border-2 border-neon-blue rotate-45 group-hover:rotate-[405deg] transition-transform duration-700"
                    ></div>
                    <div
                        class="absolute inset-1 border border-neon-purple -rotate-45 group-hover:rotate-[315deg] transition-transform duration-700"
                    ></div>
                    <span class="text-neon-blue font-bold text-sm z-10">DX</span
                    >
                </div>

                <div class="flex flex-col">
                    <h1
                        class="font-display text-xl sm:text-2xl font-black tracking-wider glitch-text text-white dark:text-white light:text-gray-900"
                    >
                        DIGIDEX
                    </h1>
                    <span
                        class="font-mono text-[10px] text-neon-blue tracking-widest"
                        >v1.0</span
                    >
                </div>
            </a>

            <div class="flex items-center gap-3">
                <div class="w-full sm:w-auto sm:min-w-[300px]">
                    <SearchBar />
                </div>
                <ThemeToggle />
                <a
                    href={portfolioUrl}
                    target="_blank"
                    rel="noopener noreferrer"
                    class="flex items-center gap-2 px-3 py-2 rounded-lg border border-neon-purple/30 bg-neon-purple/10 hover:bg-neon-purple/20 transition-all duration-300 text-neon-purple hover:text-white group"
                    title="Volver al Portfolio"
                >
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        class="w-4 h-4"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        stroke-width="2"
                    >
                        <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            d="M10 19l-7-7m0 0l7-7m-7 7h18"
                        />
                    </svg>
                    <span class="hidden sm:inline font-mono text-xs"
                        >Portfolio</span
                    >
                </a>
            </div>
        </div>
    </div>
</header>
