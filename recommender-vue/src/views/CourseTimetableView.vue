<script setup lang="ts">
import PageHeader from '@/components/page/PageHeader.vue'
import CourseTimetable from '@/components/page/CourseTimetable.vue'
import { onMounted, ref } from 'vue'
import { getCourseList } from '@/services/courseService'
import type { Course } from '@/models/course'

const courses = ref<Course[]>()

onMounted(async () => {
  const course = await getCourseList()
})
</script>

<template>
  <PageHeader title="Course Timetable"></PageHeader>
  <CourseTimetable></CourseTimetable>
</template>
