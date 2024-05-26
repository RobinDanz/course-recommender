<script setup lang="ts">
import PageHeader from '@/components/page/PageHeader.vue'
import RecommenderForm from '@/components/forms/RecommenderForm.vue'
import PageContent from '@/components/page/PageContent.vue'
</script>

<template>
  <PageHeader title="Recommender"></PageHeader>
  <PageContent>
    <template #content>
      <RecommenderForm></RecommenderForm>
    </template>
  </PageContent>
</template>
