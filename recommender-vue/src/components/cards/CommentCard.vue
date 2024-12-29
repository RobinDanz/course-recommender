<script setup lang="ts">
import type { Comment } from '@/models/comments'

const props = defineProps<{
  comment: Comment
}>()
</script>

<template>
  <div class="flex flex-column my-3 pl-2 test">
    <div>By {{ props.comment.username }}</div>
    <p>
      {{ props.comment.comment }}
    </p>
  </div>
</template>

<style scoped>
.test {
  border-left: solid 2px;
}
</style>
