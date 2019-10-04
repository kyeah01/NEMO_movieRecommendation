<template>
  <div>
    <transition name="slide" mode="out-in">
      <div>
        <div class="separater separater__trans"></div>
        <!-- <div v-for="i in movieItems">{{ i }}</div> -->
        <MovieImg v-for="movie in movieItems" :key="movie.id" :imgData="{ imgSrc: movie.poster_url, id: movie.id, varified: 'aa' }"/>
      </div>
    </transition>
  </div>
</template>

<script>
import MovieImg from './MovieImg'

export default {
  components: {
    MovieImg
  },
  props: {
    movieItems: {
      type: Array,
      required: true
    },
  },
  data: () => ({
    showBtn: false,
  }),
  methods: {
    closeInfoBtn() {
      // $store 비우기
      this.$store.commit('selectedMovie')
      // 리스트 양옆으로 넘길때 MovieCard.vue 닫기
      this.$EventBus.$emit('closeMovieCard')
    },
  },
}
</script>
