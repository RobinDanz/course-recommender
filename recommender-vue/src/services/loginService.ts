import type { Token } from '@/models/token'
import type { UserLogin } from '@/models/userLogin'

export const requestToken = async (userLogin: UserLogin): Promise<Token> => {
  const test = await fetch('http://localhost:8000/token', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    },
    body: new URLSearchParams(userLogin).toString()
  })

  const data = await test.json()
  console.log(data)
  return data
}
