<template>
  <div class="moviePage">
    <div v-for="movieItem in movieItems" :key="movieItem.varified">
      <MovieList :id="movieItem.varified" :movieItem="movieItem"/>
      <div style="color:white;">
      </div>
      <transition name="fade" mode="out-in">
        <MovieCard :varified="movieItem.varified" :movieInfo="selectInfo"/>
      </transition>
    </div>
    <div class="lds-bg"/>
  </div>
</template>

<script>
import api from '@/api'
import { mapState, mapActions, mapGetters } from "vuex"
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
    }),
    ...mapGetters({
      myMovie: 'getUserTasteMovie'
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

      // 레이팅 높은 영화 =>
      // 새로 올라온 영화

      // # 1
      // 내 추천 영화 => profile your_taste_movie
      // 문자열 split => sort
      let reAry = this.myMovie.split('|').map(Number).sort((a, b) => { return a - b })
      let recommendAry = []
      reAry.forEach((el) => { recommendAry.push(this.movieList.find(movie => movie.id === el)) })

      // # 2
      // 비슷한 연령대가 본 영화 => movie age

      // # 3
      // 장르별 영화 => movie genre
      let reGenre = []
      let redict = {}
      recommendAry.forEach((el) => { reGenre.push(el.genres) })

      for (var i=0; i < reGenre.length; i++) {
        for (var j=0; j < reGenre[i].length; j++) {
          if (!redict[reGenre[i][j]]) {
            redict[reGenre[i][j]] = 1
          } else {
            redict[reGenre[i][j]] += 1
          }
        }
      }
      let maxKey = Object.keys(redict).reduce((a, b) => redict[a] > redict[b] ? a : b);
      let genreMovie = this.genreMovie(maxKey)
      console.log(genreMovie)

      // this.movieItems.push({ varified: '추천영화', items: recommendAry})
      // this.movieItems.push({ varified: 'drama', items: this.movieList.slice(23, 44)})
      console.log('setMovieItems() :', 'done')
    },
    async selectMovie(id) {
      const resp = await api.searchMovies({'id': id})
      this.selectInfo = resp.data
    },
    async genreMovie(val) {
      const resp = await api.searchMovies({'genre': val})
      return resp.data
    }
  }
}
</script>
