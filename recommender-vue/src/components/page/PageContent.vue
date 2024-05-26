<script setup lang="ts"></script>

<template>
  <div class="px-5 overflow-y-auto height">
    <slot name="content" class=""></slot>
  </div>
</template>

<style scoped>
.height {
  max-height: 75vh;
}
</style>
