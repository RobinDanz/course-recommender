import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import AboutView from '@/views/AboutView.vue'
import LoginView from '@/views/LoginView.vue'
import CourseListView from '@/views/CourseListView.vue'
import CourseTimetableView from '@/views/CourseTimetableView.vue'
import RecommenderView from '@/views/RecommenderView.vue'
import CourseDetailsView from '@/views/CourseDetailsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/recommender',
      name: 'recommender',
      component: RecommenderView
    },
    // {
    //   path: '/about',
    //   name: 'about',
    //   component: AboutView
    // },
    // {
    //   path: '/login',
    //   name: 'login',
    //   component: LoginView
    // },
    {
      path: '/list',
      name: 'course-list',
      component: CourseListView
    },
    {
      path: '/timetable',
      name: 'course-timetable',
      component: CourseTimetableView
    },
    {
      path: '/course/:courseId',
      name: 'course-details',
      component: CourseDetailsView,
      props: true
    }
  ]
})

export default router
