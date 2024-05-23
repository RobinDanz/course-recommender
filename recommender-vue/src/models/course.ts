export interface Course extends Record<string, any> {
  id: number
  title: string
  day: number
  type: number
  site: string
  code: string
  start: string
  end: string
  track: number
  semester: number
}
