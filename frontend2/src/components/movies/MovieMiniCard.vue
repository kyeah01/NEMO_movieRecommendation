<template>
  <div>
    <p>{{ setMovie.title }}</p>
    <img class="testImg" :src="setMovie.poster_url" alt="movieposter">
  </div>
</template>

<script>
export default {
  props: {
    movieId: Number,
    require: true
  },
  computed: {
    setMovie() {
      return this.$store.state.movieSearchList[this.movieId-1]
    }
  }
}
</script>

<style scoped lang="scss">
p {
  margin: 0;
}
.testImg {
  position: absolute;
  top: 160%;
  right: 18%;
  width: 10vw;
  height: 30vh;
}
</style>
