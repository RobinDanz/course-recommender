<script setup lang="ts">
const props = defineProps<{
  title?: string
  subtitle?: string
}>()
</script>

<template>
  <div class="px-5">
    <div class="m-auto">
      <h1>{{ props.title }}</h1>
      <h2>{{ props.subtitle }}</h2>
    </div>
  </div>
</template>
