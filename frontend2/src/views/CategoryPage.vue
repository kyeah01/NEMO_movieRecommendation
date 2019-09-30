<template>
  <div class="moviePage">
    <div>
      <MovieCateForm/>
      <MovieCategory :movieItems="movieItems"/>
      <!-- <transition name="fade" mode="out-in">
        <MovieCard/>
      </transition> -->
      <div v-if="loadScroll" class="lds-dual-ring"><div class="lds-bg"></div></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieCateForm from '@/components/movies/MovieCategoryForm'
import MovieCategory from '@/components/movies/MovieCategoryList'
import MovieCard from '@/components/movies/MovieCard'

export default {
  components: {
    MovieCateForm,
    MovieCategory
  },
  data: () => ({
    movieItems: [{genre:'action', items: [1,2,3,4,5,6,7,8,9,10,11,12]}],
    loadScroll: false,
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
          this.loadScroll = true
          axios.get(`https://randomuser.me/api/`)
            .then(response => {
              let i = this.movieItems[0].items.length+1
              let a = i
              for (a; a < i+12; a++) {
                this.movieItems[0].items.push(a)
              }
              this.loadScroll = false
            })

        }
      }
    }
  }
}
</script>
<style lang="scss">
.lds-dual-ring {
  display: inline-block;
  position: fixed;
  bottom: 10vh;
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
