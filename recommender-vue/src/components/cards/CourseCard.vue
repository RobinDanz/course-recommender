<script setup lang="ts">
import { type Course, dayToString, formatCourseUniversity, formatTracks } from '@/models/course'

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
    <div class="course-card bordered m-2 w-15rem" @click="navigate">
      <div class="flex flex-column">
        <div>
          <h4>{{ props.course.title }}</h4>
        </div>
        <div class="my-1">
          {{ 'Track(s): ' + formatTracks(course) }}
        </div>
        <div>
          <div v-if="course.start != null" class="my-1">
            <i class="pi pi-calendar-clock"></i>
            {{ dayToString(props.course) + ', ' + props.course.start }}
          </div>
          <div v-else class="my-1">
            <i class="pi pi-calendar-clock"></i>
            {{ dayToString(props.course) }}
          </div>
          <div class="my-1">
            <i class="pi pi-map-marker"></i>
            {{ formatCourseUniversity(course) }}
          </div>
        </div>
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
