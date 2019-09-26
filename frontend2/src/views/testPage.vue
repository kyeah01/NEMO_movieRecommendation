<template>
  <div class="moviePage">
    <div>
      <MovieList :movieItems="movieItems"/>
      <!-- <transition name="fade" mode="out-in">
        <MovieCard/>
      </transition> -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieList from '@/components/movies/MovieSearchList'
import MovieCard from '@/components/movies/MovieCard'

export default {
  components: {
    MovieList,
    MovieCard
  },
  data: () => ({
    movieItems: [{genre:'action', items: [1,2,3,4,5,6,7,8,9,10,11,12]}],
    persons: []
  }),
  mounted() {
    // MovieImg.vue => 영화 정보 오픈 시 스크롤
    this.$EventBus.$on('movieInfoActive', (payload) => {
      this.scrollCard(payload.varified)
    })
    this.scroll(this.person)
  },
  beforeMount() {
    this.getInitialUsers()
  },
  methods: {
    scrollCard(locationId) {
      const element = document.getElementById(locationId)
      const elemRect = element.getBoundingClientRect()
      const offset = elemRect.bottom + window.pageYOffset - 100
      window.scrollTo({top: offset, behavior: 'smooth'})
    },
    getInitialUsers () {
      for (var i = 0; i < 5; i++) {
        axios.get(`https://randomuser.me/api/`)
          .then(response => {
            this.persons.push(response.data.results[0])
          })
      }
    },
    // 1. 화면길이를 지속적으로 체크 못함 2. 함수가 여러번 실행되는것 방지해야함
    scroll(person) {
      window.onscroll = () => {
        let bOfW = Math.round(document.documentElement.scrollTop + window.innerHeight) === document.documentElement.offsetHeight
        if (bOfW) {
          axios.get(`https://randomuser.me/api/`)
            .then(response => {
              let i = this.movieItems[0].items.length+1
              let a = i
              for (a; a < i+10; a++) {
                this.movieItems[0].items.push(a)
              }
            })
        }
      }
    }
  }
}
</script>
