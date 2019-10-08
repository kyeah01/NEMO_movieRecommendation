<template>
  <div class="moviePage">
    <div>
      <MovieCateForm/>
      <MovieCategory :movieItems="searchMovies"/>
      <div class="lds-bg">
        <div v-if="loadScroll" class="lds-dual-ring"></div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieCateForm from '@/components/movies/MovieCategoryForm'
import MovieCategory from '@/components/movies/MovieCategoryList'

export default {
  components: {
    MovieCateForm,
    MovieCategory
  },
  data: () => ({
    loadCall: false,
    loadScroll: false,
    searchMovies: [],

    throwData: false,
  }),
  mounted() {
    // App.vue => 영화 정보 받음
    this.$EventBus.$on('movieSearchList', (payload) => {
      if (payload.str === null || payload.str === '') {
        this.getInitialMovies()
      } else {
        this.setSearchMovies(payload.payload)
      }
    })
    this.scroll(this.searchMovies)
  },
  beforeMount() {
    this.getInitialMovies()
  },
  methods: {
    getInitialMovies () {
      this.searchMovies = []
      this.throwData = false
      for (var i = 0; i < 12; i++) {
        this.searchMovies.push(this.$store.state.movieSearchList[i])
      }
    },
    setSearchMovies(movieList) {
      this.searchMovies = movieList
      this.throwData = true
    },
    scroll(movieItem) {
      window.onscroll = () => {
        let bOfW = Math.round(document.documentElement.scrollTop + window.innerHeight) >= document.documentElement.offsetHeight
        if ( bOfW && this.loadCall === false && this.throwData === false ) {
          this.loadCall = true
          this.loadScroll = true
          let i = this.searchMovies.length
          let a = i
          for ( a; a < i+12; a++ ) {
            this.searchMovies.push(this.$store.state.movieSearchList[a])
          }
          setTimeout(() => {
            this.loadScroll = false
            this.loadCall = false
          }, 1000)
        }
      }
    }
  }
}
</script>
<style lang="scss">
.lds-bg {
  position: relative;
  height: 20vh;
  width: 100%;
  background: linear-gradient(to bottom, rgba(70, 70, 70, 0), rgb(18, 18, 18));
}
.lds-dual-ring {
  display: inline-block;
  position: absolute;
  bottom: 5vh;
  width: 64px;
  height: 64px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 46px;
  height: 46px;
  margin: 1px;
  border-radius: 50%;
  border: 5px solid #fff;
  border-color: #fff transparent #fff transparent;
  animation: lds-dual-ring 0.5s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
