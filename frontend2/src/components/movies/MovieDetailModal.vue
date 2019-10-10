<template>
    <transition name="modal" v-if="showModal">
      <div class="modal-mask">
        <div class="modal-wrapper">
          <div class="modal-container">

            <img :src="imgData.imgSrc" alt="moviePoster" style="height:auto;" onerror="this.onerror=null; this.src='http://kaverisias.com/wp-content/uploads/2018/01/catalog-default-img.gif'">
            <div>
            <div class="modal-header">
              <div>
                <slot name="header">
                  <h2>{{ imgData.title }}</h2>
                </slot>
              </div>
            </div>


            <div class="modal-body">
              <slot name="body">
                <h3>Genres</h3>
                {{ imgData.genres }}
              </slot>
            </div>

            <div class="modal-footer">
              <slot name="footer">
                <h3>Overview</h3>
                {{ imgData.overview }}
              </slot>
            </div>
            <!--rating 준 user-->
            <div v-for="info in scoredData" :scroll.passive="onScroll">
              {{ info.user }} {{ info.rating }}
            </div>

            
            <button class="modal-default-button" @click="change()">
                  OK
            </button>
            </div>
          </div>
        </div>
      </div>
    </transition>

</template>

<script>

  export default {
  props: {
    movieInfo: {
      type: Object,
      required: true
    },
    imgData: {
      type: Object,
      required: true
    },
    showModal: {
      type: Boolean
    }
  },

  data: function() {
      return {
          changeModal: true
      }
  },
  mounted() {
    console.log(this.movieInfo)
  },
  computed: {
      scoredData () {
      return this.movieInfo.rating
    },
  },

  methods: {
    change() {
      this.$emit('close', false)
    }
    }
  }

</script>

<style>
/*modal*/

.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, .5);
  display: table;
  transition: opacity .3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  display: flex;
  
  width: 850px;
  height: auto;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, .33);
  transition: all .3s ease;
  font-family: Helvetica, Arial, sans-serif;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}

/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}


</style>