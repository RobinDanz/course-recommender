<script setup lang="ts">
import PageHeader from '@/components/page/PageHeader.vue'

import { onMounted, ref } from 'vue'
import { getCourseList } from '@/services/courseService'
import type { Course } from '@/models/course'
import CourseCard from '@/components/cards/CourseCard.vue'

const courses = ref<Course[]>()

onMounted(async () => {
  courses.value = await getCourseList()
})
</script>

<template>
  <PageHeader title="Course List"></PageHeader>
  <div class="w-9 m-auto">
    <CourseCard v-for="course in courses" :course="course" :key="course.id"></CourseCard>
  </div>
</template>
