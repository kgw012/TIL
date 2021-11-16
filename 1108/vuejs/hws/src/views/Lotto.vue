<template>
  <div class="lotto">
    <h1>로또</h1>
    <button @click="getLuckyNumbers">Get Lucky Numbers</button>
    <p v-if="selectedNumbers.length">{{ selectedNumbers }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'Lotto',
  data: function() {
    return {
      selectedNumbers: [],
    }
  },
  methods: {
    getLuckyNumbers: function () {
      const numbers = _.range(1, 46)
      this.selectedNumbers = _.sampleSize(numbers, this.$route.params.lottoNum)
    }
  }
}
</script>