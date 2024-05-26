<style src="@quasar/quasar-ui-qcalendar/dist/QCalendarScheduler.min.css"></style>
<script setup lang="ts">
import { onBeforeMount, onMounted, ref } from 'vue'
import { getCourseList } from '@/services/courseService'
import { type Course, calculateDuration } from '@/models/course'
import {
  QCalendarDay,
  today,
  isBetweenDates,
  type Timestamp
} from '@quasar/quasar-ui-qcalendar/src/index.js'
import '@quasar/quasar-ui-qcalendar/src/QCalendarVariables.sass'
import '@quasar/quasar-ui-qcalendar/src/QCalendarTransitions.sass'
import '@quasar/quasar-ui-qcalendar/src/QCalendarDay.sass'
import OverlayPanel from 'primevue/overlaypanel'
import { useRouter } from 'vue-router'
import Button from 'primevue/button'
import MultiSelect from 'primevue/multiselect'
import Dropdown from 'primevue/dropdown'

const router = useRouter()

// Courses in the timetable related
const courses = ref<Course[]>()
const coursesMap = ref<Record<number, Array<Course>>>({})
const selectedDate = today()

// Filter related
const trackFilter = ref([1, 2, 3])
const selectedSemester = ref(0)
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

const courseTypeOptions = [
  { label: 'Course', option: 0 },
  { label: 'Seminar', option: 1 }
]

const trackerPos = ref({
  left: 50,
  top: 50
})

const trackerContent = ref({
  title: '',
  start: '',
  end: ''
})

const semesterOptions = ref([
  { label: 'Spring', option: 0 },
  { label: 'Autumn', option: 1 }
])

const displayTracker = ref(false)

const colorPalette = ['#81E67F', '#FF3E2E', '#E6AE84', '#2233E6', '#DE1FF0', '#F5CF35', '#31E4E6']

// === ENTRY POINT ===

onBeforeMount(async () => {
  courses.value = await getCourseList()
  refreshCoursesMap()
})

const eventStyle = (course: Course, timeStartPos: Function, timeDurationHeight: Function) => {
  const s = {
    top: '',
    height: '',
    left: '',
    width: '100%',
    backgroundColor: colorPalette[course.track]
  }

  if (timeStartPos && timeDurationHeight) {
    s.top = timeStartPos(course.start) + 'px'
    s.height = timeDurationHeight(calculateDuration(course)) + 'px'
  }

  if (coursesMap.value[course.day].length > 1) {
    let index = coursesMap.value[course.day].indexOf(course)
    const size = 100 / coursesMap.value[course.day].length
    s.left = index * size + '%'

    if (index === 0) index += 1
    s.width = size - 1 + '%'
  }

  return s
}

// === MAPPING ===
const refreshCoursesMap = () => {
  if (courses.value) {
    coursesMap.value = {}
    courses.value.forEach((c) => {
      if (!(c.day in coursesMap.value)) {
        coursesMap.value[c.day] = []
      }
      if (filter(c)) {
        coursesMap.value[c.day].push(c)
      }
    })
  }
}

// === FILTERING METHODS ===
const filter = (course: Course) => {
  return (
    trackFilter.value.includes(course.track) &&
    courseTypeFilter.value.includes(course.type) &&
    universityFilter.value.includes(course.site) &&
    selectedSemester.value == course.semester
  )
}

const resetFilter = () => {
  trackFilter.value = [1, 2, 3]
  courseTypeFilter.value = [0, 1]
  universityFilter.value = [0, 1, 2]
  selectedSemester.value = 0
  refreshCoursesMap()
}

// === PAGE ACTIONS ==
const openFilteringPanel = (event: Event) => {
  filteringPanel.value.toggle(event)
}

const courseClick = (course: Course) => {
  router.push({ name: 'course-details', params: { courseId: course.id } })
}

const mouseMove = (event: MouseEvent, course: Course) => {
  trackerPos.value.left = event.pageX
  trackerPos.value.top = event.pageY

  trackerContent.value.title = course.title
  trackerContent.value.start = course.start
  trackerContent.value.end = course.end
}
</script>

<template>
  <div class="mb-3 flex justify-content-end">
    <Button @click="openFilteringPanel">Filter</Button>
  </div>
  <div v-if="courses" class="flex" style="max-width: 2000px; width: 100%; height: 600px">
    <QCalendarDay
      v-model="selectedDate"
      view="week"
      :weekdays="[1, 2, 3, 4, 5]"
      :hour24-format="true"
      :interval-start="32"
      :interval-count="44"
      :interval-minutes="15"
      bordered
    >
      <template #day-body="{ scope: { timestamp, timeStartPos, timeDurationHeight } }">
        <template v-for="ev in coursesMap[timestamp.weekday]" :key="ev.id">
          <div
            class="event"
            :style="eventStyle(ev, timeStartPos, timeDurationHeight)"
            @click="courseClick(ev)"
            @mouseenter="displayTracker = true"
            @mouseleave="displayTracker = false"
            @mousemove="mouseMove($event, ev)"
          >
            <span class="m-auto"> {{ ev.title }} </span>
          </div>
        </template>
      </template>
    </QCalendarDay>
  </div>
  <div
    v-show="displayTracker"
    class="tracker p-2"
    :style="{ left: 15 + trackerPos.left + 'px', top: 15 + trackerPos.top + 'px' }"
  >
    {{ trackerContent.title }}
    {{ trackerContent.start }}
    {{ trackerContent.end }}
  </div>
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
          <Dropdown
            v-model="selectedSemester"
            :options="semesterOptions"
            option-label="label"
            option-value="option"
            placeholder="Select a semester"
            checkmark
            class="w-15rem"
          />
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
        <Button class="mr-1" @click="refreshCoursesMap">Apply</Button>
        <Button severity="secondary" @click="resetFilter">Reset</Button>
      </div>
    </div>
  </OverlayPanel>
</template>

<style scoped>
#calendar {
  width: 100%;
  height: 900px;
  max-height: 90vh;
}

.event {
  position: absolute;
  border: 1px solid black;
  border-radius: 3px;
  color: white;
}

.event:hover {
  background-color: chocolate;
  box-shadow: 3px 3px 5px rgb(0 0 0 / 50%);
  z-index: 1000;
  cursor: pointer;
}
.tracker {
  border-radius: 10px;
  position: absolute;
  background-color: gray;
  height: 150px;
  width: 150px;
  z-index: 1500;
  pointer-events: none;
  box-shadow: 3px 3px 5px rgb(0 0 0 / 50%);
  overflow: hidden;
}
</style>
