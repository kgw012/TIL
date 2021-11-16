<template>
  <div class="lunch">
    <h1>점심메뉴</h1>
    <button @click="pickLunch">Pick Lunch</button>
    <p>{{ menu }}</p>
    <br>
    <h2>로또를 뽑아보자</h2>
    <button @click="goLottoPage">Pick Lotto</button>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'Lunch',
  data: function () {
    return {
      menu: '',
      menus: ['국밥', '피자', '치킨', '김밥', '라면'],
    }
  },
  methods: {
    pickLunch: function () {
      this.menu = _.sample(this.menus, 1)
    },
    goLottoPage: function () {
      this.$router.push({ name: 'Lotto', params: { lottoNum: 6 }})
    },
  }
}
</script>
