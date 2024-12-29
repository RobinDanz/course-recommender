<script setup lang="ts">
import MultiSelectInput from '@/components/forms/inputs/MultiSelectInput.vue'
import SliderInput from '@/components/forms/inputs/SliderInput.vue'
import { useForm } from 'vee-validate'
import { onBeforeMount, ref } from 'vue'
import * as yup from 'yup'
import Button from 'primevue/button'
import { sendTeacherForm } from '@/services/recommenderService'
import type { Course } from '@/models/course'
import { getCourseList } from '@/services/courseService'
import Dropdown from 'primevue/dropdown'
import { useToast } from 'primevue/usetoast'
import Toast from 'primevue/toast'

const toast = useToast()

const courses = ref<Array<Course>>()

const selectedCourse = ref<number>()
const coursesOptions = ref<Array<any>>([])

onBeforeMount(async () => {
  refreshCourseList()
})

const refreshCourseList = async () => {
  courses.value = await getCourseList()
  filterCourseList()
}

const filterCourseList = () => {
  courses.value?.forEach((value) => {
    if (!value.teacher_form_filled) {
      coursesOptions.value.push({
        label: value.title,
        option: value.id
      })
    }
  })
}

const evaluation = ref([])
const lectures = ref(50)
const subject_type = ref(50)
const interactions = ref(50)
const blackboard = ref(50)
const recordings = ref(50)
const teacher_accessibility = ref(50)

const evaluationOptions = [
  { label: 'Semester Project', option: 0 },
  { label: 'Continuous', option: 1 },
  { label: 'Oral exam', option: 2 },
  { label: 'Written exam', option: 3 }
]

const schema = yup.object({
  evaluation: yup.array().of(yup.number()).min(1, 'at least one').required('at least one'),
  lectures: yup.number().required(),
  subject_type: yup.number().required(),
  interactions: yup.number().required(),
  blackboard: yup.number().required(),
  recordings: yup.number().required(),
  teacher_accessibility: yup.number().required()
})

const { values, errors, handleSubmit, resetForm } = useForm({
  validationSchema: schema
})

const onSubmit = handleSubmit(async (values) => {
  const result = await sendTeacherForm(values, selectedCourse.value)
  coursesOptions.value = coursesOptions.value.filter((val) => val.option != selectedCourse.value)
  resetForm()
  selectedCourse.value = undefined

  evaluation.value = []
  lectures.value = 50
  subject_type.value = 50
  interactions.value = 50
  blackboard.value = 50
  recordings.value = 50
  teacher_accessibility.value = 50
  showToast()
})

const showToast = () => {
  toast.add({
    severity: 'success',
    summary: 'Success',
    detail: 'Thank you for your time !',
    life: 3000
  })
}
</script>

