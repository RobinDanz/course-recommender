import { axiosClient } from '@/axios'

export async function sendRecommender(form: any): Promise<Record<string, Record<number, number>>> {
  try {
    const { data } = await axiosClient.post<Record<string, Record<number, number>>>('/forms/', form)

    return data
  } catch (error) {
    throw new Error()
  }
}

export async function sendTeacherForm(form: any, courseId: number): Promise<Record<string, any>> {
  try {
    const { data } = await axiosClient.post<Record<string, any>>(
      '/teacher-forms/' + courseId + '/',
      form
    )
    console.log(data)
    return data
  } catch (error) {
    console.log(error)
    throw new Error()
  }
}
