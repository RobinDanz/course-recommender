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
const course_type = ref([])
const track = ref([])
const lectures = ref(50)

const subject_type = ref(50)
const interactions = ref(50)
const blackboard = ref(50)
const recording = ref(50)
const teacher_accessibility = ref(50)

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

const schema = yup.object({
  university: yup.array().of(yup.number()).min(1, 'at least one').required('at least one'),
  evaluation: yup.array().of(yup.number()).min(1, 'at least one').required('at least one'),
  course_type: yup.array().of(yup.number()).min(1, 'at least one').required('at least one'),
  track: yup.array().of(yup.number()).min(1, 'at least one').required('at least one'),
  lectures: yup.number().required(),
  subject_type: yup.number().required(),
  interactions: yup.number().required(),
  blackboard: yup.number().required(),
  recordings: yup.number().required(),
  teacher_accessibility: yup.number().required()
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
    for (const key in result) {
      const course = await getCourse(parseInt(key))
      courses.push(course)
    }
    resultCourse.value = mapResult(courses, result)
  }
})

const refillForm = () => {
  resultCourse.value = []
  resultRecieved.value = false
}
</script>

<template>
  <div class="width m-auto form-container">
    <form @submit="onSubmit" v-show="!resultRecieved" id="recommender">
      <div class="survey-section-header mt-3">
        <div class="survey-section-title">
          <h2>Recommender Form</h2>
        </div>
        <div class="survey-section-label">
          <p>
            By answering the following questions, the three courses that corresponds the most to
            your responses will be recommended
          </p>
        </div>
      </div>
      <div class="university survey-section">
        <h2>Favorite University</h2>
        <div class="survey-section-label">
          <p>What are your favorite universities ?</p>
        </div>
        <div class="flex justify-content-center">
          <MultiSelectInput
            v-model="university"
            :options="universityOptions"
            name="university"
          ></MultiSelectInput>
        </div>
      </div>
      <div class="evaluation-type survey-section">
        <h2>Type of evaluation</h2>
        <div class="survey-section-label">
          <p>What is the the evaluation method that you prefer ?</p>
        </div>
        <div class="flex justify-content-center">
          <MultiSelectInput
            v-model="evaluation"
            :options="evaluationOptions"
            name="evaluation"
          ></MultiSelectInput>
        </div>
      </div>
      <div class="lecture-type survey-section">
        <h2>Type of lecture</h2>
        <div class="survey-section-label">
          <p>Are you looking for a course or for a seminar ?</p>
        </div>
        <div class="flex justify-content-center">
          <MultiSelectInput
            v-model="course_type"
            :options="courseTypeOptions"
            name="course_type"
          ></MultiSelectInput>
        </div>
      </div>
      <div class="track survey-section">
        <h2>Track</h2>
        <div class="survey-section-label">
          <p>Are you looking for a course in a specific track ?</p>
        </div>
        <div class="flex justify-content-center">
          <MultiSelectInput v-model="track" :options="trackOptions" name="track"></MultiSelectInput>
        </div>
      </div>
      <div class="lectures survey-section">
        <h2>Lectures</h2>
        <div class="survey-section-label">
          <p>Do you prefer listening to lecture or working on various projects ?</p>
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
        <h2>Type of subject</h2>
        <div class="survey-section-label">
          <p>Do you prefer a theoritical lesson or a more practical one ?</p>
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
        <h2>Teacher/Students interactions</h2>
        <div class="survey-section-label">
          <p>How important is it for you to have interactions with the teacher ?</p>
        </div>
        <div class="flex justify-content-center">
          <SliderInput
            name="interactions"
            :initial-value="50"
            v-model="interactions"
            left-label="Not important "
            right-label="Very important"
          ></SliderInput>
        </div>
      </div>
      <div class="blackboard survey-section">
        <h2>Blackboard use</h2>
        <div class="survey-section-label">
          <p>How often should the blackboard be used ?</p>
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
      <div class="survey-section">
        <h2>Teacher accessibility</h2>
        <div class="survey-section-label">
          <p>How important is teacher accessibility for you ?</p>
        </div>
        <div class="flex justify-content-center">
          <SliderInput
            name="teacher_accessibility"
            :initial-value="50"
            v-model="teacher_accessibility"
            left-label="Not important"
            right-label="Very important"
          ></SliderInput>
        </div>
      </div>
      <div class="recording survey-section">
        <h2>Recorded lectures</h2>
        <div class="survey-section-label">
          <p>How often should the course be recorded ?</p>
        </div>
        <div class="flex justify-content-center">
          <SliderInput
            name="recordings"
            :initial-value="50"
            v-model="recording"
            left-label="Never"
            right-label="Always"
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

.test {
  position: fixed;
  bottom: 50px;
  right: 50px;
}
</style>
