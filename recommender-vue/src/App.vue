<script setup lang="ts">
import NavBar from '@/components/navigation/NavBar.vue'
</script>

<template>
  <header>
    <NavBar></NavBar>
  </header>
  <main class="">
    <RouterView></RouterView>
  </main>
</template>

<style scoped></style>
