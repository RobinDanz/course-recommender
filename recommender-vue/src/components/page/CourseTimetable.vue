<style src="@quasar/quasar-ui-qcalendar/dist/QCalendarScheduler.min.css"></style>
<script setup lang="ts">
import { onBeforeMount, onMounted, ref } from 'vue'
import { getCourseList } from '@/services/courseService'
import type { Course } from '@/models/course'
import {
  QCalendarDay,
  today,
  isBetweenDates,
  type Timestamp
} from '@quasar/quasar-ui-qcalendar/src/index.js'
import '@quasar/quasar-ui-qcalendar/src/QCalendarVariables.sass'
import '@quasar/quasar-ui-qcalendar/src/QCalendarTransitions.sass'
import '@quasar/quasar-ui-qcalendar/src/QCalendarDay.sass'

const courses = ref<Course[]>()
const coursesMap = ref<Record<number, Array<Course>>>({})

const selectedDate = today()

const trackFilter = ref([1, 2, 3])
const semesterFilter = ref([0])

const trackerPos = ref({
  left: 50,
  top: 50
})

const trackerContent = ref({
  title: '',
  start: '',
  end: ''
})
const displayTracker = ref(false)

const colorPalette = ['', '', '', '', '', '', '']

const eventStyle = (course: Course, timeStartPos: Function, timeDurationHeight: Function) => {
  const s = {
    top: '',
    height: '',
    left: '',
    width: '100%'
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

const calculateDuration = (course: Course) => {
  const startVal = course.start.split(':').map((str) => Number.parseInt(str))

  const endVal = course.end.split(':').map((str) => Number.parseInt(str))

  const start = new Date()
  const startMili = start.setHours(startVal[0], startVal[1], 0, 0)

  const end = new Date()
  const endMili = end.setHours(endVal[0], endVal[1], 0, 0)

  return (endMili - startMili) / 60000
}

onBeforeMount(async () => {
  courses.value = await getCourseList()

  refreshCoursesMap()
})

const courseClick = (course: Course) => {
  console.log(course.id)
}

const refreshCoursesMap = () => {
  if (courses.value) {
    coursesMap.value = {}
    courses.value.forEach((c) => {
      console.log(c.title)
      console.log(c.id)
      console.log('================')
      if (!(c.day in coursesMap.value)) {
        coursesMap.value[c.day] = []
      }
      if (trackFilter.value.includes(c.track) && semesterFilter.value.includes(c.semester)) {
        coursesMap.value[c.day].push(c)
      }
    })
  }
  console.log(coursesMap.value)
  console.log(coursesMap.value['2'])
}

const filter = () => {
  trackFilter.value = [4, 5, 6]
  refreshCoursesMap()
}

const resetFilter = () => {
  trackFilter.value = [0, 1, 2, 3, 4, 5, 6]
  refreshCoursesMap()
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
  <button @click="filter">filter</button>
  <button @click="resetFilter">reset filter</button>
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
  background-color: blueviolet;
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
