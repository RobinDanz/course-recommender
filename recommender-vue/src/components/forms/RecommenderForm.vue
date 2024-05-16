<script setup lang="ts">
import { useForm } from 'vee-validate'
import CheckboxInput from '@/components/forms/inputs/CheckboxInput.vue'
import { ref } from 'vue'
import * as yup from 'yup'
import SliderInput from '@/components/forms/inputs/SliderInput.vue'

const evaluationType = ref([])
const university = ref([])
const lectureType = ref([])
const subjectOfInterest = ref([])

const subjectType = ref(50)
const studentInteractions = ref(50)
const blackBoardUse = ref(50)
const exampleUse = ref(50)
const TAImplication = ref(50)

const lectureRecorded = ref(false)

const schema = yup.object({
  evalType: yup.array().of(yup.string()).min(1, 'at least one').required(),
  university: yup.array().of(yup.string()).min(1, 'at least one').required(),
  lectureType: yup.array().of(yup.string()).min(1, 'at least one').required(),
  subjectOfInterest: yup.array().of(yup.string()).min(1, 'at least one').required(),
  subjectType: yup.number().required()
})

const { values, errors, handleSubmit } = useForm({
  validationSchema: schema
})

const onSubmit = handleSubmit((values) => {
  alert(JSON.stringify(values))
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
            value="BE"
            label="Bern"
            v-model="university"
          ></CheckboxInput>
          <CheckboxInput
            name="university"
            value="FR"
            label="Fribourg"
            v-model="university"
          ></CheckboxInput>
          <CheckboxInput
            name="university"
            value="NE"
            label="Neuchatel"
            v-model="university"
          ></CheckboxInput>
        </div>
      </div>
      <div class="evaluation-type">
        <h2>Type of evaluation</h2>
        <div class="flex flex-row justify-content-between">
          <CheckboxInput
            name="evalType"
            value="A"
            label="Semester Project"
            v-model="evaluationType"
          ></CheckboxInput>
          <CheckboxInput
            name="evalType"
            value="B"
            label="Evaluated Series"
            v-model="evaluationType"
          ></CheckboxInput>
          <CheckboxInput
            name="evalType"
            value="C"
            label="Non-Evaluated Series"
            v-model="evaluationType"
          ></CheckboxInput>
          <CheckboxInput
            name="evalType"
            value="D"
            label="Written exam"
            v-model="evaluationType"
          ></CheckboxInput>
          <CheckboxInput
            name="evalType"
            value="E"
            label="Oral exam"
            v-model="evaluationType"
          ></CheckboxInput>
        </div>
      </div>
      <div class="lecture-type">
        <h2>Type of lecture</h2>
        <div class="flex flex-row justify-content-between">
          <CheckboxInput
            name="lectureType"
            value="A"
            label="Course"
            v-model="lectureType"
          ></CheckboxInput>
          <CheckboxInput
            name="lectureType"
            value="B"
            label="Seminar"
            v-model="lectureType"
          ></CheckboxInput>
        </div>
      </div>
      <div class="interest">
        <h2>Subject of interest</h2>
        <div class="flex flex-row justify-content-between">
          <CheckboxInput
            name="subjectOfInterest"
            value="A"
            label="Computer Science"
            v-model="subjectOfInterest"
          ></CheckboxInput>
          <CheckboxInput
            name="subjectOfInterest"
            value="B"
            label="Logic"
            v-model="subjectOfInterest"
          ></CheckboxInput>
          <CheckboxInput
            name="subjectOfInterest"
            value="C"
            label="Math"
            v-model="subjectOfInterest"
          ></CheckboxInput>
        </div>
      </div>
      <div>
        <h2>Type of subject</h2>
        <div class="flex flex-row justify-content-center">
          <SliderInput
            name="subjectType"
            :initial-value="50"
            v-model="subjectType"
            label="coucou"
          ></SliderInput>
        </div>
      </div>
      <div>
        <h2>Teacher/Students interactions</h2>
        <div class="flex flex-row justify-content-center"></div>
      </div>
      <div>
        <h2>Black board uses</h2>
        <div class="flex flex-row justify-content-center"></div>
      </div>
      <div>
        <h2>Example use</h2>
        <div class="flex flex-row justify-content-center"></div>
      </div>
      <div>
        <h2>Teaching assistant implication</h2>
        <div class="flex flex-row justify-content-center"></div>
      </div>
      <div>
        <h2>Recorded lectures</h2>
        <div class="flex flex-row justify-content-center"></div>
      </div>
      <button type="submit">Send</button>
    </form>
  </div>
</template>
