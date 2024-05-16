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
import { time } from 'console'

const courses = ref<Course[]>()
const coursesMap = ref<Record<number, Array<Course>>>({})

const selectedDate = today()

const getCourses = (timestamp: Timestamp) => {
  return coursesMap.value[timestamp.weekday]
}

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
    s.width = index * (size - 1) + '%'
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

  courses.value.forEach((c) => {
    if (!(c.day in coursesMap.value)) {
      coursesMap.value[c.day] = []
    }

    coursesMap.value[c.day].push(c)
  })
})

const courseClick = (course: Course) => {
  console.log(course.id)
}
</script>

<template>
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
        <template v-for="ev in getCourses(timestamp)" :key="ev.id">
          <div
            class="event"
            :style="eventStyle(ev, timeStartPos, timeDurationHeight)"
            @click="courseClick(ev)"
          >
            <span class="m-auto"> {{ ev.title }} </span>
          </div>
        </template>
      </template>
    </QCalendarDay>
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
</style>
