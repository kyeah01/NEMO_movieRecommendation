<template>
  <div class="moviePage">
    <div v-for="movieItem in movieItems" :key="movieItem.varified">
      <MovieList :id="movieItem.varified" :movieItem="movieItem"/>
      <transition name="fade" mode="out-in">
        <MovieCard :varified="movieItem.varified" :movieInfo="selectInfo"/>
      </transition>
    </div>
    <div class="lds-bg"/>
  </div>
</template>

<script>
import api from '@/api'
import { mapState, mapActions } from "vuex"
import MovieList from '@/components/movies/MovieList'
import MovieCard from '@/components/movies/MovieCard'

export default {
  components: {
    MovieList,
    MovieCard
  },
  data: () => ({
    movieItems: [],
    selectInfo: {}
  }),
  computed: {
    ...mapState({
      movieList: state => state.movieSearchList
    })
  },
  mounted() {
    // MovieImg.vue => 영화 정보 오픈 시 스크롤
    this.$EventBus.$on('movieInfoActive', (payload) => {
      this.selectMovie(payload.info.id)
      setTimeout(() => {
        this.scrollCard(payload.varified)
      }, 10)
    }),
    this.searchMovies()
  },
  watch: {
    movieList() {
      this.setMovieItems()
    }
  },
  methods: {
    ...mapActions(["searchMovies"]),
    scrollCard(locationId) {
      const element = document.getElementById(locationId)
      const elemRect = element.getBoundingClientRect()
      const offset = elemRect.bottom + window.pageYOffset - 100
      window.scrollTo({top: offset, behavior: 'smooth'})
    },
    setMovieItems() {
      this.movieItems.push({ varified: 'action', items: this.movieList.slice(0, 24)})
      this.movieItems.push({ varified: 'drama', items: this.movieList.slice(23, 44)})
      console.log('setMovieItems() :', 'done')
    },
    async selectMovie(id) {
      const resp = await api.searchMovies({'id': id})
      this.selectInfo = resp.data
    }
  }
}
</script>
