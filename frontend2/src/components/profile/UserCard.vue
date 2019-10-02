<template>
    <div class="SimilarUserInfo" style="position:absolute; width;30vw;">
        <div v-if="infoBtnToggle==2">
        <!-- similar users info -->
            <!-- 유저 이미지 -->
            <div class="SimilarUserInfo_img">
            <img src="@/assets/image/defaultUserImage.jpg" alt="" style="width: 10vw; height: 10vw;">
            </div>
            <!-- 유저 신상정보 -->
            <div>
              <h1>Harry Potter</h1>
              <h5>user.gender</h5>
            </div>
            <div class="separater"></div> 
            <div>
              <h5>user.age</h5>
              <h5>user.occupation</h5>
            </div>
            <div>
              <h5>한줄평</h5>
            </div>




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
