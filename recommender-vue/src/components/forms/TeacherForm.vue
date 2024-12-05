<script setup lang="ts">
import MultiSelectInput from '@/components/forms/inputs/MultiSelectInput.vue'
import SliderInput from '@/components/forms/inputs/SliderInput.vue'
import { useForm } from 'vee-validate'
import { ref } from 'vue'
import * as yup from 'yup'
import Button from 'primevue/button'
import { sendTeacherForm } from '@/services/recommenderService'

const props = defineProps({
  selected_course_id: {
    type: Number,
    required: true
  }
})

const evaluation = ref([])
const lectures = ref([])
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

const lectureOptions = [
  { label: 'Only Lectures', option: 0 },
  { label: 'Lectures and some exercises', option: 1 },
  { label: 'Lectures and exercises', option: 2 },
  { label: 'Lectures and project(s)', option: 3 },
  { label: 'Project(s) only', option: 4 }
]

const schema = yup.object({
  evaluation: yup.array().of(yup.number()).min(1, 'at least one').required('at least one'),
  lectures: yup.array().of(yup.number()).min(1, 'at least one').required('at least one'),
  subject_type: yup.number().required(),
  interactions: yup.number().required(),
  blackboard: yup.number().required(),
  recordings: yup.number().required(),
  teacher_accessibility: yup.number().required()
})

const { values, errors, handleSubmit } = useForm({
  validationSchema: schema
})

const onSubmit = handleSubmit(async (values) => {
  const result = await sendTeacherForm(values, props.selected_course_id)
  console.log(result)
})
</script>

<template>
  <p>
    {{ values }}
    {{ errors }}
  </p>
  <div class="width m-auto">
    <form @submit="onSubmit" id="teacher-recommender-form">
      <div class="evaluation-type">
        <h2>How is your course evaluated ?</h2>
        <div class="flex justify-content-center">
          <MultiSelectInput
            v-model="evaluation"
            :options="evaluationOptions"
            name="evaluation"
          ></MultiSelectInput>
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
            name="subject_type"
            :initial-value="50"
            v-model="subject_type"
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
        <h2>Blackboard use</h2>
        <div class="flex justify-content-center">
          <SliderInput
            name="blackboard"
            :initial-value="50"
            v-model="blackboard"
            left-label="None"
            right-label="A lot"
          ></SliderInput>
        </div>
      </div>
      <div class="recordings">
        <h2>Recorded classes</h2>
        <div class="flex justify-content-center">
          <SliderInput
            name="recordings"
            :initial-value="50"
            v-model="recordings"
            left-label="None"
            right-label="A lot"
          ></SliderInput>
        </div>
      </div>
      <div class="teacher_accessibility">
        <h2>Teacher accessibility</h2>
        <div class="flex justify-content-center">
          <SliderInput
            name="teacher_accessibility"
            :initial-value="50"
            v-model="teacher_accessibility"
            left-label="None"
            right-label="A lot"
          ></SliderInput>
        </div>
      </div>

      <Button class="submit-button" type="submit" form="teacher-recommender-form">Send</Button>
    </form>
  </div>
</template>

<style scoped>
.width {
  width: 50vw;
}

.submit-button {
  position: fixed;
  bottom: 50px;
  right: 50px;
}
</style>
