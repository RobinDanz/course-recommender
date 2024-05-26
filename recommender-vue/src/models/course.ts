export interface Course extends Record<string, any> {
  id: number
  title: string
  day: number
  type: number
  site: number
  code: string
  start: string
  end: string
  track: number
  semester: number
  description: string
  url: string
}

export const calculateDuration = (course: Course) => {
  const startVal = course.start.split(':').map((str) => Number.parseInt(str))

  const endVal = course.end.split(':').map((str) => Number.parseInt(str))

  const start = new Date()
  const startMili = start.setHours(startVal[0], startVal[1], 0, 0)

  const end = new Date()
  const endMili = end.setHours(endVal[0], endVal[1], 0, 0)

  return (endMili - startMili) / 60000
}

export const dayToString = (course: Course) => {
  const days = ['On Appointment', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

  return days[course.day]
}
