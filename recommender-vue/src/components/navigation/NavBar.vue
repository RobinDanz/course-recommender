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
    label: 'Recommender',
    icon: 'pi pi-lightbulb',
    route_name: 'recommender'
  },
  // {
  //   label: 'About',
  //   icon: 'pi pi-star',
  //   route_name: 'about'
  // },
  {
    label: 'Courses',
    icon: 'pi pi-book',
    items: [
      {
        label: 'Course List',
        icon: 'pi pi-list',
        route_name: 'course-list'
      },
      {
        label: 'Timetable',
        icon: 'pi pi-calendar',
        route_name: 'course-timetable'
      }
    ]
  }
])
</script>

<template>
  <Menubar :model="items">
    <template #item="{ item, props, hasSubmenu }">
      <RouterLink
        v-if="item.route_name"
        v-slot="{ href, navigate }"
        :to="{ name: item.route_name }"
        custom
      >
        <a :href="href" v-bind="props.action" @click="navigate">
          <span :class="item.icon"></span>
          <span class="ml-2">{{ item.label }}</span>
        </a>
      </RouterLink>
      <a v-else :href="item.url" :target="item.target" v-bind="props.action">
        <span :class="item.icon"></span>
        <span class="ml-2">{{ item.label }}</span>
        <span v-if="hasSubmenu" class="pi pi-fw pi-angle-down ml-2" />
      </a>
    </template>

    <!-- <template #end>
      <RouterLink :to="{ name: 'login' }" v-slot="{ href, navigate }" custom>
        <a :href="href" @click="navigate">
          <span class="ml-2">login</span>
        </a>
      </RouterLink>
    </template> -->
  </Menubar>
</template>

<style scoped></style>
