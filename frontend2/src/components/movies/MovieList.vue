<template>
  <div
    class="movieList"
    @mouseover="mouseOver"
    @mouseleave="mouseLeave">
    <transition name="slide" mode="out-in">
      <div style="height: 2em;">
        <p>Netflix 오리지널</p>
        <MovieImg v-for="i in paginatedData" :key="i" :imgData="{imgSrc, id:i, varified: item.genre}" style="z-index:100;"/>
      </div>
    </transition>
    <div v-show="showBtn" style="display: inline; z-index: 2;">
      <button class="pageBtn pagePrev" :disabled="pageNum === 0" @click="pagination(false)">이전</button>
      <button class="pageBtn pageNext" :disabled="pageNum >= pageCount - 1" @click="pagination(true)">다음</button>
    </div>
  </div>
</template>

<script>
import MovieImg from './MovieImg'

export default {
  components: {
    MovieImg
  },
  props: {
    item: {
      type: Object,
      required: true
    },
    pageSize: {
      type: Number,
      required: false,
      default: 5
    }
  },
  data: () => ({
    pageNum: 0,
    showBtn: false,
    imgSrc: "https://w.namu.la/s/5ef7389c2e210b3a176ae30b068a73637be82cab0d09ac986e16b85a6aa66f3caa54365c528a40f056643f53c8aa32f442f423754b2317648ee65d4408e9612d7dfe4a2dd9d7db50c0d2bc4d5bc3aef988b1cb3efe57dcb27486859ad0e08113"
  }),
  computed: {
    pageCount () {
      let listLeng = this.item.items.length, listSize = this.pageSize, page = Math.floor((listLeng - 1) / listSize) + 1
      return page
    },
    paginatedData () {
      const start = this.pageNum * this.pageSize, end = start + this.pageSize;
      return this.item.items.slice(start, end)
    }
  },
  methods: {
    pagination(bool) {
      if (bool) {
        this.pageNum++
      } else {
        this.pageNum--
      }
      this.closeInfoBtn()
    },
    mouseOver() {
      this.showBtn = true
    },
    mouseLeave() {
      this.showBtn = false
    },
    closeInfoBtn() {
      // $store 비우기
      this.$store.commit('selectedMovie')
      // 리스트 양옆으로 넘길때 MovieCard.vue 닫기
      this.$EventBus.$emit('closeMovieCard')
    },
  },
}
// pagination 참고링크 : https://pewww.tistory.com/5
</script>
