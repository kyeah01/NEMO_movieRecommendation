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
                <span style ="display:inline-block;color:black; font-weight: bold; margin-right:1px;">user.name</span>
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
export default {
    name : 'UserCard',
    data: () => ({
    infoBtnToggle: 2
  }),

}
</script>
<style lang="scss" scope>
  //   background-color: grey;
  //   margin-top:var(--space-xxxxs);
  //   margin-bottom:var(--space-xxxxs);
  // }
 
</style>

