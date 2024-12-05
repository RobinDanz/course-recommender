<script setup lang="ts">
import {
  type Course,
  dayToString,
  // formatStartToEnd,
  formatCourseType,
  formatCourseUniversity
} from '@/models/course'
import { onBeforeMount, ref } from 'vue'
import { getCourse } from '@/services/courseService'
import PageHeader from '@/components/page/PageHeader.vue'
import PageContent from '@/components/page/PageContent.vue'
import Divider from 'primevue/divider'
import Chart from 'primevue/chart'

const props = defineProps({
  courseId: {
    type: String,
    required: true
  }
})

const chartData = ref()
const chartOptions = ref()

const course = ref<Course>()

onBeforeMount(async () => {
  course.value = await getCourse(parseInt(props.courseId))
  chartData.value = setChartData()
  chartOptions.value = setChartOptions()
})

const setChartData = () => {
  const data = []

  data.push(course.value?.lectures)
  data.push(course.value?.subject_type)
  data.push(course.value?.interactions)
  data.push(course.value?.blackboard)
  data.push(course.value?.recordings)
  data.push(course.value?.teacher_accessibility)

  return {
    labels: [
      'lectures',
      'subject_type',
      'interactions',
      'blackboard',
      'recordings',
      'teacher_accessibility'
    ],
    datasets: [
      {
        borderColor: 'blue',
        pointBackgroundColor: 'blue',
        pointBorderColor: 'black',
        data: data
      }
    ]
  }
}

const setChartOptions = () => {
  return {
    plugins: {
      legend: {
        display: false
      }
    },
    scales: {
      r: {
        grid: {
          color: 'gray'
        },
        suggestedMin: 0,
        suggestedMax: 100
      }
    }
  }
}
</script>

<template>
  <PageHeader :title="course?.title"></PageHeader>
  <PageContent>
    <template #content>
      <div class="grid">
        <div class="col-8 flex flex-column" v-if="course">
          <h3>Description</h3>
          <pre class="description">{{ course.description }}</pre>
          <h3>Details</h3>
          <div class="flex flex-column">
            <div class="grid">
              <div class="col-6">Day</div>
              <div class="col-6">{{ dayToString(course) }}</div>
            </div>
            <div class="grid">
              <div class="col-6">Type</div>
              <div class="col-6">{{ formatCourseType(course) }}</div>
            </div>
            <div class="grid">
              <div class="col-6">University</div>
              <div class="col-6">{{ formatCourseUniversity(course) }}</div>
            </div>
            <div class="grid">
              <div class="col-6">Course Code</div>
              <div class="col-6">{{ course.code }}</div>
            </div>
            <div class="grid">
              <div class="col-6">Schedule</div>
              <!-- <div class="col-6">{{ formatStartToEnd(course) }}</div> -->
            </div>
            <div class="grid">
              <div class="col-6">Track</div>
              <div class="col-6">{{ course.track }}</div>
            </div>
            <div class="grid">
              <div class="col-6">Semester</div>
              <div class="col-6">{{ course.semester }}</div>
            </div>
            <div class="grid">
              <div class="col-6">JMCS URL</div>
              <div class="col-6"><a :href="course.url">Visit JMCS website</a></div>
            </div>
          </div>
        </div>
        <Divider layout="vertical" />
        <div class="col flex flex-column">
          <h3>Course profile</h3>
          <div class="chart">
            <Chart
              type="radar"
              :data="chartData"
              :options="chartOptions"
              class="w-full md:w-[30rem]"
            />
          </div>
        </div>
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

.test {
  background-color: red;
}
</style>
