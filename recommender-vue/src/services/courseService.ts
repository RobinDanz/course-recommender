import { axiosClient } from '@/axios'
import type { Course } from '@/models/course'

export async function getCourseList(): Promise<Course[]> {
  try {
    const { data } = await axiosClient.get<Course[]>('/courses/')

    return data
  } catch (error) {
    throw new Error()
  }
}
