<template>
  <div>
    <div class="profile">
      <div class="profile-banner">
        <div class="profile-banner__image">
          <img src="@/assets/image/defaultUserImage.jpg" alt="" style="width: 15vw; height: 15vw;">
        </div>
        
        <div class="profile-banner-right">
          <div class="profile-banner-right__head">
            <div class="username">
              올리비아 빵수 (성별)
            </div>
            <div class="btn btn--primary btn--md">
              Edit
            </div>
          </div>
          <div class="separater"></div> 
          <div class="profile-banner-right__body">
            <div class="profile-banner-right__body-top">
              <p>나이</p>
              <p>직업</p>
            </div>
            <div class="profile-banner-right__body-bottom">
              <p>한줄 코멘트</p>
            </div>
          </div>

        </div>
        
      </div>
      <div class="profile-myMovie"></div>
      <div class="profile-similarUser"></div>
    </div>
  </div>
</template>

<script>
export default {
 data() {
   return{
     userInfo: [
       {imgurl:require("@/assets/image/defaultUserImage.jpg")},
     ]
   }
 }
}
</script>

<style scoped lang="scss">
.profile {
  height: 100vh; 
  padding: 100px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  user-select: none;

  color: white;

  &-banner {
    display: flex;
    align-items: center;
    width: 84vw;
    height: 400px;
    padding: 20px;

    &__image{
      display: flex;
      width: 15vw;
      height: 15vw;
      border-radius: 50%;
      border : 10px solid red;
      overflow: hidden;
    }

    &-right{
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: flex-start;

      width: 70vw;
      height: 100%;
      margin: var(--space-sm);

      &__head {
        width: 100%;
        display: flex;
        justify-content: space-between;

        .username {
          font-size: 2rem;
          font-weight: 700;
        }
      }

      &__body {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: flex-start;
        width: 100%;
        height: 50%;

        font-size: 1.5rem;

        &-top{
          display: flex;
          text-align: start;
          width: 100%;

          p {
            width: 50%;
            margin: 0px;
          }
        }

        &-bottom{
          text-align: start;
          width: 100%;
        }
      }
    }
  }

  &-myMovie {
    width: 84vw;
    height: 400px;
    padding: 20px;
    background-color: grey;
  }

  &-similarUser {
    width: 84vw;
    height: 400px;
    padding: 20px;
    background-color: darkcyan;
  }
}
</style>
