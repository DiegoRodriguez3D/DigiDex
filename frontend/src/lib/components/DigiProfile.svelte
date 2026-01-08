<script lang="ts">
    import { browser } from "$app/environment";
    import type { DigimonDetail } from "$lib/types";

    interface Props {
        digimon: DigimonDetail;
    }

    let { digimon }: Props = $props();

    // Detect theme
    let isLight = $state(false);
    if (browser) {
        isLight = document.documentElement.classList.contains("light");
        const observer = new MutationObserver(() => {
            isLight = document.documentElement.classList.contains("light");
        });
        observer.observe(document.documentElement, {
            attributes: true,
            attributeFilter: ["class"],
        });
    }

    function getAttributeClass(attribute: string | null): string {
        const classes: Record<string, string> = {
            vaccine: "text-neon-orange bg-neon-orange/20",
            virus: "text-neon-purple bg-neon-purple/20",
            data: "text-neon-blue bg-neon-blue/20",
            free: "text-neon-green bg-neon-green/20",
        };
        return attribute
            ? (classes[attribute.toLowerCase()] ?? "text-gray-400 bg-white/10")
            : "text-gray-400 bg-white/10";
    }

    function getColorRGB(attribute: string | null, light: boolean): string {
        const lightColors: Record<string, string> = {
            default: "0,100,120",
            vaccine: "180,90,0",
            virus: "120,0,180",
            data: "0,100,120",
            free: "0,120,50",
        };

        const darkColors: Record<string, string> = {
            default: "0,243,255",
            vaccine: "255,153,0",
            virus: "189,0,255",
            data: "0,243,255",
            free: "0,255,65",
        };

        const colors = light ? lightColors : darkColors;
        const attr = attribute?.toLowerCase() ?? "default";
        return colors[attr] ?? colors.default;
    }

    const colorRGB = $derived(getColorRGB(digimon.attribute, isLight));
</script>

