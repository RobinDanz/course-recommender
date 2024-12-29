<script setup lang="ts">
import {
  type Course,
  dayToString,
  formatStartToEnd,
  formatCourseType,
  formatCourseUniversity,
  formatTracks,
  formatCourseSemester
} from '@/models/course'
import { onBeforeMount, ref } from 'vue'
import { getCourse } from '@/services/courseService'
import PageHeader from '@/components/page/PageHeader.vue'
import PageContent from '@/components/page/PageContent.vue'
import Divider from 'primevue/divider'
import Chart from 'primevue/chart'
import CommentCard from '@/components/cards/CommentCard.vue'
import Button from 'primevue/button'
import Dialog from 'primevue/dialog'
import StudentForm from '@/components/forms/StudentForm.vue'
import type { scales, TooltipItem } from 'chart.js'
import * as yup from 'yup'
import { useForm } from 'vee-validate'
import { postComment } from '@/services/commentService'
import TextInput from '@/components/forms/inputs/TextInput.vue'
import ScrollPanel from 'primevue/scrollpanel'
import Panel from 'primevue/panel'
import TextAreaInput from '@/components/forms/inputs/TextAreaInput.vue'
import { options } from 'node_modules/axios/index.cjs'

const props = defineProps({
  courseId: {
    type: String,
    required: true
  }
})

const chartData = ref()
const chartOptions = ref()
const course = ref<Course>()
const feedbackModalVisible = ref(false)

const graphLabelToVariables = {
  Lectures: 'lectures',
  'Subject Type': 'subject_type',
  Interactions: 'interactions',
  'Blackboard Use': 'blackboard',
  Recording: 'recordings',
  'Teacher Accessibility': 'teacher_accessibility'
}

onBeforeMount(async () => {
  refreshData()
})

const setChartData = () => {
  const teacher_data = []
  const student_data = []

  teacher_data.push(course.value?.lectures)
  teacher_data.push(course.value?.subject_type)
  teacher_data.push(course.value?.interactions)
  teacher_data.push(course.value?.blackboard)
  teacher_data.push(course.value?.recordings)
  teacher_data.push(course.value?.teacher_accessibility)

  student_data.push(course.value?.lectures_fb)
  student_data.push(course.value?.subject_type_fb)
  student_data.push(course.value?.interactions_fb)
  student_data.push(course.value?.blackboard_fb)
  student_data.push(course.value?.recordings_fb)
  student_data.push(course.value?.teacher_accessibility_fb)

  return {
    labels: Object.keys(graphLabelToVariables),
    datasets: [
      {
        label: 'teacher',
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderColor: 'rgb(255, 99, 132)',
        pointBackgroundColor: 'rgb(255, 99, 132)',
        pointBorderColor: '#fff',
        pointHoverBackgroundColor: '#fff',
        pointHoverBorderColor: 'rgb(255, 99, 132)',
        data: teacher_data
      },
      {
        label: 'student',
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgb(54, 162, 235)',
        pointBackgroundColor: 'rgb(54, 162, 235)',
        pointBorderColor: '#fff',
        pointHoverBackgroundColor: '#fff',
        pointHoverBorderColor: 'rgb(54, 162, 235)',
        data: student_data
      }
    ]
  }
}

