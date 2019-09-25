<template>
  <div>
    <div>
      movie play component
    </div>
    <div>
      <MovieList/>
    </div>
  </div>
</template>

<script>
import MovieList from '@/components/movies/MovieList'

export default {
  components: {
    MovieList,
  }
}
</script>

<style scoped lang="scss">
</style>
