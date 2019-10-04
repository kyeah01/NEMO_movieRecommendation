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
                <h3>Harry Potter</h3>
                <h5>user.gender</h5>
              </div>
              <div class="separater" style="background-color: gainsboro ;">.</div> 
              <div style="color:black;" >
                 <span>user.age</span> /
                <span>user.occupation</span>
                <span>한줄평</span>
        
               
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
  .separater{
    background-color: grey;
  }
</style>

