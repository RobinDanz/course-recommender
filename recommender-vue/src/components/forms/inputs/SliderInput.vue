<script setup lang="ts">
import Slider from 'primevue/slider'
import { useField } from 'vee-validate'

const props = defineProps({
  name: String,
  initialValue: {
    type: Number
  },
  label: String
})

const modelValue = defineModel<number>('modelValue')

const { value, handleChange, errorMessage } = useField(props.name as string, undefined, {
  initialValue: props.initialValue
})
</script>

<template>
  <div class="flex flex-column align-items-center w-5">
    <div class="flex">
      {{ value }}
      <label :for="name">{{ label }}</label>
    </div>
    <div class="w-5">
      <Slider v-model="modelValue" :name="name" @update:model-value="handleChange"></Slider>
    </div>

    {{ errorMessage }}
  </div>
</template>
