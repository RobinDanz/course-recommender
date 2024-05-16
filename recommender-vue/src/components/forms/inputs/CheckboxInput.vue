<script setup lang="ts">
import Checkbox from 'primevue/checkbox'
import { useField } from 'vee-validate'

const props = defineProps({
  name: String,
  value: {
    type: String
  },
  label: String
})

const modelValue = defineModel('modelValue')

const { checked, handleChange, errorMessage } = useField(props.name as string, undefined, {
  type: 'checkbox',
  checkedValue: props.value
})
</script>

<template>
  <div class="flex flex-column align-items-center">
    <div class="flex">
      <label :for="name">{{ label }}</label>
    </div>
    <div class="flex">
      <Checkbox
        :name="name"
        v-model="modelValue"
        :value="value"
        @update:model-value="handleChange"
      ></Checkbox>
    </div>

    {{ errorMessage }}
  </div>
</template>
