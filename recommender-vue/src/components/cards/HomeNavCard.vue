<script setup lang="ts">
import { useRouter } from 'vue-router'
const props = defineProps<{
  title: string
  subtitle: string
  localRedirect?: Object
  webRedirect?: string
}>()

const router = useRouter()

const redirect = () => {
  if (props.localRedirect) {
    router.push(props.localRedirect)
  }

  if (props.webRedirect) {
    window.location.replace(props.webRedirect)
  }
}
</script>

<template>
  <div class="bordered nav-card my-4 flex flex-column" @click="redirect">
    <div class="grid grid-nogutter">
      <div class="col-10">
        <div class="font-bold">
          {{ props.title }}
        </div>
        <div>
          {{ props.subtitle }}
        </div>
      </div>
      <div class="col-2 flex justify-content-end">
        <i class="pi pi-arrow-right toggle-icon" style="font-size: 2.5rem; opacity: 0%"></i>
      </div>
    </div>
  </div>
</template>

<style scoped>
.nav-card:hover {
  cursor: pointer;
  background: rgb(16, 185, 129, 0.3);
}

.nav-card:hover .toggle-icon {
  opacity: 80% !important;
  color: #0aa831;
}
</style>
