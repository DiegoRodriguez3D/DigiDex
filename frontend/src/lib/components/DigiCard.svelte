<!-- DigiCard.svelte -->
<script lang="ts">
  import type { DigimonListItem } from '$lib/types';

  interface Props {
    digimon: DigimonListItem;
  }

  let { digimon }: Props = $props();

  // Determine glow class based on attribute
  function getGlowClass(attribute: string | null): string {
    if (!attribute) return 'glow-default';
    const attr = attribute.toLowerCase();
    if (attr === 'vaccine') return 'glow-vaccine';
    if (attr === 'virus') return 'glow-virus';
    if (attr === 'data') return 'glow-data';
    if (attr === 'free') return 'glow-free';
    return 'glow-default';
  }

  // Get border color class
  function getBorderColor(attribute: string | null): string {
    if (!attribute) return 'border-white/20';
    const attr = attribute.toLowerCase();
    if (attr === 'vaccine') return 'border-neon-orange';
    if (attr === 'virus') return 'border-neon-purple';
    if (attr === 'data') return 'border-neon-blue';
    if (attr === 'free') return 'border-neon-green';
    return 'border-white/20';
  }
</script>

<a
  href="/digimon/{digimon.id}"
  class="group glass-card border-2 {getBorderColor(digimon.attribute)} p-4 flex flex-col items-center gap-3 transition-all duration-300 hover:scale-[1.02] hover:{getGlowClass(digimon.attribute)}"
>
  <!-- Digimon Image -->
  <div class="relative w-full aspect-square flex items-center justify-center overflow-hidden">
    <img
      src={digimon.image}
      alt={digimon.name}
      class="max-w-full max-h-full object-contain transition-transform duration-300 group-hover:scale-110"
      loading="lazy"
    />
    <!-- Subtle scan line effect on hover -->
    <div class="absolute inset-0 bg-gradient-to-b from-transparent via-neon-blue/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none"></div>
  </div>

  <!-- Digimon Info -->
  <div class="text-center space-y-1 w-full">
    <h3 class="font-display text-sm sm:text-base font-bold text-white uppercase tracking-wide truncate">
      {digimon.name}
    </h3>
    {#if digimon.level}
      <p class="text-xs text-gray-400 font-mono">
        {digimon.level}
      </p>
    {/if}
  </div>

  <!-- Attribute Badge (if available) -->
  {#if digimon.attribute}
    <div class="absolute top-2 right-2">
      <span class="text-[10px] font-mono px-2 py-0.5 rounded-full {
        digimon.attribute.toLowerCase() === 'vaccine' ? 'bg-neon-orange/20 text-neon-orange' :
        digimon.attribute.toLowerCase() === 'virus' ? 'bg-neon-purple/20 text-neon-purple' :
        digimon.attribute.toLowerCase() === 'data' ? 'bg-neon-blue/20 text-neon-blue' :
        digimon.attribute.toLowerCase() === 'free' ? 'bg-neon-green/20 text-neon-green' :
        'bg-white/10 text-gray-400'
      }">
        {digimon.attribute}
      </span>
    </div>
  {/if}
</a>

<style>
  /* Ensure the card has relative positioning for absolute children */
  a {
    position: relative;
  }
</style>
