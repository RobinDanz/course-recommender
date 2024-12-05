<script setup lang="ts">
import {
  type Course,
  dayToString,
  formatCourseUniversity,
  formatCourseSemester
} from '@/models/course'

const props = defineProps<{
  course: Course
}>()

console.log(props.course.tracks)
</script>

<template>
  <RouterLink
    v-slot="{ navigate }"
    :to="{ name: 'course-details', params: { courseId: props.course.id } }"
    custom
  >
    <div class="course-card bordered m-2 w-12rem" @click="navigate">
      <div class="flex flex-column">
        <div>
          <h4>{{ props.course.title }}</h4>
        </div>
        <div class="grid">
          <div class="col-6" v-if="course.start != null">
            {{ dayToString(props.course) + ': ' + props.course.start }}
          </div>
          <div class="col-6" v-else>
            {{ dayToString(props.course) }}
          </div>
          <div class="col-6 flex justify-content-end">
            <div>
              {{
                formatCourseUniversity(course) + ', ' + formatCourseSemester(course) + ' semester'
              }}
            </div>
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
