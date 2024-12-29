<script setup lang="ts">
import { onBeforeMount, ref } from 'vue'
import { getCourseList } from '@/services/courseService'
import {
  type Course,
  calculateDuration,
  formatTracks,
  formatStartToEnd,
  formatCourseUniversity
} from '@/models/course'
import { QCalendarResource } from '@quasar/quasar-ui-qcalendar'
import '@quasar/quasar-ui-qcalendar/src/QCalendarVariables.sass'
import '@quasar/quasar-ui-qcalendar/src/QCalendarTransitions.sass'
import '@quasar/quasar-ui-qcalendar/src/QCalendarDay.sass'
import '@quasar/quasar-ui-qcalendar/src/QCalendarResource.sass'
import OverlayPanel from 'primevue/overlaypanel'
import { useRouter } from 'vue-router'
import Button from 'primevue/button'
import MultiSelect from 'primevue/multiselect'
import Dropdown from 'primevue/dropdown'

const router = useRouter()

// Courses in the timetable related
const courses = ref<Course[]>()
const coursesMap = ref<Record<number, Array<Course>>>({})

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
  schedule: '',
  university: '',
  track: ''
})

const semesterOptions = ref([
  { label: 'Spring', option: 0 },
  { label: 'Autumn', option: 1 }
])

const displayTracker = ref(false)

const colorPalette = ['#BA3211', '#2A7A5F', '#10B981', '#65362B', '#233B33', '#332927', '#BD745B']

// === ENTRY POINT ===

onBeforeMount(async () => {
  courses.value = await getCourseList()
  refreshCoursesMap()
})

const resources = ref([
  { id: 1, name: 'Monday', height: 70 },
  { id: 2, name: 'Tuesday', height: 70 },
  { id: 3, name: 'Wednesday', height: 70 },
  { id: 4, name: 'Thursday', height: 70 },
  { id: 5, name: 'Friday', height: 70 }
])

const convertTimeToNumber = (time: string) => {
  const hours = Number(time.split(':')[0])
  const minutes = Number(time.split(':')[1]) / 60
  return hours + minutes
}

const eventStyle = (course: Course, scope: Object) => {
  if (course.start) {
    const s = {
      left: '',
      width: '',
      height: '',
      top: '0px'
    }

    if (course.tracks.length == 1) {
      s['background'] = colorPalette[course.tracks[0].numeric_code]
    } else {
      let color1 = colorPalette[course.tracks[0].numeric_code]
      let color2 = colorPalette[course.tracks[1].numeric_code]
      s['background-image'] = 'linear-gradient(to right, ' + color1 + ' , ' + color2 + ')'
    }

    const divSize = 35

    s.left = scope.timeStartPosX(course.start) + 'px'
    s.width = scope.timeDurationWidth(calculateDuration(course)) + 'px'
    s.height = divSize + 'px'
    let boxSize = divSize
    let maxOverlap = 0
    if (coursesMap.value[course.day].length > 1) {
      let overlapCount = 0
      coursesMap.value[course.day].forEach((c, index) => {
        if (c.id != course.id && coursesMap.value[course.day].indexOf(course) > index) {
          let c1start = convertTimeToNumber(course.start)
          let c1end = convertTimeToNumber(course.end)

          let c2start = convertTimeToNumber(c.start)
          let c2end = convertTimeToNumber(c.end)

          if (c1end >= c2start && c1start <= c2end) {
            overlapCount++
          }
        }
      })
      if (overlapCount > maxOverlap) {
        maxOverlap = overlapCount
        console.log(maxOverlap)
      }
      s.top = maxOverlap * divSize + maxOverlap + 'px'
      boxSize += maxOverlap * divSize + maxOverlap
    }

    if (resources.value[course.day - 1].height < boxSize) {
      resources.value[course.day - 1].height = boxSize
    }
    return s
  }
}

// === MAPPING ===
const refreshCoursesMap = () => {
  if (courses.value) {
    coursesMap.value = {}
    courses.value.forEach((c) => {
      if (c.start) {
        if (!(c.day in coursesMap.value)) {
          coursesMap.value[c.day] = []
        }
        if (filter(c)) {
          coursesMap.value[c.day].push(c)
        }
      }
    })

    for (const l of Object.values(coursesMap.value)) {
      l.sort((a, b) => {
        return new Date('1970/01/01 ' + a.start) - new Date('1970/01/01 ' + b.start)
      })
    }
  }
}

// === FILTERING METHODS ===
const filter = (course: Course) => {
  return (
    trackFilter.value.some((v) => course.tracks.map((t) => t.numeric_code).includes(v)) &&
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
  trackerContent.value.schedule = formatStartToEnd(course)
  trackerContent.value.university = formatCourseUniversity(course)
  trackerContent.value.track = 'Track(s): ' + formatTracks(course)
}
</script>

<template>
  <div class="mb-1 flex justify-content-end">
    <Button @click="openFilteringPanel">Filter</Button>
  </div>
  <div v-if="courses" class="flex m-auto" style="max-width: 1102px; width: auto">
    <QCalendarResource
      v-model:model-resources="resources"
      resource-key="id"
      resource-label="name"
      :interval-start="8"
      :interval-count="10"
      :interval-minutes="60"
      :hour24-format="true"
      :cell-max-width="130"
      bordered
    >
      <template #resource-intervals="{ scope }">
        <template v-for="(event, index) in coursesMap[scope.resourceIndex + 1]" :key="index">
          <div
            class="event flex"
            :style="eventStyle(event, scope)"
            @click="courseClick(event)"
            @mouseenter="displayTracker = true"
            @mouseleave="displayTracker = false"
            @mousemove="mouseMove($event, event)"
          >
            <div class="px-2 my-auto text-xs event-text">
              {{ event.title }}
            </div>
          </div>
        </template>
      </template>
    </QCalendarResource>
  </div>
  <div
    v-if="displayTracker"
    class="tracker p-2 flex flex-column"
    :style="{ left: 15 + trackerPos.left + 'px', top: 15 + trackerPos.top + 'px' }"
  >
    <!-- <div>
      {{ trackerContent.title }}
    </div>
    <div>
      {{ trackerContent.schedule }}
    </div>
    <div>
      {{ trackerContent.university }}
    </div>
    <div>
      {{ trackerContent.track }}
    </div> -->
    <div>
      {{ trackerContent.title }}
    </div>
    <div>
      <i class="pi pi-calendar-clock"></i>
      {{ trackerContent.schedule }}
    </div>
    <div class="my-1">
      <i class="pi pi-map-marker"></i>
      {{ trackerContent.university }}
    </div>
    <div>
      {{ trackerContent.track }}
    </div>
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
  background-color: rgba(190, 190, 190, 0.9);
  /* height: 150px; */
  /* width: 150px; */
  z-index: 1500;
  pointer-events: none;
  box-shadow: 3px 3px 5px rgb(0 0 0 / 50%);
  overflow: hidden;
}

.event-text {
  text-overflow: ellipsis'...';
  overflow: hidden;
  text-wrap: nowrap;
}
</style>
