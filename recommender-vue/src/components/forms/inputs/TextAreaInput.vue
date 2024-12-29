<script setup lang="ts">
import Textarea from 'primevue/textarea'
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

const emit = defineEmits(['focused'])
</script>

<template>
  <Textarea
    @focus="emit('focused')"
    autoResize
    :name="name"
    @update:model-value="handleChange"
    :placeholder="placeholder"
    v-model="modelValue"
    rows="1"
    style="width: 100%"
  ></Textarea>
  {{ errorMessage }}
</template>
