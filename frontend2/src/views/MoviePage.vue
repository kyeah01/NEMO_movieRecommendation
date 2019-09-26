<template>
  <div class="moviePage">
    <div v-for="item in movieItems" :key="item.genre">
      <MovieList :id="item.genre" :item="item"/>
      <transition name="fade" mode="out-in">
        <MovieCard :varified="item.genre"/>
      </transition>
    </div>
  </div>
</template>

<script>
import MovieList from '@/components/movies/MovieList'
import MovieCard from '@/components/movies/MovieCard'

export default {
  components: {
    MovieList,
    MovieCard
  },
  data: () => ({
    movieItems: [{genre:'action', items: [1,2,3,4,5,6,7,8,9,10]}, {genre:'drama', items: [1,2,3,4,5,6,7]}]
  }),
  mounted() {
    // MovieImg.vue => 영화 정보 오픈 시 스크롤
    this.$EventBus.$on('movieInfoActive', (payload) => {
      this.scrollCard(payload.varified)
    })
  },
  methods: {
    scrollCard(locationId) {
      const element = document.getElementById(locationId)
      const elemRect = element.getBoundingClientRect()
      const offset = elemRect.bottom + window.pageYOffset - 100
      window.scrollTo({top: offset, behavior: 'smooth'})
    }
  }
}
</script>
