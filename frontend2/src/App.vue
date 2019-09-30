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
          <router-link :to="{ name: 'Search' }" v-if="isNotInConfig()">Category</router-link>
          <router-link :to="{ name: 'Profile' }" v-if="isNotInConfig()">Profile</router-link>
          <router-link :to="{ name: 'Sign' }" v-if="!isNotInConfig()">Login</router-link>
        </div>
      </nav>
    </header>
    <transition name="fade" mode="out-in">
      <router-view/>
    </transition>

    <footer>
      Copyright 2019. CyberGhost. All rights reserved.
    </footer>
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
footer {
  position: absolute;

  width:100%;

  line-height: 25vh;
  height: 25vh;
  color: rgba(255, 255, 255, 0.7);
  background-color: rgb(18, 18, 18);
}
</style>
