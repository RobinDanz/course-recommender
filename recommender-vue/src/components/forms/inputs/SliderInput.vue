<script setup lang="ts">
import Slider from 'primevue/slider'
import { useField } from 'vee-validate'

const props = defineProps({
  name: String,
  initialValue: {
    type: Number
  },
  leftLabel: String,
  rightLabel: String
})

const modelValue = defineModel<number>('modelValue')

const { value, handleChange, errorMessage } = useField(props.name as string, undefined, {
  initialValue: props.initialValue
})
</script>

<template>
  <div class="flex flex-column align-items-center w-full">
    <div class="grid w-full">
      <div class="col-4 flex justify-content-center">{{ leftLabel }}</div>
      <div class="col-4 my-auto">
        <Slider v-model="modelValue" :name="name" @update:model-value="handleChange"></Slider>
      </div>
      <div class="col-4 flex justify-content-center">{{ rightLabel }}</div>
    </div>
  </div>

  {{ errorMessage }}
</template>
