<script setup lang="ts">
import InputText from 'primevue/inputtext'
import { useField } from 'vee-validate'

const props = defineProps({
  name: String,
  initialValue: String,
  placeholder: String
})

const modelValue = defineModel<string>('modelValue')

const { value, handleChange, errorMessage } = useField(props.name as string, undefined, {
  initialValue: props.initialValue
})
</script>

<template>
  <InputText
    :id="name"
    :name="name"
    @update:model-value="handleChange"
    v-model="modelValue"
    :placeholder="placeholder"
  />

  {{ errorMessage }}
</template>
