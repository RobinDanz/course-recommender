<script setup lang="ts">
import Dropdown from 'primevue/dropdown'
import PageHeader from '@/components/page/PageHeader.vue'
import TeacherForm from '@/components/forms/TeacherForm.vue'
import PageContent from '@/components/page/PageContent.vue'
import { getCourseList } from '@/services/courseService'
import { onBeforeMount, ref } from 'vue'
import type { Course } from '@/models/course'

const courses = ref<Array<Course>>()

const selectedCourse = ref<number>(1)
const coursesOptions = ref<Array<any>>([])

onBeforeMount(async () => {
  courses.value = await getCourseList()
  for (var i in courses.value) {
    if (!courses.value[i].teacher_form_filled) {
      coursesOptions.value.push({
        label: courses.value[i].title,
        option: courses.value[i].id
      })
    }
  }
})
</script>

<template>
  <PageHeader title="Recommender"></PageHeader>
  <PageContent>
    <template #content>
      <Dropdown
        v-model="selectedCourse"
        :options="coursesOptions"
        name="courses"
        optionLabel="label"
        optionValue="option"
      ></Dropdown>
      <TeacherForm :selected_course_id="selectedCourse"></TeacherForm>
    </template>
  </PageContent>
</template>
