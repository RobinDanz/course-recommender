<script setup lang="ts">
import PageHeader from '@/components/page/PageHeader.vue'
import RecommenderForm from '@/components/forms/RecommenderForm.vue'
import PageContent from '@/components/page/PageContent.vue'
</script>

<template>
  <div class="px-5 overflow-y-auto height mx-auto height">
    <RecommenderForm></RecommenderForm>
  </div>
</template>

<style scoped>
.height {
  max-height: 90vh;
}
</style>
