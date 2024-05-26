<script setup lang="ts">
import MultiSelect from 'primevue/multiselect'
import { useField } from 'vee-validate'

interface MultiSelectOptions {
  label: string
  option: string | number
}

const props = defineProps<{
  name: string
  options: Array<MultiSelectOptions>
}>()

const modelValue = defineModel<number[]>('modelValue')

const { handleChange, errorMessage } = useField(props.name as string, undefined, {})
</script>

<template>
  <MultiSelect
    v-model="modelValue"
    :options="options"
    optionLabel="label"
    optionValue="option"
    placeholder="Select at least one option"
    :invalid="errorMessage != undefined"
    :showToggleAll="false"
    @update:modelValue="handleChange"
  />
</template>
