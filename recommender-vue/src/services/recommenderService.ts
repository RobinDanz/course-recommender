import { axiosClient } from '@/axios'

export async function sendRecommender(form: any): Promise<Record<string, Record<number, number>>> {
  try {
    const { data } = await axiosClient.post<Record<string, Record<number, number>>>('/forms/', form)

    return data
  } catch (error) {
    throw new Error()
  }
}
