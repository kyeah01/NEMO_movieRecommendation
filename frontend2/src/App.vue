<template>
  <div id="app" @wheel="checkScroll()">
    <header class="navBar"  :class="{navBar__down : (whereScroll !== 0)}">
      <nav class="navItems">
        <div class="navItems__title">
          <router-link :to="{ name: 'Home' }">NEMO</router-link>
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
          <router-link :to="{ name: 'Movie' }" v-if="isNotInConfig()">Movie</router-link>
          <router-link :to="{ name: 'Profile' }" v-if="isNotInConfig()">Profile</router-link>
          <router-link :to="{ name: 'Sign' }" v-if="!isNotInConfig()">Login</router-link>
        </div>
      </nav>
    </header>
    <transition name="fade" mode="out-in">
      <router-view/>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'app',
  components: {
  },
  data() {
    return{
      whereScroll : 0,
      searchToggle : true,
    }
  },
  methods: {
    isNotInConfig() {
      if (this.$router.history.current["name"] === "Home") {
        return false
      }
      else {
        return true
      }
      // if (this.$router.history.current["name"] === "Sign" ) {
      //   return fla
      // }
    },
    checkScroll() {
      this.whereScroll = window.pageYOffset
    },
    setFocus() {
      let _this = this
      _this.$nextTick()
        .then(() => { _this.$refs.search.focus() })
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
