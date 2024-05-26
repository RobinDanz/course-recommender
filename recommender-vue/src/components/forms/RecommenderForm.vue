<script setup lang="ts">
import { useForm } from 'vee-validate'
import { ref } from 'vue'
import * as yup from 'yup'
import SliderInput from '@/components/forms/inputs/SliderInput.vue'
import { sendRecommender } from '@/services/recommenderService'
import MultiSelectInput from '@/components/forms/inputs/MultiSelectInput.vue'
import Button from 'primevue/button'
import { getCourse } from '@/services/courseService'
import type { Course } from '@/models/course'
import HomeNavCard from '../cards/HomeNavCard.vue'

const evaluation = ref([])
const university = ref([])
const courseType = ref([])
const track = ref([])
const lectures = ref([])

const subjectType = ref(50)
const interactions = ref(50)
const blackboard = ref(50)
const recording = ref(50)
const accessibility = ref(50)

const universityOptions = [
  { label: 'Bern', option: 0 },
  { label: 'Fribourg', option: 1 },
  { label: 'Neuchâtel', option: 2 }
]

const evaluationOptions = [
  { label: 'Semester Project', option: 0 },
  { label: 'Continuous', option: 1 },
  { label: 'Oral exam', option: 2 },
  { label: 'Written exam', option: 3 }
]

const courseTypeOptions = [
  { label: 'Course', option: 0 },
  { label: 'Seminar', option: 1 }
]

const trackOptions = [
  { label: 'General', option: 0 },
  { label: 'Distributed Software Systems', option: 1 },
  { label: 'Security', option: 2 },
  { label: 'Visual Computing', option: 3 },
  { label: 'Theory and Logic', option: 4 },
  { label: 'Information Systems and Decision Support', option: 5 },
  { label: 'Data Science', option: 6 }
]

const lectureOptions = [
  { label: 'Only Lectures', option: 0 },
  { label: 'Lectures and some exercises', option: 1 },
  { label: 'Lectures and exercises', option: 2 },
  { label: 'Lectures and project(s)', option: 3 },
  { label: 'Project(s) only', option: 4 }
]

const schema = yup.object({
  university: yup.array().of(yup.number()).min(1, 'at least one').required('at least one'),
  evaluation: yup.array().of(yup.number()).min(1, 'at least one').required('at least one'),
  courseType: yup.array().of(yup.number()).min(1, 'at least one').required('at least one'),
  track: yup.array().of(yup.number()).min(1, 'at least one').required('at least one'),
  lectures: yup.array().of(yup.number()).min(1, 'at least one').required('at least one'),
  subjectType: yup.number().required(),
  interactions: yup.number().required(),
  blackboard: yup.number().required(),
  recordings: yup.number().required(),
  teacherAccessibilty: yup.number().required()
})

const { values, errors, handleSubmit } = useForm({
  validationSchema: schema
})

const resultRecieved = ref(false)
const resultCourse = ref<RecommendationCourse[]>([])

interface RecommendationCourse {
  id: number
  title: string
  recommendation: number
}

const mapResult = (courses: Course[], result: Record<number, number>) => {
  const resultObj = courses.map((c) => {
    return {
      id: c.id,
      title: c.title,
      recommendation: Math.ceil(result[c.id])
    }
  })
  return resultObj.sort((a, b) => b.recommendation - a.recommendation).slice(0, 3)
}

const onSubmit = handleSubmit(async (values) => {
  const result = await sendRecommender(values)

  if (result) {
    resultRecieved.value = true
    const courses = []
    for (const key in result['result']) {
      const course = await getCourse(parseInt(key))
      courses.push(course)
    }
    resultCourse.value = mapResult(courses, result['result'])
  }
})

const refillForm = () => {
  resultCourse.value = []
  resultRecieved.value = false
}
</script>

<template>
  <div class="width m-auto">
    <form @submit="onSubmit" v-show="!resultRecieved" id="recommender">
      <div class="university">
        <h2>Favorite University</h2>
        <div class="flex justify-content-center">
          <MultiSelectInput
            v-model="university"
            :options="universityOptions"
            name="university"
          ></MultiSelectInput>
        </div>
      </div>
      <div class="evaluation-type">
        <h2>Type of evaluation</h2>
        <div class="flex justify-content-center">
          <MultiSelectInput
            v-model="evaluation"
            :options="evaluationOptions"
            name="evaluation"
          ></MultiSelectInput>
        </div>
      </div>
      <div class="lecture-type">
        <h2>Type of lecture</h2>
        <div class="flex justify-content-center">
          <MultiSelectInput
            v-model="courseType"
            :options="courseTypeOptions"
            name="courseType"
          ></MultiSelectInput>
        </div>
      </div>
      <div class="track">
        <h2>Track</h2>
        <div class="flex justify-content-center">
          <MultiSelectInput v-model="track" :options="trackOptions" name="track"></MultiSelectInput>
        </div>
      </div>
      <div class="lectures">
        <h2>Lectures</h2>
        <div class="flex justify-content-center">
          <MultiSelectInput
            v-model="lectures"
            :options="lectureOptions"
            name="lectures"
          ></MultiSelectInput>
        </div>
      </div>
      <div class="subject-type">
        <h2>Type of subject</h2>
        <div class="flex justify-content-center">
          <SliderInput
            name="subjectType"
            :initial-value="50"
            v-model="subjectType"
            left-label="theoritical"
            right-label="practical"
          ></SliderInput>
        </div>
      </div>
      <div class="interactions">
        <h2>Teacher/Students interactions</h2>
        <div class="flex justify-content-center">
          <SliderInput
            name="interactions"
            :initial-value="50"
            v-model="interactions"
            left-label="None"
            right-label="A lot"
          ></SliderInput>
        </div>
      </div>
      <div class="blackboard">
        <h2>Black board uses</h2>
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
      <div class="">
        <h2>Teacher accessibility</h2>
        <div class="flex justify-content-center">
          <SliderInput
            name="teacherAccessibilty"
            :initial-value="50"
            v-model="accessibility"
            left-label="Not accessible"
            right-label="Always accessible"
          ></SliderInput>
        </div>
      </div>
      <div class="recording">
        <h2>Recorded lectures</h2>
        <div class="flex justify-content-center">
          <SliderInput
            name="recordings"
            :initial-value="50"
            v-model="recording"
            left-label="Never recorded"
            right-label="Always recorded"
          ></SliderInput>
        </div>
      </div>
      <Button class="test" type="submit" form="recommender">Send</Button>
    </form>
    <div v-show="resultRecieved">
      <h2>Here are the top three course recommended to you depending on your answers !</h2>
      <div v-for="course in resultCourse" :key="course.id">
        <HomeNavCard
          :title="course.title"
          :subtitle="'Recommended at: ' + course.recommendation + '%'"
          :local-redirect="{ name: 'course-details', params: { courseId: course.id } }"
        ></HomeNavCard>
      </div>

      <Button @click="refillForm">Go back to the form</Button>
    </div>
  </div>
</template>

<style scoped>
.width {
  width: 50vw;
}

.test {
  position: fixed;
  bottom: 50px;
  right: 50px;
}
</style>
