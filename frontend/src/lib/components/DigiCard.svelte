<!-- DigiCard.svelte - Digital tech-themed card with decorative elements -->
<script lang="ts">
  import type { DigimonListItem } from "$lib/types";

  interface Props {
    digimon: DigimonListItem;
  }

  let { digimon }: Props = $props();

  // Get attribute-based color scheme
  function getAttributeColors(attribute: string | null): {
    border: string;
    glow: string;
    accent: string;
    rgb: string;
  } {
    if (!attribute)
      return {
        border: "border-neon-blue/50",
        glow: "shadow-[0_0_15px_rgba(0,243,255,0.3)]",
        accent: "bg-neon-blue",
        rgb: "0,243,255",
      };
    const attr = attribute.toLowerCase();
    switch (attr) {
      case "vaccine":
        return {
          border: "border-neon-orange",
          glow: "shadow-[0_0_25px_rgba(255,153,0,0.5)]",
          accent: "bg-neon-orange",
          rgb: "255,153,0",
        };
      case "virus":
        return {
          border: "border-neon-purple",
          glow: "shadow-[0_0_25px_rgba(189,0,255,0.5)]",
          accent: "bg-neon-purple",
          rgb: "189,0,255",
        };
      case "data":
        return {
          border: "border-neon-blue",
          glow: "shadow-[0_0_25px_rgba(0,243,255,0.5)]",
          accent: "bg-neon-blue",
          rgb: "0,243,255",
        };
      case "free":
        return {
          border: "border-neon-green",
          glow: "shadow-[0_0_25px_rgba(0,255,65,0.5)]",
          accent: "bg-neon-green",
          rgb: "0,255,65",
        };
      default:
        return {
          border: "border-neon-blue/50",
          glow: "shadow-[0_0_15px_rgba(0,243,255,0.3)]",
          accent: "bg-neon-blue",
          rgb: "0,243,255",
        };
    }
  }

  const colors = $derived(getAttributeColors(digimon.attribute));
</script>

<a
  href="/digimon/{digimon.id}"
  class="digi-card group relative flex flex-col transition-all duration-300 hover:scale-[1.03] hover:{colors.glow}"
>
  <!-- Outer Glow Effect -->
  <div
    class="absolute -inset-1 rounded-xl opacity-0 group-hover:opacity-100 transition-opacity duration-500 blur-md"
    style="background: linear-gradient(135deg, rgba({colors.rgb},0.3), transparent, rgba({colors.rgb},0.3));"
  ></div>

  <!-- Card Frame with Corner Accents -->
  <div
    class="absolute inset-0 {colors.border} border-2 rounded-lg overflow-hidden"
  >
    <!-- Animated border glow -->
    <div
      class="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-300"
      style="box-shadow: inset 0 0 20px rgba({colors.rgb},0.3);"
    ></div>
  </div>

  <!-- Corner Brackets (Decorative) -->
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

  <!-- Background with Grid Pattern -->
  <div class="absolute inset-0 rounded-lg overflow-hidden">
    <!-- Dark gradient background -->
    <div
      class="absolute inset-0 bg-gradient-to-br from-cyber-dark-600 via-cyber-dark-800 to-cyber-dark"
    ></div>

    <!-- Digital grid pattern -->
    <div
      class="absolute inset-0 opacity-15 group-hover:opacity-30 transition-opacity duration-300"
      style="
      background-image: 
        linear-gradient(rgba({colors.rgb},0.2) 1px, transparent 1px),
        linear-gradient(90deg, rgba({colors.rgb},0.2) 1px, transparent 1px);
      background-size: 16px 16px;
    "
    ></div>

    <!-- Circuit line decorations -->
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

    <!-- Horizontal circuit lines -->
    <div
      class="absolute left-0 top-1/4 h-px w-4 opacity-30 group-hover:opacity-60 transition-opacity"
      style="background: linear-gradient(to right, rgba({colors.rgb},0.8), transparent);"
    ></div>
    <div
      class="absolute right-0 bottom-1/3 h-px w-5 opacity-25 group-hover:opacity-55 transition-opacity"
      style="background: linear-gradient(to left, rgba({colors.rgb},0.7), transparent);"
    ></div>

    <!-- Scan line effect on hover -->
    <div
      class="absolute inset-0 bg-gradient-to-b from-transparent via-white/5 to-transparent
                translate-y-full group-hover:translate-y-[-100%] transition-transform duration-700 ease-in-out"
    ></div>
  </div>

  <!-- Card Content -->
  <div class="relative z-10 p-3 flex flex-col h-full">
    <!-- Digimon Image Container -->
    <div class="relative aspect-square flex items-center justify-center mb-3">
      <!-- Inner frame with glow -->
      <div
        class="absolute inset-2 rounded opacity-20 group-hover:opacity-40 transition-opacity"
        style="border: 1px solid rgba({colors.rgb},0.5); box-shadow: inset 0 0 15px rgba({colors.rgb},0.1);"
      ></div>

      <!-- Small decorative hexagons -->
      <div
        class="absolute top-3 right-3 w-2 h-2 opacity-40 group-hover:opacity-70 transition-opacity"
        style="background: rgba({colors.rgb},0.6); clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);"
      ></div>
      <div
        class="absolute bottom-3 left-3 w-1.5 h-1.5 opacity-30 group-hover:opacity-60 transition-opacity"
        style="background: rgba({colors.rgb},0.5); clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);"
      ></div>

      <!-- Image -->
      <img
        src={digimon.image}
        alt={digimon.name}
        class="relative max-w-[85%] max-h-[85%] object-contain
               transition-all duration-300 group-hover:scale-110"
        style="filter: drop-shadow(0 0 8px rgba({colors.rgb},0.3));"
        loading="lazy"
      />
    </div>

    <!-- Digimon Info -->
    <div class="mt-auto text-center space-y-1">
      <!-- Decorative line above name -->
      <div
        class="w-8 h-px mx-auto mb-2 opacity-40 group-hover:opacity-80 group-hover:w-12 transition-all duration-300"
        style="background: linear-gradient(90deg, transparent, rgba({colors.rgb},0.8), transparent);"
      ></div>

      <h3
        class="font-display text-sm sm:text-base font-bold text-white uppercase tracking-wider truncate
                 transition-all duration-300"
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

    <!-- Bottom Accent Line with glow -->
    <div
      class="absolute bottom-0 left-1/2 -translate-x-1/2 w-1/3 h-0.5 rounded-full opacity-50
                group-hover:w-2/3 group-hover:opacity-100 transition-all duration-300"
      style="background: rgba({colors.rgb},1); box-shadow: 0 0 10px rgba({colors.rgb},0.8);"
    ></div>
  </div>

  <!-- Attribute Indicator with glow -->
  <div
    class="absolute top-2 right-2 w-2 h-2 rounded-full opacity-70 group-hover:opacity-100 transition-opacity"
    style="background: rgba({colors.rgb},1); box-shadow: 0 0 8px rgba({colors.rgb},0.8);"
  ></div>

  <!-- Small data indicator -->
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
</style>
