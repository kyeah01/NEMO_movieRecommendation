<template>
  <div class="movieImg">
    <!-- movie -->
    <img v-if="isRouterChk()" :src="imgData.info.poster_url" alt="moviePoster" @click="infoActive" :class="{ selectedMovie: isSelectedMovie }">
    <!-- category -->
    <div class="movieImg newImg" v-if="!isRouterChk()">
      <img style="cursor:default" :src="imgData.imgSrc" alt="moviePoster">
      <div class="testMovie__detail">
        <h2 style="color: white;"> {{ imgData.title }} </h2>
        <p style="color: white;">{{ imgData.genres }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    imgData: {
      type: Object,
      required: true
    },
  },
  data: () => ({
    isSelectedMovie: false,
    hoverChk: false,
  }),
  computed: {
    setToggle () {
      return this.$store.getters.getMovieToggle
    },
    setMovieInfo() {
      return this.$store.getters.getMovieInfo
    }
  },
  watch: {
    setToggle (val) {
      if (!val) { this.isSelectedMovie = false }
    },
    setMovieInfo (val) {
      if (val && val.varified === this.imgData.varified && val.info.id === this.imgData.info.id ) {
        this.isSelectedMovie = true
      } else {
        this.isSelectedMovie = false
      }
    }
  },
  methods: {
    infoActive() {
      // store selected
      this.$store.commit('selectedMovie', this.imgData)
      // MoviePage.vue -> 스크롤 이동
      this.$EventBus.$emit('movieInfoActive', this.imgData)
    },
    isRouterChk() {
      if (this.$router.history.current["name"] === "Movie") {
        return true
      } else {
        return false
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.testMovie__detail {
  // height: 43vh;
  // width: 30vh;
  // margin: {
  //   left: 5px;
  // }
  display: inline-block;
  position: relative;
  top: -162px;
  left: 0;

  text-align: start;
  padding: var(--space-md);
  background-color: rgba(0, 0, 0, 0.8);
  width: auto;
  width: 70%;
  height: 120px;
  text-align: center;
  opacity: 0;
}
</style>
