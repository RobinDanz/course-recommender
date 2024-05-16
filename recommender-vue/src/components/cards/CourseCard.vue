<script setup lang="ts">
import type { Course } from '@/models/course'

const props = defineProps<{
  course: Course
}>()
</script>

<template>
  <RouterLink
    v-slot="{ href, navigate }"
    :to="{ name: 'course-details', params: { courseId: props.course.id } }"
    custom
  >
    <a :href="href" @click="navigate">
      <div class="course-card bordered m-2">
        <div class="flex flex-column">
          <div>
            <h4>{{ props.course.title }}</h4>
          </div>
          {{ props.course.start + ' - ' + props.course.end }}
        </div>
      </div>
    </a>
  </RouterLink>
</template>
