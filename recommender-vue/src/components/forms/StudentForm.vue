<script setup lang="ts">
import SliderInput from '@/components/forms/inputs/SliderInput.vue'
import { useForm } from 'vee-validate'
import { ref } from 'vue'
import * as yup from 'yup'
import Button from 'primevue/button'
import { sendStudentFeedback } from '@/services/recommenderService'

const props = defineProps({
  selected_course_id: {
    type: Number,
    required: true
  }
})

const emit = defineEmits(['closeDialog', 'refreshCourse'])

const lectures = ref(50)
const subject_type = ref(50)
const interactions = ref(50)
const blackboard = ref(50)
const recordings = ref(50)
const teacher_accessibility = ref(50)

const schema = yup.object({
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

const onSubmit = handleSubmit((values) => {
  emit('closeDialog')
  const result = sendStudentFeedback(values, props.selected_course_id).then(() => {
    console.log('coucou')
    emit('refreshCourse')
  })
})
</script>

<template>
  <div class="width m-auto">
    <form class="flex flex-column" @submit="onSubmit" id="teacher-recommender-form">
      <div class="lectures">
        <h3>Lectures</h3>
        <div class="survey-section-label">
          <p>Was the course mainly focused on lectures or on project(s) ?</p>
        </div>
        <div class="flex justify-content-center">
          <SliderInput
            name="lectures"
            :initial-value="50"
            v-model="lectures"
            left-label="Lecture Only"
            right-label="Project(s) Only"
          ></SliderInput>
        </div>
      </div>
      <div class="subject-type">
        <h3>Type of subject</h3>
        <div class="survey-section-label">
          <p>Was the course mainly theoretical or mainly practical ?</p>
        </div>
        <div class="flex justify-content-center">
          <SliderInput
            name="subject_type"
            :initial-value="50"
            v-model="subject_type"
            left-label="Theoritical"
            right-label="Practical"
          ></SliderInput>
        </div>
      </div>
      <div class="interactions">
        <h3>Teacher/Students interactions</h3>
        <div class="survey-section-label">
          <p>Was there a lot of interaction between students and the teacher ?</p>
        </div>
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
        <h3>Blackboard use</h3>
        <div class="survey-section-label">
          <p>How often was the blackboard used ?</p>
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
      <div class="recordings">
        <h3>Recorded classes</h3>
        <div class="survey-section-label">
          <p>How often were the lessons recorded ?</p>
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
      <div class="teacher_accessibility">
        <h3>Teacher accessibility</h3>
        <div class="survey-section-label">
          <p>How accessible was the teacher ?</p>
        </div>
        <div class="flex justify-content-center">
          <SliderInput
            name="teacher_accessibility"
            :initial-value="50"
            v-model="teacher_accessibility"
            left-label="Not easily accessible"
            right-label="Easily accessible"
          ></SliderInput>
        </div>
      </div>
      <div class="mt-3 mr-3 flex justify-content-end">
        <Button type="submit" form="teacher-recommender-form">Send</Button>
      </div>
    </form>
  </div>
</template>

<style scoped>
.width {
  width: 50vw;
}
</style>
