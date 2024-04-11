<script setup lang="ts">
import { ref } from 'vue'
import InputText from 'primevue/inputtext'
import Password from 'primevue/password'
import Button from 'primevue/button'
import { type UserLogin } from '@/models/userLogin'
import { requestToken } from '@/services/loginService'

const userLogin = ref<UserLogin>({
  username: '',
  password: ''
})

const login = async () => {
  await requestToken(userLogin.value)
}
</script>

<template>
  <div class="h-auto flex justify-content-center m-5">
    <div class="w-3 bordered">
      <div class="flex justify-content-center">Login</div>
      <div class="flex flex-column gap-2">
        <label for="username">Username</label>
        <InputText id="username" v-model="userLogin.username" aria-describedby="username-help" />
        <small id="username-help">Enter your username</small>
      </div>
      <div class="flex flex-column gap-2">
        <label for="username">Password</label>
        <Password
          id="password"
          v-model="userLogin.password"
          aria-describedby="password-help"
          :feedback="false"
          toggleMask
        />
        <small id="password-help">Enter your password</small>
      </div>
      <div class="flex justify-content-center my-2">
        <Button @click="login()">Login</Button>
      </div>
    </div>
  </div>
</template>