const setChartOptions = () => {
  return {
    plugins: {
      tooltip: {
        callbacks: {
          label: (context: TooltipItem<any>) => {
            let variableName = graphLabelToVariables[context.label]
            if (context.dataset.label === 'student') {
              variableName = variableName + '_fb'
            }
            variableName = variableName + '_tooltip'

            return course.value[variableName]
          }
        }
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

const closeDialog = async () => {
  feedbackModalVisible.value = false
  await refreshData()
}

const refreshData = async () => {
  course.value = await getCourse(parseInt(props.courseId))
  chartData.value = setChartData()
  chartOptions.value = setChartOptions()
}

const username = ref('')
const comment = ref('')
const usernameModalVisible = ref(false)

const schema = yup.object({
  username: yup.string().required(),
  comment: yup.string().required()
})

const { values, errors, handleSubmit, resetForm } = useForm({
  validationSchema: schema
})

const commentFocused = ref(false)

const resetCommentForm = () => {
  commentFocused.value = false
  usernameModalVisible.value = false
  username.value = ''
  comment.value = ''
  resetForm()
}

const onSubmit = handleSubmit(async (values) => {
  const postVal = {
    username: values.username,
    comment: values.comment,
    course: props.courseId
  }
  const result = await postComment(postVal)
  resetCommentForm()
  refreshData()
  usernameModalVisible.value = false
})
</script>

<template>
  <PageHeader :title="course?.title"></PageHeader>
  <PageContent>
    <template #content>
      <div class="grid">
        <div class="col-8 flex flex-column" v-if="course">
          <h3 class="mb-0">Description</h3>
          <ScrollPanel
            class="mx-2"
            style="height: 180px"
            :pt="{
              wrapper: {
                style: { 'border-right': '10px solid var(--surface-ground)' }
              },
              bary: 'hover:bg-primary-400 bg-primary-300 opacity-100'
            }"
          >
            <pre class="description">{{ course.description }}</pre>
          </ScrollPanel>

          <Panel
            toggleable
            :collapsed="true"
            :pt="{
              root: {
                style: {
                  border: 'none'
                }
              },
              header: {
                style: { padding: '0px', color: 'black', 'justify-content': 'start' }
              },
              content: {
                style: {
                  padding: '0px',
                  color: 'black'
                }
              }
            }"
          >
            <template #header>
              <h3 class="mr-2">Details</h3>
            </template>
            <div class="flex flex-column mx-2">
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
                <div class="col-6">{{ formatStartToEnd(course) }}</div>
              </div>
              <div class="grid">
                <div class="col-6">Track</div>
                <div class="col-6">{{ formatTracks(course) }}</div>
              </div>
              <div class="grid">
                <div class="col-6">Semester</div>
                <div class="col-6">{{ formatCourseSemester(course) }}</div>
              </div>
              <div class="grid">
                <div class="col-6">JMCS URL</div>
                <div class="col-6"><a :href="course.url">Visit JMCS website</a></div>
              </div>
            </div>
          </Panel>

          <h3>Comments</h3>
          <div class="flex flex-column">
            <div class="comment-post">
              <form @submit="onSubmit" id="comment-form">
                <TextAreaInput
                  name="comment"
                  v-model="comment"
                  placeholder="Add a comment..."
                  @focused="commentFocused = true"
                ></TextAreaInput>
                <div v-if="commentFocused" class="mt-2">
                  <Button
                    outlined
                    rounded
                    size="small"
                    severity="danger"
                    @click="resetCommentForm()"
                    >Cancel</Button
                  >
                  <Button
                    rounded
                    outlined
                    :disabled="comment == ''"
                    @click="usernameModalVisible = true"
                    size="small"
                    >Post</Button
                  >
                  <Dialog v-model:visible="usernameModalVisible" modal header="Feedback form">
                    <div class="flex flex-column">
                      <p>Input an username before posting your comment:</p>
                      <TextInput
                        name="username"
                        v-model="username"
                        placeholder="Username"
                      ></TextInput>
                      <div>
                        <Button
                          outlined
                          rounded
                          size="small"
                          severity="danger"
                          @click="resetCommentForm()"
                          >Cancel</Button
                        >
                        <Button
                          outlined
                          rounded
                          type="submit"
                          form="comment-form"
                          size="small"
                          :disabled="username == ''"
                          >Post</Button
                        >
                      </div>
                    </div>
                  </Dialog>
                </div>
              </form>
            </div>
            <div v-if="course.comments.length > 0">
              <CommentCard v-for="c in course.comments" :key="c.id" :comment="c"></CommentCard>
            </div>
            <div v-else>
              <p>No comment, be the first to share your thoughts !</p>
            </div>
          </div>
        </div>
        <Divider layout="vertical" />
        <div class="col-3 flex flex-column">
          <h3>Course profile</h3>
          <div class="chart">
            <Chart type="radar" :data="chartData" :options="chartOptions" />
          </div>
          <Button class="m-auto" @click="feedbackModalVisible = true">Give a feedback</Button>
        </div>
      </div>
    </template>
  </PageContent>
  <Dialog
    v-model:visible="feedbackModalVisible"
    modal
    header="Studen Feedback Survey"
    :style="{ width: '55vw' }"
  >
    <StudentForm
      @close-dialog="closeDialog"
      @refresh-course="refreshData"
      :selected_course_id="course?.id"
    ></StudentForm>
  </Dialog>
</template>

<style scoped>
.description {
  white-space: break-spaces;
  font-family: inherit;
}

.height {
  max-height: 80vh;
}
</style>
