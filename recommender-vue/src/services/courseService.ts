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

export async function getCourse(id: number): Promise<Course> {
  try {
    const { data } = await axiosClient.get<Course>('/courses/' + id)

    return data
  } catch (error) {
    throw new Error()
  }
}
