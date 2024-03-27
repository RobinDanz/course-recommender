<script setup lang="ts">
import Menubar from 'primevue/menubar'
import { ref } from 'vue'

const items = ref([
  {
    label: 'Home',
    icon: 'pi pi-home',
    route_name: 'home'
  },
  {
    label: 'Features',
    icon: 'pi pi-star',
    route_name: 'about'
  }
])
</script>

<template>
  <header>
    <Menubar :model="items">
      <template></template>
    </Menubar>
  </header>

  <main>
    <RouterView></RouterView>
  </main>
</template>

<style scoped></style>
