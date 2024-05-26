<script setup lang="ts">
import type { Course } from '@/models/course'
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

  console.log(course.value)
})
</script>

<template>
  <PageHeader :title="course?.title"></PageHeader>
  <PageContent>
    <template #content>
      <div class="flex flex-column">
        <h3>Course Description</h3>
        <pre class="description">{{ course?.description }}</pre>
        <h3>Course Details</h3>
        <p>{{ 'day: ' + course?.day }}</p>
        <p>{{ 'type: ' + course?.type }}</p>
        <p>{{ 'university:' + course?.site }}</p>
        <p>{{ 'code:' + course?.code }}</p>
        <p>{{ 'start:' + course?.start }}</p>
        <p>{{ 'end:' + course?.end }}</p>
        <p>{{ 'track:' + course?.track }}</p>
        <p>{{ 'semester:' + course?.semester }}</p>
        <h3>External links</h3>
        <p>{{ 'JMCS url:' + course?.url }}</p>
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
