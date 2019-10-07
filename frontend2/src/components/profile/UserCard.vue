<template>
    <div class="SimilarUserInfo" >
        <!-- similar users info -->
            <!-- 유저 이미지 -->
              <div class="SimilarUserInfo-banner">
                  <div class="SimilarUserInfo-banner_img">
                  <img src="@/assets/image/defaultUserImage.jpg" alt="" style="width: 65px; height: 65px;">
                  </div>
                </div>
              <!-- 유저 신상정보 -->
              <div>
                <span style ="display:inline-block;color:black; font-weight: bold; margin-right:1px;">{{ simUserInfo.username }}</span>
                <span style ="display:inline-block;color:black;margin-left:1px;">(m)</span> 
              </div>
              <div class="separater separater__1" style="background-color: gainsboro ;">.</div> 
              <div style="color:black;" >
                 <!-- <span>user.age</span>
                <span>user.occupation</span>
                <span>한줄평</span> -->
                 <p>나이:user.age</p>
                <p>직업:user.occupation</p>
                <p>한줄평:</p>
              </div>
             
          
          
    
    </div>
    
</template>

<script>


import { mapState, mapActions } from "vuex";

export default {
    name : 'UserCard',
    data: () => ({
      //  similar user 모든 정보 담기
    simUserInfo : [],
    infoBtnToggle: 2
  }),

    computed: {
    ...mapState({
      userData: state => state.userData,
      userList: state => state.userData.similaruser,
      movieList: state => state.userData.ratingmovie,
    }),
    //axios 요청값을 받는거
    methods: {
      async selectProfile(i) {
      const resp = await api.searchProfile({'i': i})
      this.simUserInfo = resp.data
    },

    }
// api 요청하고 retrun 된 res 값을 -- this.userInfo
// const res = aixos.get("~~~")
// console.log(res)

// aixos.get("~~~").then(res=>{
//   console.log(res)
// })
  }

  
    





}
</script>
<style lang="scss" scope>
  //   background-color: grey;
  //   margin-top:var(--space-xxxxs);
  //   margin-bottom:var(--space-xxxxs);
  // }
 
</style>

