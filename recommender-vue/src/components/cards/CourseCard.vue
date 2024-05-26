<script setup lang="ts">
import { type Course, dayToString } from '@/models/course'

const props = defineProps<{
  course: Course
}>()
</script>

<template>
  <RouterLink
    v-slot="{ navigate }"
    :to="{ name: 'course-details', params: { courseId: props.course.id } }"
    custom
  >
    <div class="course-card bordered m-2" @click="navigate">
      <div class="flex flex-column">
        <div>
          <h4>{{ props.course.title }}</h4>
        </div>
        {{ dayToString(props.course) + ': ' + props.course.start + ' - ' + props.course.end }}
      </div>
    </div>
  </RouterLink>
</template>

<style scoped>
.course-card:hover {
  cursor: pointer;
  background: rgb(16, 185, 129, 0.3);
}
</style>
