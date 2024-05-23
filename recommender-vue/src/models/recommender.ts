import * as yup from 'yup'

export interface Recommender extends Record<string, any> {
  university: string[]
  evaluation: string[]
  courseType: string[]
  track: string[]
  lectures: string[]
  subjectType: number
  mainSubject: string[]
  interactions: number
  blackboard: number
  recording: number
  accessibility: number
}

const schema = yup.object<Recommender>().shape({
  university: yup.array().of(yup.string()).min(1, 'at least one').required(),
  evaluation: yup.array().of(yup.string()).min(1, 'at least one').required(),
  courseType: yup.array().of(yup.string()).min(1, 'at least one').required(),
  track: yup.array().of(yup.string()).min(1, 'at least one').required(),
  lectures: yup.array().of(yup.string()).min(1, 'at least one').required(),
  subjectType: yup.number().required(),
  mainSubject: yup.array().of(yup.string()).min(1, 'at least one').required(),
  interactions: yup.number().required(),
  blackboard: yup.number().required(),
  recording: yup.number().required(),
  accessibility: yup.number().required()
})
