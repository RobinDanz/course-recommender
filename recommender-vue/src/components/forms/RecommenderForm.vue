<script setup lang="ts">
import { useForm } from 'vee-validate'
import CheckboxInput from '@/components/forms/inputs/CheckboxInput.vue'
import { ref } from 'vue'
import * as yup from 'yup'
import SliderInput from '@/components/forms/inputs/SliderInput.vue'
import { sendRecommender } from '@/services/recommenderService'

const evaluation = ref([])
const university = ref([])
const courseType = ref([])
const track = ref([])
const mainSubject = ref([])
const lectures = ref([])

const subjectType = ref(50)
const interactions = ref(50)
const blackboard = ref(50)
const recording = ref(50)
const accessibility = ref(50)

const schema = yup.object({
  university: yup.array().of(yup.number()).min(1, 'at least one').required(),
  evaluation: yup.array().of(yup.number()).min(1, 'at least one').required(),
  courseType: yup.array().of(yup.number()).min(1, 'at least one').required(),
  track: yup.array().of(yup.number()).min(1, 'at least one').required(),
  lectures: yup.array().of(yup.number()).min(1, 'at least one').required(),
  subjectType: yup.number().required(),
  mainSubject: yup.array().of(yup.number()).min(1, 'at least one').required(),
  interactions: yup.number().required(),
  blackboard: yup.number().required(),
  recordings: yup.number().required(),
  teacherAccessibilty: yup.number().required()
})

const { values, errors, handleSubmit } = useForm({
  validationSchema: schema
})

const onSubmit = handleSubmit(async (values) => {
  console.log(values)
  await sendRecommender(values)
})
</script>

<template>
  <div class="w-8">
    {{ values }}
    {{ errors }}
    <form class="m-8" @submit="onSubmit">
      <div class="university">
        <h2>Favorite University</h2>
        <div class="flex xl:flex-row justify-content-between">
          <CheckboxInput
            name="university"
            :value="0"
            label="Bern"
            v-model="university"
          ></CheckboxInput>
          <CheckboxInput
            name="university"
            :value="1"
            label="Fribourg"
            v-model="university"
          ></CheckboxInput>
          <CheckboxInput
            name="university"
            :value="2"
            label="Neuchatel"
            v-model="university"
          ></CheckboxInput>
        </div>
      </div>
      <div class="evaluation-type">
        <h2>Type of evaluation</h2>
        <div class="flex flex-row justify-content-between">
          <CheckboxInput
            name="evaluation"
            :value="0"
            label="Semester Project"
            v-model="evaluation"
          ></CheckboxInput>
          <CheckboxInput
            name="evaluation"
            :value="1"
            label="Continuous"
            v-model="evaluation"
          ></CheckboxInput>
          <CheckboxInput
            name="evaluation"
            :value="2"
            label="Oral exam"
            v-model="evaluation"
          ></CheckboxInput>
          <CheckboxInput
            name="evaluation"
            :value="3"
            label="Written exam"
            v-model="evaluation"
          ></CheckboxInput>
        </div>
      </div>
      <div class="lecture-type">
        <h2>Type of lecture</h2>
        <div class="flex flex-row justify-content-between">
          <CheckboxInput
            name="courseType"
            :value="0"
            label="Course"
            v-model="courseType"
          ></CheckboxInput>
          <CheckboxInput
            name="courseType"
            :value="1"
            label="Seminar"
            v-model="courseType"
          ></CheckboxInput>
        </div>
      </div>
      <div class="track">
        <h2>Track</h2>
        <div class="flex flex-row justify-content-between">
          <CheckboxInput name="track" :value="0" label="General" v-model="track"></CheckboxInput>
          <CheckboxInput
            name="track"
            :value="1"
            label="Distributed Software Systems"
            v-model="track"
          ></CheckboxInput>
          <CheckboxInput name="track" :value="2" label="Security" v-model="track"></CheckboxInput>
          <CheckboxInput
            name="track"
            :value="3"
            label="Visual Computing"
            v-model="track"
          ></CheckboxInput>
          <CheckboxInput
            name="track"
            :value="4"
            label="Theory and Logic"
            v-model="track"
          ></CheckboxInput>
          <CheckboxInput
            name="track"
            :value="5"
            label="Information Systems and Decision Support"
            v-model="track"
          ></CheckboxInput>
          <CheckboxInput
            name="track"
            :value="6"
            label="Data Science"
            v-model="track"
          ></CheckboxInput>
        </div>
      </div>
      <div class="lectures">
        <h2>Lectures</h2>
        <div class="flex flex-row justify-content-between">
          <CheckboxInput
            name="lectures"
            :value="0"
            label="Only Lectures"
            v-model="lectures"
          ></CheckboxInput>
          <CheckboxInput
            name="lectures"
            :value="1"
            label="Lectures and some exercises"
            v-model="lectures"
          ></CheckboxInput>
          <CheckboxInput
            name="lectures"
            :value="2"
            label="Lectures and exercises"
            v-model="lectures"
          ></CheckboxInput>
          <CheckboxInput
            name="lectures"
            :value="3"
            label="Lectures and project(s)"
            v-model="lectures"
          ></CheckboxInput>
          <CheckboxInput
            name="lectures"
            :value="4"
            label="Project(s) only"
            v-model="lectures"
          ></CheckboxInput>
        </div>
      </div>
      <div class="main-subject">
        <h2>Main subject</h2>
        <div class="flex flex-row justify-content-between">
          <CheckboxInput
            name="mainSubject"
            :value="0"
            label="Computer Science"
            v-model="mainSubject"
          ></CheckboxInput>
          <CheckboxInput
            name="mainSubject"
            :value="1"
            label="Logic"
            v-model="mainSubject"
          ></CheckboxInput>
          <CheckboxInput
            name="mainSubject"
            :value="2"
            label="Math"
            v-model="mainSubject"
          ></CheckboxInput>
        </div>
      </div>
      <div class="subject-type">
        <h2>Type of subject</h2>
        <div class="flex flex-row justify-content-center">
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
        <div class="flex flex-row justify-content-center">
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
        <div class="flex flex-row justify-content-center">
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
        <div class="flex flex-row justify-content-center">
          <SliderInput
            name="recordings"
            :initial-value="50"
            v-model="recording"
            left-label="Never recorded"
            right-label="Always recorded"
          ></SliderInput>
        </div>
      </div>
      <button type="submit">Send</button>
    </form>
  </div>
</template>
