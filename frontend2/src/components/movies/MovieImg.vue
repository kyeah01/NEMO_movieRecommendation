<template>
  <div class="movieImg">
    <img :src="imgData.imgSrc" alt="moviePoster" @click="infoActive" :class="{ selectedMovie: isSelectedMovie }">
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
    isSelectedMovie: false
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
      if (val && val.varified === this.imgData.varified && val.id === this.imgData.id ) {
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
    }
  }
}
</script>
