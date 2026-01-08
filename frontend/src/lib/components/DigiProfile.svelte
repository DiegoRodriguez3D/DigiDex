<!-- DigiProfile.svelte - Detail view profile component -->
<script lang="ts">
    import type { DigimonDetail } from "$lib/types";

    interface Props {
        digimon: DigimonDetail;
    }

    let { digimon }: Props = $props();

    // Get attribute color class
    function getAttributeClass(attribute: string | null): string {
        if (!attribute) return "text-gray-400 bg-white/10";
        const attr = attribute.toLowerCase();
        if (attr === "vaccine") return "text-neon-orange bg-neon-orange/20";
        if (attr === "virus") return "text-neon-purple bg-neon-purple/20";
        if (attr === "data") return "text-neon-blue bg-neon-blue/20";
        if (attr === "free") return "text-neon-green bg-neon-green/20";
        return "text-gray-400 bg-white/10";
    }

    // Get border glow class
    function getBorderGlow(attribute: string | null): string {
        if (!attribute) return "border-white/20";
        const attr = attribute.toLowerCase();
        if (attr === "vaccine") return "border-neon-orange glow-vaccine";
        if (attr === "virus") return "border-neon-purple glow-virus";
        if (attr === "data") return "border-neon-blue glow-data";
        if (attr === "free") return "border-neon-green glow-free";
        return "border-white/20";
    }
</script>

<div class="glass-card border-2 {getBorderGlow(digimon.attribute)} p-6 sm:p-8">
    <div class="flex flex-col lg:flex-row gap-8">
        <!-- Image Section -->
        <div class="lg:w-1/3 flex justify-center">
            <div class="relative">
                <!-- Decorative Frame -->
                <div
                    class="absolute -inset-4 border border-neon-blue/30 rounded-lg"
                ></div>
                <div
                    class="absolute -inset-2 border border-neon-purple/20 rounded-lg rotate-3"
                ></div>

                <!-- Image -->
                <img
                    src={digimon.image}
                    alt={digimon.name}
                    class="relative max-w-[280px] w-full float-animation z-10"
                />

                <!-- Scan Line Effect -->
                <div
                    class="absolute inset-0 scanline pointer-events-none"
                ></div>
            </div>
        </div>

        <!-- Info Section -->
        <div class="lg:w-2/3 space-y-6">
            <!-- Name and Badges -->
            <div>
                <h1
                    class="font-display text-3xl sm:text-4xl font-black text-white mb-3 glitch-text"
                >
                    {digimon.name}
                </h1>

                <div class="flex flex-wrap gap-2">
                    {#if digimon.level}
                        <span
                            class="px-3 py-1 text-sm font-mono rounded-full bg-neon-yellow/20 text-neon-yellow"
                        >
                            ⭐ {digimon.level}
                        </span>
                    {/if}

                    {#if digimon.attribute}
                        <span
                            class="px-3 py-1 text-sm font-mono rounded-full {getAttributeClass(
                                digimon.attribute,
                            )}"
                        >
                            {digimon.attribute}
                        </span>
                    {/if}

                    {#each digimon.types as type}
                        <span
                            class="px-3 py-1 text-sm font-mono rounded-full bg-white/10 text-gray-300"
                        >
                            {type}
                        </span>
                    {/each}
                </div>
            </div>

            <!-- Data Log (Description) -->
            {#if digimon.description}
                <div class="space-y-2">
                    <h3
                        class="font-display text-sm text-neon-blue uppercase tracking-wider section-header"
                    >
                        <span>Data Log</span>
                    </h3>
                    <p class="font-mono text-sm text-gray-300 leading-relaxed">
                        {digimon.description}
                    </p>
                </div>
            {/if}

            <!-- Skills -->
            {#if digimon.skills.length > 0}
                <div class="space-y-3">
                    <h3
                        class="font-display text-sm text-neon-blue uppercase tracking-wider section-header"
                    >
                        <span>Battle Skills</span>
                    </h3>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
                        {#each digimon.skills.slice(0, 6) as skill}
                            <div
                                class="bg-cyber-dark-600 border border-white/10 rounded px-3 py-2"
                            >
                                <div class="font-mono text-sm text-white">
                                    {skill.name}
                                </div>
                                {#if skill.description}
                                    <div
                                        class="font-mono text-xs text-gray-500 truncate"
                                    >
                                        {skill.description}
                                    </div>
                                {/if}
                            </div>
                        {/each}
                    </div>
                    {#if digimon.skills.length > 6}
                        <p class="font-mono text-xs text-gray-500">
                            +{digimon.skills.length - 6} more skills
                        </p>
                    {/if}
                </div>
            {/if}

            <!-- Fields -->
            {#if digimon.fields.length > 0}
                <div class="space-y-3">
                    <h3
                        class="font-display text-sm text-neon-blue uppercase tracking-wider section-header"
                    >
                        <span>Fields</span>
                    </h3>
                    <div class="flex flex-wrap gap-2">
                        {#each digimon.fields as field}
                            <div
                                class="flex items-center gap-2 bg-cyber-dark-600 border border-white/10 rounded-full px-3 py-1"
                            >
                                {#if field.image}
                                    <img
                                        src={field.image}
                                        alt={field.name}
                                        class="w-4 h-4"
                                    />
                                {/if}
                                <span class="font-mono text-xs text-gray-300"
                                    >{field.name}</span
                                >
                            </div>
                        {/each}
                    </div>
                </div>
            {/if}
        </div>
    </div>
</div>
