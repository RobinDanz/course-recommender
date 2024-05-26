<script setup lang="ts">
import {
  type Course,
  dayToString,
  formatStartToEnd,
  formatCourseType,
  formatCourseUniversity
} from '@/models/course'
import { onBeforeMount, ref } from 'vue'
import { getCourse } from '@/services/courseService'
import PageHeader from '@/components/page/PageHeader.vue'
import PageContent from '@/components/page/PageContent.vue'

const props = defineProps({
  courseId: {
    type: String,
    required: true
  }
})

const course = ref<Course>()

onBeforeMount(async () => {
  course.value = await getCourse(parseInt(props.courseId))
})
</script>

<template>
  <PageHeader :title="course?.title"></PageHeader>
  <PageContent>
    <template #content>
      <div class="flex flex-column" v-if="course">
        <h3>Description</h3>
        <pre class="description">{{ course.description }}</pre>
        <h3>Details</h3>
        <div class="flex flex-column">
          <div class="grid">
            <div class="col-6">Day</div>
            <div class="col-6">{{ dayToString(course) }}</div>
          </div>
          <div class="grid">
            <div class="col-6">Type</div>
            <div class="col-6">{{ formatCourseType(course) }}</div>
          </div>
          <div class="grid">
            <div class="col-6">University</div>
            <div class="col-6">{{ formatCourseUniversity(course) }}</div>
          </div>
          <div class="grid">
            <div class="col-6">Course Code</div>
            <div class="col-6">{{ course.code }}</div>
          </div>
          <div class="grid">
            <div class="col-6">Schedule</div>
            <div class="col-6">{{ formatStartToEnd(course) }}</div>
          </div>
          <div class="grid">
            <div class="col-6">Track</div>
            <div class="col-6">{{ course.track }}</div>
          </div>
          <div class="grid">
            <div class="col-6">Semester</div>
            <div class="col-6">{{ course.semester }}</div>
          </div>
          <div class="grid">
            <div class="col-6">JMCS URL</div>
            <div class="col-6"><a :href="course.url">Visit JMCS website</a></div>
          </div>
        </div>
      </div>
    </template>
  </PageContent>
</template>

<style scoped>
.description {
  white-space: break-spaces;
  font-family: inherit;
}

.height {
  max-height: 80vh;
}
</style>
