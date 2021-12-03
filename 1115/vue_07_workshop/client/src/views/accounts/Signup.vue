<template>
  <div>
    <h2>회원가입</h2>
    <hr>
    <div>
      <label for="username">아이디 : </label>
      <input type="text" id="username"
        v-model="credentials.username">
    </div>
    <div>
      <label for="password">비밀번호 : </label>
      <input type="password" id="password"
        v-model="credentials.password">
    </div>
    <div>
      <label for="password2">비밀번호 확인 : </label>
      <input type="password" id="password2"
        @keyup.enter="signup"
        v-model="credentials.password2">
    </div>

    <button @click="signup">회원가입</button>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Singup',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
        password2: '',
      }
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/signup/`,
        data: this.credentials,
      })
        .then(() => {
          this.$router.push({ name: 'Login' })
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>