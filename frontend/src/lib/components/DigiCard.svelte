<script lang="ts">
  import { browser } from "$app/environment";
  import type { DigimonListItem } from "$lib/types";

  interface Props {
    digimon: DigimonListItem;
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

  function getAttributeColors(
    attribute: string | null,
    light: boolean,
  ): {
    border: string;
    glow: string;
    accent: string;
    rgb: string;
  } {
    // Darker colors for light theme
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
    const rgb = colors[attr] ?? colors.default;

    const borderClasses: Record<string, string> = {
      default: "border-neon-blue/50",
      vaccine: "border-neon-orange",
      virus: "border-neon-purple",
      data: "border-neon-blue",
      free: "border-neon-green",
    };

    return {
      border: borderClasses[attr] ?? borderClasses.default,
      glow: `shadow-[0_0_25px_rgba(${rgb},0.5)]`,
      accent: "bg-neon-blue",
      rgb,
    };
  }

  const colors = $derived(getAttributeColors(digimon.attribute, isLight));
</script>

<a
  href="/digimon/{digimon.id}"
  class="digi-card group relative flex flex-col transition-all duration-300 hover:scale-[1.03] hover:{colors.glow}"
>
  <div
    class="absolute -inset-1 rounded-xl opacity-0 group-hover:opacity-100 transition-opacity duration-500 blur-md"
    style="background: linear-gradient(135deg, rgba({colors.rgb},0.3), transparent, rgba({colors.rgb},0.3));"
  ></div>

  <div
    class="absolute inset-0 {colors.border} border-2 rounded-lg overflow-hidden"
  >
    <div
      class="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-300"
      style="box-shadow: inset 0 0 20px rgba({colors.rgb},0.3);"
    ></div>
  </div>

  <div
    class="absolute top-1 left-1 w-3 h-3 border-t-2 border-l-2 {colors.border} opacity-60 group-hover:opacity-100 transition-opacity"
  ></div>
  <div
    class="absolute top-1 right-1 w-3 h-3 border-t-2 border-r-2 {colors.border} opacity-60 group-hover:opacity-100 transition-opacity"
  ></div>
  <div
    class="absolute bottom-1 left-1 w-3 h-3 border-b-2 border-l-2 {colors.border} opacity-60 group-hover:opacity-100 transition-opacity"
  ></div>
  <div
    class="absolute bottom-1 right-1 w-3 h-3 border-b-2 border-r-2 {colors.border} opacity-60 group-hover:opacity-100 transition-opacity"
  ></div>

  <div class="absolute inset-0 rounded-lg overflow-hidden card-bg">
    <div
      class="absolute inset-0 opacity-15 group-hover:opacity-30 transition-opacity duration-300"
      style="background-image: linear-gradient(rgba({colors.rgb},0.2) 1px, transparent 1px), linear-gradient(90deg, rgba({colors.rgb},0.2) 1px, transparent 1px); background-size: 16px 16px;"
    ></div>

    <div
      class="absolute top-0 left-1/4 w-px h-4 opacity-30 group-hover:opacity-60 transition-opacity"
      style="background: linear-gradient(to bottom, rgba({colors.rgb},0.8), transparent);"
    ></div>
    <div
      class="absolute top-0 right-1/3 w-px h-6 opacity-20 group-hover:opacity-50 transition-opacity"
      style="background: linear-gradient(to bottom, rgba({colors.rgb},0.6), transparent);"
    ></div>
    <div
      class="absolute bottom-0 left-1/3 w-px h-5 opacity-25 group-hover:opacity-55 transition-opacity"
      style="background: linear-gradient(to top, rgba({colors.rgb},0.7), transparent);"
    ></div>
    <div
      class="absolute left-0 top-1/4 h-px w-4 opacity-30 group-hover:opacity-60 transition-opacity"
      style="background: linear-gradient(to right, rgba({colors.rgb},0.8), transparent);"
    ></div>
    <div
      class="absolute right-0 bottom-1/3 h-px w-5 opacity-25 group-hover:opacity-55 transition-opacity"
      style="background: linear-gradient(to left, rgba({colors.rgb},0.7), transparent);"
    ></div>

    <div
      class="absolute inset-0 bg-gradient-to-b from-transparent via-white/5 to-transparent translate-y-full group-hover:translate-y-[-100%] transition-transform duration-700 ease-in-out"
    ></div>
  </div>

  <div class="relative z-10 p-3 flex flex-col h-full">
    <div class="relative aspect-square flex items-center justify-center mb-3">
      <div
        class="absolute inset-2 rounded opacity-20 group-hover:opacity-40 transition-opacity"
        style="border: 1px solid rgba({colors.rgb},0.5); box-shadow: inset 0 0 15px rgba({colors.rgb},0.1);"
      ></div>

      <div
        class="absolute top-3 right-3 w-2 h-2 opacity-40 group-hover:opacity-70 transition-opacity"
        style="background: rgba({colors.rgb},0.6); clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);"
      ></div>
      <div
        class="absolute bottom-3 left-3 w-1.5 h-1.5 opacity-30 group-hover:opacity-60 transition-opacity"
        style="background: rgba({colors.rgb},0.5); clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);"
      ></div>

      <img
        src={digimon.image}
        alt={digimon.name}
        class="relative max-w-[85%] max-h-[85%] object-contain transition-all duration-300 group-hover:scale-110"
        style="filter: drop-shadow(0 0 8px rgba({colors.rgb},0.3));"
        loading="lazy"
      />
    </div>

    <div class="mt-auto text-center space-y-1">
      <div
        class="w-8 h-px mx-auto mb-2 opacity-40 group-hover:opacity-80 group-hover:w-12 transition-all duration-300"
        style="background: linear-gradient(90deg, transparent, rgba({colors.rgb},0.8), transparent);"
      ></div>

      <h3
        class="font-display text-sm sm:text-base font-bold uppercase tracking-wider truncate transition-all duration-300 card-title"
        style="text-shadow: 0 0 10px rgba({colors.rgb},0.3);"
      >
        {digimon.name}
      </h3>
      {#if digimon.level}
        <p class="text-[11px] text-gray-400 font-mono tracking-wide">
          {digimon.level}
        </p>
      {/if}
    </div>

    <div
      class="absolute bottom-0 left-1/2 -translate-x-1/2 w-1/3 h-0.5 rounded-full opacity-50 group-hover:w-2/3 group-hover:opacity-100 transition-all duration-300"
      style="background: rgba({colors.rgb},1); box-shadow: 0 0 10px rgba({colors.rgb},0.8);"
    ></div>
  </div>

  <div
    class="absolute top-2 right-2 w-2 h-2 rounded-full opacity-70 group-hover:opacity-100 transition-opacity"
    style="background: rgba({colors.rgb},1); box-shadow: 0 0 8px rgba({colors.rgb},0.8);"
  ></div>

  <div class="absolute top-2 left-2 flex gap-0.5">
    <div
      class="w-1 h-1 rounded-full"
      style="background: rgba({colors.rgb},0.4);"
    ></div>
    <div
      class="w-1 h-1 rounded-full"
      style="background: rgba({colors.rgb},0.6);"
    ></div>
    <div
      class="w-1 h-1 rounded-full"
      style="background: rgba({colors.rgb},0.8);"
    ></div>
  </div>
</a>

<style>
  .digi-card {
    position: relative;
    border-radius: 0.5rem;
  }

  .card-bg {
    background: linear-gradient(135deg, #151515 0%, #0a0a0a 50%, #050505 100%);
  }

  :global(html.light) .card-bg {
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 50%, #f1f5f9 100%);
  }

  .card-title {
    color: white;
  }

  :global(html.light) .card-title {
    color: #1a1a2e;
  }
</style>
