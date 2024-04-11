<script setup lang="ts">
import { ref } from 'vue'
import Menubar from 'primevue/menubar'

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
  <Menubar :model="items">
    <template #item="{ item }">
      <RouterLink :to="{ name: item.route_name }">
        <a>
          <span :class="item.icon" />
          <span class="ml-2">{{ item.label }}</span>
        </a>
      </RouterLink>
    </template>
    <template #end>
      <RouterLink :to="{ name: 'login' }">
        <a>
          <span class="ml-2">login</span>
        </a>
      </RouterLink>
    </template>
  </Menubar>
</template>
