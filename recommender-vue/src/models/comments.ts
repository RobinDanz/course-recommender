export interface Comment extends Record<string, any> {
  id: number
  username: string
  content: string
  course_id: number
}