<template>
  {{ selectedCourse }}
  <Toast></Toast>
  <div class="width m-auto">
    <form @submit="onSubmit" id="teacher-recommender-form">
      <div class="survey-section-header mt-3">
        <div class="survey-section-title">
          <h2>Teacher Form</h2>
        </div>
        <div class="survey-section-label">
          <p>
            Take five minutes of your time to answer the following questions to add your course to
            the recommender system !
          </p>
          <p>Start by selecting the course in the following dropdown list</p>
        </div>
        <div class="flex justify-content-center">
          <Dropdown
            v-model="selectedCourse"
            :options="coursesOptions"
            name="courses"
            optionLabel="label"
            optionValue="option"
            filter
            placeholder="Select a course"
          ></Dropdown>
        </div>
      </div>
      <div class="evaluation-type survey-section">
        <div class="survey-section-title">
          <h2>Evaluation method</h2>
        </div>
        <div class="survey-section-label">
          <p>What is the final evaluation method for this course ?</p>
        </div>
        <div class="flex justify-content-center">
          <MultiSelectInput
            v-model="evaluation"
            :options="evaluationOptions"
            name="evaluation"
          ></MultiSelectInput>
        </div>
      </div>
      <div class="lectures survey-section">
        <div class="survey-section-title">
          <h2>Lectures type</h2>
        </div>
        <div class="survey-section-label">
          <p>Is this class mainly focused around traditional lectures or working on project(s) ?</p>
        </div>
        <div class="flex justify-content-center">
          <SliderInput
            name="lectures"
            :initial-value="50"
            v-model="lectures"
            left-label="Only Lectures"
            right-label="Only Project(s)"
          ></SliderInput>
        </div>
      </div>
      <div class="subject-type survey-section">
        <div class="survey-section-title">
          <h2>Type of subject</h2>
        </div>
        <div class="survey-section-label">
          <p>Is the subject of this class mainly theoretical or practical ?</p>
        </div>
        <div class="flex justify-content-center">
          <SliderInput
            name="subject_type"
            :initial-value="50"
            v-model="subject_type"
            left-label="Theoretical"
            right-label="Practical"
          ></SliderInput>
        </div>
      </div>
      <div class="interactions survey-section">
        <div class="survey-section-title">
          <h2>Teacher/Students interactions</h2>
        </div>
        <div class="survey-section-label">
          <p>How often are you interracting with the students ?</p>
        </div>
        <div class="flex justify-content-center">
          <SliderInput
            name="interactions"
            :initial-value="50"
            v-model="interactions"
            left-label="Never"
            right-label="Always"
          ></SliderInput>
        </div>
      </div>
      <div class="blackboard survey-section">
        <div class="survey-section-title">
          <h2>Blackboard use</h2>
        </div>
        <div class="survey-section-label">
          <p>How often are you using the blackboard during the lessons ?</p>
        </div>
        <div class="flex justify-content-center">
          <SliderInput
            name="blackboard"
            :initial-value="50"
            v-model="blackboard"
            left-label="Never"
            right-label="Always"
          ></SliderInput>
        </div>
      </div>
      <div class="recordings survey-section">
        <div class="survey-section-title">
          <h2>Recorded classes</h2>
        </div>
        <div class="survey-section-label">
          <p>How often is this class recorded ?</p>
        </div>
        <div class="flex justify-content-center">
          <SliderInput
            name="recordings"
            :initial-value="50"
            v-model="recordings"
            left-label="Never"
            right-label="Always"
          ></SliderInput>
        </div>
      </div>
      <div class="teacher_accessibility survey-section">
        <div class="survey-section-title">
          <h2>Teacher accessibility</h2>
        </div>
        <div class="survey-section-label">
          <p>Are you easily accessible if students need your help or advices ?</p>
        </div>
        <div class="flex justify-content-center">
          <SliderInput
            name="teacher_accessibility"
            :initial-value="50"
            v-model="teacher_accessibility"
            left-label="Not easily"
            right-label="Easily"
          ></SliderInput>
        </div>
      </div>

      <Button
        :disabled="selectedCourse == undefined"
        class="submit-button"
        type="submit"
        form="teacher-recommender-form"
        >Send</Button
      >
    </form>
  </div>
</template>

<style scoped>
.width {
  width: 50vw;
}

.survey-section {
  border-left: solid var(--primary-color) 10px;
  border-radius: 10px;
  margin-bottom: 25px;
  padding: 10px;
  box-shadow: 3px 3px 5px 5px rgba(0, 0, 0, 0.2);
}

.survey-section:hover {
  border-left: solid var(--primary-color) 15px;
  box-shadow: 5px 5px 5px 5px rgba(0, 0, 0, 0.3);
}

.survey-section-header {
  border-top: solid var(--primary-color) 5px;
  border-radius: 10px;
  margin-bottom: 25px;
  padding: 10px;
  box-shadow: 3px 3px 5px 5px rgba(0, 0, 0, 0.3);
}

.submit-button {
  position: fixed;
  bottom: 50px;
  right: 50px;
}
</style>