<div class="space-y-6">
    <div class="flex flex-col lg:flex-row gap-6 lg:items-start">
        <div class="flex justify-center lg:justify-start lg:flex-shrink-0">
            <div class="relative inline-block">
                <div
                    class="absolute -inset-4 rounded-xl opacity-50 blur-lg"
                    style="background: radial-gradient(ellipse, rgba({colorRGB},0.3), transparent 70%);"
                ></div>

                <div
                    class="image-frame relative p-4 rounded-lg"
                    style="border: 2px solid rgba({colorRGB},0.6); box-shadow: 0 0 20px rgba({colorRGB},0.2), inset 0 0 30px rgba(0,0,0,0.2);"
                >
                    <div
                        class="absolute top-1 left-1 w-4 h-4 border-t-2 border-l-2 rounded-tl"
                        style="border-color: rgba({colorRGB},0.8);"
                    ></div>
                    <div
                        class="absolute top-1 right-1 w-4 h-4 border-t-2 border-r-2 rounded-tr"
                        style="border-color: rgba({colorRGB},0.8);"
                    ></div>
                    <div
                        class="absolute bottom-1 left-1 w-4 h-4 border-b-2 border-l-2 rounded-bl"
                        style="border-color: rgba({colorRGB},0.8);"
                    ></div>
                    <div
                        class="absolute bottom-1 right-1 w-4 h-4 border-b-2 border-r-2 rounded-br"
                        style="border-color: rgba({colorRGB},0.8);"
                    ></div>

                    <div
                        class="absolute inset-4 opacity-20 rounded"
                        style="background-image: linear-gradient(rgba({colorRGB},0.3) 1px, transparent 1px), linear-gradient(90deg, rgba({colorRGB},0.3) 1px, transparent 1px); background-size: 12px 12px;"
                    ></div>

                    <div
                        class="absolute top-4 left-1/2 -translate-x-1/2 w-1/3 h-px"
                        style="background: linear-gradient(90deg, transparent, rgba({colorRGB},0.5), transparent);"
                    ></div>
                    <div
                        class="absolute bottom-4 left-1/2 -translate-x-1/2 w-1/4 h-px"
                        style="background: linear-gradient(90deg, transparent, rgba({colorRGB},0.4), transparent);"
                    ></div>

                    <div
                        class="absolute top-3 right-3 w-2 h-2"
                        style="background: rgba({colorRGB},0.5); clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);"
                    ></div>
                    <div
                        class="absolute bottom-3 left-3 w-1.5 h-1.5"
                        style="background: rgba({colorRGB},0.4); clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);"
                    ></div>

                    <img
                        src={digimon.image}
                        alt={digimon.name}
                        class="relative w-[200px] sm:w-[220px] lg:w-[250px] h-auto float-animation z-10"
                        style="filter: drop-shadow(0 0 15px rgba({colorRGB},0.4));"
                    />

                    <div
                        class="absolute inset-4 pointer-events-none overflow-hidden rounded"
                    >
                        <div
                            class="absolute inset-0 bg-gradient-to-b from-transparent via-white/5 to-transparent animate-scan"
                        ></div>
                    </div>
                </div>
            </div>
        </div>

        <div
            class="flex-1 min-w-0 glass-card p-6 space-y-5"
            style="border: 1px solid rgba({colorRGB},0.3); box-shadow: 0 0 15px rgba({colorRGB},0.1);"
        >
            <div>
                <h1
                    class="font-display text-3xl sm:text-4xl font-black text-white mb-3"
                    style="text-shadow: 0 0 20px rgba({colorRGB},0.4);"
                >
                    {digimon.name}
                </h1>

                <div class="flex flex-wrap gap-2">
                    {#if digimon.level}
                        <span
                            class="px-3 py-1 text-sm font-mono rounded-full bg-neon-yellow/20 text-neon-yellow"
                            style="box-shadow: 0 0 10px rgba(240,255,0,0.2);"
                        >
                            ⭐ {digimon.level}
                        </span>
                    {/if}

                    {#if digimon.attribute}
                        <span
                            class="px-3 py-1 text-sm font-mono rounded-full {getAttributeClass(
                                digimon.attribute,
                            )}"
                            style="box-shadow: 0 0 10px rgba({colorRGB},0.3);"
                        >
                            {digimon.attribute}
                        </span>
                    {/if}

                    {#each digimon.types as type}
                        <span
                            class="px-3 py-1 text-sm font-mono rounded-full bg-white/10 text-gray-300"
                            >{type}</span
                        >
                    {/each}
                </div>
            </div>

            {#if digimon.description}
                <div class="space-y-2">
                    <h3
                        class="font-display text-sm uppercase tracking-wider flex items-center gap-2"
                        style="color: rgba({colorRGB},1); text-shadow: 0 0 10px rgba({colorRGB},0.5);"
                    >
                        <span
                            class="w-2 h-2 rounded-full"
                            style="background: rgba({colorRGB},0.8); box-shadow: 0 0 6px rgba({colorRGB},0.8);"
                        ></span>
                        Data Log
                        <span
                            class="flex-1 h-px"
                            style="background: linear-gradient(to right, rgba({colorRGB},0.5), transparent);"
                        ></span>
                    </h3>
                    <p class="font-mono text-sm text-gray-300 leading-relaxed">
                        {digimon.description}
                    </p>
                </div>
            {/if}

            {#if digimon.skills.length > 0}
                <div class="space-y-3">
                    <h3
                        class="font-display text-sm uppercase tracking-wider flex items-center gap-2"
                        style="color: rgba({colorRGB},1); text-shadow: 0 0 10px rgba({colorRGB},0.5);"
                    >
                        <span
                            class="w-2 h-2 rounded-full"
                            style="background: rgba({colorRGB},0.8); box-shadow: 0 0 6px rgba({colorRGB},0.8);"
                        ></span>
                        Battle Skills
                        <span
                            class="flex-1 h-px"
                            style="background: linear-gradient(to right, rgba({colorRGB},0.5), transparent);"
                        ></span>
                    </h3>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
                        {#each digimon.skills.slice(0, 6) as skill}
                            <div
                                class="bg-cyber-dark-600 border border-white/10 rounded px-3 py-2 hover:border-white/20 transition-colors"
                                style="box-shadow: inset 0 0 10px rgba(0,0,0,0.3);"
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

            {#if digimon.fields.length > 0}
                <div class="space-y-3">
                    <h3
                        class="font-display text-sm uppercase tracking-wider flex items-center gap-2"
                        style="color: rgba({colorRGB},1); text-shadow: 0 0 10px rgba({colorRGB},0.5);"
                    >
                        <span
                            class="w-2 h-2 rounded-full"
                            style="background: rgba({colorRGB},0.8); box-shadow: 0 0 6px rgba({colorRGB},0.8);"
                        ></span>
                        Fields
                        <span
                            class="flex-1 h-px"
                            style="background: linear-gradient(to right, rgba({colorRGB},0.5), transparent);"
                        ></span>
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

<style>
    @keyframes scan {
        0% {
            transform: translateY(-100%);
        }
        100% {
            transform: translateY(200%);
        }
    }
    .animate-scan {
        animation: scan 4s linear infinite;
    }
</style>
