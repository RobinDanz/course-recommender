import { axiosClient } from '@/axios'

export async function sendRecommender(form: any): Promise<any> {
  try {
    const { data } = await axiosClient.post('/forms/', form)

    console.log(data)
  } catch (error) {
    throw new Error()
  }
}
