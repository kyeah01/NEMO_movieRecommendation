<template>
    <div class="profile">
        <div class="profile-edit">
            <div class="profile-edit__list">
                <div id="passwordChange" class="change">
                    <p>비밀번호 변경</p>
                    <div class="btn btn--sm" @click="editToggle = 1" v-if="editToggle != 1">Expand</div>
                    <div class="btn btn--sm" @click="editToggle = 0" v-if="editToggle === 1">Close</div>
                </div>
                <div v-if="editToggle === 1" class="expand">
                    <div class="expand__password">
                        <label for="OLDPASSWORD">이전 비밀번호</label>
                        <input type="password" class="LoginForm__Input"  id="OLDPASSWORD" v-model="oldpassword" placeholder="이전 비밀번호" autocomplete="new-password">
                    </div>

                    <div class="expand__password">
                        <label for="OLDPASSWORD">새 비밀번호</label>
                        <input type="password" class="LoginForm__Input" :class="{LoginForm__Err : checkPassword()}" id="PASSWORD" v-model="password" placeholder="비밀번호" autocomplete="new-password">
                        <p class="checkText" v-if="checkPassword()" >비밀번호는 최소 8글자 이상이어야 합니다.</p>
                    </div>

                    <div class="expand__password">
                        <label for="OLDPASSWORD">새 비밀번호 확인</label>
                        <input type="password" class="LoginForm__Input" :class="{LoginForm__Err : checkPasswordConfirm()}" id="PASSWORDCONFIRM" v-model="passwordconfirm" placeholder="비밀번호 확인" autocomplete="new-password">
                        <p class="checkText" v-if="checkPasswordConfirm()" >비밀번호가 일치하지 않습니다.</p>
                    </div>
                    <div class="btn btn--primary btn--sm expand__btn">변경하기</div>
                </div>

                <div id="imgChange" class="change">
                    <p>프로필 이미지 변경</p>
                    <div class="btn btn--sm" @click="editToggle = 2" v-if="editToggle != 2">Expand</div>
                    <div class="btn btn--sm" @click="editToggle = 0" v-if="editToggle === 2">Close</div>
                </div>
                <div v-if="editToggle === 2" class="expand">
                    <div class="profile-banner__image">
                        <img src="@/assets/image/defaultUserImage.jpg" alt="" style="width: 10vw; height: 10vw;">
                    </div>
                    
                    <input type="file" style="width:100%;">
                        asd
                    
                </div>

                <div id="detailChange" class="change">
                    <p>개인 정보 변경</p>
                    <div class="btn btn--sm" @click="editToggle = 3" v-if="editToggle != 3">Expand</div>
                    <div class="btn btn--sm" @click="editToggle = 0" v-if="editToggle === 3">Close</div>
                </div>
            </div>
            
            
            <div class="btn btn--primary btn--md" @click="Go">
                Edit
            </div>
            <div class="btn btn--primary btn--md" @click="Go">
                Save
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return{
            oldpassword: '',
            password : '',
            passwordconfirm : '',

            editToggle : 0,
            editList : [
                {name: '비밀번호 변경', value: 1},
                {name: '프로필 이미지 변경', value: 2},
                {name: '개인 정보 변경', value: 3},
            ]
        }
    },
    methods: {
        Go() {
            this.$emit('transForm');
            window.scrollTo(0, 0);
        },
        checkPassword() {
            if (this.password != '' && this.password.length <= 7) {
                return true
            }
        },
        checkPasswordConfirm() {
            if (this.passwordconfirm != '' && this.passwordconfirm != this.password) {
                return true
            }
        }
    }
}
</script>
<style lang="scss" scope>
    .btn {
        height: 2rem;
    }
</style>