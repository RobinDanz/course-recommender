import { axiosClient } from '@/axios'

export async function postComment(form: any): Promise<Record<string, string>> {
  try {
    const { data } = await axiosClient.post<Record<string, string>>('/comments/', form)

    return data
  } catch (error) {
    throw new Error()
  }
}
