<script lang="ts">
    interface Props {
        currentPage: number;
        totalPages: number;
        hasNext: boolean;
        hasPrevious: boolean;
    }

    let { currentPage, totalPages, hasNext, hasPrevious }: Props = $props();
</script>

<nav class="flex items-center justify-center gap-4 py-8">
    <a
        href={hasPrevious ? `/?page=${currentPage - 1}` : "#"}
        class="cyber-btn {!hasPrevious ? 'opacity-40 pointer-events-none' : ''}"
        aria-disabled={!hasPrevious}
    >
        <span class="flex items-center gap-2">
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
            Previous
        </span>
    </a>

    <div class="font-mono text-sm text-gray-400">
        <span class="text-neon-blue">{currentPage + 1}</span>
        <span class="mx-2">/</span>
        <span>{totalPages}</span>
    </div>

    <a
        href={hasNext ? `/?page=${currentPage + 1}` : "#"}
        class="cyber-btn {!hasNext ? 'opacity-40 pointer-events-none' : ''}"
        aria-disabled={!hasNext}
    >
        <span class="flex items-center gap-2">
            Next
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
                    d="M9 5l7 7-7 7"
                />
            </svg>
        </span>
    </a>
</nav>
