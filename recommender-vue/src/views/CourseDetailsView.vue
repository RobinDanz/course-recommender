<script setup lang="ts">
const props = defineProps({
  courseId: {
    type: String,
    required: true
  }
})
</script>

<template>
  <div>Coucou</div>
  <div>{{ props.courseId }}</div>
</template>
