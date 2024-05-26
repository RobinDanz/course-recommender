<script setup lang="ts">
import HomeNavCard from '@/components/cards/HomeNavCard.vue'
</script>

<template>
  <div class="flex flex-column justify-content-center">
    <div class="flex flex-column my-6">
      <div class="text-7xl font-bold mx-auto">Course Recommender</div>
      <span class="text-xl font-medium mx-auto">Easily find the course made for you !</span>
    </div>
    <div class="flex flex-column align-items-center">
      <div class="w-8">
        <HomeNavCard
          title="Recommender form"
          subtitle="Fill the form to find your best suiting course"
          :local-redirect="{ name: 'recommender' }"
        ></HomeNavCard>
        <HomeNavCard
          title="Interactive timetable"
          subtitle="Take a look at the timetable"
          :local-redirect="{ name: 'course-timetable' }"
        ></HomeNavCard>
        <HomeNavCard
          title="Course list"
          subtitle="Take a look at all the courses"
          :local-redirect="{ name: 'course-list' }"
        ></HomeNavCard>
        <HomeNavCard
          title="MCS Website"
          subtitle="Go on the official MCS website"
          web-redirect="https://mcs.unibnf.ch/program/courses-timetable/"
        ></HomeNavCard>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
