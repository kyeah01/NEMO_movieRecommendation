<template>
  <div>
    <div class="profile">
      <!-- 유저 정보 시작 -->
      <div class="profile-banner">
        <!-- 유저 이미지 시작 -->
        <div class="profile-banner__image">
          <img src="@/assets/image/defaultUserImage.jpg" alt="" style="width: 10vw; height: 10vw;">
        </div>
        <!-- 유저 이미지 끝 -->

        <!-- 유저 상세 정보 시작 -->
        <div class="profile-banner-right">

          <!-- 유저 명 / 성별 / 수정 버튼 시작-->
          <div class="profile-banner-right__head">
            <div class="username">
               {{ userData.username }} (<span v-if="userData.gender == 'M'">Man</span> <span v-else>Women</span>)
            </div>
            <div class="btn btn--primary btn--md" @click="Go">
              Edit
            </div>
          </div>
          <!-- 유저 명 / 성별 / 수정 버튼 끝 -->
          
          <div class="separater"></div> 

          <div class="profile-banner-right__body">
            <!-- 유저 상세 정보 상단  -->
            <div class="profile-banner-right__body-top">
              <p v-if="userData.age === 1"><b>나이 : </b>Under 18</p>
              <p v-else><b>나이 : </b>{{ userData.age }}</p>
              <p><b>직업 : </b>{{ userData.occupation }}</p>
            </div>
            <!-- 유저 상세 정보 하단  -->
            <div class="profile-banner-right__body-bottom">
              <p><b>한줄 코멘트</b></p>
              
            </div>
          </div>
        </div>
        <!-- 유저 상세 정보 끝 -->
      </div>
      <!-- 유저 정보 끝 -->

      <!-- 프로필 토글 버튼 시작 -->
      <div class="profileToggle">
        <p class="btn" :class="{profileToggle__select : checkToggle === 1}" @click="checkToggle = 1">평가한 영화</p>
        <p class="btn" :class="{profileToggle__select : checkToggle === 2}" @click="checkToggle = 2">유사한 유저</p>
      </div>
      <!-- 프로필 토글 버튼 끝 -->

      <!-- 프로필 하단 컴포넌트 시작 -->
        <!-- 유저가 본 영화 목록 시작 -->
        <div class="profile-myMovie" v-if="checkToggle === 1">
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
        <!-- 유저가 본 영화 목록 끝 -->

        <!-- 유저와 유사한 유저 목록 시작 -->
        <div class="profile-similarUser" v-if="checkToggle === 2">
          <!-- i (similar user id 값)만 UserCard에 전달해주는 것임) -->
          <!-- userData.similaruser.slice(0,5) -->
          <UserCard v-for="i in userData.similaruser" :key="i" style="display:inline-block;" :simUserId="i"/>
       
            
        </div>
        <!-- 유저와 유사한 유저 목록 끝 -->
      <!-- 프로필 하단 컴포넌트 시작 -->
    </div>
  </div>
</template>

<script>
import MovieList from '@/components/movies/MovieList'
import MovieCard from '@/components/movies/MovieCard'
import UserCard from '@/components/profile/UserCard'
import { mapState, mapActions, mapGetters } from "vuex";

export default {
components: {
    MovieList,
    MovieCard,
    UserCard
  },
 data() {
   return{
     user: this.$route.params.user_id,

     checkToggle : 1,

     userInfo: [
       {imgurl:require("@/assets/image/defaultUserImage.jpg")},
     ],

     movieItems: [],
     selectInfo: {}
   }
 },
 computed: {
   setTest() {
     return this.$store.state.userData
   },
    ...mapState({
      userData: state => state.userData,
      userList: state => state.userData.similaruser,
      movieList: state => state.movieSearchList
      }),
      ...mapGetters({
        myMovie: 'getUserMovieData'
      })
  },
  watch: {
    movieList() {
      this.setMovieItems()
    },
    setTest() {
      console.log(this.setTest);
    }
  },
  mounted() {
    this.loadUser(this.user),
    // MovieImg.vue => 영화 정보 오픈 시 스크롤
    this.$EventBus.$on('movieInfoActive', (payload) => {
      this.scrollCard(payload.varified)
    }),
    // MovieImg.vue => 영화 정보 오픈 시 스크롤
    this.$EventBus.$on('movieInfoActive', (payload) => {
      let waitPlease = true
      if (waitPlease) {
        this.selectMovie(payload.info.id)
      }
      setTimeout(() => {
        waitPlease = false
        this.scrollCard(payload.varified)
      }, 10)
    }),
    this.searchMovies()
  },
  
  methods: {
    ...mapActions({
        loadUser: 'searchProfile'
      }),
    ...mapActions(["searchMovies"]),
      
    scrollCard(locationId) {
      const element = document.getElementById(locationId)
      const elemRect = element.getBoundingClientRect()
      const offset = elemRect.bottom + window.pageYOffset - 100
      window.scrollTo({top: offset, behavior: 'smooth'})
    },
    setMovieItems() {
      // # 1
      // 내 추천 영화 => profile your_taste_movie
      let reAry = this.myMovie.your_taste_movie.split('|').map(Number).sort((a, b) => { return a - b })
      let recommendAry = []
      reAry.forEach((el) => { recommendAry.push(this.movieList.find(movie => movie.id === el)) })

      // # 2
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
      let maxKey = Object.keys(redict).reduce((a, b) => redict[a] > redict[b] ? a : b)
      // setting genreMovieItems
      this.getMovieListItem('genre', maxKey)

      // # 3
      // 나름 높은거
      let highAry = []
      for (var i=0; i < this.movieList.length; i++) {
        if (Number(this.movieList[i].title.slice(-5, -1)) > 1997) {
          highAry.push(this.movieList[i])
        }
      }
      this.movieItems.push({ varified: `${ this.myMovie.username }님을 위한 영화`, items: recommendAry })
      this.movieItems.push({ varified: "since 98's", items: highAry })
      console.log('setMovieItems() :', 'done')
    },
    async selectMovie(id) {
      const resp = await api.searchMovies({'id': id})
      this.selectInfo = resp.data
    },
    async getMovieListItem(param, val) {
      console.log(param, val)
      if (param === 'genre') {
        const resp = await api.searchMovies({ 'genre': val })
        this.movieItems.push({ varified: val, items: resp.data })
      }
      if (param === 'occupation') {
        const resp = await api.searchMovies({ 'occupation': val })
        this.movieItems.push({ varified: val, items: resp.data })
      }
    },
    Go() {
      this.$emit('transForm');
      window.scrollTo(0, 0);
    },
  }
}

</script>

<style scoped lang="scss">

</style>
