export interface Comment extends Record<string, any> {
  id: number
  username: string
  comment: string
  course: number
  timestamp: Date
}
