<script setup lang="ts">
import PageHeader from '@/components/page/PageHeader.vue'

import { onBeforeMount, onMounted, ref } from 'vue'
import { getCourseList } from '@/services/courseService'
import type { Course } from '@/models/course'
import CourseCard from '@/components/cards/CourseCard.vue'
import PageContent from '@/components/page/PageContent.vue'
import Button from 'primevue/button'
import MultiSelect from 'primevue/multiselect'
import Dropdown from 'primevue/dropdown'
import OverlayPanel from 'primevue/overlaypanel'

const courses = ref<Course[]>()
const displayedCourse = ref<Course[]>()

const trackFilter = ref([0, 1, 2, 3, 4, 5, 6])
const semesterFilter = ref([0, 1])
const universityFilter = ref([0, 1, 2])
const courseTypeFilter = ref([0, 1])
const filteringPanel = ref()

const trackOptions = [
  { label: '0 - General', option: 0 },
  { label: '1 - Distributed Software Systems', option: 1 },
  { label: '2 - Security', option: 2 },
  { label: '3 - Visual Computing', option: 3 },
  { label: '4 - Theory and Logic', option: 4 },
  { label: '5 - Information Systems and Decision Support', option: 5 },
  { label: '6 - Data Science', option: 6 }
]

const universityOptions = [
  { label: 'Bern', option: 0 },
  { label: 'Fribourg', option: 1 },
  { label: 'Neuchâtel', option: 2 }
]

const semesterOptions = ref([
  { label: 'Spring', option: 0 },
  { label: 'Autumn', option: 1 }
])

const courseTypeOptions = [
  { label: 'Course', option: 0 },
  { label: 'Seminar', option: 1 }
]

onBeforeMount(async () => {
  courses.value = await getCourseList()

  displayedCourse.value = courses.value
})

const openFilteringPanel = (event: Event) => {
  filteringPanel.value.toggle(event)
}

const filter = (course: Course) => {
  return (
    trackFilter.value.includes(course.track) &&
    courseTypeFilter.value.includes(course.type) &&
    universityFilter.value.includes(course.site) &&
    semesterFilter.value.includes(course.semester)
  )
}

const applyFilter = () => {
  displayedCourse.value = courses.value?.filter((c) => filter(c))
}

const resetFilter = () => {
  trackFilter.value = [0, 1, 2, 3, 4, 5, 6]
  semesterFilter.value = [0, 1]
  universityFilter.value = [0, 1, 2]
  courseTypeFilter.value = [0, 1]

  displayedCourse.value = courses.value
}
</script>

<template>
  <PageHeader title="Course List"></PageHeader>
  <div class="header flex justify-content-end mb-2 mr-4">
    <Button @click="openFilteringPanel">Filter</Button>
  </div>
  <PageContent>
    <template #content>
      <div class="w-9 m-auto">
        <CourseCard
          v-for="course in displayedCourse"
          :course="course"
          :key="course.id"
        ></CourseCard></div
    ></template>
  </PageContent>
  <OverlayPanel ref="filteringPanel" class="w-25rem">
    <div class="flex flex-column">
      <div class="grid my-1">
        <div class="col-4 flex align-items-center">Track</div>
        <div class="col-8">
          <MultiSelect
            v-model="trackFilter"
            :options="trackOptions"
            placeholder="Select tracks"
            option-label="label"
            option-value="option"
            display="chip"
            class="w-15rem"
          ></MultiSelect>
        </div>
      </div>
      <div class="grid my-2">
        <div class="col-4">Semester</div>
        <div class="col-8">
          <MultiSelect
            v-model="semesterFilter"
            :options="semesterOptions"
            placeholder="Select semester"
            option-label="label"
            option-value="option"
            display="chip"
            class="w-15rem"
          ></MultiSelect>
        </div>
      </div>
      <div class="grid my-2">
        <div class="col-4 flex align-items-center">University</div>
        <div class="col-8">
          <MultiSelect
            v-model="universityFilter"
            :options="universityOptions"
            placeholder="Select universities"
            option-label="label"
            option-value="option"
            display="chip"
            class="w-15rem"
          ></MultiSelect>
        </div>
      </div>
      <div class="grid my-2">
        <div class="col-4 flex align-items-center">Type</div>
        <div class="col-8">
          <MultiSelect
            v-model="courseTypeFilter"
            :options="courseTypeOptions"
            placeholder="Select course type"
            option-label="label"
            option-value="option"
            display="chip"
            class="w-15rem"
          ></MultiSelect>
        </div>
      </div>
      <div class="flex justify-content-end">
        <Button class="mr-1" @click="applyFilter">Apply</Button>
        <Button severity="secondary" @click="resetFilter">Reset</Button>
      </div>
    </div>
  </OverlayPanel>
</template>

<style scoped></style>
