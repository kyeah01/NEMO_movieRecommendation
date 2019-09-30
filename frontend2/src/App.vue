<template>
  <div id="app" @wheel="checkScroll()">
    <header class="navBar"  :class="{navBar__down : (whereScroll !== 0) && (userDropdown === false), navBar__notHome : isNotInConfig()}" >
      <nav class="navItems">
        <div class="navItems__title">
          <div class="navItems__option" @click="checkLoginANDgo()">NEMO</div>
        </div>
        <div class="navItems__body">
          <div>
            <!-- <div v-if="isNotInConfig() && searchToggle === true" @click="searchToggle = !searchToggle">검색</div> -->
            <fa-icon
              icon="search"
              v-if="isNotInConfig() && searchToggle === true"
              @click="searchToggle = !searchToggle; setFocus();"
              />
            <transition name="fade" mode="out-in">
              <input type="text"
                v-if="isNotInConfig() && searchToggle === false"
                ref="search"
                placeholder="Search"
                @blur="searchToggle = !searchToggle"
                alt="Search"
                >
            </transition>
          </div>
          <router-link :to="{ name: 'NewTest' }" v-if="isNotInConfig()">NewTest</router-link>
          <router-link :to="{ name: 'Movie' }" v-if="isNotInConfig()">Movie</router-link>
          <router-link :to="{ name: 'Search' }" v-if="isNotInConfig()">Search</router-link>
          <div class="navItems__option" @click="userDropdown = !userDropdown; setFocus();" v-if="userInfo">{{userInfo}}</div>
          <router-link :to="{ name: 'Sign' }" v-if="!isNotInConfig()">Login</router-link>
        </div>
      </nav>
    </header>
        <ul class="divFocus" v-if="userDropdown === true" ref="search" @blur="userDropdown = !userDropdown" tabindex="1"> 
          <p @click="goProfile()">Profile</p>
          <p @click="logOut()">Logout</p>
        </ul>
    <transition name="fade" mode="out-in">
      <router-view/>
    </transition>
  </div>
</template>

<script>
import session from "@/api/modules/session";
import router from "@/router";
import api from "./api";

export default {
  name: 'app',
  components: {
  },
  data() {
    return{
      isLogin : '',
      userInfo : false,
      userDropdown : false,

      whereScroll : 0,
      searchToggle : true,
    }
  },
  updated() {
    if (session.check()) {
      const data = JSON.parse(sessionStorage.getItem("drf"))
      this.userInfo = data.username
    }
    else {
      this.userInfo = false
    }
    
  },
  methods: {
    isNotInConfig() {
      if (session.check()) {
        return true
      }
      else {
        return false
      }
    },
    checkLoginANDgo() {
        const data = JSON.parse(sessionStorage.getItem("drf"))
        if (session.check()) {
          return router.push({name : 'Movie'})
        }
        else {
          return router.push({path : '/'})
        }
    },
    goProfile(){
      const data = JSON.parse(sessionStorage.getItem("drf"))
      router.push({
            name : 'Profile', 
            params: {user_id:data.id}
          },this.blurFocus())
    },
    checkScroll() {
      this.whereScroll = window.pageYOffset
    },
    setFocus() {
      let _this = this
      _this.$nextTick()
        .then(() => { _this.$refs.search.focus() })
    },
    blurFocus() {
      let _this = this
      _this.$nextTick()
        .then(() => { _this.$refs.search.blur() })
    },
    async logOut() {
      const data = JSON.parse(sessionStorage.getItem("drf"))
      const result = await api.logOut()
      this.$router.push({ name: 'Home' },
      this.blurFocus())
    }
  },
}
</script>

<style lang="scss">
#app {
  text-align: center;
  height: 1500px;
}

// CSS transition
.fade-enter-active, .fade-leave-active {
  transition: all .3s ease;
}
.fade-enter, .fade-leave-active {
  opacity: 0;
}
</style>

<style scoped lang="scss">
// a {
//   color: $primary;
//   text-decoration: none;
// }
</style>
